#!/usr/bin/python
if __name__ == '__main__':
    pass
import sys

def my_func(liss):
    x=0
    y=0
    for l in liss:
        x,y=max(l[2],x),max(l[3],y)
    return x+1,y+1

def take_data(line):
    try:
        while True:
            line.append((sys.stdin.readline()))
            if line[-1][0]=='\n':
                line.pop()
                break
    except KeyboardInterrupt:
        pass
    
    for x in range(len(line)):
        line[x]=line[x].split(' ')
        for y in range(len(line[x])):
            line[x][y]=int(line[x][y])

def count(line,coord):
    c=0
    for l in line:
        for m in xrange(l[1],l[3]):
            for a in xrange(l[0],l[2]):
                coord[m][a]+=1
                if coord[m][a]==1:
                    c+=1
    return c

line=[]
take_data(line)
x=my_func(line)
d=[[0]*x[0] for n in xrange(x[1])]
print count(line,d)