from __future__ import annotations
from abc import ABC, abstractmethod


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        return Button()
    
    @abstractmethod
    def create_checkbox(self):
        return Checkbox()
        
   
# In one class, they offer interface to produce product family. 
class WinFactory(GUIFactory):
    def create_button(self):
        return WinButton()
    
    def create_checkbox(self):
        return WinCheckbox()
    
class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()
    
    def create_checkbox(self):
        return MacCheckbox()


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


class Application:
    def __init__(self, os):
        if (os == "Windows"):
            self.factory = WinFactory()
        elif (os == "Mac"):
            self.factory = MacFactory()
        else:
            raise Exception("Error! Unknown OS")
        
        
    def createUI(self):
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()
        print(self.button.paint())
        print(self.checkbox.paint())
        
        
    def paint(self):
        pass


if __name__ == "__main__":
    app_window = Application("Windows")
    app_mac = Application("Mac")
    app_window.createUI()    
    app_mac.createUI()
    
    
    