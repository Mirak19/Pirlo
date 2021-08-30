from tkinter import *

def Call():
 name = entry_box.get()
 message  = str (name)
 output_box["text"] = message
 output_box["bg"] = "yellow"

window = Tk()
window.geometry("350x150")

label = Label(text = "Введите имя: ")
label.place(x = 40, y = 20, width = 100, height = 25)
label ["relief"] = "ridge"
label["bg"] = "grey"

entry_box = Entry (text = 0)
entry_box.place(x = 150, y = 20, width = 100, height = 25)
entry_box ["justify"] = "center"

label = Label(text = "Введите имя: ")
label.place(x = 40, y = 20, width = 100, height = 25)
label ["relief"] = "ridge"
label["bg"] = "grey"
label["fg"] = "black"

button = Button(text = "Кликните меня", command = Call)
button.place(x = 40, y = 50, width = 100, height = 25)
button["relief"] = "raised"
button["bg"] = "grey"
button["fg"] = "black"

output_box = Message(text = 0)
output_box.place(x = 150, y = 45, width = 150, height = 25)
output_box ["relief"] = "ridge"
output_box = Message(text = 0)
output_box.place(x = 150, y = 45, width = 150, height = 25)
output_box ["relief"] = "ridge"

window.mainloop()