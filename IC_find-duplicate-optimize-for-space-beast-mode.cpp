#include <iostream>
#include <vector>
#include <assert.h>
using namespace std;

unsigned int findDuplicate(const vector<unsigned int>& intVector) {
    const size_t n = static_cast<unsigned int>(intVector.size() - 1);
    // 1. get inside a cycle
    unsigned int positionInCycle = n + 1;
    for(unsigned int i = 0; i < n; ++i) {
        positionInCycle = intVector[positionInCycle - 1];
    }
    // 2. find the length of the cycle
    unsigned int rememberedPositionInCycle = positionInCycle;
    unsigned int currentPositionInCycle = intVector[positionInCycle - 1];
    unsigned int cycleStepCount = 1;

    while(currentPositionInCycle != rememberedPositionInCycle) {
        currentPositionInCycle = intVector[currentPositionInCycle - 1];
        ++cycleStepCount;
    }
    // 3. find the first node of the cycle
    unsigned int pointerStart = n + 1;
    unsigned int pointerAhead = n + 1;
    for(unsigned int i = 0; i < cycleStepCount; ++i) {
        pointerAhead = intVector[pointerAhead - 1];
    }

    while(pointerStart != pointerAhead) {
        pointerAhead = intVector[pointerAhead - 1];
        pointerStart = intVector[pointerStart - 1];
    }

    return pointerStart;

}

int main ()
{

    vector<unsigned int> intVector {1, 3, 2, 2};

    cout << findDuplicate(intVector) << endl;
    assert(findDuplicate(intVector) == 21 && "Inequal");
    return 0;
}
