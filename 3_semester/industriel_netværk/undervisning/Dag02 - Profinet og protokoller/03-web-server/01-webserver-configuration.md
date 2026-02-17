Her er en rettet version, som er **fagligt korrekt**, stadig **simpel**, og skrevet som en øvelse til studerende. Jeg har bevaret din struktur, men rettet de steder der var misvisende (især WWW, RET_VAL, “Create blocks”, IP og rettigheder).

---

# Opsætning af Webserver på SIMATIC PLC

### 📽️ Video

Video link: [Webserver Configuration](https://www.youtube.com/watch?v=-enoZCAg5P4)

### 🖥️ Link (Siemens manual)

Siemens Webserver Configuration Guide:
[Siemens Webserver Configuration Guide](https://cache.industry.siemens.com/dl/files/931/58862931/att_12510/v1/58862931_s7-1200_webserver_doku_v11_en.pdf)

---

## Mål

Målet med denne opgave er at opsætte og konfigurere en webserver på en **fysisk SIMATIC S7-1200** og (valgfrit) en **simuleret S7-1500** via **PLCSIM Advanced**. I får praktisk erfaring med PLC’ens webserver og med at lave en simpel HTML-side (User pages), der kan **vise og ændre PLC-variabler**.

---

## Opgavebeskrivelse

### 1) Konfiguration af PLC A (S7-1200 som webserver)

#### 1.1 Opret projekt og netværk

* Opret et nyt projekt i TIA Portal og tilføj en fysisk **S7-1200**.
* Tildel en IP-adresse til PLC’en (eksempel):

  * PLC: `192.168.0.10`
  * PG/PC: `192.168.0.100`
  * Subnet: `255.255.255.0`

> Tip: Undgå at bruge `192.168.0.1`, da det ofte er routerens adresse i mange netværk.

#### 1.2 Aktivér webserver og bruger

Gå til CPU → **Properties**:

* **Web server**: Enable **“Activate Web Server on this module”**
* **User management**:

  * Opret en bruger fx `webuser` med **Read + Write**
  * (Valgfrit til øvelse) Du kan midlertidigt give “Everybody” rettigheder, men **i industrien** bruger man altid login og begrænser adgang.

#### 1.3 Opret “User pages” og generér web-DB’er

I CPU → Properties → **User pages**:

* Vælg **HTML file path** (mappe på PC’en hvor dine HTML-filer ligger)
* Sæt **Start page** (fx `index.htm`)
* Angiv et **Application name** (fx “Webserver øvelse”)
* Klik **Create blocks**

✅ Dette genererer:

* **Web Control DB** (typisk `DB333`)
* én eller flere **Fragment DB’er** (indeholder dine HTML/JS filer “pakket” til CPU’en)

> Vigtigt: PLC’en “ved ikke” at disse DB’er indeholder web-sider, før vi kalder instruktionen **WWW** i programmet.

---

### 1.4 Kald WWW-instruktionen korrekt (OB100 + OB1)

**WWW** initialiserer webserverens user pages og synkroniserer kommunikationen mellem webside og PLC-program.

**A) OB100 (Startup):**
Kald `WWW` én gang ved opstart for at **initialisere** user pages.

* `CTRL_DB := 333` (eller det DB-nummer du fik genereret)
* `RET_VAL :=` en **INT**-variabel (brug fx `MW0` eller en DB-variabel af typen INT)

**B) OB1 (cyklisk):**
Kald `WWW` cyklisk for **synkronisering/handshake** (så POST-skrivninger og dataudveksling virker stabilt).

> OBS: `RET_VAL` er **INT** → brug ikke `M0.0` (det er en bit). Brug fx `MW0` eller `DB…returnValue : INT`.

---

### 1.5 Opret DB med variabler til websiden

Opret en DB kaldet `DB_Web` med følgende variabler (datatyper som vist):

* `Out1` : `Bool`
* `Out2` : `Bool`
* `Setpoint1` : `Int` (eller `Real` – vælg én)
* `Setpoint2` : `Int` (eller `Real`)

> Industri-tip: I praksis skriver man ofte til “kommandoer” i en DB og lader PLC-logikken styre Q-udgange, men til øvelsen er DB-styring fint.

---

## 2) HTML-side (User page) – skriv 4 variabler

Gem filen som **`index.htm`** i den mappe du valgte som *HTML file path*.

> Bemærk: AWP kræver de specielle kommentartags `AWP_In_Variable` og at `name=` bruger indlejrede citationstegn `'" ... "'`.

```html
<!doctype html>
<html lang="da">
<head>
  <meta charset="utf-8">
  <title>Styring</title>
</head>
<body>
  <h2>Styring (4 variabler)</h2>

  <!-- Deklarér alt der må skrives (AWP_In_Variable) -->
  <!-- AWP_In_Variable Name='"DB_Web".Out1' -->
  <!-- AWP_In_Variable Name='"DB_Web".Out2' -->
  <!-- AWP_In_Variable Name='"DB_Web".Setpoint1' -->
  <!-- AWP_In_Variable Name='"DB_Web".Setpoint2' -->

  <h3>Out1</h3>
  <form method="post" action="">
    <input type="submit" value="Out1 ON">
    <input type="hidden" name='"DB_Web".Out1' value="1">
  </form>

  <form method="post" action="">
    <input type="submit" value="Out1 OFF">
    <input type="hidden" name='"DB_Web".Out1' value="0">
  </form>

  <h3>Out2</h3>
  <form method="post" action="">
    <input type="submit" value="Out2 ON">
    <input type="hidden" name='"DB_Web".Out2' value="1">
  </form>

  <form method="post" action="">
    <input type="submit" value="Out2 OFF">
    <input type="hidden" name='"DB_Web".Out2' value="0">
  </form>

  <h3>Setpoints</h3>
  <form method="post" action="">
    <label>Setpoint1: </label>
    <input type="text" name='"DB_Web".Setpoint1' size="6" value="0">
    <input type="submit" value="Skriv SP1">
  </form>

  <form method="post" action="">
    <label>Setpoint2: </label>
    <input type="text" name='"DB_Web".Setpoint2' size="6" value="0">
    <input type="submit" value="Skriv SP2">
  </form>

</body>
</html>
```

---

## 3) Test og verifikation

1. Download program + web blocks til PLC.
2. Åbn browser og gå til:
   `http://192.168.0.10` (brug din PLC’s IP)
3. Log ind med brugeren du oprettede (`webuser`).
4. Gå til **User pages** og åbn din side.
5. Test:

   * at du kan ændre `Out1/Out2`
   * at du kan skrive `Setpoint1/Setpoint2`
   * og at værdierne faktisk ændrer sig i PLC’en (online monitor)

> Hvis websiden ikke dukker op, er de typiske fejl:
>
> * “Create blocks” ikke lavet
> * WWW ikke kaldt i OB100/OB1
> * forkert CTRL_DB nummer
> * webserver/user pages ikke enabled

---

## Krav

* Grundlæggende forståelse af webservere i industri
* Erfaring med TIA Portal og (valgfrit) PLCSIM Advanced

---

Hvis du vil, kan jeg også lave en **tilhørende “status.htm”** (med `meta refresh` hvert 2. sekund), så de studerende både har en status-side og en control-side — det matcher ofte Siemens’ måde at demonstrere AWP på.
