# SHORTEST ROOT
from random import randint
import random 
import math
import turtle

def generate(p, points, count): #clear list to []
    pp = []
    for i in range(p):
        point = []
        x = randint(-300, 300)
        y = randint(-300, 300)
        point.append(x)
        point.append(y)
        pp.append(point)
    for i in range(count): #take out -1
        shuf = random.sample(pp, len(pp))
        points.append(shuf)
    #del points[-1] #take out
   
def fitness(s_p, d, points, p):
    tot = 0
    worst = 0
    ii = 0
    for i in points: # you are here
        tot += (((s_p[0] - i[0][0])**2 + (s_p[1]-i[0][1])**2))#**(0.5))
        i.append(s_p)
        l = 0
        while l < p:#TAKE OUt -1
            tot += (((i[l][0] - i[l+1][0])**2 + (i[l][1]-i[l+1][1])**2))#**(0.5))
            l += 1
        del i[i.index(s_p)]
        if tot > worst:
            worst = tot
            ii = i
        else:
            pass 
        #print(tot//1)
        d.append(((1*(tot//1)**(-1))*100)**3)
        tot = 0
    rr = points.index(ii)
    del points[rr]
    del d[rr]
    ii = 0
    worst = 0

'''def pick(d, points, w_r):
    global rec, rec2
    rec = 100000000000000000000
    rec2 = 0
    for i in d:
        if i < rec: # I took out a =
            rec2 = rec
            rec = i
            w_r = d.index(i)
            sk = 0
            #print(rec, 'shortest')
            #print(points[d.index(i)], 'points list shortest')
        elif i == rec:
            rec2 = i
        elif i > rec and i < rec2:
            rec2 = i
        else:
            pass'''

def pick2(d, points):
    global rec, rec2
    som = 0
    for i in d:
        som += i
        
    q = 0
    for i in d:
        d[q] = i*(som**(-1))
        q += 1
    
    r = randint(0,100)*(100**(-1))
    ind = 0
    while r > 0:
        r -= d[ind]
        ind += 1
        if r < 0 and ind == 0:
            pass
        else:
            ind -= 1
    rec = ind
    
    ind2 = 0
    aa = True
    while aa is True:
        r = randint(0,100)*(100**(-1))
        while r > 0:
            r -= d[ind2]
            ind2 += 1
            if r < 0 and ind == 0:
                pass
            else:
                ind2 -= 1
        if ind2 != rec:
            aa = False
        else:
            ind2 = 0
            pass
    
    rec2 = ind2


        
def mutate(d, points, p, w_r):
    global rec, rec2
    #pick(d, points, w_r)
    pick2(d, points)
    i_rec = rec #d.index(rec)   Index shortest root
    i_rec2 = rec2#d.index(rec2) Index second shortest root
    l1 = points[i_rec]     # shortest list
    l2 = points[i_rec2]    # second shortest list
    numa = randint(0, len(l1)//4)
    numb = randint(len(l1)//2, len(l1))
    x = l1[numa:numb]
    bnew = []
    bbb = []
    v = bbb + l2
    for i in v:
        ass = v.index(i)
        for a in x:
            if a == i:
                del x[x.index(a)]
            else:
                pass
    qaz = v + x
    bnew.append(v+x)
    points.append(bnew[0])# take out
    bnew = [] # trake out
    bnew = [points[randint(0, 9)]] # take out
    prob = randint(0, 4)
    if prob == 0:
        A1 = randint(0, len(bnew[0])//2)
        B1 = randint((len(bnew[0])//2)+1, len(bnew[0])-1)
        bnew[0][A1], bnew[0][B1] = bnew[0][B1], bnew[0][A1]
    elif prob == 1:
        A1 = randint(0, len(bnew[0])-1)
        B1 = randint(0, len(bnew[0])-1)
        bnew[0][A1], bnew[0][B1] = bnew[0][B1], bnew[0][A1]
    elif prob == 11:
        A1 = randint(0, len(bnew[0])-1)
        B1 = randint(0, len(bnew[0])-1)
        C1 = randint(0, len(bnew[0])-1)
        D1 = randint(0, len(bnew[0])-1)
        bnew[0][A1], bnew[0][B1] = bnew[0][B1], bnew[0][A1]
        bnew[0][C1], bnew[0][D1] = bnew[0][D1], bnew[0][C1]
    elif prob == 2:
        A1 = randint(1, len(points[i_rec2])-1)
        B1 = A1-1
        points[i_rec2][A1], points[i_rec2][B1] = points[i_rec2][B1], points[i_rec2][A1]
    elif prob == 4:
        pass
    else:
        pass
    #points.append(bnew[0])
    #bnew = []
    part = []

def draw(t, points, w_r):
    t.clearscreen()
    t.bgcolor('black')
    t.pencolor('red')
    t.goto(0,0)
    #t.dot()
    q = 1
    for i in points[w_r]:
        t.speed(0)
        t.penup()
        t.pencolor('blue')
        t.goto(i[0]*q,i[1]*q)
        t.dot()
    t.goto(0,0)
    for i in points[w_r]:
        t.pendown()
        t.pencolor('blue')
        t.speed(10)
        t.goto(i[0]*q, i[1]*q)
    t.goto(0,0)
    t.bgcolor('black')

def mutate2(points,p,n, d):# new mutation
        global rec, rec2
        #pick(d, points, w_r)
        pick2(d, points)
        i_rec = rec #d.index(rec)   Index shortest root
        i_rec2 = rec2#d.index(rec2) Index second shortest root
        l1 = points[i_rec]     # shortest list
        l2 = points[i_rec2]    # second shortest list
        prob = randint(0, 10)
        bnew = [points[randint(0, len(points)-1)]]
        if prob == 0:
            A1 = randint(0, len(bnew[0])//2)
            B1 = randint((len(bnew[0])//2)+1, len(bnew[0])-1)
            bnew[0][A1], bnew[0][B1] = bnew[0][B1], bnew[0][A1]
        elif prob == 1:
            A1 = randint(0, len(bnew[0])-1)
            B1 = randint(0, len(bnew[0])-1)
            bnew[0][A1], bnew[0][B1] = bnew[0][B1], bnew[0][A1]
        elif prob == 11:
            A1 = randint(0, len(bnew[0])-1)
            B1 = randint(0, len(bnew[0])-1)
            C1 = randint(0, len(bnew[0])-1)
            D1 = randint(0, len(bnew[0])-1)
            bnew[0][A1], bnew[0][B1] = bnew[0][B1], bnew[0][A1]
            bnew[0][C1], bnew[0][D1] = bnew[0][D1], bnew[0][C1]
        elif prob == 2:
            A1 = randint(1, len(points[i_rec2])-1)
            B1 = A1-1
            points[i_rec2][A1], points[i_rec2][B1] = points[i_rec2][B1], points[i_rec2][A1]
        elif prob == 4:
            pass
        else:
            pass
        numa = randint(0, len(l1)//4)
        numb = randint(len(l1)//2, len(l1))
        x = l1[numa:numb]
        bnew = []
        bbb = []
        v = bbb + l2
        for i in v:
            ass = v.index(i)
            for a in x:
                if a == i:
                    del x[x.index(a)]
                else:
                    pass
        qaz = v + x
        bnew.append(v+x)
        points.append(bnew[0])
        bnew = []
        part = []

    
def find():
    points = []
    s_p = [0, -12]
    d = []
    p = 100 # points
    count = 500
    sk = 0
    generate(p, points, count)
    t = turtle
    w_r = 0
    n = 1000000001
    while n > 0:
        t.hideturtle()
        n -= 1
        fitness(s_p, d, points, p)
        #mutate(d, points, p, w_r)
        mutate2(points,p,n,d)
        d = []
        if n%1000 == 0:
            draw(t, points, w_r)
        else:
            pass
    print(points[w_r])
find()
#[[14, 3], [42, 5], [58, 30], [72, 1], [100, -32], [77, -67], [73, -100], [15, -87], [-43, -86], [-66, -100], [-44, -68], [-14, -1], [48, 74], [70, 72], [95, 27], [93, 26], [93, 25], [-38, -11], [-64, -17], [-82, 7], [-66, 40], [-18, 58], [34, 32], [47, 32], [54, 35], [38, 57], [-35, 97], [-71, 98], [-42, 59], [-23, 56]]
#[[0,-12],[4,-6],[5,-5],[6,-5],[7,-6],[8,-8],[9,-6],[10,-5],[11,-5],[12,-6],[13,-8],[13,-9],[12,-11],[11,-12],[14,-11],[17,-9],[19,-7],[20,-5],[21,-2],[21,1],[20,4],[19,6],[17,8],[14,10],[11,11],[12,10],[13,8],[13,7],[12,5],[11,4],[9,3],[6,3],[3,4],[3,12],[1,9],[-1, 9],[-3,12],[-3,4],[-6,3],[-9,3],[-11,4],[-12,5],[-13,7],[-13,8],[-12,10],[-11,11],[-14,10],[-17,8],[-19,6],[-20,4],[-21,1],[-21,-2],[-20,-5],[-19,-7],[-17,-9],[-14,-11],[-11,-12],[-12,-11],[-13,-9],[-13,-8],[-12,-6],[-11,-5],[-10,-5],[-9,-6],[-8,-8],[-7,-6],[-6,-5],[-5,-5],[-4,-6],[0,-12]]
