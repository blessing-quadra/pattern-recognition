import pyttsx3;

def readText(statement):
    t2s = pyttsx3.init()
    rate = t2s.getProperty('rate')
    t2s.setProperty('rate', rate-
    70)
    # statement = "The oracle says we should greet you and that, the purpose of your coming is going to be positive"
    t2s.say(statement)

    t2s.runAndWait()