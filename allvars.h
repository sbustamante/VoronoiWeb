/**************************************************************************************************
			      MACROS
**************************************************************************************************/
//General Macros
#define NMAX1		1000
#define MY_FREE(ptr)	free(ptr); ptr = NULL;

//Macros for Parameters
#define LBOX		0	//Comoving length of the simulation
#define LINK		1	//Linking lenght for the FOF method
#define MAXV		2	//Minimum size to consider a void region [cells^3]

#define X		0	//X coordinate
#define Y		1	//Y coordinate
#define Z		2	//Z coordinate


/**************************************************************************************************
			      STRUCTURES
**************************************************************************************************/
struct particle{
    //Number of cells in void region
    long int Ncells;
    //Cells ID of this void region
    long long int *cells;
    
    //Number of children voids
    int Nchildren;
    //Children voids ID
    int *children;
    
    //Checked
    int check;
    //Index of this void
    long int index;
    
    //Number of neighbour voids
    int Nneighbours;
    //Indexes of neighbours
    long int *neighbours;
    //Number of shared cells with neighbours
    int *Nneigh_cells;
    //Mean FA(density) across boundaries for each neighbour
    float *neigh_mean;
    
    //ID of the cell corresponding with the Density centre of the void
    int idrhoC;
    //ID of the cell corresponding with the FA centre of the void
    int idrhoFA;
    };
    
    
/**************************************************************************************************
			      HEADERS
**************************************************************************************************/
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <sys/stat.h>
#include <dirent.h>

#include "proto.h"