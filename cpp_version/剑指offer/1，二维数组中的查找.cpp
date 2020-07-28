//
// Created by Jiang,Xinyang on 2020/7/27.
//

#include <iostream>
#include <vector>

using namespace std;

bool find(vector<vector<int>>& arr, int target){
    if (arr.empty())
        return false;

    int row = 0;
    int col = (int)arr[0].size() - 1;

    while (row < arr.size() && col >= 0){
        if (target == arr[row][col])
            return true;
        else if (target < arr[row][col])
            col--;
        else
            row++;
    }
    return false;
}


int main(){
    vector<vector<int>> arr = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int target = 5;
    int target1 = 10;

    bool res1 = find(arr, target);
    cout << res1 << endl;
    bool res2 = find(arr, target1);
    cout << res2 << endl;
}
