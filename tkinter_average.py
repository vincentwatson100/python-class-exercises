import tkinter as tk

# Initialize variables
total = 0
count = 0

# Function to add numbers and calculate the average
def calculate():
    global total, count
    inp = entry.get()  # Get input from the entry field
    
    if inp.lower() == 'done':  # If 'done' is entered, stop
        if count > 0:
            average = total / count
            result_label.config(text=f"Average: {average}")  # Display average
        else:
            result_label.config(text="No numbers entered.")
    else:
        try:
            value = float(inp)  # Convert input to a float
            total += value  # Add to the total
            count += 1  # Increment the count
            entry.delete(0, tk.END)  # Clear the entry field for the next input
            entry.focus()  # Focus back to the input field
            result_label.config(text=f"Total: {total}  Count: {count}")  # Show the updated total and count
        except ValueError:
            result_label.config(text="Please enter a valid number.")

# Create the main window
window = tk.Tk()
window.title("Average Calculator")

# Create widgets
prompt_label = tk.Label(window, text="Enter a number (or 'done' to finish):")
prompt_label.pack()

entry = tk.Entry(window)
entry.pack()

calculate_button = tk.Button(window, text="Add Number", command=calculate)
calculate_button.pack()

result_label = tk.Label(window, text="Total: 0  Count: 0")
result_label.pack()

# Start the GUI loop
window.mainloop()
