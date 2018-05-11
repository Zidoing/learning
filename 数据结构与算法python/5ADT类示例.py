#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 26/12/2017.
import datetime


class PersonTypeError(TypeError):
    pass


class PersonValueError(ValueError):
    pass


class Person(object):
    _num = 0

    def __init__(self, name, sex, birthday, ident):
        if not (isinstance(name, str) and sex in ("女", "男")):
            raise PersonValueError

        try:
            birth = datetime.date(*birthday)
        except:
            raise PersonValueError
        self._name = name
        self._sex = sex
        self._birthday = birth
        self._id = ident
        Person._num += 1

    def id(self):
        return self._id

    def name(self):
        return self._name

    def sex(self):
        return self._sex

    def birthday(self):
        return self._birthday

    def age(self):
        return datetime.date.today().year - self._birthday.year

    def set_name(self, name):
        if isinstance(name, str):
            raise PersonValueError
        self._name = name

    def __lt__(self, other):
        if not isinstance(other, Person):
            raise PersonTypeError
        return self._id < other._id

    @classmethod
    def num(cls):
        return cls._num

    def __str__(self):
        return " ".join((str(self._id), self._name, self._sex, str(self._birthday)))

    def detail(self):
        return ", ".join(("编号：" + str(self._id), "性别：" + self._sex, "姓名：" + self._name, "出生日期：" + str(self._birthday)))


class Student(Person):
    _id_num = 0

    @classmethod
    def _id_gen(cls):
        cls._id_num += 1
        year = datetime.date.today().year
        return "1{:04}{:05}".format(year, cls._id_num)

    def __init__(self, name, sex, birthday, department):
        super(Student, self).__init__(name, sex, birthday, Student._id_gen())
        self._department = department
        self._enroll_date = datetime.date.today()
        self._courses = {}

    def set_course(self, course_name):
        self._courses[course_name] = None

    def set_score(self, course_name, score):
        if course_name not in self._courses:
            raise PersonValueError("no this course selected:", course_name)

    def scores(self):
        return [(cname, self._courses[cname]) for cname in self._courses]


    def detail(self):
        return ", ".join((super(Student, self).detail(), "入学日期："+str(self._enroll_date),"学院:"+str(self._department),"课程记录："+str(self.scores())))

print Person("zhou", "男", (2017, 2, 2), 2)
print Person("zhou", "男", (2017, 2, 2), 2).detail()
print Person.num()

a = Student("zhou", "男", (2017, 2, 2), 2)
print a.detail()
