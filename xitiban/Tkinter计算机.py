# 第一步：画出图形界面
from tkinter import *
baseFrame = Tk()
baseFrame.title("计算机")

# 定义面板大小
baseFrame.geometry('270x250')
# 定义面板
# bg代表背景颜色(background),#dddddd是十六进制表示颜色的一个串
frame_show = Frame(width = 300, height = 150, background = "#dddddd")
frame_show.pack()
# 定义顶部区域
top = StringVar()
top.set("0")

show_label = Label(frame_show, textvariable = top,
                   background = "yellow" , width = 12, height = 1,
                   font = ("黑体",20,"bold"),
                    justify = LEFT, anchor = "e")
show_label.pack(padx = 10 ,pady = 10)
# 逻辑运算
# try:
num_1 =""
def delete():  # 去位  OK!!!
    global num_1
    num_1 = num_1[0:len(num_1)-1]
    top.set(num_1)
def operator():
    global num_1
    result = eval(num_1)
    top.set(result)
def clear(): # 清除 OK!!!
    global num_1
    global n
    num_1 = ""
    top.set(num_1)
    n =0

def change(num): # 数字符 OK!!!
    global  num_1
    num_1 = num_1 +num
    top.set(num_1)







# 按键区域
frame_bord = Frame(width=400, height=350, bg="#cccccc")
b_delet = Button(frame_bord,text = "←", width = 5, height = 1, command = delete).grid(row = 0 ,column = 1)
b_clear = Button(frame_bord,text = "C", width = 5, height = 1, command = clear).grid(row = 0 ,column = 0)
b_divide = Button(frame_bord,text = "÷", width = 5, height = 1, command = lambda :change("÷")).grid(row = 0 ,column = 3)
b_muplit = Button(frame_bord,text = "×", width = 5, height = 1, command = lambda :change("×")).grid(row = 1 ,column = 3)
b_sum = Button(frame_bord,text = "+", width = 5, height = 1, command = lambda :change("+")).grid(row = 3 ,column = 3)
b_jian = Button(frame_bord,text = "-", width = 5, height = 1, command = lambda :change("-")).grid(row = 2, column = 3)
b_0 = Button(frame_bord,text = "0", width = 5, height = 1, command = lambda :change("0")).grid(row = 4 ,column = 0)
b_1 = Button(frame_bord,text = "1", width = 5, height = 1, command = lambda :change("1")).grid(row = 3 ,column = 0)
b_2 = Button(frame_bord,text = "2", width = 5, height = 1, command = lambda :change("2")).grid(row = 3 ,column = 1)
b_3 = Button(frame_bord,text = "3", width = 5, height = 1, command = lambda :change("3")).grid(row = 3 ,column = 2)
b_4 = Button(frame_bord,text = "4", width = 5, height = 1, command = lambda :change("4")).grid(row = 2 ,column = 0)
b_5 = Button(frame_bord,text = "5", width = 5, height = 1, command = lambda :change("5")).grid(row = 2 ,column = 1)
b_6 = Button(frame_bord,text = "6", width = 5, height = 1, command = lambda :change("6")).grid(row = 2 ,column = 2)
b_7 = Button(frame_bord,text = "7", width = 5, height = 1, command = lambda :change("7")).grid(row = 1 ,column = 0)
b_8 = Button(frame_bord,text = "8", width = 5, height = 1, command = lambda :change("8")).grid(row = 1 ,column = 1)
b_9 = Button(frame_bord,text = "9", width = 5, height = 1, command = lambda :change("9")).grid(row = 1 ,column = 2)
b_point = Button(frame_bord,text = ".", width = 5, height = 1, command = lambda :change(".")).grid(row = 4,column = 1)
b_finally = Button(frame_bord,text = "＝",width = 5, height = 1, command = operator()).grid(row = 4 ,column = 2)
frame_bord.pack(padx = 10 ,pady = 10)
baseFrame.mainloop()







# def reduce(): # 减
#     global num_1
#     num_1 = num_1 + "-"
#     top.set(num_1)
#
# def divied():  # 除
#     global num_1
#     num_1 = num_1 + "÷"
#     top.set(num_1)
# def multiplied(): # 乘
#     global num_1
#     num_1 = num_1 + "×"
#     top.set(num_1)
# def sum(): # 加
#     global num_1
#     total_0 = 0
#     num_1 = num_1 +"+"
#     top.set(num_1)