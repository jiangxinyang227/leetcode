//
// Created by Jiang,Xinyang on 2020/7/27.
//

#include <iostream>
#include <string>

using namespace std;

void replaceSpace(char* str, int length){
    if (str == nullptr || length <= 0)
        return;

    int count = 0;
    for (int i = 0; i <= length; ++i){
        if (str[i] == ' ')
            ++count;
    }
    if (count == 0)
        return;
    int newLength = length + count * 2;

    for (int j = length; j >= 0; --j){
        if (str[j] == ' '){
            str[newLength--] = '0';
            str[newLength--] = '2';
            str[newLength--] = '%';
        }
        else
            str[newLength--] = str[j];
    }
    cout << str << endl;
}


int main(){
    string s = "We are happy";
    char* str = (char*)s.c_str();
    int length = s.size() - 1;
    cout << length << endl;
    replaceSpace(str, length);

}