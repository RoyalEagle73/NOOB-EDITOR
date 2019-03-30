from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from os import path


home=Tk()
home.title("NOOB EDITOR")

file_address = ""

#FUNCTIONS FOR MENU ITEM
def open_file():
	global file_address
	data = ""
	file_address = filedialog.askopenfilename()
	with open("%s"%file_address, "r") as file:
		data=file.read()
	my_text.delete(1.0, END)
	my_text.insert(END,data)


def data_check():
	global file_address
	if path.exists(file_address) == True :
		with open("%s"%file_address, "r") as file:
			data_1 = file.read()
		data_2 = my_text.get(1.0, END)

		if data_1 == data_2:
			return True
		else:
			return False
	else:
		return False


""""def save_dialog_quit(event):
	save_dialog.quit()"""

def save_call(event):
	save_file()
	save_dialog.quit()


def save_file():
	global file_address
	file_address = filedialog.asksaveasfilename()
	data=my_text.get(1.0, END)
	with open("%s"%file_address, "w") as file:
		file.write(data)
	messagebox.showinfo('SAVED', "FILE SAVED SUCCESSFULLY")

def exit_commands():
	home.quit()
	"""save_dialog.quit()"""

def close_without_saving_exit(event):
	exit_commands()

def close_or_save():
	save_dialog = Tk()
	if data_check() == True:
		exit_commands()
	else:
		save_dialog.title("!!! WARNING !!!")
		save_dialog.configure(background="black")

		save_label = Label(save_dialog, text="File not saved yet, would you like to save??", fg="white", bg="black")
		label_details = ('30')
		save_label.configure(font=label_details)
		save_label.place(x=40, y=20)

		close_without_saving = Button(save_dialog, text="Close Without Saving", fg="white", bg="black")
		close_without_saving.bind("<Button-1>", close_without_saving_exit)
		close_without_saving.place(x=10, y=60)	

		save = Button(save_dialog, text="save", fg="white", bg="black")
		save.bind("<Button-1>", save_call)
		save.place(x=300, y=60)
		
		save_dialog.configure(width=370, height=100)
		save_dialog.resizable(0,0)
		save_dialog.mainloop()

		"""
		cancel = Button(save_dialog, text="cancel", fg="white", bg="black")
		cancel.bind("<Button-1>", save_dialog_quit)
		cancel.place(x=200, y=60)
"""


#MENU
my_menu = Menu(home)
my_menu.configure(foreground="white",background="black")
home.configure(menu=my_menu)

#SUB MENU
file_submenu = Menu(my_menu)
my_menu.add_cascade(label="FILE", menu=file_submenu)


#CREATING AND BINDING ITEMS IN SUBMENU
file_submenu.add_command(label="Open", command=open_file)
file_submenu.add_command(label="Save", command=save_file)
file_submenu.add_separator()
file_submenu.add_command(label="Exit", command=close_or_save)	

#SCROLLBAR FOR TEXT FIELD
text_scroll=Scrollbar(home)
text_scroll.pack(side=RIGHT, fill=Y)

##TEXT FIELD
my_text = Text(home, yscrollcommand=text_scroll.set)
my_text.pack(side=LEFT, fill=X)

#JOINING SCROLL BAR AND TEXT FIELD
text_scroll.configure(command=my_text.yview, background="black")

home.resizable(0,0)
home.mainloop()
