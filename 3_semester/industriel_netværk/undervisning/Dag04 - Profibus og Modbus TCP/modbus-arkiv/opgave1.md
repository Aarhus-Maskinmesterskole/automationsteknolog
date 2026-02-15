\documentclass[a4paper,11pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[danish]{babel}
\usepackage{geometry}
\geometry{margin=2.5cm}
\usepackage{hyperref}
\usepackage{enumitem}
\usepackage{xcolor}
\usepackage{fancyhdr}
\setlength{\headheight}{14pt}
\usepackage{titlesec}
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage{listingsutf8}
\usepackage{listings}
\lstset{
  inputencoding=utf8,
  extendedchars=true,
  literate={æ}{{\ae}}1 {ø}{{\o}}1 {å}{{\aa}}1 {Æ}{{\AE}}1 {Ø}{{\O}}1 {Å}{{\AA}}1,
  basicstyle=\ttfamily\small,
  columns=fullflexible,
  keepspaces=true,
  frame=single,
  breaklines=true,
  showstringspaces=false,
  upquote=true
}
\setlist[itemize]{topsep=2pt,itemsep=2pt,parsep=0pt,leftmargin=1.2cm}

% Header og footer
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\textbf{AAMS} - Industrielt Netværk}
\fancyhead[R]{\textit{Opgave}}
\fancyfoot[C]{\thepage}

% Titel formattering
\titleformat{\section}{\normalfont\Large\bfseries\color{blue!70!black}}{\thesection}{1em}{}

\title{\textbf{\Huge Opgave 05}\\[0.2cm]
       {\Large\color{blue!70!black}Python Modbus TCP Client til S7-1200}}
\author{Underviser: Anders S. Østergaard}
\date{2. september 2025}

\begin{document}
\maketitle

\noindent\textbf{Mål:} Lav en Python applikation der læser process data fra S7-1200 via Modbus TCP.

\section{Setup}
\begin{center}
\texttt{S7-1200 (Modbus Server) - Switch - PC (Python Client)}
\end{center}

\section{IP Adresser}
\begin{center}
\begin{tabular}{|l|l|}
\hline
\textbf{Enhed} & \textbf{IP Adresse} \\ \hline
S7-1200 & 192.168.1.10 \\ \hline
PC (Python) & 192.168.1.11 \\ \hline
\end{tabular}
\end{center}
Subnet mask: 255.255.255.0

\section{S7-1200 Opsætning}

\subsection{TIA Portal Konfiguration}
\begin{lstlisting}
1. Opret projekt: "Python_Modbus_Server"
2. Tilføj S7-1200 CPU
3. Ethernet interface:
   - IP: 192.168.1.10
   - Subnet: 255.255.255.0
4. Device Configuration → Protection & Security:
   - PUT/GET communication: AKTIVER
5. Opret DB100 "ProcessData":
   - DB100.DBW0 (INT): Temperatur (test værdi: 25)
   - DB100.DBW2 (INT): Tryk (test værdi: 1013)  
   - DB100.DBW4 (INT): Status bits (test værdi: 5)
6. Download til PLC
\end{lstlisting}

\section{Python Environment Setup}

\subsection{Installation}
\begin{lstlisting}
1. Verificer Python installation:
   python --version
   (skal være 3.7 eller nyere)

2. Installer Modbus bibliotek:
   pip install pymodbus

3. Test installation:
   python -c "import pymodbus; print('OK')"
\end{lstlisting}

\section{Python Modbus Client}

\subsection{Grundlæggende Client (modbus\_client.py)}
\begin{lstlisting}[language=Python]
#!/usr/bin/env python3
"""
Simpel Python Modbus TCP Client til S7-1200
Læser process data fra PLC
"""

from pymodbus.client import ModbusTcpClient
import time
import sys

# PLC konfiguration
PLC_IP = "192.168.1.10"
PLC_PORT = 502
UNIT_ID = 1

def connect_to_plc():
    """Etabler forbindelse til S7-1200"""
    print(f"Forbinder til S7-1200 på {PLC_IP}:{PLC_PORT}")
    
    client = ModbusTcpClient(host=PLC_IP, port=PLC_PORT)
    
    if client.connect():
        print("Forbindelse etableret!")
        return client
    else:
        print("Kunne ikke forbinde til PLC")
        return None

def read_plc_data(client):
    """Læs data fra S7-1200 holding registers"""
    try:
        # Læs 3 holding registers fra adresse 0
        result = client.read_holding_registers(
            address=0,      # Start ved register 0
            count=3,        # Læs 3 registre
            unit=UNIT_ID
        )
        
        if result.isError():
            print(f"Modbus fejl: {result}")
            return None
        
        # Parse data
        registers = result.registers
        data = {
            'temperatur': registers[0],     # DB100.DBW0
            'tryk': registers[1],          # DB100.DBW2
            'status_raw': registers[2]     # DB100.DBW4
        }
        
        # Parse boolean bits fra status
        data['pumpe_on'] = bool(data['status_raw'] & 0x01)  # Bit 0
        data['alarm'] = bool(data['status_raw'] & 0x02)     # Bit 1
        data['auto_mode'] = bool(data['status_raw'] & 0x04) # Bit 2
        
        return data
        
    except Exception as e:
        print(f"Fejl ved læsning: {e}")
        return None

def main():
    """Hovedprogram"""
    print("Python Modbus Client til S7-1200")
    print("Tryk Ctrl+C for at stoppe")
    print("=" * 40)
    
    # Forbind til PLC
    client = connect_to_plc()
    if not client:
        sys.exit(1)
    
    try:
        # Kontinuerlig læsning
        while True:
            data = read_plc_data(client)
            
            if data:
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                print(f"\nData fra S7-1200 ({timestamp})")
                print(f"Temperatur: {data['temperatur']} grader C")
                print(f"Tryk: {data['tryk']} mbar")
                print(f"Pumpe: {'ON' if data['pumpe_on'] else 'OFF'}")
                print(f"Alarm: {'AKTIV' if data['alarm'] else 'OK'}")
                print(f"Auto mode: {'JA' if data['auto_mode'] else 'NEJ'}")
                print(f"Status bits: 0x{data['status_raw']:04X}")
                print("-" * 40)
            else:
                print("Ingen data modtaget")
            
            # Vent 5 sekunder
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nStopper program...")
    finally:
        client.close()
        print("Forbindelse lukket")

if __name__ == "__main__":
    main()
\end{lstlisting}

\section{Test og Verifikation}

\subsection{Connectivity Test}
\begin{lstlisting}
1. Ping test fra PC:
   ping 192.168.1.10

2. Telnet test til Modbus port:
   telnet 192.168.1.10 502
   (Forvent connection success)

3. Kør Python client:
   python modbus_client.py
\end{lstlisting}

\subsection{Forventet Output}
\begin{lstlisting}
Python Modbus Client til S7-1200
Tryk Ctrl+C for at stoppe
========================================
Forbinder til S7-1200 på 192.168.1.10:502
Forbindelse etableret!

Data fra S7-1200 (2025-09-02 19:07:39)
Temperatur: 25 grader C
Tryk: 1013 mbar
Pumpe: ON
Alarm: OK
Auto mode: JA
Status bits: 0x0005
----------------------------------------
\end{lstlisting}

\subsection{Data Validering}
\begin{lstlisting}
1. I TIA Portal online monitor:
   - Ændr DB100.DBW0 til 30 (temperatur)
   - Observer ændring i Python output

2. Test status bits:
   - Ændr DB100.DBW4 til 3 (bits 0 og 1 sat)
   - Verificer pumpe ON og alarm AKTIV i Python

3. Test connection recovery:
   - Stop PLC midlertidigt
   - Observer fejlbesked i Python
   - Start PLC igen og verificer genoprettelse
\end{lstlisting}

\section{Fejlsøgning}

\begin{itemize}
  \item \textbf{ModuleNotFoundError pymodbus:} Kør \texttt{pip install pymodbus}
  \item \textbf{Connection refused:} Check at PLC er online og PUT/GET aktiveret
  \item \textbf{Timeout fejl:} Verificer IP adresser og netværkskonfiguration
  \item \textbf{Permission denied:} Kør command prompt som administrator
  \item \textbf{Forkerte data:} Check Modbus register mapping i TIA Portal
\end{itemize}

\section{Udvidelsesmuligheder}

\begin{itemize}
  \item Tilføj CSV logging af data til fil
  \item Implementer email alarm ved kritiske værdier
  \item Lav grafisk GUI med tkinter
  \item Tilføj write funktionalitet (kommandoer til PLC)
  \item Integrer med database (SQLite/MySQL)
  \item Opret web dashboard med Flask
\end{itemize}

\medskip
\noindent \textbf{Succes kriterie:} Python læser og viser live data fra S7-1200 hvert 5. sekund.

\end{document}
