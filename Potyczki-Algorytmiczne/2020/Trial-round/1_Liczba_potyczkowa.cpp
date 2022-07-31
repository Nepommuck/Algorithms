#include <iostream>

using namespace std;

bool is_potyczkow(int num) {
    int cop = num;
    while (cop > 0) {
        int dig = cop % 10;
        if (dig == 0 || num % dig != 0)
            return false;

        cop /= 10;
    }
    return true;
}

int main() {
    for (int i=1; i<20; i++) {
        if(is_potyczkow(i))
            printf("%d \n", i);
    }
}