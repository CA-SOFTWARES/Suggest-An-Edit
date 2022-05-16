from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newFile():
    global file
    root.title("Textpad")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".CA ",
                           filetypes=[("All Files", "*.*"),
                                      ("CA Docs", "*.CA ")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Textpad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='New File.CA',
                                 defaultextension=".CA",
                                 filetypes=[("All Files", "*.CA"),
                                            ("CA Docs", "*.CA")])

        if file == '':
            file = None

        else:
            # Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Textpad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()


def cut():
    TextArea.event_generate(("<>"))


def copy():
    TextArea.event_generate(("<>"))


def paste():
    TextArea.event_generate(("<>"))


def about():
    showinfo("Textpad", "Created By Harshil Anuwadia")


if __name__ == '__main__':
    # Basic tkinter setup
    root = Tk()
    root.title("Untitled - Textpad")

    root.geometry("644x788")

    # Add TextArea
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    MenuBar = Menu(root)

    FileMenu = Menu(MenuBar, tearoff=0)

    FileMenu.add_command(label="New", command=newFile)

    FileMenu.add_command(label="Open", command=openFile)

    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)
    MenuBar.add_cascade(label="File", menu=FileMenu)
    # File Menu ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    # To give a feature of cut, copy and paste
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)

    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About Textpad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    # Help Menu Ends

    root.config(menu=MenuBar)

    # Adding Scrollbar using rules from Tkinter lecture no 22
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    root.mainloop()
