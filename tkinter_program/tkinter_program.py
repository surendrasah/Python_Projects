trace_filename=None
x_loc = 0
y_loc = 0
z_loc = 0
rotation_y = 0

import tkinter
from tkinter import ttk, StringVar
from tkinter.filedialog import askopenfilename
from tkinter import *
from PIL import ImageTk, Image


class GUI:

    def __init__(self, window):
        # 'StringVar()' is used to get the instance of input field
        self.input_text = StringVar()
        self.input_text1 = StringVar()
        self.path = ''
        self.path1 = ''

        window.title("GUI for requesting input")
        window.resizable(width=True, height=True) # this ( 0, 0) prevents from resizing the window
        window.geometry("650x600")   # windows geometry

        #add image
        img_open = Image.open("altran.png")
        img = ImageTk.PhotoImage(img_open)
        imglabel = ttk.Label(window, image=img)
        imglabel.image = img
        imglabel.grid(row=0, column=0)
        #self.entr_imagelabel = ttk.Entry()
        #imglabel.grid(row=0, ipadx=1, ipady=1)
        #self.entr_imagelabel.grid(row = 0, column=1, ipadx=1, ipady=1)

        # lets add some extra space
        ttk.Label(window).grid(row=2, column=1)

        #ttk.Label(window).grid(row=4, column=1)

        ttk.Label(window, text="ADAS trace validation tool", font=("Arial Bold", 14)).grid(row=4, column=1)

        ttk.Label(window).grid(row=5, column=1)
        ttk.Label(window).grid(row=6, column=1)
        ttk.Label(window).grid(row=7, column=1)

        ttk.Label(window, text="Please click on Users file to select the file", font=("Arial Bold", 12)).grid(row=8, column=1)
        ttk.Label(window).grid(row=10, column=1)
        ttk.Button(window, text = "Click here for trace file", command = lambda: self.set_path_users_field()).grid(row = 12, ipadx=5, ipady=15) # this is placed in 0 0
        ttk.Entry(window, textvariable = self.input_text, width = 20).grid(row = 12, column = 1, ipadx=1, ipady=1) # this is placed in 0 1

        # lets add some extra space
        ttk.Label(window).grid(row=13, column=1)

        ttk.Label(window, text="for 39 trace:x=286.7, y=-216.3, z=0.3,yaw=90", font=("Arial Bold", 12)).grid(row=14, column=1)
        ttk.Label(window, text="for 40 trace:x=287, y=-215.9, z=0.3,270", font=("Arial Bold", 12)).grid(row=15, column=1)

        ttk.Label(window, text="Please give the location of car ", font=("Arial Bold", 12)).grid(row=16, column=1)
        ttk.Label(window).grid(row=17, column=1)
        #x location
        self.label_x = ttk.Label(window, text="Location x like  283.8", font=("Arial Bold", 12))
        self.entry_x = ttk.Entry()
        self.label_x.grid(row = 18, column=0, ipadx=1, ipady=1)
        self.entry_x.grid(row = 18, column=1, ipadx=1, ipady=1)

        # lets add some extra space
        ttk.Label(window).grid(row=20, column=1)
        #y location
        self.label_y = ttk.Label(window, text="Location y like -204.1", font=("Arial Bold", 12))
        self.entry_y = ttk.Entry()
        self.label_y.grid(row = 22, ipadx=1, ipady=1)
        self.entry_y.grid(row = 22, column=1, ipadx=1, ipady=1)

        # lets add some extra space
        ttk.Label(window).grid(row=24, column=1)
        #z location
        self.label_z = ttk.Label(window, text="Location z like 0.3 ,  0 ", font=("Arial Bold", 12))
        self.entry_z = ttk.Entry()
        self.label_z.grid(row = 26, ipadx=1, ipady=1)
        self.entry_z.grid(row = 26, column=1, ipadx=1, ipady=1)

        # lets add some extra space
        ttk.Label(window).grid(row = 28, column = 1)
        #rotation
        self.label_rot_x = ttk.Label(window, text="Rotation-yaw like 90, 270", font=("Arial Bold", 12))
        self.entry_rot_x = ttk.Entry()
        self.label_rot_x.grid(row = 30, ipadx=1, ipady=1)
        self.entry_rot_x.grid(row = 30, column=1, ipadx=1, ipady=1)

        #lets add some extra space
        ttk.Label(window).grid(row = 32, column = 1)
        ttk.Label(window).grid(row = 34, column = 1)
        ttk.Label(window).grid(row = 36, column = 1)

        ttk.Button(window, text="Click here to start the Simulation", command=window.quit).grid(row = 38, column = 1)
        #ttk.Button(window, text = "Enova File", command = lambda: self.set_path_Enova_field()).grid(row = 1, ipadx=5, ipady=15) # this is placed in 0 0
        #ttk.Entry(window, textvariable = self.input_text1, width = 70).grid( row = 1, column = 1, ipadx=1, ipady=1) # this is placed in 0 1

        #ttk.Button(window, text = "Send Notifications").grid(row = 2, ipadx=5, ipady=15) # this is placed in 0 0

    def set_path_users_field(self):
        self.path = askopenfilename()
        self.input_text.set(self.path)

    #def set_path_Enova_field(self):
        #self.path1 = askopenfilename()
        #self.input_text1.set(self.path1)

    def get_user_path(self):
        """ Function provides the Users full file path."""
        return self.path

    #def get_enova_path1(self):
        """Function provides the Enova full file path."""
        #return self.path1

def main():


    window = tkinter.Tk()
    gui = GUI(window)
    window.mainloop()
    # Extracting the full file path for re-use. Two ways to accomplish this task is below.
    # print(gui.path, '\n', gui.path1)
    # print(gui.get_user_path(), '\n', gui.get_enova_path1())
    global trace_filename
    trace_filename = gui.path
    global x_loc
    global y_loc
    global z_loc
    global rotation_y

    x_loc = float(gui.entry_x.get())  #converting in float
    y_loc = float(gui.entry_y.get())
    z_loc = float(gui.entry_z.get())
    rotation_y = float(gui.entry_rot_x.get())
    print("the trace file name ", trace_filename)
    print("location of value at x", x_loc)
    print("location of value at y", y_loc)
    print("location of value at z", z_loc)
    print("location of yaw rotation", rotation_y)
    window.destroy()  # tkinter window closes

if __name__ == '__main__':
    main()
