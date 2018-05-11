#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 03/04/2018.


from state import curr, switch, stateful, State, behavior


@stateful
class People(object):
    class WorkDay(State):
        default = True

        @behavior
        def day(self):
            print "work hard "

    class Weekend(State):
        @behavior
        def day(self):
            print "play harder!"


people = People()

while True:
    for i in range(1, 8):
        if i == 6:
            switch(people, People.Weekend)
        if i == 1:
            switch(people, People.WorkDay)

        people.day()
