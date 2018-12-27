import tkinter


if __name__ == "__main__":
    root_window = tkinter.Tk()
    # 标题
    root_window.title("飞机大战")
    # 使图片大小固定
    root_window.resizable(width=False,height=False)

    # 创建画布
    window_canvas = tkinter.Canvas(root_window, width = 480, height = 600)
    window_canvas.pack()

    # 在画布上画一个图片
    # 三个步骤
    # 1.定义图片的位置
    # 2.创建PhotoImage对象
    # 3.利用Create_image函数把图片画上去

    bg_img_name = "../Images/background.gif"
    bg_img = tkinter.PhotoImage(file = bg_img_name)
    # tag作用是，以后使用创建好的image可以通过tags使用
    window_canvas.create_image(240,300,anchor = tkinter.CENTER,image =  bg_img, tags = "bg")



    # 画上一个小蜜蜂
    bee_img_name = "../Images/bee.gif"
    bee_img = tkinter.PhotoImage(file=bee_img_name)
    window_canvas.create_image(240, 300, anchor=tkinter.CENTER, image=bee_img, tags="bee")

    root_window.mainloop()