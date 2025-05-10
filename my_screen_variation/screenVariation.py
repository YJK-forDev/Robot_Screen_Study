import qi

def screenVariation(selected_Initiation, selected_Timing, selected_VisualType, selected_ModalityRelationship, selected_Amount, selected_Synchronocity, selected_RobotInteraction):
    
    if selected_RobotInteraction == "Speech":
        #Robot pose
        #keep the pose
    elif selected_RobotInteraction == "Gesture":
        #Robot pose
        #keep the pose




    #On-Demand
    if selected_Initiation == "On-Demand":
        
        if selected_Timing == "Before-Speech":
            if selected_ModalityRelationship == "Explaining" and selected_VisualType == "Visual-Img" and selected_Synchronocity == "Multiple":
                if selected_Amount == "Multiple":
                    #show image
                    #sleep(1)
                    #show image
                    #sleep(1)
                elif selected_Amount == "One":
                    #show image
                    #sleep(1)
            elif selected_ModalityRelationship == "Explaining" and selected_VisualType == "Visual-Img" and selected_Synchronocity == "One":
                if selected_Amount == "Multiple":
                    #show image
                    #sleep(1)
                    #show image
                    #sleep(1)
                elif selected_Amount == "One":
                    #show image
                    #sleep(1)
            #qi.AlProxy.SpeechtoTTS()
        elif selected_Timing == "During-Speech":
            #qi.AlProxy.SpeechtoTTS()
            if selected_ModalityRelationship == "Explaining" and selected_VisualType == "Visual-Img" and selected_Synchronocity == "Multiple":
                if selected_Amount == "Multiple":
                    #show image
                    #sleep(1)
                    #show image
                    #sleep(1)
                elif selected_Amount == "One":
                    #show image
                    #sleep(1)
            elif selected_ModalityRelationship == "Explaining" and selected_VisualType == "Visual-Img" and selected_Synchronocity == "One":
                if selected_Amount == "Multiple":
                    #show image
                    #sleep(1)
                    #show image
                    #sleep(1)
                elif selected_Amount == "One":
                    #show image
                    #sleep(1)
        elif selected_Timing == "After-Speech":
            #qi.AlProxy.SpeechtoTTS()
            #sleep(5)
            if selected_ModalityRelationship == "Explaining" and selected_VisualType == "Visual-Img" and selected_Synchronocity == "Multiple":
                if selected_Amount == "Multiple":
                    #show image
                    #sleep(1)
                    #show image
                    #sleep(1)
                elif selected_Amount == "One":
                    #show image
                    #sleep(1)
            elif selected_ModalityRelationship == "Explaining" and selected_VisualType == "Visual-Img" and selected_Synchronocity == "One":
                if selected_Amount == "Multiple":
                    #show image
                    #sleep(1)
                    #show image
                    #sleep(1)
                elif selected_Amount == "One":
                    #show image
                    #sleep(1)

    print("Finish!")
