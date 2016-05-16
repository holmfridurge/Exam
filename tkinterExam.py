from tkinter import *  # python3
#import Tkinter as tk   # python
from exam import *

TITLE_FONT = ("Helvetica", 18, "bold")

class Application(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, GetFile, Test, ResultPageTrue, ResultPageFalse):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Choose", font=TITLE_FONT)
        label.grid(row=0, column=20, padx=190, pady=5)

        button1 = Button(self, text="Generate test",
                            command=lambda: controller.show_frame("GetFile"))
        button2 = Button(self, text="Try taking a test",
                            command=lambda: controller.show_frame("Test"))
        button1.grid(row=1, column=20, padx=190, pady=5)
        button2.grid(row=2, column=20, padx=190, pady=5)


class GetFile(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Please fill in the following information",
                      font=TITLE_FONT)
        label.grid(row=0, column=0, columnspan=2, padx=20)

        labelName = Label(self, text='Name of file (export destination), do not write the file extension')
        labelDate = Label(self, text='Date of Test')
        labelNum = Label(self, text='Number of questions')
        entryName = Entry(self)
        entryDate = Entry(self)
        entryNum = Entry(self)

        labelName.grid(row=1, column=0, sticky=E)
        labelDate.grid(row=2, column=0, sticky=E)
        labelNum.grid(row=3, column=0, sticky=E)

        entryName.grid(row=1, column=1)
        entryDate.grid(row=2, column=1)
        entryNum.grid(row=3, column=1)


        def generateFile():
            filename = entryName.get()
            dateOfTest = entryDate.get()
            n = entryNum.get()
            n = int(n)
            questions(filename, n, dateOfTest)
            controller.show_frame("GetFile")
            
        c = Button(self, text="Generate", command=generateFile)
        c.grid(row=5, column=0, columnspan=2)

        
        button = Button(self, text="Back",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=6, column=0, columnspan=2)


class Test(Frame):

    def findAns():
        result = entryAns.get()
        print(result)

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Try the test", font=TITLE_FONT)
        label.grid(row=0, column=0, columnspan=2)

        def getInfo():
            question = getQuestion()
            answer = getAnswer()
            
            labelQ = Label(self, text="Question:")
            labelQuest = Message(self, width=500, text=question)
            entryAns = Entry(self)
            
            labelQ.grid(row=1, column=0)
            labelQuest.grid(row=1, column=1, sticky=E+W+S+N)
            entryAns.grid(row=2, column=1, sticky=E+W+S+N)

        getInfo()
        
        submitButton = Button(self, text="Submit", command=getInfo)
        submitButton.grid(row=3, column=1)
        
        button = Button(self, text="Back",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=4, column=1)

class ResultPageTrue(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="True", font=TITLE_FONT)
        label.grid(row=0, column=20, padx=190, pady=5)

        button1 = Button(self, text="Ok",
                            command=lambda: controller.show_frame("Test"))
        button1.grid(row=1, column=20, padx=190, pady=5)

class ResultPageFalse(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="False", font=TITLE_FONT)
        label.grid(row=0, column=20, padx=190, pady=5)

        button1 = Button(self, text="Ok",
                            command=lambda: controller.show_frame("Test"))
        button1.grid(row=1, column=20, padx=190, pady=5)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
