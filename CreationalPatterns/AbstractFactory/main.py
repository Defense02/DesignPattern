from __future__ import annotations
from abc import ABC, abstractmethod

# Abstract Factory 
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        return Button()
    
    @abstractmethod
    def create_checkbox(self):
        return Checkbox()
        
# Concrete Factory  
# In one class, they offer interface to produce product family (various instances in a factory). 
class WinFactory(GUIFactory):
    def create_button(self):
        return WinButton()
    
    def create_checkbox(self):
        return WinCheckbox()

# Concrete Factory    
class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()
    
    def create_checkbox(self):
        return MacCheckbox()

# Abstract Product A
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class WinButton(Button):
    def paint(self):
        return "window key"
        
class MacButton(Button):
    def paint(self):
        return "command"
    
# Abstract Product B
class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

class WinCheckbox(Checkbox):
    def paint(self):
        return "Window"
    
class MacCheckbox(Checkbox):
    def paint(self):
        return "Mac"

# Client works with factories and products only through abstract types: GUI Factory, Button, and Checkbox.
# Not depending on the concrete class.
class Application:
    def __init__(self, factory):
        self.factory = factory
        
        
    def createUI(self):
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()
        
    def paint(self):
        print(self.button.paint())
        print(self.checkbox.paint())

class ApplicationConfigurator:
    def __init__(self, os):
        self.factory = None
        self.os = os
        
    def main(self):
        if (self.os == "Windows"):
            self.factory = WinFactory()
        elif (self.os == "Mac"):
            self.factory = MacFactory()
        else:
            raise Exception("Error! Unknown OS")

        app = Application(self.factory)
        print(app.createUI())
        print(app.paint())

if __name__ == "__main__":
    app_window = ApplicationConfigurator("Windows")
    app_mac = ApplicationConfigurator("Mac")
    app_window.main()
    app_mac.main()
    # app_window.createUI() 
    # app_window.paint()   
    # app_mac.createUI()
    # app_mac.paint()
    
    