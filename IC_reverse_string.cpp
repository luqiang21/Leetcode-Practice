//Write a function that takes a string and reverses the letters in-place.

#include <iostream>

using namespace std;

void reverse(string& str) {
  if(str.empty()) return;

  size_t leftIndex = 0;
  size_t rightIndex = str.length() - 1;

  while(leftIndex < rightIndex) {
    swap(str[leftIndex], str[rightIndex]);

    ++ leftIndex;
    -- rightIndex;
  }
}

int main() {
  string str = "love";
  cout << str << endl;

  reverse(str);
  cout << str << endl;
}
