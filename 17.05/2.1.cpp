#include <iostream>

template<typename T>
class vector {
    T* data;
    int size;
public:
    vector():
        data(nullptr),
        size(0) {}

    ~vector() {
        delete[] data;
    }

    void push(const T& value) {
        T* tmp = new T[size];

        for (int i = 0; i < size; i++){
            tmp[i] = data[i];
        }

        delete[] data;
        data = new T[size+1];

        for (int i = 0; i < size; i++){
            data[i] = tmp[i];
        }
        data[size] = value;
        size++;
    }

    void pop() {
        T* tmp = new T[size-1];

        for (int i = 0; i < size-1; i++){
            tmp[i] = data[i];
        }

        delete [] data;
        T* data = new T[size-1];

        for (int i = 0; i < size-1; i++){
            data[i] = tmp[i];
        }
        --size;
    }

    T& get_elem(int ind){
        return data[ind];
    }

    int get_size() const {
        return size;
    }
};

int main(){
    vector<int> a;

    a.push(1);
    a.push(2);
    std::cout << a.get_elem(0) << ", " << a.get_elem(1) << std::endl;
    a.pop();
    std::cout << a.get_elem(0) << std::endl;
    return 0;
}