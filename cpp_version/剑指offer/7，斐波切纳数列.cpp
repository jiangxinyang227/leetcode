//
// Created by Jiang,Xinyang on 2020/7/28.
//

#include <iostream>

using namespace std;


int Fibonacci(int n) {
    int a = 0;
    int b = 1;

    for (int i = 0; i < n; i++) {
        int temp = a;
        a = b;
        b = temp + b;
    }
    return a;
}


int main() {

    int res = Fibonacci(9);
    cout << res << endl;

}
