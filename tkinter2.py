import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_403=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_403["font"] = ft
        GLabel_403["fg"] = "#333333"
        GLabel_403["justify"] = "center"
        GLabel_403["text"] = "label"
        GLabel_403.place(x=60,y=100,width=70,height=25)

        GButton_250=tk.Button(root)
        GButton_250["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_250["font"] = ft
        GButton_250["fg"] = "#000000"
        GButton_250["justify"] = "center"
        GButton_250["text"] = "Button"
        GButton_250.place(x=230,y=180,width=70,height=25)
        GButton_250["command"] = self.GButton_250_command

        GCheckBox_496=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_496["font"] = ft
        GCheckBox_496["fg"] = "#333333"
        GCheckBox_496["justify"] = "center"
        GCheckBox_496["text"] = "CheckBox"
        GCheckBox_496.place(x=210,y=50,width=70,height=25)
        GCheckBox_496["offvalue"] = "0"
        GCheckBox_496["onvalue"] = "1"
        GCheckBox_496["command"] = self.GCheckBox_496_command

        GRadio_476=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_476["font"] = ft
        GRadio_476["fg"] = "#333333"
        GRadio_476["justify"] = "center"
        GRadio_476["text"] = "RadioButton"
        GRadio_476.place(x=410,y=50,width=85,height=25)
        GRadio_476["command"] = self.GRadio_476_command

        GLineEdit_295=tk.Entry(root)
        GLineEdit_295["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_295["font"] = ft
        GLineEdit_295["fg"] = "#333333"
        GLineEdit_295["justify"] = "center"
        GLineEdit_295["text"] = "Entry"
        GLineEdit_295.place(x=40,y=150,width=70,height=25)

        GListBox_500=tk.Listbox(root)
        GListBox_500["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_500["font"] = ft
        GListBox_500["fg"] = "#333333"
        GListBox_500["justify"] = "center"
        GListBox_500.place(x=80,y=270,width=80,height=25)

        GMessage_358=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_358["font"] = ft
        GMessage_358["fg"] = "#333333"
        GMessage_358["justify"] = "center"
        GMessage_358["text"] = "Message"
        GMessage_358.place(x=340,y=260,width=80,height=25)

        GCheckBox_336=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_336["font"] = ft
        GCheckBox_336["fg"] = "#333333"
        GCheckBox_336["justify"] = "center"
        GCheckBox_336["text"] = "CheckBox"
        GCheckBox_336.place(x=180,y=360,width=70,height=25)
        GCheckBox_336["offvalue"] = "0"
        GCheckBox_336["onvalue"] = "1"
        GCheckBox_336["command"] = self.GCheckBox_336_command

        GButton_804=tk.Button(root)
        GButton_804["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_804["font"] = ft
        GButton_804["fg"] = "#000000"
        GButton_804["justify"] = "center"
        GButton_804["text"] = "Button"
        GButton_804.place(x=390,y=150,width=70,height=25)
        GButton_804["command"] = self.GButton_804_command

    def GButton_250_command(self):
        print("command")


    def GCheckBox_496_command(self):
        print("command")


    def GRadio_476_command(self):
        print("command")


    def GCheckBox_336_command(self):
        print("command")


    def GButton_804_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
