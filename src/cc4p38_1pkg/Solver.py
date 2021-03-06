import math , sys
class Solver:
    pass

def demo(a,b,c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        disc = math.sqrt(d)
        root1 = (-b + disc) / (2 * a)
        root2 = (-b - disc) / (2 * a)
        return root1, root2
    elif d == 0:
        return -b / (2 * a)
    else:
        return "This equation has no roots"

if __name__ == "__main__":
    s = Solver()
    a = int(input("A"))
    b = int(input("B"))
    c = int(input("C"))
    print(demo(a,b,c))