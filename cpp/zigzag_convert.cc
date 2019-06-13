#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
    public:
        string convert(string str, int numRows) 
        {
            if (numRows == 1) return str;

            vector<string> zigzag(numRows);
            bool goingDown = false;
            int row = 0;

            for (char c: str) {
                zigzag[row] += c;

                if (row == 0 || row == (numRows-1)) 
                    goingDown = !goingDown;


                row += goingDown ? 1 : -1;
            }
            
            string result;
            for (auto s: zigzag)
                result += s;

            return result;
        }
};

int main()
{
    string str("AB");
    cout << Solution().convert(str, 1) << endl;

    return 0;
}
