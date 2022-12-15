import tkinter as tk
import AppOpener

# Create the root window
root = tk.Tk()
root.title("AppOpener with Tkinter")

# Set the size and position of the window using the geometry() method
root.geometry("500x500+{}+{}".format(int(root.winfo_screenwidth()/2 - 350), int(root.winfo_screenheight()/2 - 350)))

# Create the text area
text_area = tk.Text(root, height=10, width=30, font=("Helvetica", 20))
text_area.pack()

# Create the button
button = tk.Button(root, text="Submit", font=("Helvetica", 20))
button.pack()

# Create the label
label = tk.Label(root, text="", font=("Helvetica", 20))
label.pack()
text_area.focus()
# Define the function to be called when the button is clicked
def submit(event):
  # Get the text entered in the text area
  text = text_area.get("1.0", "end")
  AppOpener.run(str(text))
  # Set the text of the label to the entered text
  label.config(text=str("Looking for "+text))
  # Clear the text area
  text_area.delete("1.0", "end")

# Bind the submit function to the button's click event
button.bind("<Button-1>", submit)

# Bind the "Return" key to the button's click event
root.bind("<Return>", submit)

# Start the main event loop
root.mainloop()
