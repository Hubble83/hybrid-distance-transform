EXEC = executable

# C Flags
C = -c
OPT = -O2
TESTFLAGS = -Wall -Wextra -pedantic -ansi
MATH = -lm -ffast-math 
LIB = -L/share/apps/papi/5.5.0/lib -I/share/apps/papi/5.5.0/include
PAPI = -lpapi
TEMPOS = -L/share/apps/mpiP-3.4.1 -lmpiP -lbfd -liberty -lunwind
VAMPIR = -I/share/apps/cuda/7.0.28/include/ -L/share/apps/cuda/7.0.28/lib64 -lcudart

# C Compiler
#CC=mpicc-vt -vt:cc gcc
CC=mpicc

all: comp uncomp contains dist dt
	$(CC) -o $(EXEC) bin/dt.o bin/distances.o bin/comp.o bin/uncomp.o bin/contains.o $(MATH) $(OPT) #$(VAMPIR)
	#export VT_BUFFER_SIZE=1024M
	#export VT_THREAD_BUFFER_SIZE=$VT_BUFFER_SIZE

contains: src/contains.c src/contains.h
	$(CC) -o bin/contains.o src/contains.c $(OPT) $(C)

comp: src/compress.c src/contains.h
	$(CC) -o bin/comp.o src/compress.c $(OPT) $(C)

uncomp: src/uncompress.c src/contains.h
	$(CC) -o bin/uncomp.o src/uncompress.c $(OPT) $(C)

dist: src/distances.c src/distances.h
	$(CC) -o bin/distances.o src/distances.c $(OPT) $(C)

dt: src/dt.c
	$(CC) -o bin/dt.o src/dt.c $(OPT) $(C)

clean:
	rm -rf $(EXEC) bin/*.o outpgm/*.pgm executable*

delete: clean
	rm -rf outpgm/*.pgm