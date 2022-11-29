def check_Answer(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 10:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 1:
                guess = input("Sorry Wrong Answer, try again")
            attempt = attempt + 1
    if attempt == 10:
        print("The Correct answer is ",answer )
score = 0
a = input("Hello!Are you ready to start?❓❔ ")
if a=="Yes" or a=="yes":
    print("Let's begin.Reminder this quiz is from SCIENCE🌺")
    print("There will be multiple choice questions(A, B, C and D")
    print("Good luck!😊")
else:
    print("You should learn")
Answer1=input(str("1.Which sub-atomic particle gives negative electrical charge? A)proton B)nucleus C)Electron D)Neutron -->                         "))
check_Answer(Answer1, "c")
Answer2=input(str("Complete the equation below !What is magnesium+oxygen--> A)Magnesium hydroxide B)Magnesium oxide C)Magnesuim D)??????? -->                         "))
check_Answer(Answer2, "b")
Answer3=input(str("Choose the correct answer.Only write the letter of correct answer.Unreactive means.....  A)Shiny    B)Dull   C)Inert   D)Malleable -->                         "))
check_Answer(Answer3, "c")
Answer4=input("Complete the formula.Only write the letter of correct answer. Metal+acid-->...  A)Metal oxide  B)Salt+hydrogen  C)Metal hydroxide+hydrogen -->                         ")
check_Answer(Answer4, "b")
Answer5=input("Which metal is the most reactive metal?A) Gold B) Silver C)Calcuim D)Francium -->                         ")
check_Answer(Answer5, "d")
print("There will be writing tests")
Answer6=input("What is the other name for air sac.Only write the answer!!! -->                         ")
check_Answer(Answer6, "alveoli")
Answer7=input("What do you think how light goes-->                         ")
check_Answer(Answer7, "straight")
Answer8=input("Very tiny blood vessels in the body are .... Find the word instead ...-->                         ")
check_Answer(Answer8, "capillaries")
Answer9=input("What is the gas which we need for our blood -->                         ")
check_Answer(Answer9, "oxygen")
Answer10=input("What do you think, where gas goes after mouth or nose. Please do not left space!-->                         ")
check_Answer(Answer10, "voice box")
print("Your Score is "+ str(score))
A=input("Was it interesting?")
if A=="Yes" or A=="yes" or A=="YES":
    print("I think you enjoyed. Good bye!!!!!!")




            
