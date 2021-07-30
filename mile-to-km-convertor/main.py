import tkinter

FONT = font = ("Arial", 24, "bold")


def button_clicked():
    # print("I got clicked")
    miles = int(input.get())
    km.config(text=str(round(miles*1.6)))


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=40, pady=40)

# Label
my_label = tkinter.Label(text="is equal to")
# my_label.config(text="New Text")
my_label.grid(column=0, row=1)
# my_label.config(padx=50, pady=50)

# Label - 2
km = tkinter.Label(text="0")
km.grid(column=1, row=1)

# Label - 3
label_3 = tkinter.Label(text="miles")
label_3.grid(column=2, row=0)

# Label - 4
label_4 = tkinter.Label(text="km")
label_4.grid(column=2, row=1)

# Button
button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# new_button = tkinter.Button(text="New Button")
# new_button.grid(column=2, row=0)

# Entry
input = tkinter.Entry(width=10)
input.insert(tkinter.END, string="0")
# print(input.get())
input.grid(column=1, row=0)


window.mainloop()
