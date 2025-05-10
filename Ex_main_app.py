from flask import Flask, render_template, request, redirect, url_for
import subprocess
import os
from flask import send_from_directory
#from my_screen_variation.screenVariation import screenVariation

app = Flask(__name__)
env=os.environ.copy()
env["PYTHONPATH"] = "/home/yujin/Desktop/robot/pepperchat/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages"

test_count = 0

@app.route("/")
def index():
    return render_template("./Ex_main_page.html")

@app.route("/Scenario/<path:filename>")
def serve_scenario_html(filename):
    folder = os.path.join(app.root_path, "screenHTML", "Scenario")
    return send_from_directory(folder, filename)

@app.route("/button_click", methods=["POST"])
def button_click():
    global test_count
    Visual_Content= "none"
    Visual_Type = "none"

    Timing = "none"

    Layout_Amount= "none"
    Layout_Synchronocity = "none"


    button_pressed = request.form['button']
    if button_pressed=='test':

        #Dimension: Timing
        
        #selected_Timing = request.form.get('Timing')
        selected_Timing = request.form.get('choiceSlider')
        
        if selected_Timing == "1":
            Timing = "Before-Speech"
        elif selected_Timing == "2":
           Timing = "During-Speech"
        elif selected_Timing == "3":
            Timing = "After-Speech"

        '''
        if selected_Timing == "Before-Speech":
            Timing = "Before-Speech"
        elif selected_Timing == "During-Speech":
           Timing = "During-Speech"
        elif selected_Timing == "After-Speech":
            Timing = "After-Speech"
        '''

        #Dimension: Content
        selected_VisualType = request.form.get('VisualType')
        if selected_VisualType == "Text":
            Visual_Type = "Text"
        elif selected_VisualType == "Image":
            Visual_Type = "Image"

        selected_VisualContent = request.form.get('VisualContent')
        if selected_VisualContent == "Emotion":
            Visual_Content = "Emotion"
        elif selected_VisualContent == "Verbal related object":
            Visual_Content = "Verbal related object"

        
        
        #Dimension: Layout
        selected_Amount = request.form.get('Amount')
  
        if selected_Amount == "One":
            Layout_Amount = "One"
        elif selected_Amount == "Multiple":
            Layout_Amount = "Multiple"
 

        selected_Synchronocity = request.form.get('Synchronocity')
  
        if selected_Synchronocity == "One":
            Layout_Synchronocity = "One"
        elif selected_Synchronocity == "Multiple":
            Layout_Synchronocity = "Multiple"

        Scenario = request.form.get('Scenario')
        
        subprocess.call(["python2", "Ex_Screen.py", Scenario, Visual_Content, Visual_Type, Timing, Layout_Amount, Layout_Synchronocity], env=env)

        test_count+=1
        print("PUSHED TEST BUTTON")
        return "", 204
    
    elif button_pressed=="preview":
        print("PUSHED PREVIEW BUTTON")
        return "Preview button was clicked!"
    
    elif button_pressed=='save':
        print("PUSHED SAVE BUTTON")
        Scenario = request.form.get('Scenario')

        #Dimension: Timing
        
        selected_Timing_num = request.form.get('choiceSlider')
        if selected_Timing_num == "1":
            selected_Timing = "Before-Speech"
        elif selected_Timing_num == "2":
            selected_Timing == "During-Speech"
        elif selected_Timing_num == "3":
            selected_Timing = "After-Speech"
        
        #Dimension: Content
        selected_VisualType = request.form.get('VisualType')
        selected_VisualContent = request.form.get('VisualContent')
        
        #Dimension: Layout
        selected_Amount = request.form.get('Amount')
        selected_Synchronocity = request.form.get('Synchronocity')
        
        

        participant_number = request.form["textfield"]
        with open("log.txt","a") as file:
            file.write("\nParticipant Number : "+str(participant_number))
            file.write("\nTest Count : "+str(test_count))
            file.write("\nScenario : "+Scenario)
            file.write("\nTiming : "+selected_Timing)
            file.write("\nVisual Type : "+selected_VisualType)
            file.write("\nVisual Content : "+selected_VisualContent)
            file.write("\nAmount : "+selected_Amount)
            file.write("\nSynchronocity : "+selected_Synchronocity)
            file.write("\n***************************************\n")
        test_count=0




        
        return "", 204

if __name__ == '__main__':
    app.run(debug=True)