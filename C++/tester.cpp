#include <iostream>
using namespace std;

double* arrayIncr(int incrementor, double* arrr){
    arrr[0] = arrr[0] + incrementor;
    return arrr;
}

int main(){
    int i = 23;
    double argr[3];
    double* ptr;
    argr[1] = 24;
    ptr = arrayIncr(i, argr);
    cout << ptr[1];

    return 0;
}