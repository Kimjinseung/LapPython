
data=['a', 'b', 'c', ['abcd', 'efg']]
data2 = ['15', '30', '25', '60', '50', '45']
print(data2)
for steps in range(4) :
    if isinstance(steps, list) :
        for step in steps :
            print(step)
        else :
            print(steps)

#print(data[0])
#print(data[-1])
#for steps in data :
#    print(steps)


guests = ['a', 'b', 'c', 'd']
guests[0] = 'greenjoa'
guests[1] = ['greenjoa1', 'greenjoa2']
guests[1-2]=['greenjoa1,' 'greenjoa2']

guests.insert(2, 'e')
guests.append('greenjoa2')
print(guests[-1])

guests.remove('c')
guests[1:2]=[]
del guests[0]

guests = ['a', 'b', 'c', 'd']

#for steps in range(4) :
#   print(guests[steps])

guests = ['a', 'b', 'c', 'd']
nEntries = len(guests)
for steps in range(nEntries) :
    print(guests[steps])

for guest in guests :
    print(guest)

scores = [85, 62, 63, 45, 90]
scores.sort()
scores.reverse()
print(scores)

num = scores.pop()
num = scores.pop()

num = scores.count(63)
print(num)

scores.extend([50,60])
print(scores)

t1 = 0
t2 = (1,)
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a', 'b', ('ab', 'cd'))