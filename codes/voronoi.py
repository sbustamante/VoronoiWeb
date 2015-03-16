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
    """
    
    def __init__( self, x, y, z = None, f ):
	#Coordinates
	self.x = x
	self.y = y
	self.z = z
	#Field
	self.f = f
	#Detecting dimension
	dim = 3
	if z == None:
	    dim = 2
	
    def mesh2d( self, condition="finite", Lx = None, Ly = None ):
	"""
	Name: mesh2d
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
	if Lx = None:
	    self.Lx = [np.min(self.x),np.max(self.x)
	self.Ly = Ly
	if Ly = None:
	    self.Ly = [np.min(self.y),np.max(self.y)
		
	#Infinite boundaries
	if condition == "infinite":
	    
	  
	  
	  
	  
	  
	  
	  