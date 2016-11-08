import hexagon
import matplotlib.pyplot as plt
import numpy as np
import user
import sys

r = float(sys.argv[1])
inner = float(sys.argv[2])
power = 80e-4

cells = np.array([])
cells = np.append(cells,[hexagon.Hexagon(np.array([0.,0.]),r,1,4,0,inner)])

points = np.array([[2,2],[1.5,2],[1,2],[0.5,2],[0,2],[-0.5,2],[-1,2],[-1.5,2],[-2,2],[-2.2,1.3],[-2.1,0],[-2,-0.7],[-2,-2],[0,-2],[2,-2],[2,-0.1],[2.1,0]])
index = 1


listing = np.array([[0,0],[0,0]])

doing = True

while(doing):
    doing = False
    for k in points:
        there = False
        for p in listing:
            if(np.array_equal(k,p)):
                there = True
                #print(k,p)
        if(not there):
            doing = True
            #print('in?')
            distance = 1e6
            cell = np.NaN
            for j in range(cells.shape[0]):
            
                closed,dist = cells[j].closest(k)

                temp1 = np.dot(dist[0],dist[0])
                if(temp1<distance):
                    distance = temp1
                    cell = j
                    clos = np.array([closed[0],closed[1]])

            if((clos[0]==0 and clos[1]==1) or (clos[1]==0 and clos[0]==1)):
                origin = np.array([1.5*r,r*np.sin(np.pi/3.)])+cells[cell].origin
                temp = False
                for i in range(cells.shape[0]):
                    if(cells[i].exists(origin)):
                        temp = True
                if((not temp)):
                    outer_band = 0
                    if(cells[cell].outer_band==1):
                        outer_band = 2
                    elif(cells[cell].outer_band==2):
                        outer_band = 3
                    else:
                        outer_band = 1
                    cells = np.concatenate([cells,[hexagon.Hexagon(origin,r,outer_band,4,index,inner)]])
                    index += 1
                    for c in points:
                        if(cells[-1].inpoly(c)):
                            listing = np.concatenate([listing,[c]])
                else:
                    listing = np.concatenate([listing,[k]])
            elif((clos[0]==2 and clos[1]==1) or (clos[0]==1 and clos[1]==2)):
                origin = np.array([0,2*r*np.sin(np.pi/3.)])+cells[cell].origin
                temp = False
                for i in cells:
                    if(i.exists(origin)):
                        temp = True
                if(not temp):
                    outer_band = 0
                    if(cells[cell].outer_band==1):
                        outer_band = 3
                    elif(cells[cell].outer_band==2):
                        outer_band = 1
                    else:
                        outer_band = 2
                    cells = np.concatenate([cells,[hexagon.Hexagon(origin,r,outer_band,4,index,inner)]])
                    index += 1
                    for c in points:
                        if(cells[-1].inpoly(c)):
                            listing = np.concatenate([listing,[c]])
                else:
                    listing = np.concatenate([listing,[k]])
            elif((clos[0]==3 and clos[1]==2) or (clos[0]==2 and clos[1]==3)):
                origin = np.array([-1.5*r,r*np.sin(np.pi/3.)])+cells[cell].origin
                temp = False
                for i in range(cells.shape[0]):
                    if(cells[i].exists(origin)):
                        temp = True
                if(not temp):
                    outer_band = 0
                    if(cells[cell].outer_band==1):
                        outer_band = 2
                    elif(cells[cell].outer_band==2):
                        outer_band = 3
                    else:
                        outer_band = 1
                    cells = np.concatenate([cells,[hexagon.Hexagon(origin,r,outer_band,4,index,inner)]])
                    index += 1
                    for c in points:
                        if(cells[-1].inpoly(c)):
                            listing = np.concatenate([listing,[c]])
                else:
                    listing = np.concatenate([listing,[k]])
            elif((clos[0]==4 and clos[1]==3) or (clos[0]==3 and clos[1]==4)):
                origin = np.array([-1.5*r,-r*np.sin(np.pi/3.)])+cells[cell].origin
                temp = False
                for i in cells:
                    if(i.exists(origin)):
                        temp = True
                if(not temp):
                    outer_band = 0
                    if(cells[cell].outer_band==1):
                        outer_band = 3
                    elif(cells[cell].outer_band==2):
                        outer_band = 1
                    else:
                        outer_band = 2
                    cells = np.concatenate([cells,[hexagon.Hexagon(origin,r,outer_band,4,index,inner)]])
                    index += 1
                    for c in points:
                        if(cells[-1].inpoly(c)):
                            listing = np.concatenate([listing,[c]])
                else:
                    listing = np.concatenate([listing,[k]])
            elif((clos[0]==5 and clos[1]==4) or (clos[0]==4 and clos[1]==5)):
                origin = np.array([0,-2*r*np.sin(np.pi/3.)])+cells[cell].origin
                temp = False
                for i in cells:
                    if(i.exists(origin)):
                        temp = True
                if(not temp):
                    outer_band = 0
                    if(cells[cell].outer_band==1):
                        outer_band = 2
                    elif(cells[cell].outer_band==2):
                        outer_band = 3
                    else:
                        outer_band = 1
                    cells = np.concatenate([cells,[hexagon.Hexagon(origin,r,outer_band,4,index,inner)]])
                    index += 1
                    for c in points:
                        if(cells[-1].inpoly(c)):
                            listing = np.concatenate([listing,[c]])
                else:
                    listing = np.concatenate([listing,[k]])
            else:
                origin = np.array([1.5*r,-r*np.sin(np.pi/3.)])+cells[cell].origin
                temp = False
                for i in cells:
                    if(i.exists(origin)):
                        temp = True
                if(not temp):
                    outer_band = 0
                    if(cells[cell].outer_band==1):
                        outer_band = 3
                    elif(cells[cell].outer_band==2):
                        outer_band = 1
                    else:
                        outer_band = 2
                    cells = np.concatenate([cells,[hexagon.Hexagon(origin,r,outer_band,4,index,inner)]])
                    index += 1
                    for c in points:
                        if(cells[-1].inpoly(c)):
                            listing = np.concatenate([listing,[c]])
                else:
                    listing = np.concatenate([listing,[k]])
       # print(index,cells[-1].origin,k,listing)

#print(cells.shape)

distr = np.random.random((1000,2))*8-4

users = np.array([])
serviced = np.array([[0,0],[0,0]])
SINR = np.array([])

for i in distr:
    distancep = 0
    gp = 0
    hp = 0
    distance = 0
    g = 0
    h = 0
    added = False
    rec = 6e-14
    signal = 0
    signal0 = 0
    for j in cells:
        if(j.inpoly(i)):
            distancep = j.distance(i)
            if(distancep<inner):
                users = np.append(users,[user.User(i,j.ide,j.inner_band)])
                signal0 = power
            else:
                users = np.append(users,[user.User(i,j.ide,j.outer_band)])
                signal0 = power
            gp = distancep**(-2.)
            hp = 1.5*np.exp(-1.5*distancep)
            signal = signal0*hp*gp
            serviced = np.concatenate([serviced,[i]])
            for k in cells:
                if(k != j):
                    if(users[-1].band == k.outer_band):
                        distance = k.distance(i)
                        g = distance**(-2)
                        h = 1.5*np.exp(-1.5*distance)
                        rec += power*h*g
                    elif(users[-1].band == k.inner_band):
                        distance = k.distance(i)
                        g = distance**(-2)
                        h = 1.5*np.exp(-1.5*distance)
                        rec += power*h*g
            SINR = np.append(SINR,[signal/rec])

print(users.shape,SINR.shape)
np.savetxt(sys.argv[3],SINR)


"""        
plt.fill(cells[1].corners[0],cells[1].corners[1],fill=False)
plt.fill(cells[0].corners[0],cells[0].corners[1],fill=False)
plt.fill(cells[2].corners[0],cells[2].corners[1],fill=False)
plt.fill(cells[3].corners[0],cells[3].corners[1],fill=False)
plt.fill(cells[4].corners[0],cells[4].corners[1],fill=False)
plt.fill(cells[5].corners[0],cells[5].corners[1],fill=False)
plt.fill(cells[6].corners[0],cells[6].corners[1],fill=False)
plt.fill(cells[7].corners[0],cells[7].corners[1],fill=False)
plt.fill(cells[8].corners[0],cells[8].corners[1],fill=False)
plt.fill(cells[9].corners[0],cells[9].corners[1],fill=False)
plt.fill(cells[10].corners[0],cells[10].corners[1],fill=False)
plt.fill(cells[11].corners[0],cells[11].corners[1],fill=False)
plt.fill(cells[12].corners[0],cells[12].corners[1],fill=False)
#plt.plot(2,2,marker='o')
#plt.plot(2,0,marker='o')
#plt.plot(-2,0,marker='o')
plt.scatter(serviced[:,0],serviced[:,1])
plt.savefig('Strict-FFR')
"""
