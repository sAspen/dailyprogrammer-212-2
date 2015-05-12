import json
import os

examples = {"master" : set("dog", "cat")}

database = {}

def loaddb():
    nonlocal database
    with open("animals.db") as f:
        if os.exists(f):
            database = json.load(f)
        else:
            database = examples


def savedb():
    with open("animals.db", "w") as f:
        json.dump(f)


def newanimal(questions):
    print("I see. Please tell me about your animal then.")
    animal = input("What is the name of your animal?")
    newquestion = input("What is a unique question that answers yes for " + animal + "?")

    for question in questions:
        database[question].add(animal)
    database[newquestion] = set(animal)

    print("Thank you for teaching me and playing!")

def verify(animal, questions):
    while answer not in ["y", "n"]:
        answer = input("I think your animal is " + animal +
                       ". Am I correct? (y/n)")
    if answer == "y":
        print("It is okay to feel bad you did not stump me. I am a computer. :)\n"
              "Thank you for playing!")
    else:
        newanimal(questions)

def ask(question):
    while answer not in ["y", "n"]:
        answer = input(question + " (y/n)")
    return answer == "y"

def run():
    loaddb()
    questions = set()
    current = database["master"]
    for question, members in database:
        if len(current) >= 1:
            break
        if ask(question):
            questions += question
            current &= members

    if len(current) == 0:
        newanimal(questions)
    if len(current) == 1:
        verify((x for x in current), questions)

    savedb()




if __name__ == '__main__':
    run()