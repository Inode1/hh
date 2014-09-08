#!/usr/bin/python
'''
Created on Sep 8, 2014

@author: ivan
'''
import sys
if __name__ == '__main__':
    pass

def take_data(line):
    try:
        while True:
            line.append((sys.stdin.readline()))
            if line[-1][0]=='\n':
                line.pop()
                break
    except KeyboardInterrupt:
        pass
    
    line=line[0].split(' ')
    k=[]
    for y in range(len(line)):
            k.append(int(line[y]))
    return k

def equal(array,num):
    l2=array
    l1=sum1(array,num)
    for x in l1:
        if x in array:
            l2.remove(x)
    l3=sum1(l2,num)
    if l3==None:
        print "Not equal"
        return
    print ' '.join(map(str, l1)),'-',' '.join(map(str, l3))
def sum1(matrix,num):
    if num == 0 or num < 1:
        return None
    elif len(matrix) == 0:
        return None
    else:
        if matrix[0] == num:
            return [matrix[0]]
        else:
            boo = sum1(matrix[1:],(num - matrix[0])) 
            if boo:
                return [matrix[0]]+boo
            else:
                return sum1(matrix[1:],num)
line=[]
line=take_data(line)           
b=sum(line)
if b%2==0:
    equal(line,b/2)
else:
    print "Not equal"
if sum(line, 100)==None:
    print "no"
else:
    print "yes"
