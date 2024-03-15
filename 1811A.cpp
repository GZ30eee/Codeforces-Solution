#include<bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    while(t--)
    {
        int n;
        string s;
        char ch;
        bool b = false;
        cin >> n >> ch >> s;
        for(int i = 0 ; i < n ; i++)
        {
            if(s[i]<ch)
            {
                cout << ch;
                b = true;
                for(int j = i ; j < n ; j++) cout << s[j];
                break;
            }
            else
            {
                cout << s[i];
            }
        }
        if(!b) cout << ch;
        cout << endl;
    }
}
