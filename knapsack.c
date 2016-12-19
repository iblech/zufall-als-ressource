#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define N 38

unsigned int weight(const unsigned int a[N], const bool vs[N]) {
    int v = 0;
    for(int j = 0; j < N; j++) {
        if(vs[j] == true) {
            v += a[j];
        }
    }
    return v;
}

int main(int argc, char *argv[]) {
    const unsigned int a[N] = {1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,5,5,7,7,7,7,7,7,7,7,9,9,9,9};
    const unsigned int b    = 40;

    bool         xs[N][N]  = { {0} };
    unsigned int totals[N] = { 0 };
    unsigned int bs[N+1]   = { 0 };

    for(int j = 1; j <= N; j++) {
        bs[j] = bs[j-1] + a[j-1];
        if(bs[j] > b) bs[j] = b;
    }

    unsigned int k = 0;
    while(1) {
        k++;
        for(int i = 0; i < N; i++) {
            if(random() % 2 == 0) {
                int j = random() % N;
                if(xs[i][j] == true) {
                    xs[i][j] = false;
                } else if(xs[i][j] == false && weight(a, xs[i]) + a[j] <= bs[i+1]) {
                    xs[i][j] = true;
                }
            }

            if(weight(a, xs[i]) <= bs[i]) totals[i]++;
        }

        if(k % 10000 == 0) {
            double size = 1;
            for(int i = 0; i < N; i++) {
                if(totals[i] == 0) {
                    size = 0;
                } else {
                    size *= (double)k / totals[i];
                }
            }
            printf("%f\n", size);
        }
    }

    return 0;
}
