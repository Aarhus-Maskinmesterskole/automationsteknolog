import snap7
import ctypes
import time
import signal
import sys
import logging
from typing import List

# --- Konfiguration af industriel logging ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger("Snap7Server")

class PLCSimulator:
    """
    En objektorienteret Snap7 Server, der agerer Siemens PLC for Emulate3D.
    """
    def __init__(self, port: int = 102, io_bytes: int = 2, mk_bytes: int = 4):
        self.port = port
        self.io_bytes = io_bytes
        self.mk_bytes = mk_bytes
        
        # Opret server instans
        self.server = snap7.server.Server(log=False) # Vi slår intern log fra for at bruge vores egen
        
        # Alloker hukommelse (C-types byte arrays)
        self.inputs = (ctypes.c_ubyte * self.io_bytes)()
        self.outputs = (ctypes.c_ubyte * self.io_bytes)()
        self.merkers = (ctypes.c_ubyte * self.mk_bytes)()
        
        # Tilstandsovervågning
        self.prev_input_state = None
        self.prev_output_state = None
        self.running = False

    def setup_areas(self) -> None:
        """Registrerer hukommelsesområderne i serveren."""
        self.server.register_area(snap7.type.SrvArea.PE, 0, self.inputs)
        self.server.register_area(snap7.type.SrvArea.PA, 0, self.outputs)
        self.server.register_area(snap7.type.SrvArea.MK, 0, self.merkers)
        logger.info(f"Hukommelse allokeret: {self.io_bytes} bytes I/O, {self.mk_bytes} bytes Merkers.")

    def start(self) -> None:
        """Starter serveren og lytter på den angivne port."""
        self.setup_areas()
        try:
            self.server.start(tcp_port=self.port)
            self.running = True
            logger.info(f"Snap7 PLC Server startet. Lytter på port {self.port}")
        except Exception as e:
            logger.error(f"Kunne ikke starte serveren. Er port {self.port} i brug? Fejl: {e}")
            sys.exit(1)

    def stop(self) -> None:
        """Stopper serveren sikkert."""
        if self.running:
            logger.info("Frakobler klienter og lukker server...")
            self.server.stop()
            self.server.destroy()
            self.running = False
            logger.info("Server stoppet.")

    # --- Hjælpefunktioner til bits ---
    @staticmethod
    def get_bit(buffer: ctypes.Array, byte_index: int, bit_index: int) -> bool:
        return bool(buffer[byte_index] & (1 << bit_index))

    @staticmethod
    def format_bits(buffer: ctypes.Array, count: int) -> str:
        bits: List[str] = []
        for i in range(count):
            byte_idx = i // 8
            bit_idx = i % 8
            bits.append('1' if PLCSimulator.get_bit(buffer, byte_idx, bit_idx) else '0')
        return ' '.join(bits)

    def monitor_loop(self, poll_rate: float = 0.2) -> None:
        """Kører et uendeligt loop, der overvåger ændringer i I/O."""
        logger.info("Begynder overvågning af I/O ændringer. Tryk Ctrl+C for at afslutte.")
        
        try:
            while self.running:
                # Konverter c_types arrays til standard Python bytes for at kunne sammenligne dem
                current_inputs = bytes(self.inputs)
                current_outputs = bytes(self.outputs)

                # Log kun hvis der er en faktisk ændring
                if current_inputs != self.prev_input_state or current_outputs != self.prev_output_state:
                    total_bits = self.io_bytes * 8 - 1 # f.eks. 15 bits for 2 bytes (0-15)
                    in_str = self.format_bits(self.inputs, total_bits)
                    out_str = self.format_bits(self.outputs, total_bits)
                    
                    print(f"\n--- I/O Opdatering ---")
                    print(f"Indgange (I): {in_str}")
                    print(f"Udgange  (Q): {out_str}")
                    
                    self.prev_input_state = current_inputs
                    self.prev_output_state = current_outputs

                time.sleep(poll_rate)
        except KeyboardInterrupt:
            self.stop()

# --- Entry point for scriptet ---
if __name__ == "__main__":
    # Opret instans af vores PLC
    plc = PLCSimulator(port=102, io_bytes=2, mk_bytes=4)
    
    # Håndter uventede nedbrud eller system-afbrydelser (SIGTERM)
    def signal_handler(sig, frame):
        plc.stop()
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Start og overvåg
    plc.start()
    plc.monitor_loop(poll_rate=0.2)
