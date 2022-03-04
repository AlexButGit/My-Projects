import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as ptchs

L = 2 ** 0.5
E = 0.001

def f(dx):
    return (1 + dx ** 2) ** 0.5

def x_el(t):
    try:
        return 1 / t
    except Exception:
        return 0

def P(dxs, dt):
    S = 0
    for dx in dxs:
        S += f(dx) * dt
    return S

def gradient(x, dt):
    dx = []
    for i in range(len(x) - 1):
        der = (x[i + 1] - x[i]) / dt
        dx.append(der)

    return np.array(dx)

def g_x(x, dt):
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    da = []

    while not it.finished:
        ix = it.multi_index
        xi = x.copy()
        xi[ix] += dt
        der = (P(gradient(xi, dt), dt) - P(gradient(x, dt), dt)) / dt
        da.append(der)
        it.iternext()

    da = np.array(da)
    return da

def new_x(dx, dt):
    h = 0.0001
    it = np.nditer(dx, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        ix = it.multi_index
        dxi1 = dx.copy()
        dxi2 = dx.copy()
        dxi1[ix] = dx[ix]
        dxi2[ix] = dx[ix] + h
        if P(gradient(dxi1, dt), dt) <= P(gradient(dxi2, dt), dt):
            dxi1 = dxi2
            h *= -1
            dxi2[ix] = dxi1[ix] + h

        while P(gradient(dxi1, dt), dt) > P(gradient(dxi2, dt), dt):
            dxi1 = dxi2
            dxi2[ix] = dxi1[ix] + h

        it.iternext()
    step = dx - dxi1
    return dxi1, step

def local_var(n):
    t0 = 0
    x0 = 0
    xt = []
    size = n + 1

    distance = [np.inf]
    t1 = np.random.uniform(1.0, 3.0)

    while True:
        x1 = x_el(t1)
        x = np.zeros(size)
        t = np.zeros(size)

        dt = (t1 - t0) / n
        dxe = (x1 - x0) / n

        x[0] = x0
        x[-1] = x1
        x[1:size-1] = np.array([x0 + dxe * i for i in range(1, n)])

        t[0] = t0
        t[-1] = t1
        t[1:size-1] = np.array([t0 + dt * j for j in range(1, n)])

        step = np.array([0.001 for i in range(n)])
        dist_prev = np.inf
        dist = 0
        while abs(dist_prev - dist) > E:
            dist_prev = dist
            dx = gradient(x, dt)
            dist = P(dx, dt)
            if dist > dist_prev:
                best_dist = dist_prev
                x[1:size - 1], step = new_x(x[1:n], dt)
            else:
                best_dist = dist
            x[1:n] += step

            # print(dist, dist_prev)

        distance.append(best_dist)
        xt.append((t, x))

        if distance[-2] != np.inf or distance[-1] != np.inf:
            if abs(distance[-2] - distance[-1]) > E:
                if distance[-2] < distance[-1]:
                    t1 -= dt / n
                else:
                    t1 += dt / n
                t1 = min(3, t1)
            else:
                best_dist = distance[-1]
                break
        else:
            break

    return x, t, best_dist

t0 = 0
x0 = 0

fg = plt.figure()
ax = plt.gca()

for n in range(3, 6):
    x, t, best_dist = local_var(n)
    print("Численный метод: {0}\nАналитичсекий метод: {1}".format(best_dist, L))
    ax.plot(t, x, label="n = {}".format(n))
    ax.scatter(t,x, color="black")


x = np.linspace(-40,40,500)
ax.plot(x, x_el(x), color='blue')
ax.plot(x,x, color="red")
ax.axhline(0, color='black', linestyle='--')
ax.axvline(0, color='black', linestyle='--')
ax.scatter(0, 0, color='red')
plt.legend()
plt.xlabel('t')
plt.ylabel('x')
plt.show()