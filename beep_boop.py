import tkinter

# Create root window

root = tkinter.Tk()

# Create widgets

lable_title = tkinter.Label(root, text="Welcome to my guessing game blah blah blah!")
lable_title.pack()

lable_result = tkinter.Label(root, text="Good Luck, hope you can figure it out!")
lable_result.pack()

btn_check = tkinter.Button(root, text="Check", fg="blue", command=root.quit)
btn_check.pack(side="left")

btn_reset = tkinter.Button(root, text="Reset", fg="red", command=root.quit)
btn_reset.pack(side="right")

txt_guess = tkinter.Entry(root, width=3)
txt_guess.pack()

# Start main loop

root.mainloop()
root.destroy()
