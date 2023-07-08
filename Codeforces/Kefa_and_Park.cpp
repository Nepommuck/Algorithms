#include <iostream>
#include <vector>

using namespace std;

int restaurants_to_visit(int vertex, int parent, int catsAtTheMoment, vector<int> neibours[], int catAt[], int maxCats) {
    catsAtTheMoment += catAt[vertex];
    if (catsAtTheMoment > maxCats)
        return 0;
    
    // We arrived succesfully at the restaurant
    if (neibours[vertex].size() <= 1 && vertex != 0)
        return 1;

    // The journey is not yet finished
    catsAtTheMoment = (catAt[vertex] == 0) ? 0 : catsAtTheMoment;
    int result = 0;
    for (auto k = neibours[vertex].begin(); k != neibours[vertex].end(); k++)
        if (*k != parent)
            result += restaurants_to_visit(*k, vertex, catsAtTheMoment, neibours, catAt, maxCats);
    return result;
}

int main() {
    int n, maxCats;
    cin >> n >> maxCats;
    int catAt[n];
    for (int i=0; i<n; i++)
        cin >> catAt[i];

    vector<int> neibours[n];

    for (int i=0; i<n-1; i++) {
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        neibours[a].push_back(b);
        neibours[b].push_back(a);
    }

    // for (int i=0; i<n; i++) {
    //     for (auto k = neibours[i].begin(); k != neibours[i].end(); k++)
    //         cout << *k << " ";
    //     cout << endl;
    // }
    cout << restaurants_to_visit(0, -1, 0, neibours, catAt, maxCats);
}
