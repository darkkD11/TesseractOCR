import PIL.Image
import PIL.ImageTk
import pytesseract
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *


def process_image(image_name, lang_code):
    return pytesseract.image_to_string(Image.open(image_name), lang=lang_code)


def print_data(data):
    print(data)


def output_file(filename, data):
    file = open(filename, "a+")
    file.write(data)
    file.close()


def main():
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

    b1 = Button(topFrame, text="BROWSE")
    b1.pack(side=RIGHT)
    b2 = Button(topFrame, text="BROWSE FOLDER")
    b2.pack(side=RIGHT)

    frame1 = LabelFrame(window, text="Image Viewer", padx=50, pady=50)
    frame1.pack(side=LEFT, expand=True, fill=BOTH, padx=10, pady=10)

    img = PIL.ImageTk.PhotoImage(PIL.Image.open("banana.jpg"))
    panel = Label(frame1, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    # b1 = Button(frame1, text="BROWSE")
    # b1.pack()
    # b2 = Button(frame1, text="BROWSE FOLDER")
    # b2.pack()

    frame2 = LabelFrame(window, text="Image Viewer", padx=50, pady=50)
    frame2.pack(side=LEFT, expand=True, fill=BOTH, padx=10, pady=10)
    
    quote = "Output will be shown Here"
    text = Text(frame2)
    text.pack(side = "bottom", fill = "both", expand = "yes")
    text.insert(END,quote)

    
    # b1 = Button(frame2, text="BROWSE")
    # b1.pack()
    # b2 = Button(frame2, text="BROWSE FOLDER")
    # b2.pack()

    window.mainloop()

    # open('Output.txt', 'w').close()
    # root = tk.Tk()
    # root.withdraw()
    # file_path = filedialog.askdirectory()
    # print(file_path)
    # arr = os.listdir(file_path)
    # print(arr)
    # for files_index in arr:
    #     print_data(files_index)
    #     files_location = file_path + '/' + files_index
    #     print_data(files_location)
    #     data_ind = process_image(files_location, "ind")
    #     print_data(data_ind)
    #     output_file("Output.txt", data_ind)


if __name__ == '__main__':
    main()
