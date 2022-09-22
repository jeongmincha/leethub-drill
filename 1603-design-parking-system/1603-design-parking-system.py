class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.remainders = [small, medium, big]

    def addCar(self, carType: int) -> bool:
        available = False
        
        idx = 3 - carType
        if self.remainders[idx] > 0:
            available = True
            self.remainders[idx] -= 1
        
        return available
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)