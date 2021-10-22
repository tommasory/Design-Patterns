from command import Command, DoorCommand, Action

if __name__ == "__main__":  
    command: Command = DoorCommand()  
    command.execute(Action.DOOR_OPEN)  
    command.execute(Action.DOOR_CLOSE)  
    command.unDoExecute() 