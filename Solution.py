import math
from sys import stdin
def mul(a,b,c,d,m):
    x = a*c - b*d
    y = a*d + b*c
    x = (m + x%m)%m
    y = (m + y%m)%m
    return (x,y)
def po(a,b,k,m):
    if k==0:
        return (1,0)
    u,v = po(a,b,k/2,m)
    u,v = mul(u,v,u,v,m)
    if k%2:
        u,v = mul(u,v,a,b,m)
    return (u,v)
t = int(stdin.readline())
for _ in xrange(t):
    a,b,k,m = map(int,stdin.readline().split())
    x,y = po(a,b,k,m)
    print x,y
