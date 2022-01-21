'''
1. Feladat
Írj egy programot, amely tartalmaz egy 'osszegzo' nevű függvényt, ami a paraméterként átvett listaelemeket (egész számokat) összeadja és az összegükkel tér vissza! 
A program tartalmazza a függvény hívását is!
'''


 
def osszegzes(*args):
    return sum( [ num for num in args ] )
print(osszegzes(1,3,5))