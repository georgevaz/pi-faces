import speech_recognition as sr

def run_speech_recognition():
    # Initialize the recognizer 
    r = sr.Recognizer()

    # Loop infinitely for user to
    # speak
    response = ''
    while(not response):    
        
        # Exception handling to handle
        # exceptions at the runtime
        try:
            print('Listening...')
            # use the microphone as source for input.
            with sr.Microphone() as mic_source:
                
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level 
                r.adjust_for_ambient_noise(mic_source, duration=0.2)
                
                #listens for the user's input 
                user_input = r.listen(mic_source, 10)
                
                # Using google to recognize audio
                speech_to_text = r.recognize_google(user_input)
                speech_to_text = speech_to_text.lower()

                print("\nYou said: ", speech_to_text)
                response = speech_to_text
                return response
                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("unknown error occurred")

    