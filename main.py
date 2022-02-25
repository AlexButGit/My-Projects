import matplotlib.pyplot as plt







def _z(z, t0):
    return (z - z ** 2) / 2 * _x(t0)





def _x(t0):
    return pow((3 * t0 - 1) ** 2, 1/3)




def global_x(z, t0, del_t):
    return _x(t0) - _z(z, t0 + del_t)

t1 = 0
t0 = 0.33
z = 1
del_t, del_t1 = 0.008, 0.012
x = 0
fig, ax = plt.subplots()
step = 0
while x < 1.587:
    X = t0 + del_t
    G = t1 + del_t1
    Y = global_x(z, t0, del_t)
    ax.plot((t0, X), (x, Y), linewidth=0.85, color="red")
    x = global_x(z, t0, del_t)
    z = _z(z, t0)
    t0 += del_t
    t1 += del_t1
    step += 1
    print("x= ", x, " t0= ", t1)
print(step)


plt.show()