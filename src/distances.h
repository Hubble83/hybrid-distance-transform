#ifndef DH
	#define DH 1
	
	#include <stdio.h>	
	#include <math.h>

	#define EUCLIDEAN 1
	#define MANHATTAN 2
	#define CHESSBOARD 3

	#define ONE_ALLTOALL 0
	#define ALLTOALL 1
	#define SCATTER 2
	#define ATA_MANY 3
	#define ALLTOALL_COMPRESS 4

	int max(int a, int b);
	int min(int a, int b);

	int EDTf(int x, int i, int g);
	int EDTSep(int i, int u, int gi, int gu, int infinity);

	int MDTf(int x, int i, int g);
	int MDTSep(int i, int u, int gi, int gu, int infinity);

	int CDTf(int x, int i, int g);
	int CDTSep(int i, int u, int gi, int gu, int infinity);
#endif