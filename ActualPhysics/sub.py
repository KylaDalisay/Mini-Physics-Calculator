import tkinter as tk
import ctypes
from PIL import Image, ImageTk
from tkinter import messagebox, ttk
from misc import Text as text, Colors as colors

class SubWindow:
    def __init__(self, root) -> None:
        self.setup_window(root)

    def setup_window(self, root) -> None:
        self.width, self.height = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
        self.root = root
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.title("Lunatech Mini Physics Calculator | Blank Window")
        self.root.resizable(False, False)
        self.root.state("zoomed")

class ProjectileMotion(SubWindow):
    def __init__(self, root) -> None:
        super().__init__(root)
        self.create_top_panel()
        self.create_bot_panel()
        self.logo_and_header()
        self.create_control_panel()
        self.create_command_panel()
        self.create_display_panel()

    def setup_window(self, root) -> None:
        super().setup_window(root)
        self.root.bind("<Escape>", lambda event: self.root.destroy())
        self.root.title("Lunatech Mini Physics Calculator | Projectile Motion Calculator")

    def create_top_panel(self) -> None:
        self.top_panel = tk.Canvas(self.root, bg=colors.grey, highlightthickness=0)
        self.top_panel.place(anchor="n", relx=0.5, rely=0, relwidth=1, relheight=0.125)

        self.exit_image_inactive = ImageTk.PhotoImage(Image.open("Exit_Inactive.jpg").resize((80, 80)))
        self.exit_image_active = ImageTk.PhotoImage(Image.open("Exit_Active.jpg").resize((80, 80)))

        self.exit_image_container = tk.Canvas(self.top_panel, bg=colors.grey, highlightthickness=0, cursor="hand2", width=80, height=80)
        self.exit_image_container.place(anchor="e", relx=0.975, rely=0.5)
        self.exit_image_container.create_image(0, 0, anchor=tk.NW, image=self.exit_image_inactive)
        self.exit_image_container.image = self.exit_image_inactive
        self.exit_image_container.bind("<Enter>", lambda event: self.exit_image_container.create_image(0, 0, anchor=tk.NW, image=self.exit_image_active))
        self.exit_image_container.bind("<Leave>", lambda event: self.exit_image_container.create_image(0, 0, anchor=tk.NW, image=self.exit_image_inactive))

    def create_bot_panel(self) -> None:
        self.bot_panel = tk.Canvas(self.root, bg=colors.white, highlightthickness=0)
        self.bot_panel.place(anchor="n", relx=0.5, rely=0.123, relwidth=1, relheight = 0.875)

    def logo_and_header(self) -> None:
        self.logo = ImageTk.PhotoImage(Image.open("Logo2.png").resize((100, 100)))
        self.logo_image_box = tk.Label(self.top_panel, bg=colors.grey, image=self.logo)
        self.logo_image_box.image = self.logo
        self.logo_image_box.place(anchor="w", relx=0.01, rely=0.5)

        self.header = tk.Label(self.top_panel, font=text.H2, fg=colors.white, bg=colors.grey, text="LUNATECH INC.")
        self.header.place(anchor="w", relx=0.1, rely=0.3)

        self.sub_header = tk.Label(self.top_panel, font=text.P1, fg=colors.white, bg=colors.grey, text="PROJECTILE MOTION CALCULATOR")
        self.sub_header.place(anchor="w", relx=0.1, rely=0.7)

    def create_control_panel(self) -> None:
        self.container_image = Image.open("Control_Container.png")
        self.container_image_width, self.container_image_height = self.container_image.size

        self.control_panel = tk.Canvas(self.bot_panel, bg=colors.white, width=self.container_image_width, height=self.container_image_height)
        self.control_panel.config(highlightthickness=0)
        self.control_panel.place(anchor="nw", relx=0.015, rely=0.03)

        self.container_image = ImageTk.PhotoImage(self.container_image)
        self.control_panel.create_image(1, 1, anchor=tk.NW, image=self.container_image)
        self.control_panel.image = self.container_image

        self.entry_image = Image.open("Entry_Container.png")
        self.entry_image_width, self.entry_image_height = self.entry_image.size
        self.entry_image = ImageTk.PhotoImage(self.entry_image)

        self.velocity_panel = tk.Canvas(self.control_panel, bg=colors.grey, highlightthickness=0)
        self.velocity_panel.place(anchor="center", relx=0.5, rely=0.2, relwidth=0.85, relheight=0.25)
        
        self.velocity_entry_panel = tk.Canvas(self.velocity_panel, bg=colors.grey, width=self.entry_image_width, height=self.entry_image_height, highlightthickness=0)
        self.velocity_entry_panel.config(cursor="xterm")
        self.velocity_entry_panel.place(anchor="center", relx=0.4, rely=0.5)
        self.velocity_entry_panel.bind("<Button-1>", lambda event: self.velocity_entry.focus_set())
        self.velocity_entry_panel.create_image(1, 1, anchor=tk.NW, image=self.entry_image)
        self.velocity_entry_panel.image = self.entry_image

        self.velocity_entry = tk.Entry(self.velocity_entry_panel, font=text.P1, fg="grey", bg=colors.white, justify="center", relief="flat")
        self.velocity_entry.insert(0, "Velocity")
        self.velocity_entry.place(anchor="center", relx=0.5, rely=0.5, relwidth=0.9, relheight=0.7)
        self.velocity_entry.bind("<FocusIn>", lambda event: self.velocity_entry_focus_in())
        self.velocity_entry.bind("<FocusOut>", lambda event: self.velocity_entry_focus_out())

        self.velocity_unit_label = tk.Label(self.velocity_panel, font=text.P1, fg=colors.white, bg=colors.grey, text="m/s")
        self.velocity_unit_label.place(anchor="center", relx=0.8, rely=0.5)

        self.angle_panel = tk.Canvas(self.control_panel, bg=colors.grey, highlightthickness=0)
        self.angle_panel.place(anchor="center", relx=0.5, rely=0.5, relwidth=0.85, relheight=0.25)

        self.angle_entry_panel = tk.Canvas(self.angle_panel, bg=colors.grey, width=self.entry_image_width, height=self.entry_image_height, highlightthickness=0)
        self.angle_entry_panel.config(cursor="xterm")
        self.angle_entry_panel.place(anchor="center", relx=0.4, rely=0.5)
        self.angle_entry_panel.bind("<Button-1>", lambda event: self.angle_entry.focus_set())
        self.angle_entry_panel.create_image(1, 1, anchor=tk.NW, image=self.entry_image)
        self.angle_entry_panel.image = self.entry_image

        self.angle_entry = tk.Entry(self.angle_entry_panel, font=text.P1, fg="grey", bg=colors.white, justify="center", relief="flat")
        self.angle_entry.insert(0, "Angle")
        self.angle_entry.place(anchor="center", relx=0.5, rely=0.5, relwidth=0.9, relheight=0.7)
        self.angle_entry.bind("<FocusIn>", lambda event: self.angle_entry_focus_in())
        self.angle_entry.bind("<FocusOut>", lambda event: self.angle_entry_focus_out())

        self.angle_unit_label = tk.Label(self.angle_panel, font=text.P1, fg=colors.white, bg=colors.grey, text="deg")
        self.angle_unit_label.place(anchor="center", relx=0.8, rely=0.5)

        self.distance_panel = tk.Canvas(self.control_panel, bg=colors.grey, highlightthickness=0)
        self.distance_panel.place(anchor="center", relx=0.5, rely=0.8, relwidth=0.85, relheight=0.25)

        self.distance_entry_panel = tk.Canvas(self.distance_panel, bg=colors.grey, width=self.entry_image_width, height=self.entry_image_height, highlightthickness=0)
        self.distance_entry_panel.config(cursor="xterm")
        self.distance_entry_panel.place(anchor="center", relx=0.4, rely=0.5)
        self.distance_entry_panel.bind("<Button-1>", lambda event: self.distance_entry.focus_set())
        self.distance_entry_panel.create_image(1, 1, anchor=tk.NW, image=self.entry_image)
        self.distance_entry_panel.image = self.entry_image

        self.distance_entry = tk.Entry(self.distance_entry_panel, font=text.P1, fg="grey", bg=colors.white, justify="center", relief="flat")
        self.distance_entry.insert(0, "Maximum Distance")
        self.distance_entry.place(anchor="center", relx=0.5, rely=0.5, relwidth=0.9, relheight=0.7)
        self.distance_entry.bind("<FocusIn>", lambda event: self.distance_entry_focus_in())
        self.distance_entry.bind("<FocusOut>", lambda event: self.distance_entry_focus_out())

        self.distance_unit_label = tk.Label(self.distance_panel, font=text.P1, fg=colors.white, bg=colors.grey, text="meters")
        self.distance_unit_label.place(anchor="center", relx=0.825, rely=0.5)
        
    def create_command_panel(self) -> None:
        self.container_image = Image.open("Command_Container.png")
        self.container_image_width, self.container_image_height = self.container_image.size

        self.command_panel = tk.Canvas(self.bot_panel, bg=colors.white, width=self.container_image_width, height=self.container_image_height)
        self.command_panel.place(anchor="sw", relx=0.015, rely=0.995)

        self.container_image = ImageTk.PhotoImage(self.container_image)
        self.command_panel.create_image(1, 1, anchor=tk.NW, image=self.container_image)
        self.command_panel.image = self.container_image

        self.play_image_inactive = ImageTk.PhotoImage(Image.open("Play_Inactive.jpg").resize((90, 90)))
        self.play_image_active = ImageTk.PhotoImage(Image.open("Play_Active.jpg").resize((90, 90)))
        self.clear_image_inactive = ImageTk.PhotoImage(Image.open("Clear_Inactive.jpg").resize((90, 90)))
        self.clear_image_active = ImageTk.PhotoImage(Image.open("Clear_Active.jpg").resize((90, 90)))
        self.delete_image_inactive = ImageTk.PhotoImage(Image.open("Delete_Inactive.jpg").resize((90, 90)))
        self.delete_image_active = ImageTk.PhotoImage(Image.open("Delete_Active.jpg").resize((90, 90)))

        self.play_image_container = tk.Canvas(self.command_panel, bg=colors.grey, highlightthickness=0, width=90, height=90, cursor="hand2")
        self.play_image_container.place(anchor="center", relx=0.2, rely=0.5)
        self.play_image_container.create_image(0, 0, anchor=tk.NW, image=self.play_image_inactive)
        self.play_image_container.image = self.play_image_inactive
        self.play_image_container.bind("<Enter>", lambda event: self.play_image_container.create_image(0, 0, anchor=tk.NW, image=self.play_image_active))
        self.play_image_container.bind("<Leave>", lambda event: self.play_image_container.create_image(0, 0, anchor=tk.NW, image=self.play_image_inactive))
        
        self.clear_image_container = tk.Canvas(self.command_panel, bg=colors.grey, highlightthickness=0, width=90, height=90, cursor="hand2")
        self.clear_image_container.place(anchor="center", relx=0.5, rely=0.5)
        self.clear_image_container.create_image(0, 0, anchor=tk.NW, image=self.clear_image_inactive)
        self.clear_image_container.image = self.clear_image_inactive
        self.clear_image_container.bind("<Enter>", lambda event: self.clear_image_container.create_image(0, 0, anchor=tk.NW, image=self.clear_image_active))
        self.clear_image_container.bind("<Leave>", lambda event: self.clear_image_container.create_image(0, 0, anchor=tk.NW, image=self.clear_image_inactive))

        self.delete_image_container = tk.Canvas(self.command_panel, bg=colors.grey, highlightthickness=0, width=90, height=90, cursor="hand2")
        self.delete_image_container.place(anchor="center", relx=0.8, rely=0.5)
        self.delete_image_container.create_image(0, 0, anchor=tk.NW, image=self.delete_image_inactive)
        self.delete_image_container.image = self.delete_image_inactive
        self.delete_image_container.bind("<Enter>", lambda event: self.delete_image_container.create_image(0, 0, anchor=tk.NW, image=self.delete_image_active))
        self.delete_image_container.bind("<Leave>", lambda event: self.delete_image_container.create_image(0, 0, anchor=tk.NW, image=self.delete_image_inactive))
        

    def create_display_panel(self) -> None:

        self.container_image = Image.open("Display_Container.png")
        self.container_image_width, self.container_image_height = self.container_image.size
        
        self.display_panel = tk.Canvas(self.bot_panel, bg=colors.white, width=self.container_image_width, height=self.container_image_height)
        self.display_panel.place(anchor="e", relx=0.9925, rely=0.515)

        self.container_image = ImageTk.PhotoImage(self.container_image)
        self.display_panel.create_image(1, 1, anchor=tk.NW, image=self.container_image)
        self.display_panel.image = self.container_image

    def velocity_entry_focus_in(self):
        if self.velocity_entry.get() == "Velocity":
            self.velocity_entry.delete(0, tk.END)
            self.velocity_entry.config(fg=colors.grey)

    def velocity_entry_focus_out(self):
        if self.velocity_entry.get() == "":
            self.velocity_entry.insert(0, "Velocity")
            self.velocity_entry.config(fg="grey")

    def angle_entry_focus_in(self):
        if self.angle_entry.get() == "Angle":
            self.angle_entry.delete(0, tk.END)
            self.angle_entry.config(fg=colors.grey)

    def angle_entry_focus_out(self):
        if self.angle_entry.get() == "":
            self.angle_entry.insert(0, "Angle")
            self.angle_entry.config(fg="grey")

    def distance_entry_focus_in(self):
        if self.distance_entry.get() == "Maximum Distance":
            self.distance_entry.delete(0, tk.END)
            self.distance_entry.config(fg=colors.grey)

    def distance_entry_focus_out(self):
        if self.distance_entry.get() == "":
            self.distance_entry.insert(0, "Maximum Distance")
            self.distance_entry.config(fg="grey")
class OhmVoltage(SubWindow):
    def __init__(self, root) -> None:
        super().__init__(root)
        
    def setup_window(self, root) -> None:
        super().setup_window(root)
        self.root.title("Lunatech Mini Physics Calculator | Voltage and Ohm Calculator")

class DensityVolume(SubWindow):
    def __init__(self, root) -> None:
        super().__init__(root)

    def setup_window(self, root) -> None:
        super().setup_window(root)
        self.root.title("Lunatech Mini Physics Calculator | Density and Volume Calculator")

class WorkEnergy(SubWindow):
    def __init__(self, root) -> None:
        super().__init__(root)

    def setup_window(self, root) -> None:
        super().setup_window(root)
        self.root.title("Lunatech Mini Physics Calculator | Work and Energy Calculator")

class AngularMomentum(SubWindow):
    def __init__(self, root) -> None:
        super().__init__(root)

    def setup_window(self, root) -> None:
        super().setup_window(root)
        self.root.title("Lunatech Mini Physics Calculator | Angular Momentum Calculator")


if __name__ == "__main__":
    print("Lunatech Incorporated @ 2024, Mini Physics Calculator. Version 0.2.1")
