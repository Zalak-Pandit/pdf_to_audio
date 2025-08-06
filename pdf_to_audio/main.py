import pyttsx3
import PyPDF2

def pdf_to_audio(pdf_path):

    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""


        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text() + "\n"


    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  
    engine.setProperty('volume', 1.0) 

  
    engine.say(text)
    engine.runAndWait()


pdf_to_audio("Digital Document Permission Web Application.pdf")
