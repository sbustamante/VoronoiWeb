#****************************************************************************************
#	VORONOI TESSELLATIONS
#	Sebastian Bustamante (macsebas33@gmail.com)
#****************************************************************************************

#========================================================================================
#		IMPORTS
#========================================================================================
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import collections
from scipy.spatial import Voronoi

#========================================================================================
#		OBJECTS
#========================================================================================
class voronoifield(object):
    """voronoifield class
    
    Class of fields mapped over voronoi meshes
    
    Attributes
    ----------
    x : x coordinates
    y : y coordinates
    z : z coordinates
    f : associated field
    
    dim : dimension of the problem
    Lx : x dimension of the embedding box
    Ly : y dimension of the embedding box
    Lz : z dimension of the embedding box
    
    condition : boundary conditions for voronoi mesh
    point_region: indices of the Voronoi region for each input point
    regions: indices of Voronoi vertices forming each region
    vertices: coordinates of the Voronoi vertices
    
    volume : array with volumes of Voronoi cells
    """
    
    
    def __init__( self, x, y, f = None, z = None ):
	#Coordinates
	self.x = np.array(x)
	self.y = np.array(y)
	self.z = np.array(z)
	#Field
	self.f = np.array(f)
	#Detecting no field
	if f == None:
	    self.f = np.ones(len(self.x))
	#Detecting dimension
	self.dim = 3
	if z == None:
	    self.dim = 2
	
	
    def voronoimesh2d( self, condition="finite", Lx = None, Ly = None ):
	"""
	Name: voronoimesh2d
	Function: calculates the voronoi tessellation of a set of provided points in 2D.
	Arguments:
	    self: voronoifield object
	    P: set of points. 
	    condition: this parameter indicates how to deal with boundary conditions. 
	    "finite" would produce mirror images of the points so the total volume
	    of the voronoi volumes equals the volume of the box Lx*Ly.
	    "infinite" would produce open boundaries.
	    "periodic" makes a periodic copy of the points, so the voronoi volumes
	    are also periodic.
	    Lx: x dimensions of box
	    Ly: y dimensions of box
	"""
	#Default box size
	self.Lx = Lx
	if Lx == None:
	    self.Lx = [np.min(self.x),np.max(self.x)]
	self.Ly = Ly
	if Ly == None:
	    self.Ly = [np.min(self.y),np.max(self.y)]
		
	self.condition = condition
		
	#Infinite boundaries
	if condition == "infinite":
	    #Creating voronoi mesh
	    vor = Voronoi(zip(self.x,self.y))
	    self.point_region = np.array(vor.point_region)
	    self.regions = np.array(vor.regions)
	    self.vertices = np.array(vor.vertices)
	elif condition == "finite":
	    #Creating mirrored images of points X
	    Xtmp = list(self.x)
	    Xtmp += list(self.x)
	    Xtmp += list(self.x)
	    Xtmp += list(Lx[0]-self.x)
	    Xtmp += list(2*Lx[1]-Lx[0]-self.x)
	    #Creating mirrored images of points Y
	    Ytmp = list(self.y)
	    Ytmp += list(Ly[0]-self.y)
	    Ytmp += list(2*Ly[1]-Ly[0]-self.y)
	    Ytmp += list(self.y)
	    Ytmp += list(self.y)
	    #Creating voronoi mesh
	    vor = Voronoi(np.transpose(np.array([Xtmp,Ytmp])))
	    self.point_region = np.array(vor.point_region[ :len(self.x) ])
	    self.regions = np.array(vor.regions)
	    self.vertices = np.array(vor.vertices)
	elif condition == "periodic":
	    #Creating mirrored images of points X
	    Xtmp = list(self.x)
	    Xtmp += list(self.x)
	    Xtmp += list(self.x)
	    Xtmp += list(Lx[0]-self.x)
	    Xtmp += list(2*Lx[1]-Lx[0]-self.x)
	    #Creating mirrored images of points Y
	    Ytmp = list(self.y)
	    Ytmp += list(Ly[0]-self.y)
	    Ytmp += list(2*Ly[1]-Ly[0]-self.y)
	    Ytmp += list(self.y)
	    Ytmp += list(self.y)
	    #Creating voronoi mesh
	    vor = Voronoi(np.transpose(np.array([Xtmp,Ytmp])))
	    self.point_region = np.array(vor.point_region[ :len(self.x) ])
	    self.regions = np.array(vor.regions)
	    self.vertices = np.array(vor.vertices)
	else:
	    print("ERROR: Condition %s is not allowed."%(condition))
	    
    
    def voronoisurface( self ):
	"""
	Name: voronoisurface
	Function: calculates the surface of each Voronoi cell (2D tessellations)
	Arguments:
	    self: voronoifield object
	"""
	if self.dim != 2:
	    print("ERROR: voronoisurface only can compute surface over 2D tessellations")
	    return 0
	  
	self.surface = []
	for reg in self.regions[self.point_region]:
	    vertices = self.vertices[reg]
	    nver = len(vertices)
	    vertices = np.append( vertices, vertices[0] )
	    vertices = vertices.reshape( (nver+1,2) )
	    surface = 0
	    for i in xrange(nver):
		surface += vertices[i,0]*vertices[i+1,1] - vertices[i+1,0]*vertices[i,1]
	    self.surface.append( 0.5*abs(surface) )
	self.surface = np.array(self.surface)
	
    
    def voronoishow( self, cmap="jet", axes = None, **kargs ):
      	"""
	Name: voronoishow
	Function: calculates the surface of each Voronoi cell (2D tessellations)
	Arguments:
	    self: voronoifield object
	    cmap: color map
	    axes: plot environment
	    kargs: extra arguments for poly function
	"""
	#Detecting axes
	if axes == None:
	    fig = plt.figure()
	    axes = fig.add_subplot(1,1,1)
	#Detecting cmap
	exec( "cmapvor = matplotlib.cm.%s"%(cmap) )

	#Plotting
	i=0
	for reg in self.regions[self.point_region]:
	    if sum(np.array(reg)<0)==0:
		polys = self.vertices[reg]
		colors = cmapvor( int(255*(self.f[i]-np.min(self.f))/(np.max(self.f)-np.min(self.f))) )
		p = matplotlib.patches.Polygon( polys, facecolor=colors, **kargs )
		axes.add_patch(p)
	    i+=1
	axes.set_xlim( self.Lx )
	axes.set_ylim( self.Ly )
	return axes