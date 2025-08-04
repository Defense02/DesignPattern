# enabling forward refs before it is defined.
from __future__ import annotations
from abc import ABC, abstractmethod


# Creator
class Dialog(ABC):
    def __init__(self):
        pass

    @abstractmethod        
    def create_button(self) -> Button:
        return 
        
    def operation(self):
        # instance start with small letter.
        button = self.create_button()
        click_msg = button.onClick()
        render_msg = button.render()
        result = f"Result of product: {button.render()}"
        print(click_msg)
        print(render_msg)
        return result
        
# Concrete Creator        
class WindowDialog(Dialog):     
    # overriding the factory method   
    def create_button(self) -> Button:
        # not WindowButton: Class, WindowButton(): Instance
        return WindowButton()
        
class WebDialog(Dialog):        
    def create_button(self) -> Button:
        return HTMLButton()
    

# Product
class Button(ABC):
    # if abstract method, every subclass must be implemented with that method. -> discrete interface ( every Button has click action. )
    @abstractmethod
    def render(self):
        pass
    def onClick(self):
        pass
    
# Concrete Product - various implementations of the product interface
class WindowButton(Button):
    def render(self):
        return "Render a Window-style button" 
    def onClick(self):
        return "Windows button clicked" 

        
class HTMLButton(Button):
    def render(self):
        return "Render a Web-style button" 
    def onClick(self):
        return "HTML button clicked" 
    
    
class Application:
        
    def __init__(self, OS_kind: str):
        if (OS_kind == "Windows"):
            self.dialog = WindowDialog()
        elif (OS_kind == "Web"):
            self.dialog = WebDialog()
        else:
            raise Exception("Error! Unknown OS")

    def main(self):
        print(self.dialog.operation())

if __name__ == "__main__":
    app = Application("Windows")
    app.main()        
        