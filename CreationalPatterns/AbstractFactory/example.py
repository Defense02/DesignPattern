from __future__ import annotations
from abc import ABC, abstractmethod

class FurnitureFactory(ABC):
    @abstractmethod    
    def create_chair(self):
        # result = print(self.create_chair().has_legs())
        # return result
        print (f"chair: {self.create_chair().has_legs()}")
    
    @abstractmethod
    def create_coffeetable(self):
        pass 

    # abstract method of subclasses will override the abstract method of parent class.
    def assemble_furniture(self):
        chair = self.create_chair()
        #coffee_table = self.create_coffeetable()
        return f"Chair : {chair.has_legs()} and Coffee Table: {self.create_coffeetable().material()}"
    
# Concrete factory 
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()
    
    def create_coffeetable(self) -> CoffeeTable:
        return ModernCoffeeTable()
    
    
class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()
    
    def create_coffeetable(self) -> CoffeeTable:
        return VictorianCoffeeTable()
    
    
# abstract product A
class Chair(ABC):
    @abstractmethod
    def has_legs(self):
        pass
    
# concrete product A-1 
class ModernChair(Chair):
    def has_legs(self):
        return "it has 4 legs"

# concrete product A-2
class VictorianChair(Chair):
    def has_legs(self):
        return "it has 4 legs"
    
    
# abstract product B
class CoffeeTable(ABC):
    @abstractmethod
    def material(self):
        pass
    
# concrete product B-1
class ModernCoffeeTable(CoffeeTable):
    def material(self):
        return "Wood"
    
# concrete product B-2
class VictorianCoffeeTable(CoffeeTable):
    def material(self):
        return "Silk"

def client_code(factory: FurnitureFactory):
    # print(factory.create_chair())
    # print(factory.create_coffeetable())
    result = factory.assemble_furniture()
    print(f"{result}")
    # return result   
    

if __name__ == "__main__":
    print("Client: Testing client code with the Modern type furnitures.\n")
    print("Modern style: ")
    # we should call instances, not the class itself.
    client_code(ModernFurnitureFactory())
    print("\n")
    
    print("Client: Testing client code with the Victorian type furnitures")
    print(f"Victorian style: ")
    client_code(VictorianFurnitureFactory())
    print("\n")

    # if the method has no return, the output will be None, differed from printf.
    