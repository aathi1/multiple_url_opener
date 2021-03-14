from tkinter import *
import webbrowser, time, base64, os
from threading import Thread
# from iconbase64 import icon


def thread_gui():
	enter_button = Thread(target = on_click)
	enter_button.daemon = True
	enter_button.start()


def on_click():
	secs = var.get()
	global mylist
	content = url_box.get("1.0", END)
	mylist = content.split('\n')
	mylist = list(filter(None, mylist))
	print(mylist)
	url_box.delete("1.0", END)
	length = len(mylist)
	total_time = secs*length
	url_box.insert(INSERT, 'Opening '+ str(length) + ' links now.\n')
	url_box.insert(INSERT, 'Close this window to exit the process\n')
	url_box.insert(INSERT, 'Approximate Time Estimation: '+ str(total_time) +' secs')
	time.sleep(3)
	return link_opener(mylist, secs)


def link_opener(url_list, secs):
	for links in url_list:
		if links.startswith('http'):
			try:
				webbrowser.open(links)
				time.sleep(int(secs))
			except:
				pass
		else:
			pass


window = Tk()
window.title("Link Opener")



# #icon fix
# icondata= base64.b64decode(icon)

# tempFile= "icon.ico"
# iconfile= open(tempFile,"wb")

# iconfile.write(icondata)
# iconfile.close()

# window.wm_iconbitmap(tempFile)

# os.remove(tempFile)

#fonts
font = ('calibri', 11, "italic")

#window configs
window.rowconfigure(0, minsize=300, weight=1)
window.columnconfigure(1, minsize=300, weight=1)

#Frames
text_frame = Frame(window, bd=2)
fr_buttons = Frame(window, relief=RAISED, bd=2)

#text_frame_configs
text_frame.rowconfigure(1, weight=1)
text_frame.columnconfigure(0, weight=1)


#Frame Grids
text_frame.grid(row=0, column=1, sticky="nsew")
fr_buttons.grid(row=0, column=0, sticky="ns")

#Label
tlabel=Label(text_frame, text='Paste the links below', font=font)
tlabel.grid(row=0, column=0, sticky="nsew")

tlabel1=Label(text_frame, text='Time intervals are sleep time between links', font=font)
tlabel1.grid(row=2, column=0, sticky="nsew")
tlabel1.config(bg="lightblue")

tlabel2=Label(text_frame, text='Set the time intervals accordingly to your speed of Internet', font=font)
tlabel2.grid(row=3, column=0, sticky="nsew")
tlabel2.config(bg="lightblue")

#url_box
url_box = Text(text_frame)
url_box.grid(row=1, column=0, sticky="nsew")


#left buttons
btn_open = Button(fr_buttons, text="Open all", font=font,command = thread_gui)
btn_clear = Button(fr_buttons, text="Reset", font=font, command = lambda: url_box.delete("1.0", END))
btn_close = Button(fr_buttons, text="Close tasks", font=font, command = window.destroy)

#radio buttons
var = IntVar()
var.set(1)

secs = var.get()

time_intreval =Label(fr_buttons, text=' Time intervals ', font=font)
time_2 = Radiobutton(fr_buttons, text = "2 secs", variable=var, value = 2)
time_4 = Radiobutton(fr_buttons, text = "4 secs", variable=var, value = 4)
time_6 = Radiobutton(fr_buttons, text = "6 secs", variable=var, value = 6)
time_8 = Radiobutton(fr_buttons, text = "8 secs", variable=var, value = 8)


#framebutton left_grids
time_intreval.grid(row=0, column=0, sticky="ew")
time_2.grid(row=1, column=0, sticky="ew")
time_4.grid(row=2, column=0, sticky="ew")
time_6.grid(row=3, column=0, sticky="ew")
time_8.grid(row=4, column=0, sticky="ew")

btn_open.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
btn_clear.grid(row=6, column=0, sticky="ew", padx=5)
btn_close.grid(row=7, column=0, sticky="ew", padx=5, pady=5)


window.mainloop()