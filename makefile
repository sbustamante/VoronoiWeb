#==============================================================================
#	VORONOI WEB
#==============================================================================
# Sebastian Bustamante (Universidad de Antioquia)
# Nataly Mateus (Universidad de Antioquia)

CC	= gcc

CFLAGS	= -g -I. -c

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