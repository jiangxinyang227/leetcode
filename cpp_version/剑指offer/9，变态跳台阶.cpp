//
// Created by Jiang,Xinyang on 2020/7/28.
//

#include <iostream>
#include <cmath>

using namespace std;


int jumpFloorII(int number) {
    if (number == 0)
        return 0;

    return 1 << (number - 1);
}


int main() {

    int res = jumpFloorII(5);
    cout << res << endl;

}