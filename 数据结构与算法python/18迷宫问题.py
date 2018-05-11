#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 03/01/2018.


maze = [
    list('11111111111111'),
    list('10001100010001'),
    list('10100001010101'),
    list('10101111010101'),
    list('10100000011101'),
    list('10111111110001'),
    list('10100000000101'),
    list('10001110101101'),
    list('10101010101001'),
    list('10101010111101'),
    list('10100010010001'),
    list('11111111111111')
]

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def mark(maze, pos):
    """是否走过了"""
    maze[pos[0]][pos[1]] = 2


def passable(maze, pos):
    """是否可通行"""
    return maze[pos[0]][pos[1]] == 0


def find_path(maze, pos, end):
    mark(maze, pos)
    if pos == end:
        print pos
        return True
    for i in range(4):
        nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
        if passable(maze, nextp):
            if find_path(maze, nextp, end):
                print pos
                return True
    return False


print maze[1][1]
print maze[10][12]

find_path(maze, (1, 1), (10, 12))
