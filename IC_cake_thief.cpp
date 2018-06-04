#include <iostream>
#include <vector>
using namespace std;
class CakeType
{
public:
    unsigned int weight_;
    unsigned int value_;

    CakeType(unsigned int weight = 0, unsigned int value = 0) :
        weight_(weight),
        value_(value)
    {
    }
};
// recursive
int helper(const vector<CakeType> &cakeTypes, int capacity, int res, int temp ) {
    if(capacity == 0) {
        if(temp > res) {
            res = temp;
        }
        return res;
    }
    else if(capacity < 0) return 0;
    else {
        for(int i = 0; i < cakeTypes.size(); ++i) {
            int weight = cakeTypes[i].weight_, value = cakeTypes[i].value_;
            if(weight == 0 && value != 0) throw invalid_argument("not possible");

            if(value == 0) continue;

            temp += value;
            res = max(res, helper(cakeTypes, capacity - weight, res, temp));
            temp -= value;
        }
    }
    return res;
}

int maxDuffelBagValue(const vector<CakeType>& cakeTypes, int capacity) {
    int res = 0;
    int temp = 0;
    res = helper(cakeTypes, capacity, res, temp);

    return res;


}


// iterative from interview cake solution
unsigned long long maxDuffelBagValue1(const vector<CakeType>& cakeTypes, unsigned int capacity) {
  // make a vector to hold the maximum possible value at every duffel bag weight
  // from 0 to capacity
  vector<unsigned long long> maxValueAtCapacities(capacity + 1);

  for(unsigned int currentCapacity = 0; currentCapacity <= capacity; ++currentCapacity) {
    unsigned long long currentMax = 0;

    for(const CakeType& cakeType: cakeTypes) {
      // if a cake weight 0, and has positive value, the Max value is infinity
      if(cakeType.weight_ == 0 && cakeType.value_ != 0) throw range_error("Max value is infinity");

      // if current cake weights less or equal than current capacity
      // it is possible to take the cake and get a better value
      if(cakeType.weight_ <= currentCapacity) {
        currentMax = max(currentMax, cakeType.value_ +
                  maxValueAtCapacities[currentCapacity - cakeType.weight_]);
      }
    }
    maxValueAtCapacities[currentCapacity] = currentMax;
  }

  return maxValueAtCapacities[capacity];
}

int main() {
  const vector<CakeType> cakeTypes {
                                    CakeType(7, 160),
                                    CakeType(3, 90),
                                    CakeType(2, 15),
                                    };

  unsigned int capacity = 20;

  cout << maxDuffelBagValue(cakeTypes, capacity) << endl;
  cout << maxDuffelBagValue1(cakeTypes, capacity) << endl;

    return 0;
}
