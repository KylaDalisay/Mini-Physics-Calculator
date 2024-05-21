import tkinter as tk
import ctypes
from PIL import Image, ImageTk
from misc import Text as text, Colors as colors
from tkinter import messagebox
from sub import ProjectileMotion, OhmVoltage, DensityVolume, WorkEnergy, AngularMomentum

class MainWindow:
    def __init__(self, root) -> None:
        self.setup_root_window(root)
        self.Bar_isOpen = False
        self.create_background()
        self.create_main_panel()
        self.logo_and_header()
        self.application_tab()

    def setup_root_window(self, root):
        width, height = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
        self.root = root
        self.root.geometry(f"{width}x{height}")
        self.root.title("Mini Physics Calculator | Main Menu")
        self.root.resizable(False, False)
        self.root.state("zoomed")

    def create_background(self):
        self.background = tk.Canvas(self.root, bg=colors.white, highlightthickness=0)
        self.background.place(anchor="center", relx=0.5, rely=0.5, relwidth=1, relheight=1)

    def create_main_panel(self):
        self.main_panel = tk.Canvas(self.root, bg=colors.grey, highlightthickness=0)
        self.main_panel.place(anchor="w", relx=0.075, rely=0.5, relwidth=0.26, relheight=1.005)

    def logo_and_header(self) -> None:
        self.Logo = ImageTk.PhotoImage(Image.open("Logo2.png").resize((150, 150)))
        self.Logo_ImageBox = tk.Label(self.main_panel, bg=colors.grey, image=self.Logo)
        self.Logo_ImageBox.place(anchor="center", relx=0.5, rely=0.1)
        self.Logo_ImageBox.image = self.Logo

        self.header = tk.Label(self.main_panel, font=text.H2, fg=colors.white, bg=colors.grey, text="LUNATECH INC.")
        self.header.place(anchor="n", relx=0.5, rely=0.175)

        self.sub_header = tk.Label(self.main_panel, font=text.P1, fg=colors.white, bg=colors.grey, text="MINI-PHYSICS CALCULATOR")
        self.sub_header.place(anchor="n", relx=0.5, rely=0.235)

    def application_tab(self) -> None:
        self.application_panel = tk.Canvas(self.main_panel, bg=colors.grey, highlightthickness=3)
        self.application_panel.place(anchor="center", relx=0.5, rely=0.625, relwidth=1, relheight=0.6)

        self.image_1_inactive = ImageTk.PhotoImage(Image.open("ProjectileMotion_Inactive.jpg").resize((60, 60)))
        self.image_1_active = ImageTk.PhotoImage(Image.open("ProjectileMotion_Active.jpg").resize((60, 60)))

        self.option_1 = tk.Canvas(self.application_panel, bg=colors.grey, highlightthickness=0, cursor="hand2")
        self.option_1.place(anchor="n", relx=0.5, rely=0, relwidth=1, relheight=0.2)
        self.option_1.bind("<Enter>", self.on_option_1_enter)
        self.option_1.bind("<Leave>", self.on_option_1_leave)
        self.option_1.bind("<Button-1>", lambda event: self.proceed(1))

        self.image_box_1 = tk.Label(self.option_1, bg=colors.grey, image=self.image_1_inactive)
        self.image_box_1.image = self.image_1_inactive
        self.image_box_1.place(anchor="w", relx=0.075, rely=0.5)
        self.image_box_1.bind("<Button-1>", lambda event: self.proceed(1))

        self.image_label_1 = tk.Label(self.option_1, bg=colors.grey, fg=colors.white, font=text.P1, text="PROJECTILE MOTION\nCALCULATOR")
        self.image_label_1.place(anchor="e", relx=0.9, rely=0.5)
        self.image_label_1.bind("<Button-1>", lambda event: self.proceed(1))

        self.image_2_inactive = ImageTk.PhotoImage(Image.open("Ohm_Inactive.jpg").resize((60, 60)))
        self.image_2_active = ImageTk.PhotoImage(Image.open("Ohm_Active.jpg").resize((60, 60)))

        self.option_2 = tk.Canvas(self.application_panel, bg=colors.grey, highlightthickness=0, cursor="hand2")
        self.option_2.place(anchor="n", relx=0.5, rely=0.2, relwidth=1, relheight=0.2)
        self.option_2.bind("<Enter>", self.on_option_2_enter)
        self.option_2.bind("<Leave>", self.on_option_2_leave)
        self.option_2.bind("<Button-1>", lambda event: self.proceed(2))

        self.image_box_2 = tk.Label(self.option_2, bg=colors.grey, image=self.image_2_inactive)
        self.image_box_2.image = self.image_2_inactive
        self.image_box_2.place(anchor="w", relx=0.075, rely=0.5)
        self.image_box_2.bind("<Button-1>", lambda event: self.proceed(2))

        self.image_label_2 = tk.Label(self.option_2, bg=colors.grey, fg=colors.white, font=text.P1, text="OHM AND VOLTAGE\nCALCULATOR")
        self.image_label_2.place(anchor="e", relx=0.9, rely=0.5)
        self.image_label_2.bind("<Button-1>", lambda event: self.proceed(2))

        self.image_3_inactive = ImageTk.PhotoImage(Image.open("Density_Inactive.jpg").resize((60, 60)))
        self.image_3_active = ImageTk.PhotoImage(Image.open("Density_Active.jpg").resize((60, 60)))

        self.option_3 = tk.Canvas(self.application_panel, bg=colors.grey, highlightthickness=0, cursor="hand2")
        self.option_3.place(anchor="n", relx=0.5, rely=0.4, relwidth=1, relheight=0.2)
        self.option_3.bind("<Enter>", self.on_option_3_enter)
        self.option_3.bind("<Leave>", self.on_option_3_leave)
        self.option_3.bind("<Button-1>", lambda event: self.proceed(3))

        self.image_box_3 = tk.Label(self.option_3, bg=colors.grey, image=self.image_3_inactive)
        self.image_box_3.image = self.image_3_inactive
        self.image_box_3.place(anchor="w", relx=0.075, rely=0.5)
        self.image_box_3.bind("<Button-1>", lambda event: self.proceed(3))

        self.image_label_3 = tk.Label(self.option_3, bg=colors.grey, fg=colors.white, font=text.P1, text="DENSITY AND VOLUME\nCALCULATOR")
        self.image_label_3.place(anchor="e", relx=0.9, rely=0.5)
        self.image_label_3.bind("<Button-1>", lambda event: self.proceed(3))

        self.image_4_inactive = ImageTk.PhotoImage(Image.open("Work_Inactive.jpg").resize((60, 60)))
        self.image_4_active = ImageTk.PhotoImage(Image.open("Work_Active.jpg").resize((60, 60)))

        self.option_4 = tk.Canvas(self.application_panel, bg=colors.grey, highlightthickness=0, cursor="hand2")
        self.option_4.place(anchor="n", relx=0.5, rely=0.6, relwidth=1, relheight=0.2)
        self.option_4.bind("<Enter>", self.on_option_4_enter)
        self.option_4.bind("<Leave>", self.on_option_4_leave)
        self.option_4.bind("<Button-1>", lambda event: self.proceed(4))
                
        self.image_box_4 = tk.Label(self.option_4, bg=colors.grey, image=self.image_4_inactive)
        self.image_box_4.image = self.image_4_inactive
        self.image_box_4.place(anchor="w", relx=0.075, rely=0.5)
        self.image_box_4.bind("<Button-1>", lambda event: self.proceed(4))

        self.image_label_4 = tk.Label(self.option_4, bg=colors.grey, fg=colors.white, font=text.P1, text="WORK AND ENERGY\nCALCULATOR")
        self.image_label_4.place(anchor="e", relx=0.9, rely=0.5)
        self.image_label_4.bind("<Button-1>", lambda event: self.proceed(4))

        self.image_5_inactive = ImageTk.PhotoImage(Image.open("Angular_Inactive.jpg").resize((60, 60)))
        self.image_5_active = ImageTk.PhotoImage(Image.open("Angular_Active.jpg").resize((60, 60)))

        self.option_5 = tk.Canvas(self.application_panel, bg=colors.grey, highlightthickness=0, cursor="hand2")
        self.option_5.place(anchor="n", relx=0.5, rely=0.8, relwidth=1, relheight=0.2)
        self.option_5.bind("<Enter>", self.on_option_5_enter)
        self.option_5.bind("<Leave>", self.on_option_5_leave)
        self.option_5.bind("<Button-1>", lambda event: self.proceed(5))

        self.image_box_5 = tk.Label(self.option_5, bg=colors.grey, image=self.image_5_inactive)
        self.image_box_5.image = self.image_5_inactive
        self.image_box_5.place(anchor="w", relx=0.075, rely=0.5)
        self.image_box_5.bind("<Button-1>", lambda event: self.proceed(5))

        self.image_label_5 = tk.Label(self.option_5, bg=colors.grey, fg=colors.white, font=text.P1, text="ANGULAR VELOCITY\nCALCULATOR")
        self.image_label_5.place(anchor="e", relx=0.9, rely=0.5)
        self.image_label_5.bind("<Button-1>", lambda event: self.proceed(5))
    
    def on_option_1_enter(self, event):
        self.option_1.config(bg=colors.highlight)
        self.image_box_1.config(image=self.image_1_active, bg=colors.highlight)
        self.image_box_1.image = self.image_1_active
        self.image_label_1.config(bg=colors.highlight)
        
    def on_option_1_leave(self, event):
        self.option_1.config(bg=colors.grey)
        self.image_box_1.config(image=self.image_1_inactive, bg=colors.grey)
        self.image_box_1.image = self.image_1_inactive
        self.image_label_1.config(bg=colors.grey)

    def on_option_2_enter(self, event):
        self.option_2.config(bg=colors.highlight)
        self.image_box_2.config(image=self.image_2_active, bg=colors.highlight)
        self.image_box_2.image = self.image_2_active
        self.image_label_2.config(bg=colors.highlight)

    def on_option_2_leave(self, event):
        self.option_2.config(bg=colors.grey)
        self.image_box_2.config(image=self.image_2_inactive, bg=colors.grey)
        self.image_box_2.image = self.image_2_inactive
        self.image_label_2.config(bg=colors.grey)

    def on_option_3_enter(self, event):
        self.option_3.config(bg=colors.highlight)
        self.image_box_3.config(image=self.image_3_active, bg=colors.highlight)
        self.image_box_3.image = self.image_3_active
        self.image_label_3.config(bg=colors.highlight)

    def on_option_3_leave(self, event):
        self.option_3.config(bg=colors.grey)
        self.image_box_3.config(image=self.image_3_inactive, bg=colors.grey)
        self.image_box_3.image = self.image_3_inactive
        self.image_label_3.config(bg=colors.grey)

    def on_option_4_enter(self, event):
        self.option_4.config(bg=colors.highlight)
        self.image_box_4.config(image=self.image_4_active, bg=colors.highlight)
        self.image_box_4.image = self.image_4_active
        self.image_label_4.config(bg=colors.highlight)

    def on_option_4_leave(self, event):
        self.option_4.config(bg=colors.grey)
        self.image_box_4.config(image=self.image_4_inactive, bg=colors.grey)
        self.image_box_4.image = self.image_4_inactive
        self.image_label_4.config(bg=colors.grey)

    def on_option_5_enter(self, event):
        self.option_5.config(bg=colors.highlight)
        self.image_box_5.config(image=self.image_5_active, bg=colors.highlight)
        self.image_box_5.image = self.image_5_active
        self.image_label_5.config(bg=colors.highlight)

    def on_option_5_leave(self, event):
        self.option_5.config(bg=colors.grey)
        self.image_box_5.config(image=self.image_5_inactive, bg=colors.grey)
        self.image_box_5.image = self.image_5_inactive
        self.image_label_5.config(bg=colors.grey)

    def proceed(self, target) -> None:
        self.root.withdraw()
        SubWindow = tk.Toplevel()
        if target == 1:
            ProjectileMotion(SubWindow)
        elif target == 2:
            OhmVoltage(SubWindow)
        elif target == 3:
            DensityVolume(SubWindow)
        elif target == 4:
            WorkEnergy(SubWindow)
        elif target == 5:
            AngularMomentum(SubWindow)

       
    
if __name__ == "__main__":
    Root = tk.Tk()
    MainWindow(Root)
    Root.mainloop()
