from guizero import App, Box, PushButton, Text, TextBox

# Function to handle button presses
def button_press(value):
    if value == "=":  # Calculate the result
        try:
            result.value = str(eval(expression.value))
        except Exception:
            result.value = "Error"
    elif value == "C":  # Clear the input
        expression.value = ""
        result.value = ""
    else:  # Append the pressed button's value to the expression
        expression.value += value

# Create the app
app = App("Calculator", width=300, height=400)

# Display for the calculator
expression = TextBox(app, width=20, align="top")
expression.disable()  # Prevent manual typing
result = Text(app, text="", size=18, color="blue")

# Create a grid of buttons for the calculator
buttons = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["C", "0", "=", "/"]
]

button_box = Box(app, layout="grid")
for row_index, row in enumerate(buttons):
    for col_index, button_text in enumerate(row):
        PushButton(
            button_box,
            text=button_text,
            grid=[col_index, row_index],
            width=3,
            command=button_press,
            args=[button_text]
        )

# Run the app
app.display()
