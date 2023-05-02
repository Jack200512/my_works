#include <iostream>
using namespace std;
int main(){
    int a=1;
    switch (
        a
    )
    {
    case 1:
        a=2;
        cout<<a;
        break;
    case 2:
        a=3;
        cout<<a;
        break;
    case 3:
        a=5;
        cout<<a;
        break;
    
    default:
        break;
    }
}