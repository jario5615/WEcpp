from tkinter import *


root = Tk()
root.title("Task Manager")

menuTitle = Label(root, text="Task Management System", background="yellow")

root.minsize(800,800)

Lframe = LabelFrame(background="blue")
Rframe = LabelFrame(background="red")
RsubFrame = LabelFrame(Rframe)
LsubFrame = LabelFrame(Lframe)

itemlist = []

def repackFrame(frame: LabelFrame, itemlist):
    for widget in frame.winfo_children():
        widget.forget()
    for item in itemlist:
        item[0].pack(padx=10, pady=10)


enterTask = Entry(Lframe, width=30)
enterPriority = Spinbox(Lframe, width=5, from_=-50, to=50)
enterPriority.delete(0, END)
enterPriority.insert(0, 0)
enterDesc = Entry(Lframe, width=30)
DescText = Text(LsubFrame, width=50, wrap=WORD, padx=5, pady=5)
DescText.insert(0.0,"Descriptions will go here")
DescText.config(state=DISABLED)
activeEntry = Button

def AddToRight():
    text = enterTask.get()
    priority = enterPriority.get()
    desc = enterDesc.get()
    if text != "":

        selfDestructButton = Button(RsubFrame, text=text, padx=5, pady=5)
        selfDestructButton.configure(command=lambda b=selfDestructButton: onpress(b))
        selfDestructButton.pack(padx=10, pady=10)
        itemlist.append([selfDestructButton, int(priority), desc])
        itemlist.sort(key=lambda k: k[1], reverse=True)
        print(itemlist)
        repackFrame(RsubFrame, itemlist)
        enterTask.delete(0,END)

def Destruct():
    global itemlist
    global DescText
    print("DESTROY")
    for i in range(len(itemlist)):
        if itemlist[i][0] == activeEntry:
            print(itemlist[i])
            target = itemlist.pop(i)
            target[0].destroy()
            updateButton.config(state=DISABLED)
            deleteButton.config(state=DISABLED)
            break

def onpress(self: Widget):
    updateButton.config(state=NORMAL)
    deleteButton.config(state=NORMAL)
    global itemlist
    global DescText
    global activeEntry
    for i in range(len(itemlist)):
        if itemlist[i][0] == self:
            DescText.config(state=NORMAL)
            DescText.delete(0.0, END)
            DescText.insert(0.0, itemlist[i][2])
            DescText.config(state=DISABLED)
            activeEntry = self
            break

def update():
    global activeEntry
    text = enterTask.get()
    priority = enterPriority.get()
    desc = enterDesc.get()
    for i in range(len(itemlist)):
        if itemlist[i][0] == activeEntry:
            activeEntry.configure(text=text)
            itemlist[i][0] = activeEntry
            itemlist[i][1] = priority
            itemlist[i][2] = desc
            break
    repackFrame(RsubFrame, itemlist)
    enterTask.delete(0, END)

taskEnterButton = Button(Lframe, text= "Press to add task to right side", command=AddToRight, pady=5, padx=5)
priorityEnterLabel = Label(Lframe, text="Enter priority for item to enter", padx=5, pady=5)
DescEnterLabel = Label(Lframe, text="Enter description for item to enter", padx=5, pady=5)
TaskEnterLabel = Label(Lframe, text="Enter name for item to enter", padx=5, pady=5)

updateButton = Button(LsubFrame, text= "Update Entry", pady=5, padx=5)
deleteButton = Button(LsubFrame, text= "Delete Entry", pady=5, padx=5)
deleteButton.configure(command=Destruct)
updateButton.configure(command=update)
updateButton.config(state=DISABLED)
deleteButton.config(state=DISABLED)

rightlabel = Label(Rframe, text="Data entry: ", padx=5, pady=5)
leftlabel = Label(Lframe, text="Tasks: ", padx=5, pady=5)
bottomLabel = Label(LsubFrame, text="Description of Task")


menuTitle.grid(column=0, row=0, columnspan=5, sticky="ew")

leftlabel.pack(padx=10, pady=10)
rightlabel.pack(padx=10, pady=10)
RsubFrame.pack(expand=True, fill=BOTH, padx=10, pady=10)
TaskEnterLabel.pack(padx=10, pady=10)
enterTask.pack(padx=10, pady=10)
priorityEnterLabel.pack(padx=10, pady=10)
enterPriority.pack(padx=10, pady=10)
DescEnterLabel.pack(padx=10, pady=10)
enterDesc.pack(padx=0, pady=10)
taskEnterButton.pack(padx=10, pady=10)
Lframe.grid(column=0, row=1, columnspan=2, sticky="nsew")
Rframe.grid(column=2, row=1, columnspan=3, sticky="nsew")
DescText.grid(column=0, row=1, columnspan=2)
bottomLabel.grid(column=0,row=0, columnspan=2)
updateButton.grid(column=0, row=2, pady=10, padx=10)
deleteButton.grid(column=1, row=2, pady=10, padx=10)
LsubFrame.pack(expand=True, fill=BOTH, padx=10, pady=10)

LsubFrame.columnconfigure("all", weight=1)
LsubFrame.rowconfigure("1", weight=1)
LsubFrame.rowconfigure("2", weight=1)

root.columnconfigure("all", weight=1)
root.rowconfigure("1", weight=1)

root.mainloop()