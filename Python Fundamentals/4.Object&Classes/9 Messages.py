#Messages

#Solution_1

import itertools as it


class User:
    def __init__(self, username, received_messages=[]):
        self.username = username
        self.received_messages = received_messages

    def add_received_messages(self, message):
        if not self.received_messages:
            self.received_messages = []
            # a new empty list because else it shares the same list from the default with the other Users
        self.received_messages += [message]

    def __str__(self):
        return self.username


class Message:
    def __init__(self, content, sender):
        self.content = content
        self.sender = sender


def main():
    data = input()
    usernames_list = []  # registered users
    while data != 'exit':
        registered_usernames = [obj.username for obj in usernames_list]
        data = data.split()
        if data[0] == 'register':
            username = data[1]
            user = User(username)
            if username not in registered_usernames:
                usernames_list.append(user)
        else:
            sender = data[0]
            recipient = data[2]
            content = data[3:]  # returns a list
            if sender in registered_usernames and recipient in registered_usernames:
                for obj in usernames_list:
                    if obj.username == recipient:
                        User.add_received_messages(obj, Message(*content, sender))
        data = input()

    user_sender, user_recipient = input().split()

    filtered_usernames = list(filter(lambda x: x.username == user_sender or x.username == user_recipient,
                                     usernames_list))

    recipient_received_msgs = [msg.content
                               for obj in filtered_usernames
                               if obj.username == user_recipient
                               for msg in obj.received_messages
                               if msg.sender == user_sender
                               ]
    sender_received_msgs = [msg.content
                            for obj in filtered_usernames
                            if obj.username == user_sender
                            for msg in obj.received_messages
                            if msg.sender == user_recipient
                            ]

    conversation = list(it.zip_longest(recipient_received_msgs, sender_received_msgs))
    if not conversation:
        print("No messages")
        return

    for pair in conversation:
        if pair[0]:
            print(f"{user_sender}: {pair[0]}")
        if pair[1]:
            print(f"{pair[1]} :{user_recipient}")


if __name__ == '__main__':
    main()


#Solution_2

# from pprint import pprint        # Prints debugging output each class attribute on a new line


class User:

    def __init__(self, username):
        self.username = username
        self.received_messages = []

    def add_message(self, message):
        self.received_messages.append(message)

    # """ To print the class objects if the class is nested """
    # def __repr__(self):
    #     return str(vars(self))


class Message:

    def __init__(self, content, sender):
        self.content = content
        self.sender = sender

    """ To print the class objects if the class is nested """

    def __repr__(self):
        return str(vars(self))


users = []
messages = []  # Not in use

while True:
    cin = input()

    if cin == "exit":
        break

    entered = list(map(str, cin.split()))

    if len(entered) == 2 and entered[0] == "register":
        not_found = True
        for i in range(len(users)):
            if users[i].username == entered[1]:
                not_found = False
                break
        if not_found:
            users.append(User(entered[1]))

    if len(entered) == 4 and entered[1] == "send":
        if any(x.username == entered[0] for x in users) and any(x.username == entered[2] for x in users):

            messages.append(Message(entered[3], entered[0]))  # Not in use

            for user in users:  # Looping through list of objects and searching attribute
                if user.username == entered[2]:
                    user.add_message(Message(entered[3], entered[0]))
                    # user.add_message(entered[3])
                    break

persons = tuple(map(str, input().split()))
user_1_filtered = []
user_2_filtered = []

for i in range(len(users)):
    if users[i].username == persons[1]:
        for j in range(len(users[i].received_messages)):
            if users[i].received_messages[j].sender == persons[0]:
                user_1_filtered.append(users[i].received_messages[j].content)

for i in range(len(users)):
    if users[i].username == persons[0]:
        for j in range(len(users[i].received_messages)):
            if users[i].received_messages[j].sender == persons[1]:
                user_2_filtered.append(users[i].received_messages[j].content)

if user_1_filtered == [] and user_2_filtered == []:
    print("No messages")
else:
    for i in range(max(len(user_1_filtered), len(user_2_filtered))):
        if i < len(user_1_filtered):
            print(f"{persons[0]}: {user_1_filtered[i]}")
        if i < len(user_2_filtered):
            print(f"{user_2_filtered[i]} :{persons[1]}")

""" Test section follows """

# print(user_1_filtered)
# print(user_2_filtered)
#
# for item in users:
#     pprint(vars(item))
#
# for item in messages:
#     pprint(vars(item))


#Solution_3

class Message:
    def __init__(self, content, sender):
        self.content = content
        self.sender = sender


class User:
    def __init__(self, username):
        self.username = username
        self.messages = []


users = dict()

while True:
    info = input().split(" ")
    if len(info) == 1:
        break

    if len(info) == 2:
        username = info[1]
        users.__setitem__(username, User(username))

    if len(info) > 2:
        sender = info[0]
        receiver = info[2]
        content = info[3]

        # Check if both users exists
        if users.__contains__(sender) and users.__contains__(receiver):
            sms = Message(content, sender)
            users[receiver].messages.append(sms)

chat = input().split(" ")
messagesOfSecond = list(filter(lambda x: x.sender == chat[1], users[chat[0]].messages))
messagesOfFirst = list(filter(lambda x: x.sender == chat[0], users[chat[1]].messages))
conversation = list(zip(messagesOfFirst + [None] * (len(messagesOfSecond) - len(messagesOfFirst)),
                        messagesOfSecond + [None] * (len(messagesOfFirst) - len(messagesOfSecond))))

if conversation.__len__() == 0:
    print("No messages")
    exit()

for ch in conversation:
    if ch[0] != None:
        print(f"{ch[0].sender}: {ch[0].content}")

    if ch[1] != None:
        print(f"{ch[1].content} :{ch[1].sender}")