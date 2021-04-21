from tkinter import *

def clickMouse(event) :
     txt = ""
     
     if event.num == 1 :
        if button1.text() == button2.text():
             messagebox.showinfo("강아지 버튼", "강아지가 귀엽죠? ^^")

     elif event.num == 3 :
        txt += "마우스 오른쪽 버튼이 ("

    
    label1.configure(text = txt)

window = Tk()
button1 = Button(window, text = "1번")
button2 = Button(window, text = "1번")
button3 = Button(window, text = "2번")

button1.place(x = 40, y = 40)
button2.place(x = 80, y = 40)
button2.place(x = 120, y = 40)

window.bind("<Button>", clickMouse)
window.mainloop()