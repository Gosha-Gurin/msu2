
EPS = 1e-15




class Polynomial:

    def __init__(self):

        self.coefficients = []
        self.x_dots = []
        self.y_dots = []

    def add_dot(self, x, y):

        for i in range(len(self.x_dots)):

            if abs(self.x_dots[i] - x) <= EPS:

                self.y_dots[i] = y
                return

        self.x_dots.append(float(x))
        self.y_dots.append(float(y))


    def coeff_calc(self):

        n = len(self.x_dots)

        self.coefficients = [0.0] * n

        for i in range(n):

            basis_poly = [1]

            denominator = 1

            for j in range(n):

                if j != i:

                    basis_poly = multiply_polynomials(
                        basis_poly,
                        [-self.x_dots[j], 1]
                    )

                    denominator *= (
                        self.x_dots[i]
                        - self.x_dots[j]
                    )

            factor = self.y_dots[i] / denominator

            for k in range(len(basis_poly)):

                self.coefficients[k] += (
                    basis_poly[k] * factor
                )


    def poly_calc(self, x):
        result = 0.0

        #А я вот такой вот крутой, буду такую функцию использовать =)
        for power, coef in enumerate(self.coefficients):

            result += coef * (x ** power)

        return result

    def dot_delete(self, x, y):

        for i in range(len(self.x_dots)):

            if (self.x_dots[i] == x and self.y_dots[i] == y):

                del self.x_dots[i]
                del self.y_dots[i]

                return

        print("Удаляешь точку, которой нет.")

    
    # Сравнение == и !=

    #Оказывается тут и так можно

    def __eq__(self, other):

        if len(self.coefficients) != len(other.coefficients):
            return False

        for a, b in zip(
            self.coefficients,
            other.coefficients
        ):

            if abs(a - b) >= EPS:
                return False

        return True



    def __ne__(self, other):
        return not self.__eq__(other)

def multiply_polynomials(first_poly, second_poly):

    if len(second_poly) != 2:
        print("Второй полином должен быть скобкой")

    result = [0] * (len(first_poly) + 1)

    # Сдвиг коэффициентов
    for i in range(len(first_poly)):
        result[i + 1] = first_poly[i]

    # Добавляем умножение на (-a)
    for i in range(len(first_poly)):
        result[i] += second_poly[0] * first_poly[i]

    return result

poly1 = Polynomial()
poly2 = Polynomial()

poly1.add_dot(1, 2)
poly1.add_dot(2, 3)

poly1.coeff_calc()

print("poly1:\n")
print(poly1.coefficients)

print(
    "\npoly1(2.5) =",
    poly1.poly_calc(2.5)
)

print()

poly1.add_dot(4, 4)

poly1.coeff_calc()

print("poly1:\n")
print(poly1.coefficients)

print()

poly2.add_dot(1, 2)
poly2.add_dot(2, 3)
poly2.add_dot(4, 4)
poly2.add_dot(10, -1.7)

poly2.coeff_calc()

print("poly2:\n")
print(poly2.coefficients)

print()

poly3 = Polynomial()

# Копирование
poly3.coefficients = poly2.coefficients.copy()
poly3.x_dots = poly2.x_dots.copy()
poly3.y_dots = poly2.y_dots.copy()

if poly3 == poly2:

    print("True\n")

    print("poly3:\n")
    print(poly3.coefficients)

    print("\npoly2:\n")
    print(poly2.coefficients)

print()

poly3.dot_delete(4, 4)

poly3.coeff_calc()

if poly3 != poly2:

    print("\nFalse\n")

    print("poly3:\n")
    print(poly3.coefficients)

    print("\npoly2:\n")
    print(poly2.coefficients)