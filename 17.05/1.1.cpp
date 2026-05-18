#include <iostream>

#define DYN_ARR(type, name)		\
struct name {					\
	type* data;					\
	int size;					\
};								\
								\
void name##_init(name* arr){	\
	arr->data = nullptr;		\
	arr->size = 0;				\
}								\
								\
void name##_rm(name* arr){		\
	delete[] arr->data;			\
	arr->size = 0;				\
}								\
								\
void name##_add(name* arr, type a){				\
	type* tmp = new type[arr->size];		\
	for (int i = 0; i < arr->size; i++){	\
		tmp[i] = arr->data[i];				\
	}										\
	delete[] arr->data;						\
	arr->data = new type[arr->size+1];		\
	for (int i = 0; i < arr->size; i++){	\
		arr->data[i] = tmp[i];				\
	}										\
	arr->data[arr->size] = a;				\
	arr->size++;							\
}											\
											\
void name##_pop(name* arr, int ind){		\
	type* tmp = new type[arr->size-1];		\
	for (int i = 0; i < ind; i++){			\
		tmp[i] = arr->data[i];				\
	}										\
	for (int i = ind; i < arr->size-1; i++){\
		tmp[i] = arr->data[i+1];			\
	}										\
	delete[] arr->data;						\
	arr->data = new type[arr->size-1];		\
	for (int i = 0; i < arr->size-1; i++){	\
		arr->data[i] = tmp[i];				\
	}										\
	arr->size -= 1;							\
}											\
											\
type arr##_get(name* arr, int ind){			\
	return arr->data[ind];					\
}											\


DYN_ARR(int, arr)


int main(){
	arr A;
	arr_init(&A);
	arr_add(&A, 1);
	arr_add(&A, 2);
	std::cout << arr_get(&A, 0) << ", " << arr_get(&A, 1) << std::endl;
	arr_pop(&A, 0);
	std::cout << arr_get(&A, 0) << std::endl;
	arr_rm(&A);
	return 0;
}