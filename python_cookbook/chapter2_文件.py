#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime :
# @Author   : Z LEI

"""
2.1 读取文件
"""

all_the_text = open('chapter1_1.py').read()  # 文本中的所有文本
all_the_data = open('chapter1_1.py', 'rb').read()  # 二进制文件中的所有数据
print all_the_data

file_object = open('chapter1_1.py')
list_of_all_the_lines = file_object.readlines()  # 文本会带'\n'
# 不带'\n'
list_of_all_the_lines = file_object.read().splitlines()  #
list_of_all_the_lines = file_object.read().split('\n')
list_of_all_the_lines = [L.rstrip('\n')for L in     file_object]