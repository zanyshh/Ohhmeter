
import customtkinter as ctk

def calculate_resistance():
    # Color code values for resistance and tolerance
    color_values = {
        'black': 0, 'brown': 1, 'red': 2, 'orange': 3,
        'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7,
        'gray': 8, 'white': 9
    }
    multiplier_values = {
        'black': 1, 'brown': 10, 'red': 100, 'orange': 1_000,
        'yellow': 10_000, 'green': 100_000, 'blue': 1_000_000,
        'gold': 0.1, 'silver': 0.01
    }
    tolerance_values = {
        'brown': '±1%', 'red': '±2%', 'green': '±0.5%',
        'blue': '±0.25%', 'violet': '±0.1%', 'gray': '±0.05%',
        'gold': '±5%', 'silver': '±10%'
    }

    # Get selected colors
    band1 = band1_var.get()
    band2 = band2_var.get()
    band3 = band3_var.get()
    band4 = band4_var.get()

    # Validate selection
    if band1 not in color_values or band2 not in color_values:
        result_label.configure(text="Error: Invalid color for band 1 or 2.")
        return
    if band3 not in multiplier_values:
        result_label.configure(text="Error: Invalid color for multiplier.")
        return
    if band4 not in tolerance_values:
        result_label.configure(text="Error: Invalid color for tolerance.")
        return

    # Calculate resistance
    first_digit = color_values[band1]
    second_digit = color_values[band2]
    multiplier = multiplier_values[band3]
    tolerance = tolerance_values[band4]
    resistance = (first_digit * 10 + second_digit) * multiplier

    # Update the result
    result_label.configure(text=f"Resistance: {resistance} Ohms\nTolerance: {tolerance}")

    # Update the resistor image bands
    update_resistor_band(resistor_canvas, band1, 40)
    update_resistor_band(resistor_canvas, band2, 80)
    update_resistor_band(resistor_canvas, band3, 120)
    update_resistor_band(resistor_canvas, band4, 160)

def update_resistor_band(canvas, color, x_position):
    """Update a specific band color on the resistor image."""
    canvas.create_rectangle(x_position, 50, x_position + 20, 100, fill=color, outline=color)

# CustomTkinter GUI setup
ctk.set_appearance_mode("System")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")
               

root = ctk.CTk()
root.title("Ohhhmeter")
root.iconbitmap("resources/resistor.ico")

# Define color options
color_options = [
    'black', 'brown', 'red', 'orange', 'yellow', 'green',
    'blue', 'violet', 'gray', 'white', 'gold', 'silver'
]

# Resistor drawing
resistor_canvas = ctk.CTkCanvas(root, width=300, height=150, bg="#3a3a3a")
resistor_canvas.grid(row=0, column=0, columnspan=3, pady=10)

# Draw resistor base
resistor_canvas.create_oval(30, 50, 50, 100, fill="lightgray", outline="black")  # Left rounded 
resistor_canvas.create_oval(250, 50, 270, 100, fill="lightgray", outline="black")  # Right rounded end
resistor_canvas.create_rectangle(40, 50, 260, 100, fill="lightgray", outline="black")  # Main bodycanvas
resistor_canvas.create_line(10, 75, 30, 75, width=5)  # Left lead
resistor_canvas.create_line(270, 75, 290, 75, width=5)  # Right lead  # Right lead

# Create dropdowns for each band
band1_var = ctk.StringVar(value="Select Color")
band2_var = ctk.StringVar(value="Select Color")
band3_var = ctk.StringVar(value="Select Color")
band4_var = ctk.StringVar(value="Select Color")

band1_label = ctk.CTkLabel(root, text="Band 1:")
band1_label.grid(row=1, column=0, padx=10, pady=5)
band1_menu = ctk.CTkComboBox(root, variable=band1_var, values=color_options[:10])
band1_menu.grid(row=1, column=1, padx=10, pady=5)

band2_label = ctk.CTkLabel(root, text="Band 2:")
band2_label.grid(row=2, column=0, padx=10, pady=5)
band2_menu = ctk.CTkComboBox(root, variable=band2_var, values=color_options[:10])
band2_menu.grid(row=2, column=1, padx=10, pady=5)

band3_label = ctk.CTkLabel(root, text="Band 3 (Multiplier):")
band3_label.grid(row=3, column=0, padx=10, pady=5)
band3_menu = ctk.CTkComboBox(root, variable=band3_var, values=color_options)
band3_menu.grid(row=3, column=1, padx=10, pady=5)

band4_label = ctk.CTkLabel(root, text="Band 4 (Tolerance):")
band4_label.grid(row=4, column=0, padx=10, pady=5)
band4_menu = ctk.CTkComboBox(root, variable=band4_var, values=color_options[-4:])
band4_menu.grid(row=4, column=1, padx=10, pady=5)

# Calculate button
calculate_button = ctk.CTkButton(root, text="Calculate Resistance", command=calculate_resistance,fg_color="#4a4e69",hover_color="#8e9aaf")
calculate_button.grid(row=5, column=0, columnspan=3, pady=10)

# Result label
result_label = ctk.CTkLabel(root, text="Select colors and click Calculate", font=("Arial", 12))
result_label.grid(row=6, column=0, columnspan=3, pady=10)

# Run the CustomTkinter event loop

if __name__ == '__main__':
    root.mainloop()
