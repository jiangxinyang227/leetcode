//
// Created by Jiang,Xinyang on 2020/7/28.
//

#include <iostream>
#include <vector>

using namespace std;


int minNumberInRotateArray(vector<int> rotateArray) {
    int left = 0;
    int right = (int)rotateArray.size() - 1;

    while (left < right){
        int mid = (left + right) / 2;
        if (rotateArray[mid] > rotateArray[right])
            left = mid + 1;
        else if (rotateArray[mid] < rotateArray[right])
            right = mid;
        else
            right--;
    }
    return rotateArray[left];

}


int main() {

    vector<int> arr = {4, 5, 6, 1, 2, 3};
    int res = minNumberInRotateArray(arr);
    cout << res << endl;

}