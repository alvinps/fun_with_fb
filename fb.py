import fbchat 
from fbchat.models import *
import time

username ="username"
password ="Password"
client = fbchat.Client(username, password) 

	#friends = client.fetchAllUsers() # return a list of names 
name = "Friends Name"
friend = client.searchForUsers(name)

for i in range(0,50):
	msg = str("Hey there,this was a message from python script. If you see this text me back.")
	client.send(Message(msg), friend[0].uid, friend[0].type)
	print("(%d) Message sent ...\n" % i)
	time.sleep(1)

client.logout()
