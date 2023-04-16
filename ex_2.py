import math
# trojkat
a = 10
b = 12
c = 8
h = 6

pole = 1/2*a*h
obwod = a+b+c

print("Pole trojkata wynosi " +  str(pole) + ",a obwod wynosi "+str(obwod))

#romb

obw_romb = 4*a
pole_romb = a*h
print("Pole wynosi " +  str(pole_romb) + ",a obwod wynosi "+str(obw_romb))
#kolo

r = 8

obw_kolo = 2*math.pi*r
pole_kolo = math.pi*r**2
print("Pole wynosi " +  str(pole_kolo) + ",a obwod wynosi "+str(obw_kolo))
#trapez

d=14

obw_trapez = a+b+c+d
pole_trapez = 1/2*(a+b)*h
print("Pole wynosi " +  str(pole_trapez) + ",a obwod wynosi "+str(obw_trapez))
#prostokat
obw_prostokat = 2*a+2*b
pole_prostokat = a*b

print("Pole wynosi " +  str(pole_prostokat) + ",a obwod wynosi "+str(obw_prostokat))