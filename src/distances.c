#include <math.h>

int max(int a, int b) {
	return a>b ? a : b;
}

int min(int a, int b) {
	return a<b ? a : b;
}

int EDTf(int x, int i, int g) {
	return (x-i)*(x-i) + g*g;
}

int EDTSep(int i, int u, int gi, int gu, int infinity) {
	return (u*u - i*i + gu*gu - gi*gi)/(2*(u-i));
}

int MDTf(int x, int i, int g){	
	return abs(x-i) + g;
}

int MDTSep(int i, int u, int gi, int gu, int infinity) {
	if (gu >= (gi + u - i))
		return infinity;
	if (gi > (gu + u - i))
		return -infinity;
	return (gu - gi + u + i)/2;

}

int CDTf(int x, int i, int g) {	
	return max( abs(x-i), g);
}

int CDTSep(int i, int u, int gi, int gu, int infinity) {
	if (gi <= gu)
		return max(i+gu, (i+u)/2 );
	else
		return min(u-gi, (i+u)/2 );
}