from PIL import Image
import pytesseract
import os
import tkinter as tk
from tkinter import filedialog

def process_image(image_name, lang_code):
	return pytesseract.image_to_string(Image.open(image_name), lang=lang_code)

def print_data(data):
	print(data)

def output_file(filename, data):
	file = open(filename, "a+")
	file.write(data)
	file.close()

def main():
	open('Output.txt', 'w').close()
	root = tk.Tk()
	root.withdraw()
	file_path = filedialog.askdirectory()
	print(file_path)
	arr = os.listdir(file_path)
	print(arr)
	for files_index in arr:
		print_data(files_index)
		files_location = file_path + '/' + files_index
		print_data(files_location)
		data_ind = process_image(files_location, "ind")
		print_data(data_ind)
		output_file("Output.txt", data_ind)
	
if  __name__ == '__main__':
	main()