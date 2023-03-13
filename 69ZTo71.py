# # Assignment One
# values = (0, 1, 2)

# if any(values):
#     my_var = 0

# my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

# if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):
#     print("Good")  # This is the result

# else:
#     print("Bad")


# Assignment Two
# v = 40

# my_range = list(range(v))

# print(sum(my_range, v) + pow(v, v, v))  # 820


# Assignment Three
# n = 20

# l = list(range(n))

# if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):
#     print("Good")

# # Output => Good


# Assignment Four
# Built function acts like Built in function all()
def my_all(items):
    for item in items:
        if bool(item) == False:
            return False
    return True


print(my_all([1, 2, 3]))  # True
print(my_all([1, 2, 3, []]))  # False

# Built function acts like Built in function any()


def my_any(items):
    for item in items:
        if bool(item):
            return True
    return False


# my_any
print(my_any([0, 1, [], False]))  # True
print(my_any([(), 0, False]))  # False

# my_max


def my_max(items):
    biggest = 0
    for item in items:
        if item > biggest:
            biggest = item
    return biggest


# my_max
print(my_max([10, 100, -20, -100, 50, 700]))  # 700
print(my_max((10, 100, -20, -100, 50, 700)))  # 700


# my_min
def my_min(items):
    smallest = 0
    for item in items:
        if item < smallest:
            smallest = item
    return smallest


# my_min
print(my_min([10, 100, -20, -100, 50]))  # -100
print(my_min((10, 100, -20, -100, 50)))  # -100
