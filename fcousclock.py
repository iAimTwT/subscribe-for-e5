import time
import tkinter as tk
from tkinter import messagebox

# 设置倒计时时间（以秒为单位）
countdown_seconds = 1500  # 25分钟

def start_countdown():
    global countdown_seconds
    while countdown_seconds:
        mins, secs = divmod(countdown_seconds, 60)
        timeformat = f'{mins:02d}:{secs:02d}'
        countdown_label.config(text=timeformat)
        root.update()
        time.sleep(1)
        countdown_seconds -= 1

    # 显示提醒消息
    messagebox.showinfo("提醒", "时间到！请专注工作。")

# 创建主窗口
root = tk.Tk()
root.title("专注时钟")

# 创建倒计时标签
countdown_label = tk.Label(root, text="", font=("Helvetica", 48))
countdown_label.pack(pady=20)

# 创建开始按钮
start_button = tk.Button(root, text="开始", command=start_countdown)
start_button.pack()

root.mainloop()
