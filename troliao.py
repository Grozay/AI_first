import speech_recognition 
from datetime import date , datetime
import pyttsx3
robot_ear = speech_recognition.Recognizer()
robot_say = pyttsx3.init()
robot_brand = ""
    
while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.listen(mic)
        
    print("Robot: ...")
        
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
        
    print('You: '  + you)

    if you == "":
        robot_brand = "I Can't Understand"
    elif "hello" in you:
        robot_brand = "hello"
    elif "how are you" in you:
        robot_brand = "I am fine"
    elif 'today' in you:
        today = date.today()
        robot_brand = today.strftime("%B %d, %Y")
    elif 'time' in you:
        now = datetime.now()
        robot_brand = now.strftime("%H:%M:%S")
    elif 'bye' in you:
        print('Robot: '+ robot_brand)
        robot_say.say(robot_brand)
        robot_say.runAndWait()
        break
    elif "how are you doing" in you:
        robot_brand = "I am also fine"
        
    print('Robot: '+ robot_brand)
    robot_say.say(robot_brand)
    robot_say.runAndWait()