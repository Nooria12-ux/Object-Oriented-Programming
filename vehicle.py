class Vehicle:
    
    def __init__(self, maxSpeed, mileage):
        self.maxSpeed = maxSpeed
        self.mileage = mileage
        
tesluu = Vehicle(180, 0)
bombardiroCrocodilo = Vehicle(2300, 0.8)

print(f"Teslu's MaxSpeed : {tesluu.maxSpeed}\nTeslu's Mileage : {tesluu.mileage}\n\n")
print(f"Teslu's MaxSpeed : {bombardiroCrocodilo.maxSpeed}\nbombardiroCrocodilo Mileage : {bombardiroCrocodilo.mileage}\n\n")
