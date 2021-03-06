import sys
sys.path.append('/Users/devya/Desktop')
from splitwise.controller.user_controller import UserController

from splitwise.controller.group_controller import GroupController

from splitwise.controller.bill_controller import BillController

from splitwise.services.bill_service import BillService
from splitwise.services.user_service import UserService
from splitwise.services.group_service import GroupService

 #object for each controller
userController = UserController(UserService())
groupController = GroupController(GroupService())
billController = BillController(BillService())

user1 = userController.addUser('user1','Devyani')
user2 = userController.addUser('user2','Ayush')
user3 = userController.addUser('user3','Pawan')
user4 = userController.addUser('user4','Piyush')
user5 = userController.addUser('user5','Gauri')

members = [user1,user2,user3,user4,user5]
group1 = groupController.addGroup('group1','friends',members)

#print(group1.getMembers())

paidBy = {'user1': 200, 'user2' :100,'user3': 50, 'user4' :50,'user5': 100}
contribution = {'user1': 100, 'user2' :100,'user3': 100, 'user4' :100,'user5': 100}

bill = billController.addBill('bill1','group1',500, contribution,paidBy) #If paidBy then added to the user balance
balance = billController.getUserBalance('user2')

print(balance)