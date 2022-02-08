from random import  randint
num = str(randint(100000000, 999999999))
new = num

rev = 10
total = 0
for ind in range (19):
     if ind > 8:
          ind -= 9
     total += int(new[ind]) * rev
     rev -= 1
     if rev < 2:
          rev = 11
          d = 11 - (total % 11)
          if d >9:
               d = 0
          total = 0
          new += str(d)

print(new)