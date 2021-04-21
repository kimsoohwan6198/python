import functools as fc
import tkinter as t
def click_button(number):
    print("you clicked %d" % number)
root = t.Tk()
for number in range(0, 10):
    btn = t.Button(
        root,
        text=number,
        padx=15,
        command=fc.partial(click_button, number))
    btn.grid(row=20, column=number)
root.mainloop()
 