import tkinter
import time
import random as rd
'''
蜜蜂从上到下运动
可以通过键盘进行控制
'''

step = 0 # ji
direction = (1,1)

x = 0
y = 10

def set_right(e):
    global x
    x += 20
def set_left(e):
    global x
    x -= 20

root_window = tkinter.Tk()
root_window.title("wu")

root_window.bind('<Key-Left>', set_left)
root_window.bind('<Key-Right>', set_right)
root_window.resizable(width=False, height=False)


# 创建画布
window_canvas = tkinter.Canvas(root_window,width = 480, height = 600)
window_canvas.pack()

def main():
    bg_img_fullname = "../Images/background.gif"
    start_img = tkinter.PhotoImage(file=bg_img_fullname)
    # tag作用是，以后使用创建好的image可以通过tags使用
    window_canvas.create_image(240, 300, anchor=tkinter.CENTER, image=start_img, tags="start")
    #小蜜蜂
    bee_img_name = "../Images/bee.gif"
    bee_img = tkinter.PhotoImage(file=bee_img_name)
    window_canvas.create_image(240, 300, anchor=tkinter.CENTER, image=bee_img, tags="bee")
    #小飞机
    sp = "../Images/重复的图片/old-airplane.gif"
    sp_img = tkinter.PhotoImage(file = sp)
    window_canvas.create_image(50,50,anchor = tkinter.CENTER,image = sp_img,tags = "sp")



    # 让小飞机动起来
    ap_move()
    root_window.mainloop()
def ap_move():
    global step
    global x
    global y

    y += 5
    print(x,y)
    window_canvas.move("sp",x,y)

    step += 1
    window_canvas.after(1000,ap_move)


if __name__ == "__main__":
    main()
