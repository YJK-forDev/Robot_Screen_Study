import sys
import time
from naoqi import ALProxy
sys.path.append('/home/yujin/Desktop/robot/pepperchat/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages')

Scenario, Visual_Content, Visual_Type, Timing, Layout_Amount, Layout_Synchronocity = sys.argv[1:7]
#print("Visual_Content:", Visual_Content)
#print("Visual_Type:", Visual_Type)


pepper_ip="10.134.71.248"
port = 9559

motionProxy = ALProxy("ALMotion", pepper_ip, port)
motionProxy.setDiagnosisEffectEnabled(False)

tts=ALProxy("ALTextToSpeech", pepper_ip, port)
tablet_service = ALProxy("ALTabletService", pepper_ip, port)

if Scenario == "Scenario1":
    if Visual_Content == "Verbal related object" and Visual_Type == "Image":
        if Layout_Amount == "Multiple" and Layout_Synchronocity == "Multiple":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_VVMM.html")
                time.sleep(1.2)
                tts.say("Do you mean the corn sugar?")
                time.sleep(1.2)     
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")       
            elif Timing == "During-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_VVMM.html")
                tts.say("Do you mean the corn sugar?")
                time.sleep(2.2) 
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("Do you mean the corn sugar?")
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_VVMM.html")
                time.sleep(2.2)
        elif Layout_Amount == "Multiple" and Layout_Synchronocity == "One":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_VVMO_1.html")
                time.sleep(1)
                tts.say("Do you mean the corn sugar?") 
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_VVMO_2.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "During-Speech":
                tts.post.say("Do you mean the corn sugar?")
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_VVMO_1.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_VVMO_2.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("Do you mean the corn sugar?")
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_VVMO_1.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_VVMO_2.html")
                time.sleep(1)
        elif Layout_Amount == "One" and Layout_Synchronocity == "One":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_VVOO.html")
                time.sleep(1.2)
                tts.say("Do you mean the corn sugar?")
                time.sleep(1.2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")         
            elif Timing == "During-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_VVOO.html")
                tts.say("Do you mean the corn sugar?")
                time.sleep(2.2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("Do you mean the corn sugar?")
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_VVOO.html")
                time.sleep(2.2)
    elif Visual_Content == "Verbal related object" and Visual_Type == "Text":
        if Layout_Amount == "Multiple" and Layout_Synchronocity == "Multiple":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_VTMM.html")
                time.sleep(1.2)
                tts.say("Do you mean the corn sugar?")
                time.sleep(1.2)     
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")       
            elif Timing == "During-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_VTMM.html")
                tts.say("Do you mean the corn sugar?")
                time.sleep(2.2) 
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("Do you mean the corn sugar?")
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_VTMM.html")
                time.sleep(2.2)
        elif Layout_Amount == "Multiple" and Layout_Synchronocity == "One":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_VTMO_1.html")
                time.sleep(1)
                tts.say("Do you mean the corn sugar?") 
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_VTMO_2.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "During-Speech":
                tts.post.say("Do you mean the corn sugar?")
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_VTMO_1.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_VTMO_2.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("Do you mean the corn sugar?")
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_VTMO_1.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_VTMO_2.html")
                time.sleep(1)
        elif Layout_Amount == "One" and Layout_Synchronocity == "One":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_VTOO.html")
                time.sleep(1.2)
                tts.say("Do you mean the corn sugar?")
                time.sleep(1.2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")         
            elif Timing == "During-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_VTOO.html")
                tts.say("Do you mean the corn sugar?")
                time.sleep(2.2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("Do you mean the corn sugar?")
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_VTOO.html")
                time.sleep(2.2)
    elif Visual_Content == "Emotion" and Visual_Type == "Text":
        if Layout_Amount == "Multiple" and Layout_Synchronocity == "Multiple":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_ETMM.html")
                time.sleep(1.2)
                tts.say("Do you mean the corn sugar?")
                time.sleep(1.2)     
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")       
            elif Timing == "During-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_ETMM.html")
                tts.say("Do you mean the corn sugar?")
                time.sleep(2.2) 
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("Do you mean the corn sugar?")
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_ETMM.html")
                time.sleep(2.2)
        elif Layout_Amount == "Multiple" and Layout_Synchronocity == "One":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_ETMO_1.html")
                time.sleep(1)
                tts.say("Do you mean the corn sugar?") 
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_ETMO_2.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "During-Speech":
                tts.post.say("Do you mean the corn sugar?")
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_ETMO_1.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_ETMO_2.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("Do you mean the corn sugar?")
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_ETMO_1.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_ETMO_2.html")
                time.sleep(1)
        elif Layout_Amount == "One" and Layout_Synchronocity == "One":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_ETOO.html")
                time.sleep(1.2)
                tts.say("Do you mean the corn sugar?")
                time.sleep(1.2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")         
            elif Timing == "During-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_ETOO.html")
                tts.say("Do you mean the corn sugar?")
                time.sleep(2.2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("Do you mean the corn sugar?")
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_ETOO.html")
                time.sleep(2.2)
    elif Visual_Content == "Emotion" and Visual_Type == "Image":
        if Layout_Amount == "Multiple" and Layout_Synchronocity == "Multiple":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_EVMM.html")
                time.sleep(1.2)
                tts.say("Do you mean the corn sugar?")
                time.sleep(1.2)     
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")       
            elif Timing == "During-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_EVMM.html")
                tts.say("Do you mean the corn sugar?")
                time.sleep(2.2) 
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("Do you mean the corn sugar?")
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_EVMM.html")
                time.sleep(2.2)
        elif Layout_Amount == "Multiple" and Layout_Synchronocity == "One":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_EVMO_1.html")
                time.sleep(1)
                tts.say("Do you mean the corn sugar?") 
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_EVMO_2.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "During-Speech":
                tts.post.say("Do you mean the corn sugar?")
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_EVMO_1.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_EVMO_2.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("Do you mean the corn sugar?")
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_EVMO_1.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_EVMO_2.html")
                time.sleep(1)
        elif Layout_Amount == "One" and Layout_Synchronocity == "One":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_EVOO.html")
                time.sleep(1.2)
                tts.say("Do you mean the corn sugar?")
                time.sleep(1.2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")         
            elif Timing == "During-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_EVOO.html")
                tts.say("Do you mean the corn sugar?")
                time.sleep(2.2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("Do you mean the corn sugar?")
                tablet_service.showWebview("http://10.134.71.232:8000/SC1_EVOO.html")
                time.sleep(2.2)


elif Scenario == "Scenario2":
    if Visual_Content == "Verbal related object" and Visual_Type == "Image":
        if Layout_Amount == "Multiple" and Layout_Synchronocity == "Multiple":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_VVMM.html")
                time.sleep(1.2)
                tts.say("But the box was torn, when it was delivered.")
                time.sleep(1.2)     
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")       
            elif Timing == "During-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_VVMM.html")
                tts.say("But the box was torn, when it was delivered.")
                time.sleep(2.2) 
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("But the box was torn, when it was delivered.")
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_VVMM.html")
                time.sleep(2.2)
        elif Layout_Amount == "Multiple" and Layout_Synchronocity == "One":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_VVMO_1.html")
                time.sleep(1)
                tts.say("But the box was torn, when it was delivered.") 
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_VVMO_2.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "During-Speech":
                tts.post.say("But the box was torn, when it was delivered.")
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_VVMO_1.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_VVMO_2.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("But the box was torn, when it was delivered.")
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_VVMO_1.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_VVMO_2.html")
                time.sleep(1)
        elif Layout_Amount == "One" and Layout_Synchronocity == "One":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_VVOO.html")
                time.sleep(1.2)
                tts.say("But the box was torn, when it was delivered.")
                time.sleep(1.2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")         
            elif Timing == "During-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_VVOO.html")
                tts.say("But the box was torn, when it was delivered.")
                time.sleep(2.2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("But the box was torn, when it was delivered.")
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_VVOO.html")
                time.sleep(2.2)
    elif Visual_Content == "Verbal related object" and Visual_Type == "Text":
        if Layout_Amount == "Multiple" and Layout_Synchronocity == "Multiple":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_VTMM.html")
                time.sleep(1.2)
                tts.say("But the box was torn, when it was delivered.")
                time.sleep(1.2)     
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")       
            elif Timing == "During-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_VTMM.html")
                tts.say("But the box was torn, when it was delivered.")
                time.sleep(2.2) 
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("But the box was torn, when it was delivered.")
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_VTMM.html")
                time.sleep(2.2)
        elif Layout_Amount == "Multiple" and Layout_Synchronocity == "One":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_VTMO_1.html")
                time.sleep(1)
                tts.say("But the box was torn, when it was delivered.") 
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_VTMO_2.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "During-Speech":
                tts.post.say("But the box was torn, when it was delivered.")
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_VTMO_1.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_VTMO_2.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("But the box was torn, when it was delivered.")
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_VTMO_1.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_VTMO_2.html")
                time.sleep(1)
        elif Layout_Amount == "One" and Layout_Synchronocity == "One":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_VTOO.html")
                time.sleep(1.2)
                tts.say("But the box was torn, when it was delivered.")
                time.sleep(1.2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")         
            elif Timing == "During-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_VTOO.html")
                tts.say("But the box was torn, when it was delivered.")
                time.sleep(2.2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("But the box was torn, when it was delivered.")
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_VTOO.html")
                time.sleep(2.2)
    elif Visual_Content == "Emotion" and Visual_Type == "Text":
        if Layout_Amount == "Multiple" and Layout_Synchronocity == "Multiple":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_ETMM.html")
                time.sleep(1.2)
                tts.say("But the box was torn, when it was delivered.")
                time.sleep(1.2)     
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")       
            elif Timing == "During-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_ETMM.html")
                tts.say("But the box was torn, when it was delivered.")
                time.sleep(2.2) 
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("But the box was torn, when it was delivered.")
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_ETMM.html")
                time.sleep(2.2)
        elif Layout_Amount == "Multiple" and Layout_Synchronocity == "One":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_ETMO_1.html")
                time.sleep(1)
                tts.say("But the box was torn, when it was delivered.") 
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_ETMO_2.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "During-Speech":
                tts.post.say("But the box was torn, when it was delivered.")
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_ETMO_1.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_ETMO_2.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("But the box was torn, when it was delivered.")
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_ETMO_1.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_ETMO_2.html")
                time.sleep(1)
        elif Layout_Amount == "One" and Layout_Synchronocity == "One":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_ETOO.html")
                time.sleep(1.2)
                tts.say("But the box was torn, when it was delivered.")
                time.sleep(1.2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")         
            elif Timing == "During-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_ETOO.html")
                tts.say("But the box was torn, when it was delivered.")
                time.sleep(2.2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("But the box was torn, when it was delivered.")
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_ETOO.html")
                time.sleep(2.2)
    elif Visual_Content == "Emotion" and Visual_Type == "Image":
        if Layout_Amount == "Multiple" and Layout_Synchronocity == "Multiple":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_EVMM.html")
                time.sleep(1.2)
                tts.say("But the box was torn, when it was delivered.")
                time.sleep(1.2)     
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")       
            elif Timing == "During-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_EVMM.html")
                tts.say("But the box was torn, when it was delivered.")
                time.sleep(2.2) 
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("But the box was torn, when it was delivered.")
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_EVMM.html")
                time.sleep(2.2)
        elif Layout_Amount == "Multiple" and Layout_Synchronocity == "One":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_EVMO_1.html")
                time.sleep(1)
                tts.say("But the box was torn, when it was delivered.") 
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_EVMO_2.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "During-Speech":
                tts.post.say("But the box was torn, when it was delivered.")
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_EVMO_1.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_EVMO_2.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("But the box was torn, when it was delivered.")
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_EVMO_1.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_EVMO_2.html")
                time.sleep(1)
        elif Layout_Amount == "One" and Layout_Synchronocity == "One":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_EVOO.html")
                time.sleep(1.2)
                tts.say("But the box was torn, when it was delivered.")
                time.sleep(1.2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")         
            elif Timing == "During-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_EVOO.html")
                tts.say("But the box was torn, when it was delivered.")
                time.sleep(2.2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("But the box was torn, when it was delivered.")
                tablet_service.showWebview("http://10.134.71.232:8000/SC2_EVOO.html")
                time.sleep(2.2)

elif Scenario == "Scenario3":
    if Visual_Content == "Verbal related object" and Visual_Type == "Image":
        if Layout_Amount == "Multiple" and Layout_Synchronocity == "Multiple":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_VVMM.html")
                time.sleep(1.2)
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                time.sleep(1.2)     
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")       
            elif Timing == "During-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_VVMM.html")
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                time.sleep(2.2) 
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_VVMM.html")
                time.sleep(2.2)
        elif Layout_Amount == "Multiple" and Layout_Synchronocity == "One":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_VVMO_1.html")
                time.sleep(1)
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!") 
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_VVMO_2.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "During-Speech":
                tts.post.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_VVMO_1.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_VVMO_2.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_VVMO_1.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_VVMO_2.html")
                time.sleep(1)
        elif Layout_Amount == "One" and Layout_Synchronocity == "One":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_VVOO.html")
                time.sleep(1.2)
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                time.sleep(1.2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")         
            elif Timing == "During-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_VVOO.html")
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                time.sleep(2.2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_VVOO.html")
                time.sleep(2.2)
    elif Visual_Content == "Verbal related object" and Visual_Type == "Text":
        if Layout_Amount == "Multiple" and Layout_Synchronocity == "Multiple":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_VTMM.html")
                time.sleep(1.2)
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                time.sleep(1.2)     
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")       
            elif Timing == "During-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_VTMM.html")
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                time.sleep(2.2) 
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_VTMM.html")
                time.sleep(2.2)
        elif Layout_Amount == "Multiple" and Layout_Synchronocity == "One":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_VTMO_1.html")
                time.sleep(1)
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!") 
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_VTMO_2.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "During-Speech":
                tts.post.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_VTMO_1.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_VTMO_2.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_VTMO_1.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_VTMO_2.html")
                time.sleep(1)
        elif Layout_Amount == "One" and Layout_Synchronocity == "One":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_VTOO.html")
                time.sleep(1.2)
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                time.sleep(1.2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")         
            elif Timing == "During-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_VTOO.html")
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                time.sleep(2.2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_VTOO.html")
                time.sleep(2.2)
    elif Visual_Content == "Emotion" and Visual_Type == "Text":
        if Layout_Amount == "Multiple" and Layout_Synchronocity == "Multiple":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_ETMM.html")
                time.sleep(1.2)
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                time.sleep(1.2)     
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")       
            elif Timing == "During-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_ETMM.html")
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                time.sleep(2.2) 
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_ETMM.html")
                time.sleep(2.2)
        elif Layout_Amount == "Multiple" and Layout_Synchronocity == "One":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_ETMO_1.html")
                time.sleep(1)
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!") 
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_ETMO_2.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "During-Speech":
                tts.post.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_ETMO_1.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_ETMO_2.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_ETMO_1.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_ETMO_2.html")
                time.sleep(1)
        elif Layout_Amount == "One" and Layout_Synchronocity == "One":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_ETOO.html")
                time.sleep(1.2)
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                time.sleep(1.2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")         
            elif Timing == "During-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_ETOO.html")
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                time.sleep(2.2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_ETOO.html")
                time.sleep(2.2)
    elif Visual_Content == "Emotion" and Visual_Type == "Image":
        if Layout_Amount == "Multiple" and Layout_Synchronocity == "Multiple":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_EVMM.html")
                time.sleep(1.2)
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                time.sleep(1.2)     
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")       
            elif Timing == "During-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_EVMM.html")
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                time.sleep(2.2) 
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_EVMM.html")
                time.sleep(2.2)
        elif Layout_Amount == "Multiple" and Layout_Synchronocity == "One":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_EVMO_1.html")
                time.sleep(1)
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!") 
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_EVMO_2.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "During-Speech":
                tts.post.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_EVMO_1.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_EVMO_2.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_EVMO_1.html")
                time.sleep(2)
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_EVMO_2.html")
                time.sleep(1)
        elif Layout_Amount == "One" and Layout_Synchronocity == "One":
            if Timing == "Before-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_EVOO.html")
                time.sleep(1.2)
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                time.sleep(1.2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")         
            elif Timing == "During-Speech":
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_EVOO.html")
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                time.sleep(2.2)
                tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
            elif Timing == "After-Speech":
                tts.say("The fennec fox, has big ears, that help it stay cool in the desert!")
                tablet_service.showWebview("http://10.134.71.232:8000/SC3_EVOO.html")
                time.sleep(2.2)


time.sleep(1.3)
tablet_service.showWebview("http://10.134.71.232:8000/Blank.html")
print(tablet_service)

