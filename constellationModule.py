
"""
Модуль в котором содержатся звезды и тд
Допустим есть звезда. У нее есть методы, которые соответствуют стадиям эволюции звезд.
(протозвезда, звездоподобная звезда, красный карлик и т.д.)
есть конкретный экземляр звезды , который может быть класса 1. 2, 3, и т.д.
эволюция данного экзепляра звезды складывается из методов родительского класса star
"""

from tkinter import *
from random import *
from constants import *


class sky():

    root = Tk()
    root.title('Star Sky')

    canvas_for_label = Canvas(root, bg = 'red')
    canvas_for_label.grid(sticky = "w")
    label_star_quantity = Label(canvas_for_label, text ='количество звезд')
    label_star_quantity.grid(row = 0, column = 0, sticky = "w")

    label_cpu = Label(canvas_for_label, text = '  загрузка ЦПУ  ')
    label_cpu.grid(row = 0, column = 1, sticky = "w")
    label_memory= Label(canvas_for_label, text='  загрузка памяти  ')
    label_memory.grid(row=0, column=2, sticky="w")
    c = Canvas(root, width=maxcoordx, height=maxcoordy, bg='black')
    c.grid()



class star():
    radius = 0
    radiusMax = 0
    current_radiusMax = 0
    x = 0
    y = 0
    xMax = maxcoordx
    yMax = maxcoordy
    stage = 0
    counter = 0

    def __init__(self):
        self.x = randint(0, self.xMax)
        self.y = randint(0, self.yMax)
        self.current_radiusMax = randint(1, self.radiusMax)
        self.nebula1 = sky.c.create_oval(self.x - 1, self.y - 1,
                                         self.x + 1, self.y + 1, fill = 'gray10')
        #self.nebula2 = sky.c.create_oval(self.x - 1, self.y - 1,
        #                                 self.x + 1, self.y + 1, fill='red')
        self.body = sky.c.create_oval(self.x - 1, self.y - 1,
                                      self.x + 1, self.y + 1, fill = 'red')


    def protostar(self):
        if self.radius < self.current_radiusMax:
            self.radius = self.radius + 1
            sky.c.coords(self.body, self.x - self.radius, self.y - self.radius,
                         self.x + self.radius, self.y + self.radius)
        else:
            self.stage = self.stage + 1

    def brown_dwarf(self):
        self.counter = self.counter + 1
        if self.counter < (randint(6, life_brown_dwarf)):
            sky.c.itemconfig(self.body, fill = 'brown')
        else:
            self.stage = self.stage + 1
            self.counter = 0

    def red_dwarf(self):
        self.counter = self.counter + 1
        if self.counter < (randint(life_red_dwarf - 10, life_red_dwarf)):
            sky.c.itemconfig(self.body, fill='red')
        else:
            self.stage = self.stage + 1
            self.counter = 0

    def white_dwarf(self):
        self.radius =self.current_radiusMax - 1
        sky.c.coords(self.body, self.x - self.radius, self.y - self.radius,
                     self.x + self.radius, self.y + self.radius)
        self.counter = self.counter + 1
        if self.counter < (randint(6, life_white_dwarf)):
            sky.c.itemconfig(self.body, fill='white')
        else:
            self.stage = self.stage + 1
            self.counter = 0

    def sunlike_star(self):
        self.counter = self.counter + 1
        if self.counter <= (life_sunlike_star):
            sky.c.itemconfig(self.body, fill='yellow')
        else:
            self.stage = self.stage + 1
            self.counter = 0

    def red_giant(self):
        if self.radius < (2*self.current_radiusMax):
            self.radius = self.radius + 1
            sky.c.coords(self.body, self.x - self.radius, self.y - self.radius,
                         self.x + self.radius, self.y + self.radius)
            sky.c.itemconfig(self.body, fill='orange red')
        else:
            self.stage = self.stage + 1

    def planetary_nebula(self):
        if self.radius < (3*self.current_radiusMax):
            self.radius = self.radius + 1
            sky.c.coords(self.nebula1, self.x - (self.radius), self.y - (self.radius),
                         self.x + (self.radius), self.y + (self.radius))
            sky.c.coords(self.body, self.x - self.current_radiusMax, self.y - self.current_radiusMax,
                         self.x + self.current_radiusMax, self.y + self.current_radiusMax)
            sky.c.itemconfig(self.body, outline = 'white', fill = 'white')
        else:
            self.stage = self.stage + 1

            sky.c.coords(self.nebula1, self.x - 1, self.y - 1,
                         self.x + 1, self.y + 1)
            sky.c.coords(self.body, self.x - self.current_radiusMax, self.y - self.current_radiusMax,
                         self.x + self.current_radiusMax, self.y + self.current_radiusMax)

    def blue_supergiant(self):
        self.counter = self.counter + 1
        if self.counter < (randint(life_blue_supergiant - 10, life_blue_supergiant)):
            sky.c.itemconfig(self.body, fill='SkyBlue1')
        else:
            self.stage = self.stage + 1
            self.counter = 0

    def blue_giant(self):
        pass

    def supernova(self):
        pass

    def neytron_star(self):
        pass

    def black_hole(self):
        pass

    def delete(self):
        sky.c.delete(self.body)
        sky.c.delete(self.nebula1)

        self.stage = 10


class star_type1(star):
    radiusMax = 2

    def star_life(self):

        if self.stage == 0:
            self.protostar()

        if self.stage == 1:
            self.brown_dwarf()

        if self.stage == 2:
            self.delete()

        sky.root.after(tik, self.star_life)


class star_type2(star):
    radiusMax = 3

    def star_life(self):
        if self.stage == 0:
            self.protostar()

        if self.stage == 1:
            self.red_dwarf()

        if self.stage == 2:
            self.white_dwarf()

        if self.stage == 3:
            self.delete()

        sky.root.after(tik, self.star_life)


class star_type3(star):
    radiusMax = 3

    def star_life(self):
        if self.stage == 0:
            self.protostar()

        if self.stage == 1:
            self.sunlike_star()

        if self.stage == 2:
            self.red_giant()

        if self.stage == 3:
            self.planetary_nebula()

        if self.stage == 4:
            self.white_dwarf()

        if self.stage == 5:
            self.delete()

        sky.root.after(tik, self.star_life)


class star_type4(star):
    radiusMax = 4

    def star_life(self):
        if self.stage == 0:
            self.protostar()

        if self.stage == 1:
            self.blue_supergiant()

        if self.stage == 2:
            self.red_giant()
        """"    
        if self.stage == 3:
            self.planetary_nebula()

        if self.stage == 4:
            self.white_dwarf()
        """
        if self.stage == 3:
            self.delete()

        sky.root.after(tik, self.star_life)


#class constellation():






