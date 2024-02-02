#include <stdio.h>
#include <inttypes.h>

int main(void){

    double aboat = 320000.0;
    double abet = 2.214e-20;
    abet = abet + 1.34e-20;

    printf("%f can be written %e\n", aboat, aboat);
    printf("%.25f can be written %e\n", abet, abet);

    return 0;
}