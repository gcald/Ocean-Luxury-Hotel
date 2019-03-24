from tkinter import *
from tkinter import ttk


class OceanLuxuryGUI:
    def __init__(self, master):
        self.img_00 = PhotoImage(file='OL-Assets/OceanLuxuryBanner.png')
        self.img_01 = PhotoImage(file='OL-Assets/home.png')
        self.img_02 = PhotoImage(file='OL-Assets/aboutus.png')
        self.img_03 = PhotoImage(file='OL-Assets/booking.png')
        self.img_04 = PhotoImage(file='OL-Assets/services.png')
        self.img_05 = PhotoImage(file='OL-Assets/login.png')
        self.img_06 = PhotoImage(file='OL-Assets/signup.png')
        self.img_07 = PhotoImage(file='OL-Assets/white_button.png')

        # 3 main areas of the screen
        # banner displays the Ocean Luxury logo
        # sidebar_frame displays buttons for navigation
        # main_frame is the parent frame of the other important frames
        self.banner = ttk.Label(master, text="Ocean Luxury Banner", image=self.img_00)
        self.sidebar_frame = ttk.Frame(master)
        self.main_frame = ttk.Frame(master)

        # 3 frames within main_frame
        # center_frame used as default to display
        # message_frame used to display messages/popups to user
        # backup_frame as a extra frame just in case user needs to submit a form without losing the center_frame
        self.center_frame = ttk.Frame(self.main_frame)
        self.message_frame = ttk.Frame(self.main_frame)
        self.backup_frame = ttk.Frame(self.main_frame)

        # sidebar buttons displayed on the side, used for navigation
        self.home = ttk.Button(self.sidebar_frame, text="Home", image=self.img_01)
        self.about = ttk.Button(self.sidebar_frame, text="About Us", image=self.img_02)
        self.booking = ttk.Button(self.sidebar_frame, text="Booking", image=self.img_03)
        self.services = ttk.Button(self.sidebar_frame, text="Services", image=self.img_04)
        self.login = ttk.Button(self.sidebar_frame, text="Log-in", image=self.img_05)
        self.signup = ttk.Button(self.sidebar_frame, text="Sign Up", image=self.img_06)
        self.logout = ttk.Button(self.sidebar_frame, text="Logout", image=self.img_07)

        self.display_default()

    # places all tkinter objects on the screen in their default settings
    # used for initialization
    def display_default(self):
        self.banner.grid(column=0, row=0, columnspan=2, sticky=W)
        self.sidebar_frame.grid(column=0, row=1, sticky=W)
        self.main_frame.grid(column=1, row=1)
        self.center_frame.grid()
        self.message_frame.grid()
        self.message_frame.grid_remove()
        self.home.grid()
        self.about.grid()
        self.booking.grid()
        self.services.grid()
        self.set_sidebar_frame(0)


    # clear_center used to destroy all tkinter objects from the center and message frame when not needed
    def clear_center(self):
        self.center_frame.destroy()
        self.center_frame = ttk.Frame(self.main_frame)
        self.center_frame.grid()
        self.message_frame.destroy()
        self.message_frame = ttk.Frame(self.main_frame)
        self.message_frame.grid()
        self.backup_frame.destroy()
        self.backup_frame = ttk.Frame(self.main_frame)
        self.backup_frame.grid()

    # message_press function used to display messages to user over the center frame without affecting the current state
    def display_message_frame(self, msg):
        self.center_frame.grid_forget()
        self.backup_frame.grid_forget()
        self.message_frame.grid()
        self.message = ttk.Label(self.message_frame, text=msg).grid(column=0, row=0)
        self.ok_button = ttk.Button(self.message_frame, text="Ok", command=self.message_confirm).grid(column=0, row=1)

    # message_confirm used on confirmation of a message to return to the previous state of
    def message_confirm(self):
        self.message_frame.destroy()
        self.message_frame = ttk.Frame(self.main_frame)
        self.center_frame.grid()

    # layout : 0 / default = logout not displayed
    # layout : 1 = login/signup not displayed
    def set_sidebar_frame(self, layout):

        if layout == 1:
            self.logout.grid()
            self.login.grid_forget()
            self.signup.grid_forget()

        else:
            self.login.grid()
            self.signup.grid()
            self.logout.grid_forget()

    def get_center_frame(self):
        return self.center_frame

    def get_backup_frame(self):
        return self.backup_frame

    def display_center_frame(self):
        self.backup_frame.grid_forget()
        self.center_frame.grid()

    def display_backup_frame(self):
        self.center_frame.grid_forget()
        self.backup_frame.grid()