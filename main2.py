import matplotlib.pyplot as plt
import numpy as np

C0 = 9
C1 = 14
Cvx = 12
m0 = 4.2
m1 = 6.5
mvx = 4.5
T0 = 123
T1 = 138
Tp = 132
# consts:
Tr = 90
r = 2.26*10**6
kt = 5000
F = 10
ct = 4187

Cvix = lambda Cvx0, mvx0, Tp0: (mvx0*Cvx0*(ct*Tr-r))/(kt*F*(Tp0-Tr) + ct*Tr*mvx0 - r*mvx0)

cvxt = np.arange(C0, C1+0.001, 0.4)
fig, ax = plt.subplots()
ax.set_xlabel('C.вх')
ax.set_ylabel('C.вых')
ax.plot(cvxt, Cvix(cvxt, mvx, Tp), color='blue')
plt.show()


fig, ax = plt.subplots()
ax.set_xlabel('Mвх')
ax.set_ylabel('C.вых')
mvxt = np.arange(m0, m1+0.001, 0.2)
ax.plot(mvxt, Cvix(Cvx, mvxt, Tp), color='orange')
plt.show()


fig, ax = plt.subplots()
ax.set_xlabel('T.вх')
ax.set_ylabel('C.вых')
tvxt = np.arange(T0, T1+0.001, 0.5)
ax.plot(tvxt, Cvix(Cvx, mvx, tvxt), color='green')
plt.show()
