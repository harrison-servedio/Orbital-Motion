Xi = 149597870700
Yi = 0
ViX = 0
ViY = 29784
G = 6.67*10**-11
H = 1.989E+30
tInc = 60



xPos = [Xi]
yPos = [Yi]
VX = [ViX]
VY = [ViY]

dist = (xPos[-1]**2 + yPos[-1]**2)

AXi = -(G*xPos[-1]*H)/dist**1.5
AYi = -(G*yPos[-1]*H)/dist**1.5

AX = []
AY = []


states = [(Xi, Yi, AXi, AYi, ViX, ViY)]

def increment(timeIncr, G, state):
    x, y, xA, yA, xVel, yVel = state
    VXOut = xVel+xA*timeIncr
    VYOut = yVel+yA*timeIncr
    xPosOut = x+VXOut*timeIncr
    yPosOut = y+VYOut*timeIncr
    dist = (xPosOut**2 + yPosOut**2)
    AXOut = -(G*xPosOut*H)/dist**1.5
    AYOut = -(G*yPosOut*H)/dist**1.5
    
    return (xPosOut, yPosOut, AXOut, AYOut, VXOut, VYOut)

# import tqdm

# for i in tqdm.tqdm(range(1526974)):
#     states.append(increment(tInc, G, states[-1]))

# Xs = []
# Ys = []

# for i in tqdm.tqdm(states):
#     Xs.append(i[0])
#     Ys.append(i[1])



# import matplotlib
# import matplotlib.pyplot as plt

# fig, ax = plt.subplots(figsize=(5, 5), layout='constrained')
# ax.plot(Xs, Ys, label = "testLabel")
# ax.plot(0, 0, "ro", markerfacecolor="orange")
# ax.plot(Xs[-1], Ys[-1], "ro", markeredgecolor="green", markerfacecolor="green")

# print(states[-1])

# plt.axis('equal')
# plt.show()

print(increment(tInc, G, states[-1]))