from abc import ABC, abstractmethod


# Creator
class Dialog():
    def __init__(self):
        pass

    @abstractmethod        
    def create_button(self) -> Button:
        return Button
        
    def render(self):
        okButton = self.create_button()
        okButton.onClick()
        okButton.render()
        
# Concrete Creator        
class WindowDialog(Dialog):        
    def create_button() -> Button:
        return WindowButton
        
class WebDialog(Dialog):        
    def create_button() -> Button:
        return HTMLButton
    

# Product
class Button(ABC):
    @abstractmethod
    def render(self):
        pass
    def onClick(self):
        pass
    
# Concrete Product - various implementations of the product interface
class WindowButton(Button):
    def render(a,b):
        return a + b
    def onClick():
        pass
        
class HTMLButton(Button):
    def render(a,b):
        return a * b
    def onClick():
        pass
    
    
class Application:
        
    def __init__(self):
        
        if (config.OS == "Windows"):
            self.dialog = WindowDialog
        elif (config.OS == "Web"):
            self.dialog = WebDialog
        else:
            raise Exception("Error! Unknown OS")

    def __main__(self):
        
        self.dialog.render()
        
        