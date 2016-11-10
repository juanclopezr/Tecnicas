import numpy as np
import matplotlib.path as myp

class Hexagon:
    def __init__(self, origin, radius, outer_band, inner_band, ide, inner_radius):
        self.origin = origin;
        self.corners = radius*np.array([[np.cos(0.),np.cos(np.pi/3.),np.cos(2.*np.pi/3.),np.cos(np.pi),np.cos(4*np.pi/3),np.cos(5.*np.pi/3.)],[np.sin(0.),np.sin(np.pi/3.),np.sin(2.*np.pi/3.),np.sin(np.pi),np.sin(4.*np.pi/3.),np.sin(5*np.pi/3.)]])
        self.corners[0] = self.corners[0]+origin[0]
        self.corners[1] = self.corners[1]+origin[1]
        self.outer_band = outer_band
        self.inner_band = inner_band
        self.inner_radius = inner_radius
        self.ide = ide

    def exists(self,center):
        return np.array_equal(self.origin,center)

    def distance(self,point):
        return np.dot(self.origin-point,self.origin-point)**0.5

    def inpoly(self,point):
        polygon = myp.Path(self.corners.T)
        return polygon.contains_point(point)

    def closest(self,point):
        #print(point)
        temp = (point[0]-self.corners[0])**2+(point[1]-self.corners[1])**2
        #print("distance",(point[1]-self.corners[1])**2+(point[0]-self.corners[0])**2)
        index = temp.argsort()
        #return cor[:,][index]
        return index,temp[index]

    def inreg(self,point):
        #print(self.corners[:,:3],self.origin)
        #La funcion concatenate se usa para añadir el origen a la lista de esquinas por region.
        #Esquinas 0, 1 y 2 para el poligono 1
        polygon1 = myp.Path(np.concatenate([self.corners[:,:3].T,[self.origin]]))
        #Esquinas 2, 3 y 4 para el poligono 2
        polygon2 = myp.Path(np.concatenate([self.corners[:,2:5].T,[self.origin]]))
        if(self.distance(point)<=self.inner_radius):
            return 4
        elif(polygon1.contains_point(point)):
            return 1
        elif(polygon2.contains_point(point)):
            return 2
        else:
            return 3
