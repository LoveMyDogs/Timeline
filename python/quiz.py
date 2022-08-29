import getpass, sys

def question_and_answer(prompt):
    print("Question: " + prompt)
    msg = input()
    print("Answer: " + msg)
    
def question_with_response(prompt):
    print("Question: " + prompt)
    msg = input()
    return msg

questions = 5
correct = 0

print('Hello, ' + getpass.getuser() + " running " + sys.executable)
print("You will be asked " + str(questions) + " questions.")
question_and_answer("Are you ready to take a test?")

rsp = question_with_response("What is 9+9")
if rsp == "18":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

rsp = question_with_response("What is my favorite electronic device")
if rsp == "computer":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

rsp = question_with_response("Do you have any pets?")
if rsp == "Yes":
    print(rsp + " nice!")
    correct += 1
else:
    print(rsp + " hrm")
    correct += 1

rsp = question_with_response("Is this a fun quiz?")
if rsp == "no":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " herm")
    correct += 1

rsp = question_with_response("I'll let you go free now, are you enthused?")
if rsp == "Yes":
    print(rsp + " hee, rude")
    correct += 1
else:
    print(rsp + " welp")
    correct += 1

print(getpass.getuser() + " you scored " + str(correct) +"/" + str(questions))