print("Welcome to speed quiz")
# In this program we want to the user to get answers to the quiz
# and also how they scored
# the print function will enable one to see the output
# for the score, score = 0 will iterate through the quiz and give scores
# if the answer given is not Yes the program will stop running # since we don't know which format the user will use to answer
    # by using.lower the program turns all letters to lower case

do_quiz = input("Ready to start playing?  ")
# the input function allows the user to type something
# the space after the closing quotes is to give room for the user to input the answer
if do_quiz.lower() != "yes":
   quit()
   
print("Lets start playing")

# If its correct the system will proceed to print
do_quiz = input("What are .py files?  ").lower()
if do_quiz.lower() == "py files are python source files":
    print("Correct!")
else:
    print("Incorect!")

do_quiz = input("Define String in Python? ")
if do_quiz.lower() == "string in python is formed using a sequence of characters":
    print("Correct!")
else:
    print("Incorect!")
    
do_quiz = input("Are strings mutable or immutable?  ")
if do_quiz.lower() == "python strings are immutable":
    print("Correct!")
else:
    print("Incorect!")
    
do_quiz = input("How are strings denoted in python?  ")
if do_quiz.lower() == "using double or single quotes":
    print("Correct!")
else:
    print("Incorect!")
    
do_quiz = input("What is namespace in Python?  ")
if do_quiz.lower() == "a system that provides unique names for objects":
    print("Correct!")
else:
    print("Incorect!")
    
do_quiz = input("What is OOP?  ")
if do_quiz.lower() == "objects oriented programming":
    print("Correct!")
else:
    print("Incorect!")
    
do_quiz = input("Which command is used to delete files in Python?  ")
if do_quiz.lower() == "x.remove(filename)":
    print("Correct!")
else:
    print("Incorect!")
    
do_quiz = input("What is append used for in Python?  ")
if do_quiz == "it is used to add elements at the end of a list":
    print("Correct!")
else:
    print("Incorect!")
    
do_quiz = input("What is a boolean in Python?  ")
if do_quiz.lower() == "it contains two values, which are true and false":
    print("Correct!")
else:
    print("Incorect!")
    
do_quiz = input("What are the functions in Python?  ")
if do_quiz.lower() == "a block of code that is executable only when it is called":
    print("Correct!")
else:
    print("Incorect!")
    

    

    

