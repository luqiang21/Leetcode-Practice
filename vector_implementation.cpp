#include <iostream>
#include <assert.h>
using namespace std;

template<typename T>
class myVector {
private:
    int vCapacity; // amount of available space
    int vSize; // number of elements in the list
    T *vArr; // the dynamic array
    void reserve(int n, bool copy);


public:
    myVector(): vCapacity(0), vSize(0), vArr(NULL) {}
    myVector(int vSize): vSize(vSize), vCapacity(vSize) {vArr = new T[vSize];}
    myVector(int vSize, T value): vSize(vSize), vCapacity(vSize){
        vArr = new T[vSize];
        for(int i = 0; i < vSize; ++i) {
            vArr[i] = value;
        }
    }

    int size();
    void push_back(const T& item); // increase capacity if needed.
    T back();
    T front();
    void pop_back();
    T at(int index);
    // void insert(T value);
    // void erase(T value);
    T & operator[ ] (unsigned int i);
    ~myVector() {delete [] vArr;}
};
template<typename T>
T myVector<T>::back() {
    return vArr[vSize-1];
}
template<typename T>
T myVector<T>::front() {
    return vArr[0];
}
template<typename T>
T myVector<T>::at(int index) {
    return vArr[index];
}
template<typename T>
void myVector<T>::pop_back() {
    vSize --;
}
template<typename T>
T & myVector<T>::operator[ ] (unsigned int i) {
    assert ((i >= 0) && (i < vSize));
    return vArr[i];
}
/*
When we add to the end of a myVector that is already filled to capacity(),
we allocate a new array with twice the capacity() O(1)
copy the old elements into the new array O(size())
discard the old array O(1)
add the new element to the end. O(1)
Total is O(size())
*/
template<typename T>
void myVector<T>::reserve(int n, bool copy) {
    T *newArr;

    // allocate a new dynamic array with n elements
    newArr = new T[n];
    cout << "******increase capacity from " << n/2 << " to " << n<< endl;
    if(newArr == NULL)
        // throw memoryAllocationError("myVector::reserve(): memory allocation failed.");
        cout << "myVector::reserve(): memory allocation failed." << endl;

    if(copy) {
        for(int i = 0; i < vSize; ++i) {
            newArr[i] = vArr[i];
        }
    }

    // delete old dynamic array, if vArr is NULL, the myVector was empty, no memory to delete
    if(vArr != NULL) {
        delete [] vArr;
    }

    vArr = newArr;
    vCapacity = n;
}

template<typename T>
void myVector<T>::push_back(const T& item) {
    // if space is full, allocate more capacity
    if(vSize == vCapacity) {
        if(vCapacity == 0) {
            // if capacity is 0, set to 1
            // set copy to false, because no existing elements
            reserve(1, false);
        }
        else{
            reserve(2*vCapacity, true);
        }
    }

    // add item to the list, update vSize
    vArr[vSize] = item;
    vSize ++;
}

template<typename T>
int myVector<T>::size() {
    return vSize;
}
int main() {
    myVector<int> v;
    v.push_back(1);
    v.push_back(3);
    v.push_back(4);
    cout << v[0] << "  " << v.at(1) << endl;
    v.pop_back();
    cout << v.size()<<endl;

    myVector<int> v2(10, 3);
    v2[8] = 132;
    v2[0] = 0;
    cout << "v2 is"<< endl;
    for(size_t i = 0; i < v2.size(); ++i) {
      cout << v2[i] << "    ";
    }
    cout << endl;
    v2.pop_back();
    cout << "after pop_back, v2 back is " << v2.back() << endl;
    cout << "head is " << v2.front() << endl;

    myVector<float> v3(4);
    for(size_t i = 0; i < v3.size(); ++i) {
      v3[i] = 0;
    }
    v3.push_back(7.4);
    cout << v3.at(0) <<endl;
    cout << v3.size() << endl;
    v3.push_back(8.8);

  std::cout << "Hello World!\n" << endl;
}
