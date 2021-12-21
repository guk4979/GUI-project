import tkinter
from start import *


imrawling = tkinter.Tk()

imrawling.title("사진 줍줍")
imrawling.geometry("1200x800+300+100")
imrawling.resizable(False,False)

# def click():
#     print("click")



def active_btn():
    sel = start(keyword_entry.get(), int(limit_entry.get()))

    sel.active()

title = tkinter.Label(imrawling, text="사진 줍줍",font='Helvetica 20 bold')
title.place(x=95, y=50)

keyword_entry = tkinter.Entry(imrawling)
keyword_entry.insert(0, "키워드를 입력하세요")
keyword_entry.bind("<Return>", active_btn)
keyword_entry.place(x=95, y=200, height=30, width=500)

limit_text = tkinter.Label(imrawling, text="다운로드할 사진 개수 :", font= "Helvetica 13")
limit_text.place(x=95, y=250)

limit_entry = tkinter.Entry(imrawling)
limit_entry.insert(0, 0)
limit_entry.bind("<Return>", active_btn)
limit_entry.place(x=275, y=250, height=30, width=320)

# start_img = PhotoImage(".\시작 버튼.png")
start_btn = tkinter.Button(imrawling, overrelief="solid", command=active_btn, repeatdelay=10, repeatinterval=10)
start_btn.place(x=930, y=625, height=80, width=80) 

# def motion(event):
#     x, y = event.x, event.y
#     print('{}, {}'.format(x, y))
# imrawling.bind('<Motion>', motion)


imrawling.mainloop()


# sel = start("keyword",3) #초기 세팅

# sel.active() #실행