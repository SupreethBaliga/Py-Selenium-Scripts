import time 
import fbchat 
from getpass import getpass 
username = str(input("Username: ")) 
client = fbchat.Client(username, getpass()) 
no_of_friends = int(input("Number of friends: "))
for i in range(no_of_friends): 
    name = str(input("Name: ")) 
    friends = client.searchForUsers(name) # return a list of names 
    friend = friends[0]
    print(friend) 
    msg = "sarthak is waving at you" 
    for j in range (0,500):
        sent = client.sendMessage(msg, thread_id=friend.uid) 
        if sent: 
            print("Message sent successfully!")
        time.sleep(1)
