import matplotlib.pyplot as plt




def restrikt(color, del_t, del_t1):
    t1 = 0
    t0 = 0.33
    z = 1
    x = 0
    while x < 1.587:
        X = t0 + del_t
        G = t1 + del_t1
        Y = global_x(z, t0, del_t)
        ax.plot((t1, G), (x, Y), linewidth=0.85, color=color)
        x = global_x(z, t0, del_t)
        z = _z(z, t0)
        t0 += del_t
        t1 += del_t1



def _z(z, t0):
    return (z - z ** 2) / 2 * _x(t0)


def _x(t0):
    return pow((3 * t0 - 1) ** 2, 1/3)


def global_x(z, t0, del_t):
    return _x(t0) - _z(z, t0 + del_t)


fig, ax = plt.subplots()
restrikt("blue", 0.02, 0.029)
#restrikt("blue", 0.005, 0.0074)






def search(color, del_t, del_t1):
    t1 = 0
    t0 = 0.33
    z = 1
    x = 0

    while t0 <= 1:
        X = t0 + del_t
        G = t1 + del_t1
        Y = global_x(z, t0, del_t)
        ax.plot((t1, G), (x, Y), linewidth=0.85, color=color)
        x = global_x(z, t0, del_t)
        z = _z(z, t0)
        if(x>Y):
            x = -global_x(z, t0, del_t)
        else:
            x = global_x(z, t0, del_t)

        t0 += del_t
        t1 += del_t1
        print("x= ", x, " t0= ", t1)


search("red", 0.01, 0.0148)

plt.show()