# -*- coding: utf-8 -*-
import re
import string

import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("字数统计工具")
root.geometry("")
cleaned = None


def update_word_count(event=None):
    """更新字数显示"""
    text_content = text_box.get("1.0", "end-1c")  # 获取输入框中的内容
    if cleaned == 1:
        pattern = r"[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）《》【】「」『』；：]+"
        # 去除标点符号
        cleaned_text = re.sub(pattern, "", text_content)
        # 创建翻译表，将标点符号替换为空字符
        translator = str.maketrans('', '', string.punctuation)
        # 去除标点符号
        text_content = cleaned_text.translate(translator)

    word_count = len(text_content.replace('\n', '').replace('\r', '').replace(" ", ""))
    word_count_label.config(text=f"字数：{word_count}")


def cleaned_1():
    global cleaned
    cleaned = 1
    update_word_count()


def cleaned_0():
    global cleaned
    cleaned = 0
    update_word_count()


# 创建文本输入框
text_box = tk.Text(root, wrap="word", font=("微软雅黑", 14))
text_box.grid(row=0, column=1, sticky="nsew")

text_box.bind("<KeyRelease>", update_word_count)  # 监听键盘输入事件
# 创建字数显示标签
word_count_label = tk.Label(root, text="字数：0", font=("微软雅黑", 12))
# 使用grid布局
word_count_label.grid(row=2, column=1, padx=10)
# 创建按钮并绑定事件
button = tk.Button(root, text="去掉标点计算", font=("微软雅黑", 14), command=cleaned_1)
button.grid(row=2, column=0, padx=10, sticky="w")
# 创建按钮并绑定事件
button = tk.Button(root, text="加上标点计算", font=("微软雅黑", 14), command=cleaned_0)
button.grid(row=2, column=2, padx=10, sticky="e")
root.mainloop()
