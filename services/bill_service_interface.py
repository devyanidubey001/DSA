import abc #class for interface
class BillServiceInterface(metaclass=abc.ABCMeta):
   @abc.abstractmethod
   def addBill(self,id,groupId,amount,contribution,paidBy):
       pass
