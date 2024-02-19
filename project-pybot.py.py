name = input("Hi! I'm PyBot,May I know your name?")
print("Hi, " + name + "!")

questions = ["What is your age?" , "What is your hobby?" , "Do you like to play football?" , "Do you like to programming?"]
for ques in questions:
    ans = input(ques).lower()
    if(ans == "yes"):
        print("Oh! That's great!")
    elif ( ans == "no"):
        print("Oh!That's okay.")
    else:
        print("Okay, so it is " + ans)
