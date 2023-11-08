#!/usr/bin/python3
'''
Module of the Student class.
'''


class Student:
    '''class Student

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    '''
    def __init__(self, first_name, last_name, age):
        '''The defeault constructor of class Student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''to_json

        Retrieves a dictionary representation of a Student
        instance (same as `8-class_to_json.py`).
        '''
        class_d = self.__dict__
        sel_d = dict()

        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is not str:
                    return class_d

                if attr in class_d:
                    sel_d[attr] = class_d[attr]

            return sel_d

        return class_d

    def reload_from_json(self, json):
        '''reload_from_json

        Replaces all attributes of the Student instance
        '''
        for i in json:
            if i in self.__dict__.keys():
                self.__dict__[i] = json[i]
