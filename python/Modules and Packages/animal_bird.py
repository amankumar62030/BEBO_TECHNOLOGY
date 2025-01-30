import Animal
Animal.fly()
Animal.colour()


import bird
bird.fly()
bird.colour()


from Animal import*
fly()
colour()

from bird import*
fly()
colour()


import Animal,bird as b
Animal.fly()
Animal.colour()

b.fly()
b.colour()