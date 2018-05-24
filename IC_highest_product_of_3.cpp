// Given a vector of integers, find the highest product you can get from three of the integers.

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int highest_product_of_3(const vector<int>& v) {
    if(v.size() < 3) {
        throw invalid_argument("less than 3 items");
    }
    int highest, lowest, highest_2, lowest_2, res;
    highest = max(v[0], v[1]);
    lowest = min(v[0], v[1]);
    highest_2 = v[0] * v[1];
    lowest_2 = highest_2;
    res = v[0] * v[1] * v[2];

    for(size_t i = 2; i < v.size(); ++i) {
        int cur = v[i];
        res = max(max(res, cur * highest_2), cur * lowest_2);

        highest_2 = max(max(highest_2, cur * highest), cur * lowest);

        lowest_2 = min(min(lowest_2, cur * highest), cur * lowest);

        highest = max(highest, cur);
        lowest = min(lowest, cur);

    }

    return res;
}



int list_of_ints[] = {1, 10, -5, 1, -100};
int a[] = {-10,-10,1,3,2};

int main() {
    vector<int> v1, v2;
    v1.assign(list_of_ints, list_of_ints + sizeof(list_of_ints)/sizeof(list_of_ints[0]));
    v2.assign(a, a + sizeof(a)/sizeof(a[0]));

    cout << highest_product_of_3(v1) << endl;
    cout << highest_product_of_3(v2) << endl;

    return 0;
}
