#include <stdlib.h>
#include "contains.h"

void compress(int* compressed, int *data, int *c, int *u, int dataLen, int max) {
	int i, j, p, k;
	int count=0, used=0;
	int* dictionary = (int*) malloc( MAXDICTSIZE * 2 *sizeof(int) );
	int last = 0;
	int wewwe=0;
	
	for (i=0; i<dataLen; i+=last) {

		while ( last>0 && (p=contains(i,i+last+1,data,dictionary,used))==-1 ) last--;

		last++;

		if (used< (MAXDICTSIZE*2) ) {
			dictionary[used++] = i;
			dictionary[used++] = i+last+1;
		}
		if ( last <= 1 ) {
			compressed[count++] = data[i];
		}
		else {
			compressed[count++] = p+max+1;
		}
	}
	*c=count;
	*u=used;
	free(dictionary);
}
/*
int main() {
	int i, max = 3;
	int dataLen = 36;
	int count, used;
	int* compressed = (int*)malloc( dataLen *sizeof(int) );
	//R=0, G=1, B=2, Y=3
	int *data = (int*) malloc( dataLen *sizeof(int) );
	data = (int[36]){0, 0, 0, 0, 0, 0,
					 0, 1, 1, 1, 1, 0,
					 0, 1, 1, 1, 1, 0,
					 0, 2, 2, 3, 3, 3,
					 0, 2, 2, 3, 3, 3,
					 0, 0, 0, 3, 3, 3};

	printf("data:\n");
	for(i=0; i<dataLen; i++)
		printf("%3d",data[i]);
	printf("\n");


	compress(compressed, data, &count, &used, dataLen, max);

	printf("compressed:\n");
	for(i=0; i<count; i++)
		printf("%3d",compressed[i]);
	printf("\n");
	return 0;
}*/
