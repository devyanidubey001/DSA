class UserController(object):
    def __init__(self,userService): #like an object to access the user interface
            self.userService = userService
    def addUser(self,id,name):
        return self.userService.addUser(id,name)