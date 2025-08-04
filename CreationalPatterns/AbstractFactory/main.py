from __future__ import annotations
from abc import ABC, abstractmethod


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        return Button()
    
    @abstractmethod
    def create_checkbox(self):
        return Checkbox()
    
    
class WinFactory(GUIFactory):
    def create_button(self):
        return WinButton()
    
    def create_checkboc(self):
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
        self.factory = GUIFactory
        self.button = Button()
        
        
    def createUI(self):
        button = factory.createButton()
        
    def paint(self):
        

class ApplicationConfigurator():
    
        
if __name__ == "__main__":
    app_window = Application("Windows")
    app_mac = Application("Mac")
    
    
    