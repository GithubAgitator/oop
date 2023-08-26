# class Coda:
#     def __init__(self, dobavka=None):
#         self.dobavka = dobavka
#
#     def show_my_drink(self):
#         if self.dobavka:
#             print(f"Газировка и {self.dobavka}")
#         else:
#             print("Обычная газировка")
#
# a = Coda('aqua')
# a.show_my_drink()
#*************************8



#
# class TriangleChecker:
#     def __init__(self, a: int, b: int, c: int):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_triangle(self):
#         if (self.a + self.b) > self.c and (self.b + self.c) > self.a and (self.a + self.c) > self.b:
#             print('Ура, можно построить треугольник!')
#         elif self.a < 0 or self.b < 0 or self.c < 0:
#             print('С отрицательными числами ничего не выйдет!')
#         else:
#             print('Жаль, но из этого треугольник не сделать.')
#
# a = TriangleChecker(4, 0, 15)
# a.is_triangle()



#*************************************************

class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    def to_pound(self):
        return self.__kg * 2.205

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, kg):
        if isinstance(kg, (int, float)):
            self.__kg = kg
        else:
            raise ValueError('Килограммы задаются только числами')

        




