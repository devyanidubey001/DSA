import abc #class for interface
class GroupServiceInterface(metaclass=abc.ABCMeta):
   @abc.abstractmethod
   def addGroup(self,id,name,members):
       pass

       