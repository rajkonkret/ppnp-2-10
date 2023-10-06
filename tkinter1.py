import tkinter


# aplikacje okienkowe

class MyGui:
    def __init__(self):  # konstruktor
        self.main_window = tkinter.Tk()

        self.label1 = tkinter.Label(self.main_window, text="Witaj świecie")
        self.label2 = tkinter.Label(self.main_window, text="Python")
        self.label3 = tkinter.Label(self.main_window, text="Gora")
        self.label4 = tkinter.Label(self.main_window, text="Dół")

        self.label1.pack(side='left')
        self.label2.pack(side='right')
        self.label3.pack(side='top')
        self.label4.pack(side='bottom')

        tkinter.mainloop()
        # dodac 3 labelki
        # umiescić right, top,, bottom


my_gui = MyGui()
