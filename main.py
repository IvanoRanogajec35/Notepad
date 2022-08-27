from tkinter import *
from tkinter import filedialog

def saveFile():
    openFile = filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    if openFile is None:
        return
    text = str(entry.get(1.0,END))
    openFile.write(text)
    openFile.close()

def openFile():
    file = filedialog.askopenfile(mode="r",filetype=[("text files","*.txt")])
    if file is not None:
        content = file.read()
    entry.insert(INSERT,content)

app = Tk()
app.geometry("600x600")
app.title("Notepad")
app.config(bg="grey")
app.resizable(False,False)

btn1 = Button(app,width="20",height="2",bg="#fff",text="Save File",command=saveFile).place(x=100,y=7.5)
btn2 = Button(app,width="20",height="2",bg="#fff",text="Open File",command=openFile).place(x=300,y=7.5)

entry = Text(app,height = "33",width="72",wrap=WORD)
entry.place(x=10,y=60)

app.mainloop()
