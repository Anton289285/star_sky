from tkinter import *
from random import *
root = Tk()
c = Canvas(root, width = 300, height = 200, bg = 'white')
c.pack()
radius1 = 1
radius2 = 1

class star:
    color = ''
    x = 0
    y = 0
    radius = 0
    max_radius = 0
    max_lifetime = 2000

    def __init__(self):
        self.x = randint(0, 200)
        self.y = randint(0, 200)
        self.radius = randint(1, 6)
        self.color ='green'
        self.body = c.create_oval(self.x-self.radius, self.y-self.radius,
                                  self.x+self.radius, self.y+self.radius, fill=self.color)

    def growth(self):
        self.radius = self.radius + 1
        c.coords(self.body, self.x - self.radius, self.y - self.radius,
                 self.x + self.radius, self.y + self.radius)
        if self.radius > randint(5, 20):
            self.radius = 2
            self.x =randint(0, 200)
            self.y = randint(0, 200)

            c.delete(self.body)
            root.after(2000, self.growth())
            self.body = c.create_oval( self.x - self.radius, self.y - self.radius,
                                       self.x + self.radius, self.y +self.radius, fill = 'red')

        root.after(randint(1, self.max_lifetime), self.growth)



star3 = star()
star4 = star()

star3.growth()
star4.growth()

mainloop()


