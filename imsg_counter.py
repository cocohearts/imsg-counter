from imessage_tools import read_messages, print_messages, send_message
# Also requires terminal to have full access to disk, as described https://osxdaily.com/2018/10/09/fix-operation-not-permitted-terminal-error-macos/

# Path to the chat.db file
chat_db = "/Users/Me/Library/Messages/chat.db"
# Path to the vcf contacts file
path = "/Users/Me/Downloads/contacts.vcf"

# Phone number or label for "you"
self_number = "Me"
# Number of messages to return
n = input("Number of messages to return: ")

# Read the messages
messages = read_messages(chat_db, n=n, self_number=self_number, human_readable_date=True)

all_msg_count_dict = {}
their_msg_count_dict = {}
my_msg_count_dict = {}

def increment(mydict, mykey):
    if mykey not in mydict:
        mydict[mykey] = 1
    else:
        mydict[mykey] += 1

for message in messages:
    if message['group_chat_name'] != '': continue

    phone_number = message['phone_number']
    increment(all_msg_count_dict,phone_number)
    if message['is_from_me']:
        increment(their_msg_count_dict,phone_number)
    else:
        increment(my_msg_count_dict,phone_number)

mylist = list(all_msg_count_dict.values())
mylist.sort(reverse=True)

def fetch(mydict, key):
    if key not in mydict:
        return '0'
    return mydict[key]

def namefetch(mydict, key):
    if key not in mydict:
        return key
    return mydict[key]

def parse_vcard_name_num(path):
    with open(path, 'r') as f:

        num_name_dict = {}
        for line in f:
            if line[:2]=='FN':
                name = line[3:-1]
            if line[:3]=='TEL':
                raw_number = line[4:-1]
                real_number = ""
                if "+" not in raw_number:
                    real_number = "+1"
                for char in raw_number:
                    if char=="+" or char.isdigit():
                        real_number += char
                try:
                    num_name_dict[real_number] = name
                except:
                    pass
    return num_name_dict

num_name_dict = parse_vcard_name_num(path)

def top(n):
    prev_value = -1
    for value in mylist[:n]:
        if (value == prev_value):
            continue
        prev_value = value

        keys = [key for key in all_msg_count_dict if all_msg_count_dict[key]==value]
        print([[fetch(all_msg_count_dict,key),fetch(their_msg_count_dict,key),fetch(my_msg_count_dict,key),namefetch(num_name_dict,key)] for key in keys])
