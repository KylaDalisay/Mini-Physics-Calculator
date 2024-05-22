import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def projectile_motion(v0, theta, g):
    """
    Calculate the trajectory of a projectile and return trajectory data points.

    Parameters:
    v0 (float): Initial velocity in m/s.
    theta (float): Angle of projection in degrees.
    g (float): Gravitational acceleration in m/s^2.

    Returns:
    dict: A dictionary containing time of flight, range, maximum height, and trajectory data points (x, y).
    """
    # Convert angle to radians
    theta_rad = math.radians(theta)

    # Decompose initial velocity into horizontal and vertical components
    v0x = v0 * math.cos(theta_rad)
    v0y = v0 * math.sin(theta_rad)

    # Calculate time of flight
    T = (2 * v0y) / g

    # Calculate range
    R = (v0 ** 2 * math.sin(2 * theta_rad)) / g

    # Calculate maximum height
    H = (v0y ** 2) / (2 * g)

    # Calculate trajectory points
    num_points = 500  # Number of points to plot
    t_values = [i * T / num_points for i in range(num_points + 1)]
    x_values = [v0x * t for t in t_values]
    y_values = [v0y * t - 0.5 * g * t ** 2 for t in t_values]

    return {
        'time_of_flight': T,
        'range': R,
        'maximum_height': H,
        'x_values': x_values,
        'y_values': y_values
    }

def plot_trajectory(v0, theta, g):
    trajectory = projectile_motion(v0, theta, g)
    
    fig, ax = plt.subplots()
    ax.plot(trajectory['x_values'], trajectory['y_values'], label=f'Trajectory (v0={v0} m/s, θ={theta}°)')
    ax.set_title('Projectile Motion Trajectory')
    ax.set_xlabel('Horizontal Distance (m)')
    ax.set_ylabel('Vertical Distance (m)')
    ax.legend()
    ax.grid(True)

    return fig

def update_plot(*args):
    global canvas
    try:
        v0 = float(velocity_var.get())
        theta = float(angle_var.get())
        g = float(gravity_var.get())
    except ValueError:
        return
    
    fig = plot_trajectory(v0, theta, g)
    
    if canvas is not None:
        canvas.get_tk_widget().pack_forget()  # Remove the old canvas

    canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create main window
window = tk.Tk()
window.title("Projectile Motion Trajectory")

# Create variables and trace them
velocity_var = tk.StringVar()
angle_var = tk.StringVar()
gravity_var = tk.StringVar()
velocity_var.trace('w', update_plot)
angle_var.trace('w', update_plot)
gravity_var.trace('w', update_plot)

# Create input fields
frame = tk.Frame(window)
frame.pack(side=tk.TOP, pady=10)

label_velocity = tk.Label(frame, text="Initial Velocity (m/s):")
label_velocity.pack(side=tk.LEFT)
entry_velocity = tk.Entry(frame, textvariable=velocity_var)
entry_velocity.pack(side=tk.LEFT, padx=5)

label_angle = tk.Label(frame, text="Angle (degrees):")
label_angle.pack(side=tk.LEFT)
entry_angle = tk.Entry(frame, textvariable=angle_var)
entry_angle.pack(side=tk.LEFT, padx=5)

label_gravity = tk.Label(frame, text="Gravity (m/s^2):")
label_gravity.pack(side=tk.LEFT)
entry_gravity = tk.Entry(frame, textvariable=gravity_var)
entry_gravity.pack(side=tk.LEFT, padx=5)

# Set default values
velocity_var.set("10")  # Example initial velocity
angle_var.set("45")  # Example angle
gravity_var.set("1.625")  # Default to Moon gravity

# Initialize canvas variable
canvas = None

# Start the Tkinter event loop
window.mainloop()
