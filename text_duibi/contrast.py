"""
@Author: Li Yu Cai
@Date: 2024/10/25 下午5:55
@FileName: contrast.py
"""
import re
import string

import tkinter as tk

def contrast_(text_1,text_2):
    contrast_text_1=text_1.replace('\n', '').replace('\r', '').replace(" ", "")
    contrast_text_2=text_2.replace('\n', '').replace('\r', '').replace(" ", "")
    if contrast_text_1==contrast_text_2:
        print("两段文字一致（忽略空格）")
    else:
        print("两段文字不一致")

if __name__ == '__main__':
    text_1="""text1 = "Hello World"
text2 = "Hello World"

if text1 == text2:
    print("两段文字一致")
else:
    print("两段文字不一致")"""
    text_2 = """text1 = "Hello World"
    text2 = "Hello World"
    
    if text1 == text2:
        print("两段文字一致")，
    else:
        print("两段文字不一致")"""
    contrast_(text_1,text_2)