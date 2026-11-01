#my_list = [1,2,3]
#print(type(my_list))
from oops_proj import Chatbook
user1 = Chatbook()
#print(user1.name)
# encapsulated attribute ko access kaise kr skte hai -> obj._class_name__attribute_name
#print(user1._Chatbook__name) 
print(user1.getter())
user1.setter("Fortuner")
print(user1.getter())
print(user1.id)
user2 = Chatbook()
print(user2.id)

user3 = Chatbook()
print(user3.id)

Chatbook.set_ter(10)
user4 = Chatbook()
print(user4.id)