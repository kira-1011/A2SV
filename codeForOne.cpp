#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>

using namespace std;

string codeOneArray(unsigned long long int n);
string leftArr = "";

int main()
{
    ios::sync_with_stdio(false);
    cout.tie(0); 
    cin.tie(0);

    unsigned long long int n, l, r;
    unsigned int ones = 0;

    cin >> n >> l >> r;

    string onesArray = codeOneArray(n).substr(l - 1, r - l + 1);

    // ones = count(onesArray.begin(), onesArray.end(), '1');

    // cout << ones << endl;

    return 0;
}
string codeOneArray(unsigned long long int n)
{
    if(n == 1)
        return "1";
    
    else
    {
        leftArr = codeOneArray(n / 2);

        leftArr += (to_string(n % 2));
        // leftArr.append(leftArr);

        leftArr += leftArr;

        return leftArr;
    }   
}