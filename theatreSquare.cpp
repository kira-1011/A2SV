#include<iostream>

using namespace std;


int main(int argc, char const *argv[])
{
    long long n, m, a, result;

    cin >> n >> m >> a;
    
    if(n % a == 0)
        n /= a;

    else{
        n /= a;
        n ++;
    }


    if(m % a == 0)
        m /= a;
    
    else{
        m /= a;
        m ++;
    }

    result = n * m;
    cout << result << endl;

    return 0;
}

