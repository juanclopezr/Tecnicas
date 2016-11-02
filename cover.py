import hexagon
import matplotlib.pyplot as plt
import numpy as np

r = 1.

cells = np.array([])
cells = np.append(cells,[hexagon.Hexagon(np.array([0.,0.]),r)])

points = np.array([[2,2],[-2,2],[0,2]])
a=0

while(a<6):
    for k in range(points.shape[0]):
        distance = 1e6
        cell = np.NaN
        for j in range(cells.shape[0]):
            clos,dist = cells[j].closest(points[k])

            temp1 = np.dot(dist[0],dist[0])
            if(temp1<distance):
                distance = temp1
                cell = j
            print(j,temp1,cells[j].origin)
        print(cell,points[k])

        if((clos[0]==0 and clos[1]==1) or (clos[1]==0 and clos[0]==1)):
            origin = np.array([1.5*r,r*np.sin(np.pi/3.)])+cells[cell].origin
            temp = False
            for i in range(cells.shape[0]):
                #
                #print(1,cells[i].exists(origin),origin,i)
                if(cells[i].exists(origin)):
                    temp = True
            if(temp == False):
                cells = np.concatenate([cells,[hexagon.Hexagon(origin,r)]])
                if(cells[-1].inpoly(points[k])):
                    points = points
        elif((clos[0]==2 and clos[1]==1) or (clos[0]==1 and clos[1]==2)):
            origin = np.array([0,2*r*np.sin(np.pi/3.)])+cells[cell].origin
            temp = False
            for i in cells:
                print(i.exists(origin),origin)
                if(i.exists(origin)):
                    temp = True
            if(temp == False):
                cells = np.concatenate([cells,[hexagon.Hexagon(origin,r)]])
                if(cells[-1].inpoly(points[k])):
                    points = points
        elif((clos[0]==3 and clos[1]==2) or (clos[0]==2 and clos[1]==3)):
            origin = np.array([-1.5*r,r*np.sin(np.pi/3.)])+cells[cell].origin
            temp = False
            for i in range(cells.shape[0]):
                #
                #print(2,cells[i].exists(origin),origin,i)
                if(cells[i].exists(origin)):
                    temp = True
            if(temp == False):
                cells = np.concatenate([cells,[hexagon.Hexagon(origin,r)]])
                if(cells[-1].inpoly(points[k])):
                    points = points
        elif((clos[0]==4 and clos[1]==3) or (clos[0]==3 and clos[1]==4)):
            origin = np.array([-1.5*r,-r*np.sin(np.pi/3.)])+cells[cell].origin
            temp = False
            for i in cells:
                print(i.exists(origin),origin)
                if(i.exists(origin)):
                    temp = True
            if(temp == False):
                cells = np.concatenate([cells,[hexagon.Hexagon(origin,r)]])
                if(cells[-1].inpoly(points[k])):
                    points = points
        elif((clos[0]==5 and clos[1]==4) or (clos[0]==4 and clos[1]==5)):
            origin = np.array([0,-2*r*np.sin(np.pi/3.)])+cells[cell].origin
            temp = False
            for i in cells:
                print(i.exists(origin),origin)
                if(i.exists(origin)):
                    temp = True
            if(temp == False):
                cells = np.concatenate([cells,[hexagon.Hexagon(origin,r)]])
                if(cells[-1].inpoly(points[k])):
                    points = points
        else:
            origin = np.array([1.5*r,-r*np.sin(np.pi/3.)])+cells[cell].origin
            temp = False
            for i in cells:
                print(i.exists(origin),origin)
                if(i.exists(origin)):
                    temp = True
            if(temp == False):
                cells = np.concatenate([cells,[hexagon.Hexagon(origin,r)]])
                if(cells[-1].inpoly(points[k])):
                    points = points
        a+=1

print(points)

print(cells.shape)

plt.plot(cells[1].corners[0],cells[1].corners[1])
plt.plot(cells[0].corners[0],cells[0].corners[1])
plt.plot(cells[2].corners[0],cells[2].corners[1])
plt.plot(cells[3].corners[0],cells[3].corners[1])
plt.plot(cells[4].corners[0],cells[4].corners[1])
plt.plot(cells[5].corners[0],cells[5].corners[1])
plt.plot(cells[6].corners[0],cells[6].corners[1])
plt.show()


