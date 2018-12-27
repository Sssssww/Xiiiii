import threading
import time
import p

moive_list = ["一出好戏.mp4","复仇者联盟.avi","aaa.rmvb"]
music_list = ["周杰伦.mp3",'五月天.mp3']
movie_format = ['mp4','avi']
music_format = ['mp3']

def play(playlist):
    for i in playlist:
        if i.split(".")[1] in movie_format:
            print("你现在收看的是：{}" .format(i))
            time.sleep(1)
        if i.split(".")[1]  in music_format :
            print("你现在收听的是：{}" . format(i))
            time.sleep(1)
        else:
            print("没有这个格式")
def thread_run():
    t1 = threading.Thread(target = play ,args = (moive_list,))
    t2 = threading.Thread(target = play ,args = (music_list,))#元组
    t1.start()
    t2.start()
if __name__ == "__main__" :
    thread_run()