#include <iostream>
#include <cmath>

using namespace std;


int rectCover(int number) {
    if (number == 0)
        return 0;
    int a = 1;
    int b = 2;
    for (int i = 1; i < number; i++){
        int temp = a;
        a = b;
        b = temp + b;
    }
    return a;
}


int main() {

    int res = rectCover(9);
    cout << res << endl;

}