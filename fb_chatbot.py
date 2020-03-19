import fbchat 
from fbchat.models import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time
import getpass

my_bot = ChatBot(name='PyBot', read_only=True,
                 logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.BestMatch'])

small_talk = ['hi there!',
              'hi!',
              'how do you do?',
              'how are you?',
              'i\'m cool.',
              'fine, you?',
              'always cool.',
              'i\'m ok',
              'glad to hear that.',
              'i\'m fine',
              'glad to hear that.',
              'i feel awesome',
              'excellent, glad to hear that.',
              'not so good',
              'sorry to hear that.',
              'what\'s your name?',
              'i\'m pybot. ask me a math question, please.']
math_talk_1 = ['pythagorean theorem',
               'a squared plus b squared equals c squared.']
math_talk_2 = ['law of cosines','c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']


list_trainer = ListTrainer(my_bot)
for item in (small_talk, math_talk_1, math_talk_2):
    list_trainer.train(item)



username ="alvinpoudels@gmail.com"
password =getpass.getpass()
client = fbchat.Client(username, password) 


	#friends = client.fetchAllUsers() # return a list of names 
name = "Krishna Khadka"
friend = client.searchForUsers(name)
user = friend[0]
while True:
	message = client.fetchThreadMessages(user.uid)
	str_message = message.text
	if str_message.lower()== "bye":
		client.send(Message(str("Good Bye")),user.uid,user.type)
		break
	else:
		reply = (my_bot.get_response(str_message))
		print("Sending reply: %s" % reply)
		client.send(Message(str(reply)),user.uid,user.type)
		


client.logout()
