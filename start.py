from tkinter import *
from tkinterdnd2 import *
from PIL import ImageTk,Image
from remove import remove_bg

def DropImage(event):
    testvariable.set(event.data)
    # get the value from string variable
    window.file_name=testvariable.get()
    # takes path using dragged file
    image_path = Image.open(str(window.file_name))
    # resize image
    reside_image = image_path.resize((300, 205), Image.ANTIALIAS)
    # displays an image
    window.image = ImageTk.PhotoImage(reside_image)
    image_label = Label(labelframe, image=window.image).pack()

window = TkinterDnD.Tk()
window.title('Background remover')
window.geometry('500x500')
window.config(bg='white')

testvariable = StringVar()
textlabel=Label(window, text='Drop the file here', bg='white')
textlabel.pack(anchor=NW, padx=10)
entrybox = Entry(window, textvar=testvariable, width=180,)
entrybox.pack(fill=X, padx=10,ipady=100)
entrybox.drop_target_register(DND_FILES)
entrybox.dnd_bind('<<Drop>>', DropImage)

labelframe = LabelFrame(window, bg='white')
labelframe.pack(fill=BOTH, expand=True, padx=9, pady=9)

def remove_background():
	print("removing background .......")
	remove_bg(entrybox.get())
	entrybox.delete(0, 'end')
	for widget in labelframe.winfo_children():
		widget.destroy()
	print("DONE!!!")

button = Button(window, text ="remove background", command=remove_background)
button.pack()

window.mainloop()
