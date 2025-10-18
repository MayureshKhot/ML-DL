import tkinter as tk

#Create 
root=tk.Tk()
root.title("Simple Tkinter App")
root.geometry("200x100")

#Function
def say_hello():
    print("Hello world")
    print('Good bye')
    
#Create a button that triggers the say_hello function
hello_button = tk.Button(root, text="Click Me", command=say_hello)
hello_button.pack(pady=20) #Pack the button

root.mainloop()