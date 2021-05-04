#s = 'student'

#print(s[2:5]) #prints from 2 to 4 (excludes 5)
#print(s[2:]) #prints everything after s[2]
#print(s[:5]) #prints everything before s[5] not including s[5]

l = [6,12,18,24,30]
for i in l:
    for j in range(1,i%4):
        print(j,'#',end = '')
    print()