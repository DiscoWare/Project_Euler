#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    ifstream i;
    i.open("Preprocessed.txt");
    string s;
    ofstream o;
    o.open("Postprocessed.txt");
    string result;
    result += "[";
    while (i >> s)
    {
        result += s + ",\n";
    }
    result += "]";
    o << result;
    i.close();
    o.close();

    return 0;
}
