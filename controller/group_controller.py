class GroupController(object):
    def __init__(self,groupService): #like an object to access the user interface
            self.groupService = groupService
    def addGroup(self,id,name,members):
        return self.groupService.addGroup(id,name,members)