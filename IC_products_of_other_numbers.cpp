#include <iostream>
#include <vector>
using namespace std;

vector<int> int_list = {1, 7, 3, 4};
vector<int> get_products_of_all_ints_except_at_index(vector<int> int_list) {
  if (int_list.size() < 2) {
          throw invalid_argument("Getting the product of numbers at"
              " other indices requires at least 2 numbers");
      }
    vector<int> res = int_list;

    for(int i = 1; i < int_list.size(); ++i) {
        cout << i << "  " << int_list[i] << endl;
        res[i] *= res[i-1] * int_list[i];
    }

    int accu = 1;
    for(int i = int_list.size() - 2; i > -1; --i) {
        accu *= int_list[i+1];
        res[i] *= accu;
    }

    return res;
}
int main() {

  vector<int> res = get_products_of_all_ints_except_at_index(int_list);
     for(int i = 0; i < res.size(); ++i) {
     std::cout << res[i] << endl;

     }
}
