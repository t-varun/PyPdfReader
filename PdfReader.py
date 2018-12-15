import pyttsx3  #pywin32 required
import PyPDF2

engine = pyttsx3.init()
file = open('unit-3 full notes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(file)
n = pdfReader.numPages
for i in range(n):
    # creating a page object 
    pageObj = pdfReader.getPage(i) 
      
    # extracting text from page 
    engine.say(pageObj.extractText()) 
      
file.close() 
engine.runAndWait()
