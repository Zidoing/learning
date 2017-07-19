cmake_minimum_required(VERSION 3.7)
project(learning)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
        fluent_python/__init__
        fluent_python/chapter1.py
        fluent_python/xx.md
        progit/readme.md
        python_cookbook/chapter1_1.py
        python_cookbook/readme.md
        代码大全/file.md
        __init__.py
        README.md)

add_executable(learning ${SOURCE_FILES})