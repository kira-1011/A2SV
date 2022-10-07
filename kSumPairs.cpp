#include<iostream>
#include<vector>
#include<map>

using namespace std;

int main(){

    vector<int> v = {3,1,3,4,3};

    multimap<int, int> map;

    for(int i = 0; i < v.size(); i++)
        map.insert(pair<int, int>(v[i], i));


    for(auto t : map){

        cout << "Key: " << t.first << " Value: " << t.second << endl;
    }

    string str = "1";

    int num = 1;

    

    cout << map.count(3) << endl; 
    return 0;
}