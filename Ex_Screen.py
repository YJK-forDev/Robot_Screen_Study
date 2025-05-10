import sys
import time
from naoqi import ALProxy
sys.path.append('/home/yujin/Desktop/robot/pepperchat/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages')

Scenario, Visual_Content, Visual_Type, Timing, Layout_Amount, Layout_Synchronocity = sys.argv[1:7]
#print("Visual_Content:", Visual_Content)
#print("Visual_Type:", Visual_Type)


pepper_ip="10.134.71.214"
http_ip="10.134.71.205"
port = 9559
motionProxy = ALProxy("ALMotion", pepper_ip, port)
motionProxy.setDiagnosisEffectEnabled(False)


tts=ALProxy("ALTextToSpeech", pepper_ip, port)
tablet_service = ALProxy("ALTabletService", pepper_ip, port)

if Scenario == "Scenario1":
    if Timing == "Before-Speech":
        tablet_service.showWebview("http://"+http_ip+":8000/Pepper_SC1.html")
        time.sleep(2.7)
        tts.say("Do you mean the corn sugar?")
        time.sleep(0.3)     
        tablet_service.showWebview("http://"+http_ip+":8000/Blank.html")       
    elif Timing == "During-Speech":
        tablet_service.showWebview("http://"+http_ip+":8000/Pepper_SC1.html")
        tts.say("Do you mean the corn sugar?")
        time.sleep(3.3) 
        tablet_service.showWebview("http://"+http_ip+":8000/Blank.html")
    elif Timing == "After-Speech":
        tts.say("Do you mean the corn sugar?")
        tablet_service.showWebview("http://"+http_ip+":8000/Pepper_SC1.html")
        time.sleep(3.3)
        

elif Scenario == "Scenario2":
    if Timing == "Before-Speech":
        tablet_service.showWebview("http://"+http_ip+":8000/Pepper_SC2.html")
        time.sleep(3.7)
        tts.say("But the box was torn, when it was delivered.")
        time.sleep(1.3)     
        tablet_service.showWebview("http://"+http_ip+":8000/Blank.html")       
    elif Timing == "During-Speech":
        tablet_service.showWebview("http://"+http_ip+":8000/Pepper_SC2.html")
        tts.say("But the box was torn, when it was delivered.")
        time.sleep(3.3) 
        tablet_service.showWebview("http://"+http_ip+":8000/Blank.html")
    elif Timing == "After-Speech":
        tts.say("But the box was torn, when it was delivered.")
        tablet_service.showWebview("http://"+http_ip+":8000/Pepper_SC2.html")
        time.sleep(3.3)
       

elif Scenario == "Scenario3":
    if Timing == "Before-Speech":
        tablet_service.showWebview("http://"+http_ip+":8000/Pepper_SC3.html")
        time.sleep(3.7)
        tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
        time.sleep(1.3)     
        tablet_service.showWebview("http://"+http_ip+":8000/Blank.html")       
    elif Timing == "During-Speech":
        tablet_service.showWebview("http://"+http_ip+":8000/Pepper_SC3.html")
        tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
        time.sleep(3.3) 
        tablet_service.showWebview("http://"+http_ip+":8000/Blank.html")
    elif Timing == "After-Speech":
        tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
        tablet_service.showWebview("http://"+http_ip+":8000/Pepper_SC3.html")
        time.sleep(3.3)
        
time.sleep(1.3)
tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
print(tablet_service)

