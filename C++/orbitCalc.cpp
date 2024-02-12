#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

int increment(int timeIncr, double G, double H, double X, double Y, double Xa, double Ya, double Xv, double Yv, double* output){;
    output[4] = Xv+Xa*timeIncr;
    output[5] = Yv+Ya*timeIncr;
    output[0] = X+output[4]*timeIncr;
    output[1] = Y+output[5]*timeIncr;
    double dist = pow(output[0]*output[0] + output[1]*output[1], 1.5);
    output[2] = -(G*output[0]*H)/dist;
    output[3] = -(G*output[1]*H)/dist;
    return 0;
    }


int main(){
    // Defining initial conditions
    double Xi = 149597870700;
    double Yi = 0;
    double ViX = 0;
    double ViY = 29784;
    double G = 6.67e-11;
    double H = 1.989E+30;
    int tInc = 60;

    struct {
        double X;
        double Y;
        double Xa;
        double Ya;
        double Xv;
        double Yv;
    } currentState;


    currentState.X = Xi;
    currentState.Y = Yi;
    currentState.Xv = ViX;
    currentState.Yv = ViY;

    vector<double> Xs;
    vector<double> Ys;
    Xs.emplace_back(Xi);
    Ys.emplace_back(Yi);

    cout << Ys.at(0);

    double out[6];

    increment(tInc, G, H, currentState.X, currentState.Y, currentState.Xa, currentState.Ya, currentState.Xv, currentState.Yv, out);

    for (int i = 0; i < 6; i++){
        cout << out[i] << "\n";
    }
    

    return 0;
}
// (149597870678.65912, 1787040.0, -0.005928021812426769, -7.081392302992428e-08, -0.3556813087202593, 29784.0)