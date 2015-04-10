#include "allvars.h"


int main( int argc, char *argv[] )
{
    //Parameters
    float p[NMAX1];
    
    printf( "\n\n******************************** VORONOI WEB ********************************\n" );
    //Loading Configuration------------------------------------------------------------------------
    read_parameters( p, argv[1] );

    printf("%f %f %f\n", p[LBOX], p[LINK], p[NBOX]);
    
    return 0;
}