cmake_minimum_required(VERSION 3.7)
project(learning)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
        C语言/array.c)

add_executable(learning ${SOURCE_FILES})