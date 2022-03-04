import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin, sqrt


def new_coordinate(left, start, right):
    new_cords = [0, 0]
    middle = [0, 0]
    middle[0] = (left[0] + right[0]) / 2
    middle[1] = (left[1] + right[1]) / 2
    new_cords[0] = middle[0] * 2 - start[0]
    new_cords[1] = middle[1] * 2 - start[1]
    return new_cords


def new_coordinate_del2(left, start, right):
    new_cords = [0, 0]
    middle = [0, 0]
    middle[0] = (left[0] + right[0]) / 2
    middle[1] = (left[1] + right[1]) / 2
    new_cords[0] = (middle[0] * 3 - start[0]) / 2
    new_cords[1] = (middle[1] * 3 - start[1]) / 2
    return new_cords


def perimetr(S1, S2, S3):
    s1s2 = sqrt((S2[0]-S1[0])**2+(S2[1]-S1[1])**2)
    s2s3 = sqrt((S3[0]-S2[0])**2+(S3[1]-S2[1])**2)
    s3s1 = sqrt((S1[0]-S3[0])**2+(S1[1]-S3[1])**2)
    perimetre = s1s2 + s2s3 + s3s1
    return perimetre


def method_simplex_f2(s1, s2, s3):
    ax2.plot((s1[0], s2[0]), (s1[1], s2[1]), linewidth=0.85, color="purple")
    ax2.plot((s2[0], s3[0]), (s2[1], s3[1]), linewidth=0.85, color="purple")
    ax2.plot((s3[0], s1[0]), (s3[1], s1[1]), linewidth=0.85, color="purple")
    Steps1 = 0
    _s1 = (-3, -1.4)
    _s2 = (-3, -2.4)
    _s3 = (-2, -1.4)
    ax2.plot((s1[0], _s2[0]), (s1[1], _s2[1]), linewidth=0.85, color="brown")
    ax2.plot((s2[0], _s3[0]), (s2[1], _s3[1]), linewidth=0.85, color="brown")
    ax2.plot((s3[0], _s1[0]), (s3[1], _s1[1]), linewidth=0.85, color="brown")
    s1 = _s1
    s2 = _s2
    s3 = _s3
    while perimetr(s1, s2, s3) > 1.2:
        if f1(s1[0], s1[1]) == max(f1(s1[0], s1[1]), f1(s2[0], s2[1]), f1(s3[0], s3[1])):
            new_cord = new_coordinate(s2, s1, s3)
            if f1(s1[0], s1[1]) == max(f1(s1[0], s1[1]), f1(new_cord[0], new_cord[1])):
                ax2.plot((s1[0], new_cord[0]), (s1[1], new_cord[1]), linewidth=0.85, color="blue", linestyle='--')
                s1 = new_cord
                ax2.plot((s1[0], s2[0]), (s1[1], s2[1]), linewidth=0.85, color="black")
                ax2.plot((s2[0], s3[0]), (s2[1], s3[1]), linewidth=0.85, color="black")
                ax2.plot((s3[0], s1[0]), (s3[1], s1[1]), linewidth=0.85, color="black")
            else:
                new_cord = new_coordinate_del2(s2, s1, s3)
                ax2.plot((s1[0], new_cord[0]), (s1[1], new_cord[1]), linewidth=0.85, color="blue", linestyle='--')
                s1 = new_cord
                ax2.plot((s1[0], s2[0]), (s1[1], s2[1]), linewidth=0.85, color="black")
                ax2.plot((s2[0], s3[0]), (s2[1], s3[1]), linewidth=0.85, color="black")
                ax2.plot((s3[0], s1[0]), (s3[1], s1[1]), linewidth=0.85, color="black")
        elif f1(s2[0], s2[1]) == max(f1(s1[0], s1[1]), f1(s2[0], s2[1]), f1(s3[0], s3[1])):
            new_cord = new_coordinate(s1, s2, s3)
            if f1(s2[0], s2[1]) == max(f1(s2[0], s2[1]), f1(new_cord[0], new_cord[1])):
                ax2.plot((s2[0], new_cord[0]), (s2[1], new_cord[1]), linewidth=0.85, color="orange", linestyle='--')
                s2 = new_cord
                ax2.plot((s1[0], s2[0]), (s1[1], s2[1]), linewidth=0.85, color="black")
                ax2.plot((s2[0], s3[0]), (s2[1], s3[1]), linewidth=0.85, color="black")
                ax2.plot((s3[0], s1[0]), (s3[1], s1[1]), linewidth=0.85, color="black")
            else:
                new_cord = new_coordinate_del2(s1, s2, s3)
                ax2.plot((s2[0], new_cord[0]), (s2[1], new_cord[1]), linewidth=0.85, color="orange", linestyle='--')
                s2 = new_cord
                ax2.plot((s1[0], s2[0]), (s1[1], s2[1]), linewidth=0.85, color="black")
                ax2.plot((s2[0], s3[0]), (s2[1], s3[1]), linewidth=0.85, color="black")
                ax2.plot((s3[0], s1[0]), (s3[1], s1[1]), linewidth=0.85, color="black")
        elif f1(s3[0], s3[1]) == max(f1(s1[0], s1[1]), f1(s2[0], s2[1]), f1(s3[0], s3[1])):
            new_cord = new_coordinate(s1, s3, s2)
            if f1(s3[0], s3[1]) == max(f1(s3[0], s3[1]), f1(new_cord[0], new_cord[1])):
                ax2.plot((s3[0], new_cord[0]), (s3[1], new_cord[1]), linewidth=0.85, color="yellow", linestyle='--')
                s3 = new_cord
                ax2.plot((s1[0], s2[0]), (s1[1], s2[1]), linewidth=0.85, color="black")
                ax2.plot((s2[0], s3[0]), (s2[1], s3[1]), linewidth=0.85, color="black")
                ax2.plot((s3[0], s1[0]), (s3[1], s1[1]), linewidth=0.85, color="black")
            else:
                new_cord = new_coordinate_del2(s1, s3, s2)
                ax2.plot((s3[0], new_cord[0]), (s3[1], new_cord[1]), linewidth=0.85, color="yellow", linestyle='--')
                s3 = new_cord
                ax2.plot((s1[0], s2[0]), (s1[1], s2[1]), linewidth=0.85, color="black")
                ax2.plot((s2[0], s3[0]), (s2[1], s3[1]), linewidth=0.85, color="black")
                ax2.plot((s3[0], s1[0]), (s3[1], s1[1]), linewidth=0.85, color="black")
        Steps1 += 1
    print("1-я функция сделала ", Steps1, "шагов")


def method_simplex_f1(s1, s2, s3):
    ax1.plot((s1[0], s2[0]), (s1[1], s2[1]), linewidth=0.85, color="purple")
    ax1.plot((s2[0], s3[0]), (s2[1], s3[1]), linewidth=0.85, color="purple")
    ax1.plot((s3[0], s1[0]), (s3[1], s1[1]), linewidth=0.85, color="purple")
    Steps1 = 0
    while perimetr(s1, s2, s3) > 1.2:
        if f1(s1[0], s1[1]) == max(f1(s1[0], s1[1]), f1(s2[0], s2[1]), f1(s3[0], s3[1])):
            new_cord = new_coordinate(s2, s1, s3)
            if f1(s1[0], s1[1]) == max(f1(s1[0], s1[1]), f1(new_cord[0], new_cord[1])):
                ax1.plot((s1[0], new_cord[0]), (s1[1], new_cord[1]), linewidth=0.85, color="blue", linestyle='--')
                s1 = new_cord
                ax1.plot((s1[0], s2[0]), (s1[1], s2[1]), linewidth=0.85, color="black")
                ax1.plot((s2[0], s3[0]), (s2[1], s3[1]), linewidth=0.85, color="black")
                ax1.plot((s3[0], s1[0]), (s3[1], s1[1]), linewidth=0.85, color="black")
            else:
                new_cord = new_coordinate_del2(s2, s1, s3)
                ax1.plot((s1[0], new_cord[0]), (s1[1], new_cord[1]), linewidth=0.85, color="blue", linestyle='--')
                s1 = new_cord
                ax1.plot((s1[0], s2[0]), (s1[1], s2[1]), linewidth=0.85, color="black")
                ax1.plot((s2[0], s3[0]), (s2[1], s3[1]), linewidth=0.85, color="black")
                ax1.plot((s3[0], s1[0]), (s3[1], s1[1]), linewidth=0.85, color="black")
        elif f1(s2[0], s2[1]) == max(f1(s1[0], s1[1]), f1(s2[0], s2[1]), f1(s3[0], s3[1])):
            new_cord = new_coordinate(s1, s2, s3)
            if f1(s2[0], s2[1]) == max(f1(s2[0], s2[1]), f1(new_cord[0], new_cord[1])):
                ax1.plot((s2[0], new_cord[0]), (s2[1], new_cord[1]), linewidth=0.85, color="orange", linestyle='--')
                s2 = new_cord
                ax1.plot((s1[0], s2[0]), (s1[1], s2[1]), linewidth=0.85, color="black")
                ax1.plot((s2[0], s3[0]), (s2[1], s3[1]), linewidth=0.85, color="black")
                ax1.plot((s3[0], s1[0]), (s3[1], s1[1]), linewidth=0.85, color="black")
            else:
                new_cord = new_coordinate_del2(s1, s2, s3)
                ax1.plot((s2[0], new_cord[0]), (s2[1], new_cord[1]), linewidth=0.85, color="orange", linestyle='--')
                s2 = new_cord
                ax1.plot((s1[0], s2[0]), (s1[1], s2[1]), linewidth=0.85, color="black")
                ax1.plot((s2[0], s3[0]), (s2[1], s3[1]), linewidth=0.85, color="black")
                ax1.plot((s3[0], s1[0]), (s3[1], s1[1]), linewidth=0.85, color="black")
        elif f1(s3[0], s3[1]) == max(f1(s1[0], s1[1]), f1(s2[0], s2[1]), f1(s3[0], s3[1])):
            new_cord = new_coordinate(s1, s3, s2)
            if f1(s3[0], s3[1]) == max(f1(s3[0], s3[1]), f1(new_cord[0], new_cord[1])):
                ax1.plot((s3[0], new_cord[0]), (s3[1], new_cord[1]), linewidth=0.85, color="yellow", linestyle='--')
                s3 = new_cord
                ax1.plot((s1[0], s2[0]), (s1[1], s2[1]), linewidth=0.85, color="black")
                ax1.plot((s2[0], s3[0]), (s2[1], s3[1]), linewidth=0.85, color="black")
                ax1.plot((s3[0], s1[0]), (s3[1], s1[1]), linewidth=0.85, color="black")
            else:
                new_cord = new_coordinate_del2(s1, s3, s2)
                ax1.plot((s3[0], new_cord[0]), (s3[1], new_cord[1]), linewidth=0.85, color="yellow", linestyle='--')
                s3 = new_cord
                ax1.plot((s1[0], s2[0]), (s1[1], s2[1]), linewidth=0.85, color="black")
                ax1.plot((s2[0], s3[0]), (s2[1], s3[1]), linewidth=0.85, color="black")
                ax1.plot((s3[0], s1[0]), (s3[1], s1[1]), linewidth=0.85, color="black")
        Steps1 += 1
    print("1-я функция сделала ", Steps1, "шагов")


f1 = lambda x1, x2: (((x1 - 2) * cos(35) + (x2 - 1) * sin(35)) ** 2 / 4) + (((x2 - 1) * cos(35) - (x1 - 2) * sin(35)) ** 2 / 25) + ((1/(x1 + x2 * sin(35) - 1)) + (1/(x1**2 + x2**2 - 16)))
f1_print = lambda x1, x2: (((x1 - 2) * cos(35) + (x2 - 1) * sin(35)) ** 2 / 4) + (((x2 - 1) * cos(35) - (x1 - 2) * sin(35)) ** 2 / 25)
internal_f1 = lambda x1, x2: x1**2 + x2**2 - 16
internal_f2 = lambda x1, x2: x1 + x2 * sin(35) - 1
function_fine = lambda x1, x2: ((1/(x1 + x2 * sin(35) - 1)) + (1/(x1**2 + x2**2 - 16)))
x1, x2 = np.linspace(-20, 20, 100), np.linspace(-20, 20, 100)
x1, x2 = np.meshgrid(x1, x2)
fig, (ax1, ax2) = plt.subplots(1,2)
ax1.contour(x1, x2, f1_print(x1, x2), levels=np.linspace(0, 30, 10))
ax1.scatter(2, 1, color="red")
ax1.contour(x1, x2, internal_f1(x1, x2), levels=np.linspace(0, 80, 100))
ax1.contour(x1, x2, internal_f2(x1, x2), levels=np.linspace(0, 80, 100))
ax2.contour(x1, x2, f1_print(x1, x2), levels=np.linspace(0, 30, 10))
ax2.scatter(2, 1, color="red")
ax2.contour(x1, x2, internal_f1(x1, x2), levels=np.linspace(0, 80, 100))
ax2.contour(x1, x2, internal_f2(x1, x2), levels=np.linspace(0, 80, 100))
method_simplex_f1((-3.5, 1), (-3.5, 0), (-2.5, 1))
method_simplex_f2((0, -15), (-1, -15), (0, -14))
plt.show()
#print(internal_f1() + internal_f2())
