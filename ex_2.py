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

#kolo

r = 8

obw_kolo = 2*math.pi*r
pole_kolo = math.pi*r^2

#trapez

d=14

obw_trapez = a+b+c+d
pole_trapez = 1/2*(a+b)*h

#prostokat
obw_prostokat = 2*a+2*b
pole_prostokat = a*b

