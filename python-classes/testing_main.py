Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (2, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, ("a", 1))
my_square_3.my_print()

print("--")