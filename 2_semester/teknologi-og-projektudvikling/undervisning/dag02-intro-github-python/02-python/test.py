class PController:
    def __init__(self, kp, output_min=0, output_max=100):
        self.kp = kp
        self.output_min = output_min
        self.output_max = output_max
        self.last_error = 0
    
    def calculate(self, setpoint, process_value):
        """Beregn control output"""
        error = setpoint - process_value
        output = self.kp * error
        
        # Begræns output
        output = max(self.output_min, min(self.output_max, output))
        
        self.last_error = error
        return round(output, 2)
    
    def get_error(self):
        """Hent sidste error"""
        return self.last_error

# Brug
controller = PController(kp=3, output_min=0, output_max=100)

SP = 50
PV = 45

output = controller.calculate(SP, PV)
print(f"Output: {output}%")
print(f"Error: {controller.get_error()}")
print(controller.get_error() * controller.kp)  # Skal være lig med output (minus begrænsning)