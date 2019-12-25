
from tkinter import *
root=Tk()
root.title('123')
label= Label(root, text = 'количество звезд', width = 25, height = 5, bg = 'black', fg = 'red',
                 font = 'arial 14')
label.pack()
counter = 0
print('количество звезд', counter)


def count():
    global  counter
    counter = counter + 1

    label['text'] = 'количество звезд    ' + str(counter)
    root.after(100, count)
count()
root.mainloop()
