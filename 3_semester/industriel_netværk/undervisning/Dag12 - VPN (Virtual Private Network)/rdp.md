# Step-by-step guide til at sætte RDP op mellem to Windows-maskiner.

Vi har to maskiner:
* **Computer A** = den du *sidder ved* (klient)
* **Computer B** = den du vil *fjernstyre* (server)

---

# 0. Forudsætninger

1. **Windows-udgave på Computer B** ⬅️

   * Skal være **Windows Pro / Enterprise / Education** (10 eller 11).
     Home-udgaver kan ikke være RDP-server.

2. **Netværk**

   * Computer A skal kunne nå Computer B over netværket (samme LAN eller via VPN).
   * Du skal kende:

     * IP-adresse på Computer B
     * Brugernavn + adgangskode på en konto på Computer B

---

# 1. Find IP-adresse på Computer B

På **Computer B**:

1. Tryk `Win + R`

2. Skriv `cmd` → Enter

3. I Kommandoprompt:

   ```cmd
   ipconfig
   ```

4. Find den relevante adapter (Ethernet eller Wi-Fi).
   Notér **IPv4 Address**, f.eks.:

   ```text
   IPv4 Address . . . . . : 10.0.0.20
   ```

Den IP-adresse bruger du senere på Computer A.

---

# 2. Aktivér Remote Desktop på Computer B

1. Tryk `Win + R`

2. Skriv:

   ```text
   SystemPropertiesRemote.exe
   ```

   → Enter

3. I fanen **Fjernforbindelse** / **Remote**:

   * Under **Fjernskrivebord / Remote Desktop**:

     * Vælg **“Tillad fjernforbindelser til denne computer”**
       (engelsk: *Allow remote connections to this computer*).

4. Hvis du får en dialog om Windows-firewall → vælg **Tillad / Allow**.

5. Klik **OK**.

---

# 3. Sørg for at brugeren på Computer B har RDP-adgang

Vi antager, at der findes en lokal bruger på Computer B, fx:

* Brugernavn: `User1`

> Brugere i gruppen **Administrators** har automatisk RDP-adgang.
> Andre brugere skal tilføjes.

### 3.1 Tjek brugeren

På Computer B → åbn Kommandoprompt:

```cmd
whoami
hostname
net user
```

Eksempel:

```text
whoami   → DESKTOP-ABC123\User1
hostname → DESKTOP-ABC123
```

Nu ved du:

* Maskinnavn: `DESKTOP-ABC123`
* Brugernavn: `User1`

### 3.2 Tilføj brugeren (hvis den ikke er admin)

1. I vinduet **Systemegenskaber → Fjernforbindelse** klik på **“Vælg brugere…” / “Select Users…”**.
2. Klik **“Tilføj…” / “Add…”**.
3. Skriv brugernavnet, fx `User1`.
4. Klik **OK** → **OK** igen.

**Alternativt via kommandoprompt (Computer B):**

```cmd
net localgroup "Remote Desktop Users" User1 /add
```

---

# 4. (Valgfrit men anbefalet) Sæt en kendt adgangskode til brugeren

På **Computer B** (Kommandoprompt som administrator):

1. Højreklik på **Kommandoprompt** → **Kør som administrator**.
2. Kør:

   ```cmd
   net user User1 MinSikreKode123!
   ```

Nu ved du med sikkerhed, hvilken adgangskode du skal bruge, når du logger på via RDP.

---

# 5. Test netværksforbindelsen fra Computer A

På **Computer A**:

1. Åbn Kommandoprompt eller PowerShell.
2. Test ping:

   ```powershell
   ping 10.0.0.20
   ```

   (brug IP-adressen fra Computer B)

* Hvis der er svar → netværksforbindelsen er OK.
* Hvis der ikke er svar → der er et netværksproblem (forkert IP, manglende route, VPN nede osv.), som skal løses **før** RDP kan virke.

---

# 6. Start RDP-klient på Computer A

På **Computer A**:

1. Tryk `Win + R`

2. Skriv:

   ```text
   mstsc
   ```

   → Enter (åbner **Forbindelse til Fjernskrivebord / Remote Desktop Connection**)

3. I feltet **Computer** skriv IP-adressen til Computer B, f.eks.:

   ```text
   10.0.0.20
   ```

4. Klik **Forbind / Connect**.

---

# 7. Log korrekt ind på Computer B

Når loginvinduet kommer frem, skal du være opmærksom på **hvilken type konto** du bruger.

### 7.1 Lokalt brugernavn på Computer B

Hvis din bruger på Computer B er lokal (fx `User1`), og `whoami` viste noget ala:

```text
DESKTOP-ABC123\User1
```

så skal du i RDP-login skrive:

**Metode A (mest sikker):**

* Klik **Flere valgmuligheder / More choices**

* Klik **Brug en anden konto / Use a different account**

* Brugernavn:

  ```text
  .\User1
  ```

  (punktum-backslash betyder “lokal bruger på den pc jeg forbinder til”)

* Adgangskode:

  ```text
  MinSikreKode123!
  ```

**Metode B (alternativ):**

```text
DESKTOP-ABC123\User1
```

* adgangskode.

---

### 7.2 Microsoft-konto på Computer B

Hvis Computer B bruger en Microsoft-konto (login med e-mail), bruges:

* Brugernavn: hele mailadressen, fx:

  ```text
  bruger@outlook.com
  ```

* Adgangskode: password til den Microsoft-konto.

---

# 8. Typiske fejl og hurtige løsninger

### Fejl: “Dine legitimationsoplysninger virkede ikke”

* Tjek at du bruger **lokal konto** korrekt:

  * `.\User1`
    eller
  * `MASKINENAVN\User1`
* Tjek at du har sat adgangskoden korrekt på Computer B:

  ```cmd
  (Computer B, CMD som administrator)
  net user User1 MinSikreKode123!
  ```

---

### Fejl: “Der kunne ikke oprettes forbindelse til fjerncomputeren”

* Forkert IP (tjek `ipconfig` på Computer B)
* VPN/route mangler
* Computer B er slukket/sover
* RDP ikke slået til (gå tilbage til trin 2)

---

## 9. Ultrakort opsummering

1. På Computer B:

   * Find IP: `ipconfig`
   * Slå RDP til: `SystemPropertiesRemote.exe` → *Tillad fjernforbindelser*
   * Sørg for at brugeren har RDP-adgang (administrator eller i “Remote Desktop Users”)
   * (valgfrit) Sæt adgangskode: `net user User1 MinSikreKode123!`

2. På Computer A:

   * `ping <IP-Computer-B>`
   * `mstsc` → Computer: `<IP-Computer-B>`
   * Login: `.\User1` + adgangskode

Så har du en generel, reproducerbar måde at få RDP til at virke mellem to Windows-maskiner, uanset om det er i et lab, hjemme, eller på et kursus.
