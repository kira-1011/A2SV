#include<iostream>
#include<vector>

using namespace std;

int main()
{
    int k = 2;
    vector<int> test(k, 0);

    for(auto v : test)
    {
        cout << v << " ";
    }
    cout << endl;

    k = 5;

    for(auto v : test)
    {
        cout << v << " ";
    }
   
    return 0;
}