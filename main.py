import openai
import pyttsx3
import speech_recognition as sr
import time

openai.api_key="YOUR_OPENAI_API_KEY"

# Initialize the speech engine
engine = pyttsx3.init()

def audio_to_text(filename):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # open the file
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = recognizer.record(source)
        try:
            # recognize (convert from speech to text)
            text = recognizer.recognize_google(audio_data, language='es-CO')
            return text
        except:
            print('Skipping unknown error')

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1000,
        n=1,                
        stop=None
    )
    return response.choices[0].text

def text_to_audio(text):
    engine.say(text)
    engine.runAndWait()

def main():
    for voice in engine.getProperty('voices'):
        
        print(voice)
    while True:
    # Wait for user to say "genius"
        print("Say 'Genius' to start recording your question..." )
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer. listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower()=="genius":
                    # Record audio
                    filename="input .wav"
                    print("Say your question..." )
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source,phrase_time_limit=None,timeout=None)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())
                        
                        # Transcribe audio to text
                        text=audio_to_text(filename)
                        if text:
                            print(f"You said: {text}" )
                            
                            # Generate response using GPT-3
                            response = generate_response(text)
                            print(f"GPT-3 says: {response}")

                            # Read response using text—to-speech
                            text_to_audio(response)
            except Exception as e:
                print("An error occurred: {}".format(e))
        
if __name__ == "__main__":
    main()
