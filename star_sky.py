from constellationModule import *

sky()

constellation = []
for i in range(20):
    constellation.append(star_type1())
    constellation[i].star_life()

for i in range(20, 40):
    constellation.append(star_type2())
    constellation[i].star_life()


for i in range(40, 60):
    constellation.append(star_type3())
    constellation[i].star_life()


for i in range(60, 80):
    constellation.append(star_type4())
    constellation[i].star_life()


def garbage_collector():
    i = 0
    while (i != len(constellation)):
        if constellation[i].stage == 10:
            constellation.pop(i)
        else:
            i = i + 1
    sky.root.after(tik_gc_and_append, garbage_collector)
    print(len(constellation))
    sky.label_star_quantity['text'] = 'количество звезд = ' + str(len(constellation))

garbage_collector()

"""
def garbage_collector():
    print(len(constellation))
    sky.root.after(tik_gc_and_append, garbage_collector)


garbage_collector()

"""
def constellation_append():
    i = randint(0,40)

    if (i < 10):
        constellation.append(star_type1())

    elif (i >= 10)and(i < 20):
        constellation.append(star_type2())

    elif (i >= 20)and(i < 30):
        constellation.append(star_type3())

    elif (i >= 30)and(i<40):
        constellation.append(star_type4())

    constellation[len(constellation)-1].star_life()

    sky.root.after(randint(100, tik_gc_and_append), constellation_append)

constellation_append()

mainloop()
