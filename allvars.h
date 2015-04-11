/**************************************************************************************************
			      MACROS
**************************************************************************************************/
//General Macros
#define NMAX1		100
#define NMAX2		1000
#define MY_FREE(ptr)	free(ptr); ptr = NULL;

//Macros for Parameters
#define LBOX		0		//Comoving length of the simulation
#define LINK		1		//Linking lenght for the FOF method
#define NBOX		2		//Linking lenght for the FOF method

//Other macros
#define X		0		//X coordinate
#define Y		1		//Y coordinate
#define Z		2		//Z coordinate


/**************************************************************************************************
			      STRUCTURES AND TYPEDEFS
**************************************************************************************************/
//Type of variables to be used
#ifdef DOUBLEPRECISION
typedef double decimal;
#else
typedef float decimal;
#endif

//Structure of particles including voronoi information
struct particle{
    //GENERAL PROPERTIES---------------------------------------------
    //Mass of each particle
    decimal mass;
    //Position
    decimal r[3];
    //Velocity
    decimal v[3];
    };
    

/**************************************************************************************************
			      HEADERS
**************************************************************************************************/
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

#include "proto.h"