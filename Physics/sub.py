import tkinter as tk
import ctypes
from PIL import Image, ImageTk
from tkinter import messagebox, ttk
from misc import Text as text, Colors as colors

class SubWindow:
    def __init__(self, root) -> None:
        self.setup_window(root)

    def setup_window(self, root) -> None:
        width, height = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
        self.root = root
        self.root.geometry(f"{width}x{height}")
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
        self.root.title("Lunatech Mini Physics Calculator | Projectile Motion Calculator")

    def create_top_panel(self) -> None:
        self.top_panel = tk.Canvas(self.root, bg=colors.grey, highlightthickness=0)
        self.top_panel.place(anchor="n", relx=0.5, rely=0, relwidth=1, relheight=0.125)

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
        self.control_panel = tk.Canvas(self.bot_panel, bg=colors.grey, highlightthickness=3)
        self.control_panel.place(anchor="nw", relx=0.025, rely=0.05, relwidth=0.325, relheight=0.7)

        self.control_panel_label_container = tk.Canvas(self.control_panel, bg=colors.grey, highlightthickness=3)
        self.control_panel_label_container.config(highlightcolor=colors.border, highlightbackground=colors.border)
        self.control_panel_label_container.place(anchor="n", relx=0.5, rely=0, relwidth=1, relheight=0.1)

        self.control_panel_label = tk.Label(self.control_panel_label_container, font=text.P1, fg=colors.white, bg=colors.grey, text="S L I D E R S   P A N E L")
        self.control_panel_label.place(anchor="center", relx=0.5, rely=0.5)

        self.velocity_container = tk.Canvas(self.control_panel, bg=colors.grey, highlightthickness=0)
        self.velocity_container.place(anchor="n", relx=0.5, rely=0.1, relwidth=1, relheight=0.225)

        self.velocity_label = tk.Label(self.velocity_container, font=text.P1, fg=colors.white, bg=colors.grey, text="Velocity : ")
        self.velocity_label.place(anchor="center", relx=0.25, rely=0.5)

        self.velocity_entry = tk.Entry(self.velocity_container, font=text.P2, fg=colors.grey, bg=colors.white, relief="flat", justify="center")
        self.velocity_entry.place(anchor="center", relx=0.525, rely=0.5, relwidth=0.35, relheight=0.325)

        self.velocity_unit = tk.Label(self.velocity_container, font=text.P1, fg=colors.white, bg=colors.grey, text="m/s")
        self.velocity_unit.place(anchor="center", relx=0.75, rely=0.5)
        
        self.distance_container = tk.Canvas(self.control_panel, bg=colors.grey, highlightthickness=0)
        self.distance_container.place(anchor="n", relx=0.5, rely=0.325, relwidth=1, relheight=0.225)

        self.distance_label = tk.Label(self.distance_container, font=text.P1, fg=colors.white, bg=colors.grey, text="Distance : ")
        self.distance_label.place(anchor="center", relx=0.25, rely=0.5)

        self.distance_entry = tk.Entry(self.distance_container, font=text.P2, fg=colors.grey, bg=colors.white, relief="flat", justify="center")
        self.distance_entry.place(anchor="center", relx=0.525, rely=0.5, relwidth=0.35, relheight=0.325)

        self.distance_unit = tk.Label(self.distance_container, font=text.P1, fg=colors.white, bg=colors.grey, text="kg")
        self.distance_unit.place(anchor="center", relx=0.75, rely=0.5)

        self.angle_container = tk.Canvas(self.control_panel, bg=colors.grey, highlightthickness=0)
        self.angle_container.place(anchor="n", relx=0.5, rely=0.55, relwidth=1, relheight=0.225)

        self.angle_label = tk.Label(self.angle_container, font=text.P1, fg=colors.white, bg=colors.grey, text="Angle : ")
        self.angle_label.place(anchor="center", relx=0.25, rely=0.5)

        self.angle_entry = tk.Entry(self.angle_container, font=text.P2, fg=colors.grey, bg=colors.white, relief="flat", justify="center")
        self.angle_entry.place(anchor="center", relx=0.525, rely=0.5, relwidth=0.35, relheight=0.325)

        self.angle_unit = tk.Label(self.angle_container, font=text.P1, fg=colors.white, bg=colors.grey, text="deg")
        self.angle_unit.place(anchor="center", relx=0.75, rely=0.5)

        self.gravity_container = tk.Canvas(self.control_panel, bg=colors.grey, highlightthickness=0)
        self.gravity_container.place(anchor="n", relx=0.5, rely=0.775, relwidth=1, relheight=0.225)

        self.gravity_label = tk.Label(self.gravity_container, font=text.P1, fg=colors.white, bg=colors.grey, text="Gravity : ")
        self.gravity_label.place(anchor="center", relx=0.25, rely=0.5)

        self.gravity_options = ["Earth (9.81)"]
        self.gravity_selected = tk.StringVar()
        self.gravity_selected.set(self.gravity_options[0])
        self.gravity_selection_box= ttk.Combobox(self.gravity_container, value=self.gravity_options, font=text.P1, width=13, cursor="hand2")
        self.gravity_selection_box.config(state="readonly", textvariable=self.gravity_selected)
        self.gravity_selection_box.current(0)
        self.gravity_selection_box.place(anchor="center", relx=0.525, rely=0.5)

        self.gravity_unit = tk.Label(self.gravity_container, font=text.P1, fg=colors.white, bg=colors.grey, text="m/s^2")
        self.gravity_unit.place(anchor="center", relx=0.75, rely=0.5)


    def create_command_panel(self) -> None:
        self.command_panel = tk.Canvas(self.bot_panel, bg=colors.grey, highlightthickness=3)
        self.command_panel.place(anchor="sw", relx=0.025, rely=0.95, relwidth=0.325, relheight=0.15)

        self.play_image_inactive = ImageTk.PhotoImage(Image.open("Play_Inactive.jpg").resize((70, 70)))
        self.play_image_active = ImageTk.PhotoImage(Image.open("Play_Active.jpg").resize((70, 70)))
        self.play_image_box = tk.Label(self.command_panel, bg=colors.grey, image=self.play_image_inactive, cursor="hand2")
        self.play_image_box.image = self.play_image_inactive
        self.play_image_box.place(anchor="center", relx=0.2, rely=0.5)
        #self.play_image_box.bind("<Button-1>", lambda event: )

        self.clear_image_inactive = ImageTk.PhotoImage(Image.open("Clear_Inactive.jpg").resize((70, 70)))
        self.clear_image_active = ImageTk.PhotoImage(Image.open("Clear_Active.jpg").resize((70, 70)))
        self.clear_image_box = tk.Label(self.command_panel, bg=colors.grey, image=self.clear_image_inactive, cursor="hand2")
        self.clear_image_box.image = self.clear_image_inactive
        self.clear_image_box.place(anchor="center", relx=0.5, rely=0.5)
        #self.clear_image_box.bind("<Button-1>", lambda event: pass)

        self.delete_image_inactive = ImageTk.PhotoImage(Image.open("Delete_Inactive.jpg").resize((70, 70)))
        self.delete_image_active = ImageTk.PhotoImage(Image.open("Delete_Active.jpg").resize((70, 70)))
        self.delete_image_box = tk.Label(self.command_panel, bg=colors.grey, image=self.delete_image_inactive, cursor="hand2")
        self.delete_image_box.image = self.delete_image_inactive
        self.delete_image_box.place(anchor="center", relx=0.8, rely=0.5)
        #self.delete_image_box.bind("<Button-1>", lambda event: pass)

    def create_display_panel(self) -> None:
        self.display_panel = tk.Canvas(self.bot_panel, bg=colors.grey, highlightthickness=0)
        self.display_panel.place(anchor="e", relx=0.975, rely=0.5, relwidth=0.6, relheight = 0.9)



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
