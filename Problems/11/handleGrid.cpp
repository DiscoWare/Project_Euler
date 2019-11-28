#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    ifstream i;
    i.open("grid.txt");
    string s;
    string result;
    int count = 1;
    while(i >> s)
    {
        if (s[0] == '0')
        {
            s = s[1];
        }
        result += s;
        if (count % 20 == 0)
        {
            result += "\n";
        }
        else
        {
            result += ", ";
        }
        ++count;
    }

    cout << result << endl;

    ofstream o;
    o.open("readyGrid.txt");
    o << result;
    i.close();
    o.close();

    return 0;
}