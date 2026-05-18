//g++ 2.3.cpp -std=c++20

#include <iostream>
#include <cmath>
#include <array>

# define PI           3.14159265358979323846 

template<int N>
struct table{
	static constexpr double step = (2 * PI) / (N-1);

	std::array<double, N> val;

	constexpr table(){
		for (int i = 0; i < N; i++){
			val[i] = std::sin(i * step);
			//Гадина работает с погрешностью, так что не пугайся ешек в выводе
		}
	}

	// ~table(){
	// 	delete val;
	// }
};

constexpr int CONST_STEP_TABLE = 10000;

constexpr table<CONST_STEP_TABLE> sin_table;

double my_sin(const double x){
	double	mod_x = x;
	if (x >= 0){
		while (x > 2 * PI){
			mod_x -= 2 * PI;
		}
	} else {
		while (x < 0){
			mod_x -= 2 * PI;
		}
	}

	//Где мы по таблице
	int ind = static_cast<int>(x / sin_table.step);

	if (ind != CONST_STEP_TABLE-1){
		return sin_table.val[ind] + (x/sin_table.step - ind) * (sin_table.val[ind] - sin_table.val[ind+1]);
	} else{
		return sin_table.val[CONST_STEP_TABLE-1];
	}

}

int main()
{
	std::cout << my_sin(M_PI/3) << std::endl;
	return 0;
}