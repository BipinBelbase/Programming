import tkinter as tk
# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry('400x500')  # Adjust size
root.resizable(0, 0)


# Configure grid rows and columns for responsiveness
for i in range(6):  # 6 rows: 1 for input, 5 for buttons
    root.grid_rowconfigure(i, weight=1)
    if(i<4):
        root.grid_columnconfigure(i, weight=1)
# Variable to store the current expression
expression = ""
# Function to handle button clicks
def button_click(value):
    global expression
    if value == "C":
        expression = ""  # Clear expression
        text_result.delete(0, tk.END)  # Clear input field
    elif value == "=":
        try:
            result = str(eval(expression))  # Safely evaluate the expression
            text_result.delete(0, tk.END)
            text_result.insert(0, result)  # Display the result
            expression = result  # Store result for further operations
        except Exception as e:
            text_result.delete(0, tk.END)
            text_result.insert(0, "Error")  # Show error for invalid expressions
            expression = ""
    else:z
        expression += value  # Append the button value to the expression
        text_result.delete(0, tk.END)
        text_result.insert(0, expression)  # Update the input field
# Input field spanning 4 columns
text_result = tk.Entry(
    root, bg="red", fg="white", font=('verdana', 20, 'bold'),
    justify="right", borderwidth=5
)
text_result.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")
# Button layout: List of button labels
button_labels = [
    "7", "8", "9", "C",  # Row 1
    "4", "5", "6", "/",  # Row 2
    "1", "2", "3", "*",  # Row 3
    "0", ".", "=", "-",  # Row 4
    "+"                  # Row 5
]
# Create and place buttons
buttons = []
for index, label in enumerate(button_labels):
    row = (index // 4) + 1  # Start at row 1 (input is row 0)
    column = index % 4      # 4 buttons per row
    button = tk.Button(
        root, text=label, bg="yellow", fg="black", font=('verdana', 18, 'bold'),
        borderwidth=1, relief="raised",
        command=lambda x=label: button_click(x)  # Pass label to button_click
    )
    button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
    buttons.append(button)
# Run the GUI event loop
root.mainloop()
