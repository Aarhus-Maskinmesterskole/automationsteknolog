# Hvad er et subnet?
Et subnet (subnetværk) er en del af et større netværk, der er opdelt i mindre segmenter for at forbedre ydeevnen og sikkerheden. Subnetting gør det muligt at organisere og administrere netværket mere effektivt ved at opdele det i mindre, mere håndterbare dele.

## Subnetmaske
En subnetmaske er en 32-bit værdi, der bruges til at bestemme, hvilke dele af en IP-adresse der repræsenterer netværksdelen og hvilke dele der repræsenterer værtsdelen. En almindelig subnetmaske er 255.255.255.0, hvilket betyder, at de første tre oktetter repræsenterer netværksdelen, og den sidste oktet repræsenterer værtsdelen.

Octet er de fire tal i en IP-adresse eller subnetmaske og repræsenterer 8 bits. For eksempel, i IP-adressen 192.168.1.1, er hver af de fire tal en oktet.
Binær repræsentation af IP-adresse og subnetmaske:
- IP-adresse: 192.168.1.1 -> 11000000.10101000.00000001.00000001
- Subnetmaske: 255.255.255.0 -> 11111111.11111111.11111111.00000000