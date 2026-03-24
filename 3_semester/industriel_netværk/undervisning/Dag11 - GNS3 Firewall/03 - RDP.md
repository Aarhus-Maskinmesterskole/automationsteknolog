# Guide: Få en Windows-VM til at køre RDP (host → VM)

## Forudsætninger

* VM kører **Windows Pro/Enterprise/Education** (Home kan ikke modtage RDP).
* Du ved, hvilket **VMware-net** VM’en sidder på (NAT = VMnet8, Host-only = VMnet1).
* Du har lokal admin på VM’en.

---

## Trin A — Netværk (så hosten kan nå VM’en)

**I VMware (på VM’en):**
Settings → **Network Adapter**:

* Vælg **Host-only (VMnet1)** eller **NAT (VMnet8)**.
* Hak i **Connected** og **Connect at power on**.
* Start VM’en og find IP: `ipconfig` (notér fx `192.168.x.y`).

**På værts-PC’en:**
Bekræft at du har en **VMware Network Adapter VMnet1/8** i `ncpa.cpl` med IP i samme subnet (så host↔VM kan snakke).

---

## Trin B — Slå RDP til (GUI-vej)

På **VM’en**:

1. Start → **Indstillinger** → **System** → **Fjernskrivebord** → **Slå Fjernskrivebord til**.
   (Accepter evt. NLA — vi kan slå den midlertidigt fra senere, hvis login driller.)
2. **Windows Firewall** åbner normalt reglerne automatisk. Hvis ikke, se Trin D.

---

## Trin C — Opret en lokal bruger til RDP

Undgå domæne-forvirring ved at bruge en **lokal** konto. Navnet må ikke være lig **computernavnet**.

**PowerShell (Admin) på VM’en:**

```powershell
# Opret bruger (justér navn/kode)
cmd /c 'net user "aso-local" adminadmin /add'
cmd /c 'net user "aso-local" /expires:never'

# Tilføj til "Remote Desktop Users" (sprog-agnostisk via SID 555)
$rdp = (Get-CimInstance Win32_Group -Filter 'SID="S-1-5-32-555"').Name
cmd /c "net localgroup `"$rdp`" `"aso-local`" /add"

# (Valgfrit, til første login) Læg også brugeren i lokale Administratorer (SID 544)
$adm = (Get-CimInstance Win32_Group -Filter 'SID="S-1-5-32-544"').Name
cmd /c "net localgroup `"$adm`" `"aso-local`" /add"
```

---

## Trin D — Sørg for at tjeneste og firewall er OK

**PowerShell (Admin) på VM’en:**

```powershell
# Tillad RDP i system
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" `
  /v fDenyTSConnections /t REG_DWORD /d 0 /f | Out-Null

# Åbn inbound TCP 3389 (uanset sprog)
if (-not (Get-NetFirewallRule -Name Allow-RDP-3389 -ErrorAction SilentlyContinue)) {
  New-NetFirewallRule -Name 'Allow-RDP-3389' -DisplayName 'Allow RDP 3389' `
    -Direction Inbound -Protocol TCP -LocalPort 3389 -Action Allow | Out-Null
}

# Sæt Remote Desktop Services til Auto og start
Set-Service TermService -StartupType Automatic
Start-Service TermService

# Sæt netværksprofil til Private (letter firewallregler)
$prof = Get-NetConnectionProfile
Set-NetConnectionProfile -InterfaceAlias $prof.InterfaceAlias -NetworkCategory Private
```

> **Tjek at 3389 lytter:**

```powershell
Get-NetTCPConnection -LocalPort 3389 -State Listen
```

---

## Trin E — Første login fra værts-PC’en


1. Åbn **mstsc** og forbind til **VM’ens IP**.  
`mstsc /v:<VM-IP>`
2. Klik **Flere valgmuligheder → Brug en anden konto** og brug **lokal syntaks**:
   * Brugernavn: `.\aso-local`   *(punktum = “denne maskine”)*
   * Kode: `adminadmin`

> Hvis du stadig får credential-fejl, kan du **midlertidigt** slå NLA fra for at isolere problemet:

```powershell
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" `
  /v UserAuthentication /t REG_DWORD /d 0 /f | Out-Null
Restart-Service TermService
```

Log ind, opret/ret brugere, og slå NLA til igen bagefter (`/d 1`).

---

## Trin F — Hurtig fejlfinding (to kommander afslører 90% af fejl)

**På værts-PC’en:**

```powershell
Test-NetConnection <VM-IP> -Port 3389   # Skal være True
```

**På VM’en:**

```powershell
Get-NetTCPConnection -LocalPort 3389 -State Listen   # Skal vise 'Listen'
```

* `False` / ingen “Listen” → firewall, tjeneste, edition (Home), eller forkert netprofil.
* “Legitimationsoplysninger virkede ikke” → brug **`.\brugernavn`** og sørg for at brugeren findes, er aktiv og i **Remote Desktop Users** (evt. også **Administratorer**).

> Se præcis årsag i log: **Event Viewer → Windows Logs → Security → Event ID 4625** (Logon Type 10).

---

## Bonus: netvalg og rute

* **Host-only (VMnet1)**: super til host↔VM.
* **NAT (VMnet8)**: også fint; giver VM internet via host.
* **Bridged**: VM får IP på dit fysiske LAN — kun nødvendigt hvis andre maskiner på LAN’et skal RDP’e direkte til VM’en.

---

## Mini-tjekliste (print-venlig)
* [ ] Windows-edition ≠ Home
* [ ] VMware-net: Host-only eller NAT, “Connected” ✓
* [ ] VM-IP noteret (`ipconfig`)
* [ ] RDP slået til (GUI eller `fDenyTSConnections=0`)
* [ ] Firewallregel for TCP/3389
* [ ] TermService = Auto + Running
* [ ] Netværksprofil = Private
* [ ] Lokal bruger oprettet (ikke samme navn som computeren)
* [ ] Medlem af **Remote Desktop Users** (og evt. **Administratorer**)
* [ ] Første login med `.\brugernavn`
* [ ] `Test-NetConnection <IP> -Port 3389` = True
