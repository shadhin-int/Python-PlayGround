import pyttsx3, PyPDF2

pdf_reader = PyPDF2.PdfFileReader(open('chapter2.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(pdf_reader.numPages):
    text = pdf_reader.getPage(page_num).extractText()
    clean_text = text.strip().replace('\n', '')
    print(clean_text)
    speaker.save_to_file('cleaned_text', 'story.mp3')
    speaker.runAndWait()
speaker.stop()