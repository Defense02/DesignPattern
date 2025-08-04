from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):
    # abstractmethod : "Any subclass must implement this method"
    @abstractmethod
    def factory_method(self):
        print("pass")
        pass
    
    def some_operation(self):
        print("when do they call?")
        # they directly call the factory method of ConcreteCreator1, 
        # without calling the factory method of Creator class.
        # they don't know how to product Product, but able to utilze Product through factory method.
        # bad example : product = ConcreteProduct1() 
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result
    
# when they make new product, make subclass for new product.    
class ConcreteCreator1(Creator):
    # -> : the type of value that function would return 
    # factory_method was being overrided.
    def factory_method(self) -> Product:
        print("making product1")
        return ConcreteProduct1()
    
    # if Child class has same method with parent class, then the method of child is working, not the method of parent.
    def some_operation(self):
        print("call")
    
class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()
    

class Product(ABC):
    print("product")
    # only for creator and proudct, they need abstract method.
    # In product class, they only define mutual interface, as abstract method.
    @abstractmethod
    def operation(self):
        pass
   
   
# print() inside class body - when the class is first defined
# print() inside __init()__ - when the class is first instantiated 
class ConcreteProduct1(Product):
    def __init__(self):
        # when we want the input from upper class, super init is utilized.
        super().__init__(self)
    print("product1")
    def operation(self):
        return "{Result of the ConcreteProduct1}"
    
class ConcreteProduct2(Product):
    def operation(self):
        return "{Result of the ConcreteProduct2}"

# client code without any class.                            
# input creator should be an instance from an Creator or its subclass like ConcreteCreator1 or ConcreteCreator2.                                                                                                                                              
def client_code(creator: Creator):
    # when I want to check whether the input is the Creator class
    # if creator != Creator:
    #     raise TypeError

    if not isinstance(creator, Creator):
        raise TypeError("creator must be an instance of Creator or its subclass")       
    
    print(f"Client: I'm not aware of creator's class.\n"
            f"{creator.some_operation()}", end="")
    
    
if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1")
    creator1 = ConcreteCreator1()
    client_code(creator1)
    print("\n")
    
    print("App: Launched with the ConcreteCreator2")
    client_code(ConcreteCreator2())
    print("\n")
