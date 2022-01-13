#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    vector<string> list;

    cout << "Enter the number of elements in the list: ";
    cin >> n;
    cin.ignore();

    for (int i = 0; i < n; ++i) {
        string str;
        getline(cin, str);
        list.push_back(str);
    }

    sort(list.begin(), list.end(), [](const string &a, const string &b) -> bool {
        string str1 = "", str2 = "";
        for (int i = 0; i < a.length(); ++i) {
            str1 += tolower(a[i]);
        }
        for (int i = 0; i < b.length(); ++i) {
            str2 += tolower(b[i]);
        }

        return str1 < str2;
    });

    cout << "\nSorted List:" << endl;
    for (string s : list) {
        cout << s << endl;
    }

    return 0;
}