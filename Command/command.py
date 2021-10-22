"""
EXAMPLE

Definición del problema: proporcione una interfaz al usuario para abrir y cerrar la puerta. Si el usuario lo desea, debería poder deshacer su última acción.

Este ejemplo realmente muestra el caso de uso del requisito de acción de hacer y deshacer. Para otros requisitos, escribiré artículos separados.

Players here

* ICommand - ICommand
* ConcreateCommand - DoorCommand
* Invoker - cliente, en nuestro caso operaremos el cliente en la función principal (clase de inicio)
* Receiver – Door

"""
from enum import Enum 
from abc import ABC, abstractmethod
  
class Action(Enum):  
    DOOR_OPEN = 0,  
    DOOR_CLOSE = 1

class Command(ABC):  
 
    @abstractmethod  
    def execute(self, action: Action):  
        pass  
 
    @abstractmethod  
    def unDoExecute(self, action: Action):  
        pass

class Door :  
    def open(self):  
        print("------------Door Opened---------------")  
  
    def close(self) :  
        print("------------Door Closed---------------")

class DoorCommand(Command):  
  
    def __init__(self):  
        self.door = Door()  
  
    def execute(self, action: Action):  
        switcher = {Action.DOOR_OPEN: self.door.open, Action.DOOR_CLOSE: self.door.close}  
        self.lastAction = action  
        # Get the function object from switcher dictionary  
        function = switcher.get(action, None)  
        # Execute the function  
        function()  
  
    def unDoExecute(self):  
        switcher = {Action.DOOR_OPEN: self.door.close, Action.DOOR_CLOSE: self.door.open}  
        # Get the function object from switcher dictionary  
        function = switcher.get(self.lastAction, None)  
        # Execute the function  
        function() 