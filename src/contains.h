#ifndef MAXDICTSIZE
#define MAXDICTSIZE 10
inline int contains(int start, int end, int* data, int *dictionary, int used);
void compress(int* compressed, int *data, int *c, int *u, int dataLen, int max);
void uncompress (int*b, int*compressed, int dictSize, int compSize, int max);
#endif