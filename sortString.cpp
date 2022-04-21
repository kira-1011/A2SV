class Solution {
public:
    string sortSentence(string s) {
        int found = 0; 
        int start, dis;
        string temp;
        string result;
        bool finished;

        for (int i = 1; found != -1; i++)
        {
            found = s.find(to_string(i));
            start = 0;
            dis = s.find(" ");
            finished = false;

            while (!finished)
            {
                if(dis != -1){
                    temp = s.substr(start, dis);
                    start = start + dis + 1;
                    dis = s.substr(start).find(" ");
                }

                else{
                     temp = s.substr(start);
                     finished = true;
                }



                if(temp.find(to_string(i)) != -1){
                    temp = temp.substr(0, temp.find(to_string(i)));
                    result = result + temp + " ";
                    break;
                }

            }
        }

        return result.substr(0, result.length() - 1);

    }
};        
 
