import datetime

Time = datetime.datetime.now()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return("Good Morning Sir!")

    elif hour>=12 and hour<15:
        return("Good afternoon Sir!")
    
    else:
        return("Good Evening!")

while True:
    print("USER : ",end="")
    query = input()
    print("BOT : ",end="")
    if "hello" in query or "hi" in query:
        print(wishme())
        print("\thow can i help you")
    elif "your name" in query or "who are you" in query:
        print("Hi, I am alicia, a ChatBot 😊")
        print("\tHow can I help you")
    elif "time now" in query:
        print("Sir the time is : ",Time)
    elif "bye" in query:
        print("Ok, Sir see you soon")
    else:
        print("I couldn't understand")