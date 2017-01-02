
#include <stdio.h>
inline int contains(int start, int end, int* data, int *dictionary, int used) {
	int i,j;
	int search = end-start;
	int found = 0, value = -1;
	for(i=used-2; i>=0 && !found; i-=2) {
		if ( dictionary[i+1]-dictionary[i] == search ) {
			found = 1;
			for (j=0; j<search && found; j++) {
				found = data[start + j] == data[dictionary[i] + j];
			}
		} 
	}
	if (found) value = (i+2)/2;
	return value;
}
