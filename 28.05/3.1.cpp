#include <iostream>

template<typename T>
class vec{
    T* data;
    int size;
    int capacity;

    void reserve(int new_capacity) {
        if (new_capacity <= capacity)
            return;

        T* new_data = new T[new_capacity];

        for (int i = 0; i < size; ++i) {
            new_data[i] = data[i];
        }

        delete[] data;

        data = new_data;
        capacity = new_capacity;
    }

public:
    vec():
        data(nullptr),
        size(0),
        capacity(0) {}

    ~vec() {
        delete[] data;
    }

    void push(const T& value) {
        if (size == capacity) {

            int new_capacity;

            if (capacity == 0)
                new_capacity = 1;
            else
                new_capacity = capacity * 2;

            reserve(new_capacity);
        }

        data[size] = value;
        ++size;
    }

    void pop() {
        size--;
        
        T* tmp = new T[size];
        
        for (int i = 0;  i < size; i++){
            tmp[i] = data[i];
        }
        
        delete [] data;
        
        data = new T[size];
        
        for (int i = 0;  i < size; i++){
            data[i] = tmp[i];
        }
        
        delete [] tmp;
    }

    T& operator[](int index) {
        return data[index];
    }

    const T& operator[](int index) const {
        return data[index];
    }

    int get_size() const {
        return size;
    }

    class iterator {
        T* ptr;

    public:
        iterator(T* ptr):
            ptr(ptr) {}

        T& operator*() {
            return *ptr;
        }

        iterator& operator++() {
            ++ptr;
            return *this;
        }
    };

    iterator begin() {
        return iterator(data);
    }

    iterator end() {
        return iterator(data + size);
    }
};

int main() {
    vec<int> a;

    a.push(10);
    a.push(20);
    a.push(30);
    
    a.pop();

    // for (auto x : v) {
    //     std::cout << x << ' ';
    // }

    std::cout << *a.begin() << ", " << *(++a.begin()) << std::endl;
}