# Атрибуты класса

# class Person:
#     name = 'Ivan'
#     age = 30
#
# class Book:
#     name = '1984'
#     writer = 'Джордж Оруэлл'
#     pages = 213

# 1.3________________________________

class SuperHero:
    pass

batman = SuperHero()
superman = SuperHero()

batman.can_fly = False
setattr(SuperHero, 'damage', 175)

superman.can_fly = True
setattr(SuperHero, 'damage', 285)
setattr(SuperHero, 'alter_ago', 'Клерк Кент')
