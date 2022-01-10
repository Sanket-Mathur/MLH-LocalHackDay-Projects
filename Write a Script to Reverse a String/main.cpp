#include<iostream>

using namespace std;

int main() {
    string str;

    // Enter the string
    cout << "Enter a String: ";
    getline(cin, str);

    // Reversing the string
    for (int i = 0; i < str.length() / 2; i++) {
        swap(str[i], str[str.length() - i - 1]);
    }

    // Print the resultant string
    cout << "Reversed String: " << str << endl;

    return 0;
}