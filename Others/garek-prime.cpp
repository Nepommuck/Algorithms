// Garek's Prime
// Get a smallest prime number of a given sum of digits (for example 101)


#include <iostream>
#include <cmath>

#define lint long long int


using namespace std;

bool is_prime(lint n) {
    if (n == 2 || n == 3)
        return true;
    if (n < 2 || n % 2 == 0 || n % 3 == 0)
        return false;
    for (int i=6; i<sqrt(n) + 2; i++)
        if (n % (i-1) == 0 || n % (i+1) == 0)
            return false;
    return true;
}

lint smallest_of_sum(int sum) {
    int nines = sum / 9;
    lint num = sum % 9;

    while (nines) {
        num = 10*num + 9;
        nines -= 1;
    }
    
    return num;
}


class Node {
public:
    Node* left;
    Node* right;
    int val;

    Node(int v) {
        val = v;
        left = nullptr;
        right = nullptr;
    }
};


// Digital representation: number is a list of digits (0-9)
class Digrep{
public:
    Node* first;
    Node* last;
    
    // Create digital representation of a smallest number with sum of digits s
    Digrep(int s) {
        lint n = smallest_of_sum(s);
        int akt = n % 10;
        n /= 10;
        last = new Node(akt);
        first = last;

        while (n > 0) {
            int akt = n % 10;
            n /= 10;
            first->left = new Node(akt);
            first->left->right = first;
            first = first->left;
        }
    }

    // Get a integer value of a number
    lint calculate() {
        lint rez = 0;
        Node* p = first;
        while (p != nullptr) {
            rez = 10*rez + p->val;
            p = p->right;
        }
        return rez;
    }

    // Get a next number with the same sum of digits
    void increment() {
        Node* ob = last;
        // int ballance = ob->val;
        int ballance = 0;
        bool new_ness = false;

        // While not found anything to subtrack or not able to increment
        while (true) {
            ballance += ob->val;
            ob->val = 0;

            if (ballance > 0 && (ob->left == nullptr || ob->left->val < 9))
                break;
            else
                ob = ob->left;
        }

        // Not a single node at left
        if (ob->left == nullptr) {
            ob->left = new Node(1);
            first = ob->left;
            first->right = ob;
        }
        else
            (ob->left->val)++;        

        ballance--;

        // Making ...002999
        Node* p = last;
        while (ballance > 0)
        {
            int delta = min(ballance, 9);
            p->val = delta;
            ballance -= delta;

            p = p->left;
        }
    }
};


int main() {
    // Sum of digits and number of results
    int sum = 101, k = 20;

    Digrep* d1 = new Digrep(sum);

    int i=0;
    while (i < k)
    {
        lint a = d1->calculate();
        d1->increment();

        if ( is_prime(a) ) {
            i++;
            cout << (i < 10 ? " ": "") << i << ".  " << a << '\n';
        }
    }    

    return 0;
}
