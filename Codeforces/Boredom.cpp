// https://codeforces.com/contest/25/problem/A

#include <iostream>

using namespace std;


long long fun(long long tab[], long long i, int len, long long pom[]) {
    if (i >= len)
        return 0;
    
    if (pom[i] < 0)
        pom[i] = max(
            i * tab[i] +  fun(tab, i+2, len, pom),
            fun(tab, i+1, len, pom)
        );

    return pom[i];
}

int main() {
    int len;
    cin >> len;
    int* nums = new int[len];
    int mx = 0;
    for (int i=0; i<len; i++) {
        cin >> nums[i];
        mx = max(mx, nums[i]);
    }

    long long* counter = new long long[mx + 1];
    long long* pom = new long long[mx + 1];

    for (int i=0; i<mx + 1; i++) {
        counter[i] = 0;
        pom[i] = -1;
    }

    for (int i=0; i<len; i++)
        counter[ nums[i] ] += 1;

    
    cout << fun(counter, 1, mx+1, pom);    

    return 0;
}