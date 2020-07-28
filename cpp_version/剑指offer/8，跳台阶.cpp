//
// Created by Jiang,Xinyang on 2020/7/28.
//

#include <iostream>

using namespace std;


int jumpFloor(int number) {
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

    int res = jumpFloor(9);
    cout << res << endl;

}