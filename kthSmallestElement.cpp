#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int main()
{

    vector<int> nums = {9,0,8,2,1};

    make_heap(nums.begin(), nums.end());

    for(auto v : nums)
        cout << v << " ";
    cout << endl;

    return 0;
}