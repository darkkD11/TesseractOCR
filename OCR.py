import PIL.Image
import PIL.ImageTk
import pytesseract
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *


class OcrTesseract():

    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
        window = tk.Tk()
        window.state('zoomed')
        window.title('OCR ~ By darkkD11')
        # Code to add widgets will go here...
        # Added "container" Frame.
        topFrame = Frame(window, padx=10, pady=10,
                         highlightbackground="green", highlightthickness=3)
        topFrame.pack(side=TOP, fill=X, padx=10, pady=10)

        titleLabel = Label(topFrame, font=('arial', 12, 'bold'), text="OCR")
        titleLabel.pack(side=LEFT)

        b1 = Button(topFrame, text="BROWSE", command=self.browseFiles)
        b1.pack(side=RIGHT)

        frame1 = LabelFrame(window, text="Image Viewer", padx=50, pady=50)
        frame1.pack(side=LEFT, expand=False, fill=BOTH, padx=10, pady=10)

        img = PIL.ImageTk.PhotoImage(PIL.Image.open(".\images\\banana.jpg"))
        self.panel = Label(frame1, image=img)
        self.panel.pack(side="bottom", fill=BOTH, expand=False)

        frame2 = LabelFrame(window, text="Output Text", padx=50, pady=50)
        frame2.pack(side=LEFT, expand=True, fill=BOTH, padx=10, pady=10)

        quote = "Output will be shown Here"
        self.text1 = Text(frame2)
        self.text1.pack(side="bottom", fill=BOTH, expand=True)
        self.text1.insert(END, quote)

        window.mainloop()

    def process_image(self, image_name, lang_code):
        return pytesseract.image_to_string(PIL.Image.open(image_name), lang=lang_code)

    def print_data(self, data):
        print(data)

    def setTextInput(self, text):
        self.text1.delete(1.0, END)
        self.text1.insert(END, text)

    def output_file(self, filename, data):
        file = open(filename, "a+")
        file.write(data)
        file.close()
        self.setTextInput(data)

    def browseFiles(self):
        open('Output.txt', 'w').close()
        root = tk.Tk()
        root.withdraw()
        filepath = filedialog.askopenfilename(
            initialdir="/", title="Select a File", filetypes=(("Images", "*.jpg *.jpeg *.png *.bmp"), ("All Files", "*.*")))
        print(filepath)
        self.updateImage(filepath)
        data_ind = self.process_image(filepath, "eng")
        self.print_data(data_ind)
        self.output_file("Output.txt", data_ind)

    def updateImage(self, path):
        img2 = PIL.ImageTk.PhotoImage(PIL.Image.open(path))
        self.panel.configure(image=img2)
        self.panel.image = img2


ocrTesseract = OcrTesseract()
