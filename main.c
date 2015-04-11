#include "allvars.h"


int main( int argc, char *argv[] )
{
    //Parameters
    float p[NMAX1];
    
    printf( "\n\n******************************** VORONOI WEB ********************************\n" );
    //Loading Configuration File
    read_parameters( p, argv[1] );
    
    return 0;
}