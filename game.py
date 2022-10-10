import json

json_file_path = "data.json"
chapter = "1"
is_alive = True

with open(json_file_path, "r") as j:
    data = json.loads(j.read())


def check_choice(chap):
    choice = input("what do you want to do? : ")
    if choice in data[chap]["options"]:
        return choice
    else : 
        print("That was not a valid choice ... ")
        return


def print_text(chap, d):
    global chapter
    print(d[chap]["text"])
    for i in data[chap]["options"]:
        print(i + ") " + data[chap]["options"][i]["text"]) 
    choice = check_choice(chap)
    if choice != None:
        chapter = data[chap]["options"][choice]["direction"]

while is_alive == True :
    print_text(chapter, data)
    
