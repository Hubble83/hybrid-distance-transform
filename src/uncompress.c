#include <stdlib.h>
#include "contains.h"

#include <stdio.h>

void uncompress (int*b, int*compressed, int dictSize, int compSize, int max) {
	
	int i, j, c, antst=0, antend=1, pos=1, used=0;
	int* dictionary = (int*) calloc (dictSize,sizeof(int));
	b[0] = compressed[0];

	for (i=1; i<compSize; i++) {
		c=compressed[i];

		if ( c <= max ) {// é só um pixel
			b[pos++] = c;
		} // sao vários pixeis comprimidos (está no dicionario)
		else if ( dictionary[ (c-max-1) *2 ] + dictionary[ (c-max-1) *2 + 1 ] > 0  ) {

			for (j=dictionary[ (c-max-1) *2 ]; j<dictionary[ (c-max-1) *2 + 1 ]; j++) { ////////////////
				b[pos++] = b[j];
			}
		} // se nao exisitir no dicionario...
		else {
			for (j=antst; j<antend; j++) {
				b[pos++] = b[j];
			}
			b[pos++] = b[antst];
		}
		//adicionar atual ao dicionario () se não existir
		if ( used<(MAXDICTSIZE*2) && ( (antend +1 - antst) > 1) && (contains(antst, antend+1, b, dictionary, used) == -1) ) {
			dictionary[used++] = antst;
			dictionary[used++] = antend+1;
		}

		//cAnt = c;
		antst = antend;
		antend = pos; 
	}
}
/*
int main() {
	int N=8, M=8, P=2;
	int i, j, max = 2;
	int compSize = 9;
	int dictSize = 18;
	int* b = (int*) malloc ( N/P * M/P *sizeof(int));
	int* compressed = (int*) malloc( compSize *sizeof(int) );
	compressed = (int[36]){ 0,  3,  4,  5,
							1,  1,  3,  2,
							2,  0,  0,  0,
							0,  0,  0,  0};


	printf("compressed:\n");
	for(i=0; i<compSize; i++)
		printf("%3d",compressed[i]);
	printf("\n");

	
	uncompress(b, compressed, dictSize, compSize, max);

	printf("uncompressed:\n");
	for(i=0; i<N/P; i++) {
		for (j=0; j<M/P; j++)
			printf("%d ", b[i*M/P+j] );
		printf("\n");
	}
	return 0;
}*/