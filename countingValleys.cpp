#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'countingValleys' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER steps
 *  2. STRING path
 */

int countingValleys(int steps, string path) {
    int total = 0;
    int countValley = 0;
    char start = path[0];
    
    for(int i = 0; i < steps; i ++){
        
        if(path[i] == 'U')
            total += 1;
            
        else
            total += -1;
        
        if(start != 'D')
            start = path[i];
        
         //if starting with a step down from sea level and ending with a step up to sea level. count valley
        if((total == 0 && start == 'D' && path[i] == 'U')){
            countValley ++;
            start = path[i];
        }
            
        
        
        
       
        
    }
    
    return countValley;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string steps_temp;
    getline(cin, steps_temp);

    int steps = stoi(ltrim(rtrim(steps_temp)));

    string path;
    getline(cin, path);

    int result = countingValleys(steps, path);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
