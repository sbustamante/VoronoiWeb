#**************************************************************************************************
#	VORONOI WEB
#**************************************************************************************************
# Sebastian Bustamante (Universidad de Antioquia)
# Nataly Mateus (Universidad de Antioquia)

#--------------------------------------------------------------------------------------------------
# From the next list you can activate/deactivate the options to be applied to your run. If you 
# modify some of these values, make sure that you recompile the code by typing "make clean; make 
# VoronoiWeb"
#--------------------------------------------------------------------------------------------------
#Double precision
OPT   +=  -DDOUBLEPRECISION


#--------------------------------------------------------------------------------------------------
# Find below the compilation options
#--------------------------------------------------------------------------------------------------

CC	= gcc

CFLAGS	= $(OPT)

LIBS	= 

EXEC   = VoronoiWeb

OBJS   = main.o  inout.o

INCL   = allvars.h  proto.h  makefile


#Compiling
$(EXEC): $(OBJS) 
	$(CC) $(OBJS) $(LIBS)   -o  $(EXEC)

$(OBJS): $(INCL) 

clean:
	rm -f $(OBJS) $(EXEC)