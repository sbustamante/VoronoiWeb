#include "allvars.h"


/**************************************************************************************************
 NAME:	     parameter_index
 FUNCTION:   returns the integer index associated to that parameter
 INPUTS:     name of the parameter
 RETURN:     index of the parameter
**************************************************************************************************/
int parameter_index( char parameter_name[] )
{
    int i, index=-1;
    //Declaring parameters (Exactly as configuration file)
    char *parameter_names[NMAX1];
    parameter_names[LBOX] = "lbox";
    parameter_names[LINK] = "link";
    parameter_names[NBOX] = "nbox";
    
    //Searching index
    for( i=0; i<NMAX1; i++ )
	if( strcmp( parameter_names[i], parameter_name ) == 0 ){
	    index = i;
	    break;}
	    
    return index;
}


/**************************************************************************************************
 NAME:	     conf2dump
 FUNCTION:   converts a data file text in plain text 
 INPUTS:     name of configuration file
 RETURN:     0
**************************************************************************************************/
int conf2dump( char filename[] )
{
    char buf[NMAX1];
    //Parameters
    sprintf( buf, "grep -v \"#\" %s | grep -v \"^$\" | gawk -F\"=\" '{print $2}' > %s.values", 
	     filename, filename );
    system( buf );
    //Names
    sprintf( buf, "grep -v \"#\" %s | grep -v \"^$\" | gawk -F\"=\" '{print $1}' > %s.names", 
	     filename, filename );
    system( buf );

    return 0;
}


/**************************************************************************************************
 NAME:       read_parameters
 FUNCTION:   reads the file with given name and load information of array given
 INPUTS:     array where it returns reading data and file name 
	     with configuration file
 RETURN:     0 if file read ok
	     1 if file dont exist
**************************************************************************************************/
int read_parameters( float parameters[],
		     char filename[] )
{
    char buf[NMAX1], filenamedump[NMAX1];
    char names[NMAX1];
    FILE *file_names, *file_values;

    //Load of File
    file_values = fopen( filename, "r" );
    if( file_values==NULL ){
	printf( "  * The file '%s' don't exist!\n", filename );
	return 1;}
    fclose(file_values);
    
    //Converting to plain text
    conf2dump( filename );
    
    //Opening File with parameter names
    sprintf( filenamedump, "%s.names", filename );
    file_names = fopen( filenamedump, "r" );
    //Opening File with parameter values
    sprintf( filenamedump, "%s.values", filename );
    file_values = fopen( filenamedump, "r" );
    
    //Reading
    while( getc( file_values ) != EOF ){
	fscanf( file_names, "%s", names );
// 	printf("%d   %s\n",parameter_index( names ), names );
	fscanf( file_values, "%f", &parameters[ parameter_index( names ) ] );}
	
    fclose( file_names );
    fclose( file_values );
    
    printf( "  * The file '%s' has been loaded!\n", filename );

    sprintf( buf, "rm -rf %s.values %s.names", filename, filename );
    system( buf );
    
    return 0;
}