import hexagon
import matplotlib.pyplot as plt
import numpy as np

r = 1.
inner = 0.5

cells = np.array([])
cells = np.append(cells,[hexagon.Hexagon(np.array([0.,0.]),r,1,4,0,inner)])

points = np.array([[2,2],[0,2],[-2,2],[-2,0],[-2,-2],[0,-2],[2,-2]])
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
                print(k,p)
        if(not there):
            doing = True
            print('in?')
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
    print(index,cells[-1].origin,k,listing)

print(cells.shape)

#x = np.random.random(
        
plt.plot(cells[1].corners[0],cells[1].corners[1])
plt.plot(cells[0].corners[0],cells[0].corners[1])
plt.plot(cells[2].corners[0],cells[2].corners[1])
plt.plot(cells[3].corners[0],cells[3].corners[1])
plt.plot(cells[4].corners[0],cells[4].corners[1])
plt.plot(cells[5].corners[0],cells[5].corners[1])
plt.plot(2,2,marker='o')
plt.show()


