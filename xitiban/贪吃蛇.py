import tkinter
import time
import threading
import queue
from  queue import Queue
from  tkinter import  Tk

class Food():
    '''
    功能：
        1. 出现在画面的某一个地方
        2. 一旦被吃，则增加蛇的分数

    '''

    def __init__(self, queue):
        '''
        自动产生一个食物
        '''
        self.queue = queue
        self.new_food()

    def new_food():
        '''
        功能：产生一个食物
        产生一个食物的过程就是随机产生一个食物坐标的过程
        '''
        # 注意横纵坐标产生的范围
        x = random.randrange(50, 480, 10)
        y = random.randrange(50, 480, 10)
        # 需要注意的是，我们的正给游戏屏幕一般不需要把他设置成正方形

        self.positon = x, y  # position存放食物的位置

        # 队列，就是一个不能够随意访问内部元素，只能从头弹出一个元素并只能
        # 从队尾追加元素的list
        #  把一个食物产生的消息放入队列
        # 消息的格式，自己定义
        # 我的定义是： 消息是一个dict， k代表消息类型，v代表此类型的数据
        self.queue.put({"food": self.postion})

        class Snake(threading.Thread):
            '''
            蛇的功能：
                1. 蛇能懂，由我们的上下左右按键控制
                2. 蛇每次懂，都需要重新计算蛇头的位置
                3. 检测是否游戏结束的功能
            '''

            def __init__(self, world, queue):
                threading.Thread.__init__(self)

                self.world = world
                self.queue
                self.potion_earned = 0  # 分数
                self.food = Food(self.queue)
                self.snake_points = [(495, 55), (485, 55), (475, 55), (465, 55), (455, 55)]

                self.start()

            def run(self):
                '''
                一旦启用多线成调用次函数
                '''
                if self.world.is_game_over:
                    self._delete()
                while not self.world.is_game_over:
                    self.queue.put({"move": self.snake_points})
                    time.sleep(0.5)  # 控制蛇的速度
                    self.moc

            def move(self):
                '''
                负责蛇的移动
                1.重新计算蛇头的坐标
                2. 当蛇头与食物相遇，则加分，重新生成食物，通知world，加分
                3. 否则，蛇需要动
                '''

                new_snake_point = set.cal_new_pos()  # 重新计算蛇头位置

                # 蛇头位置跟食物相同
                if self.food.postion == new_snake_point:
                    self.points_earned += 1  # 得分加1
                    self.queue.put({"point_earned": self.point_earned})
                else:
                    # 需要注意蛇的信息的保存方式
                    # 每次移动是删除存放蛇的最前位置，并在后面追加
                    self.snake_points.pop(0)
                    # 判断程序是否突出，因为新的蛇可能撞墙
                    self.check_game_over(new_snake_point)
                    slef.snake_point.append(new_snake_point)

            def call_new_position(self):
                '''
                计算新的蛇头的位置
                '''
                last_x, lasty = self.snake_point[-1]
                if self.direction == "Up":  # direction负责存储蛇移动的方向
                    new_snake_point = last_x, last_y - 10  # 每次移动的跨度是10像素
                elif self.direction == "Donw":
                    new_snake_point = last_x, last_y + 10
                elif self.direction == "Right":
                    new_snake_point = last_x + 10, last_y
                elif self.direction == "Left":
                    new_snake_point = last_x - 10, last_y

                return new_snake_point

            def key_pressed(self, e):
                # keysym 是按键名称
                self.dircection == e.keysym

            def check_game_over(self, snake_point):
                '''
                判断依据蛇头是否撞墙
                '''
                x, y = snake_point[0], snake_point[1]
                if not -5 < x < 505 or not -5 < y < 315 or snake_point in self.snake_point:
                    self.queue.put({"game_over": True})

class World(Tk):
    def __init__(self):
        Tk.__init__(self)


        # self.queue
        self.is_game_over = False

        # 定义画布
        self.canvas = tkinter.Canvas(self, width=500, height=300)
        self.canvas.pack()

        # 画出蛇和食物
        self.snake = self.canvas.create_line((0, 0), (0, 0), fill="black", width=10)
        self.food = self.canvas.create_rectangle(0, 0, 0, 0, fill="yellow", outline="yellow")
        self.point_earned = self.canvas.create_text(450, 20, fill="white", text="SCORE :0")
        self.queue_handler()

    def queue_handler(self):
        try:
            # 需要不断的从消息队列拿到消息，所以要用死循环
            while True:
                task = self.queue.get(block=False)
                if task.get("game_over"):
                    self.game_over()
                if task.get("move"):
                    points = [x for point in task['move'] for x in point]
                    # 重新绘制蛇
                    self.canvas.coords(self.snake, *points)
                # 同样道理，还需处理食物，得分
        except queue.Empty:  # 爆出队为空异常
            if not self.is_game_over:
                # after的含义是，在多少毫秒后调用后面的函数
                self.canvas.after(100, self.queue_handler)

    def game_over(self):
        '''
        结束优先，清理现场
        '''

        self.os_game_over = True
        self.canvas.create_text("Game Over")
        qb = Button(self, text="Quit", command=self.destory)
        rb = Button(self, text="Again", command=self.__init__)


if __name__ == "__main__":
    q = queue.Queue()
    world = World()
    snake = snake(world, q)

    world.bind("<Key-Left>", snake.key_pressed)
    x = random.randrange(50, 480, 10)