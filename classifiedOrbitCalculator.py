from itertools import permutations # Used to iterate through the planets
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from dateutil.relativedelta import relativedelta as rd

# G constant defined and unchanging
G = 6.67E-11

class planet:
    def __init__(self, name, mass, x, y, VX, VY, color=""):
        self.name = name
        self.mass = mass
        # Keeps track of the history of Xs and Ys for graphing purposes
        self.Xs = [x]
        self.Ys = [y]
        self.nState = [x, y, 0, 0, VX, VY]
        self.color = color
    
    # Preps the planet class for accel computations with other planets
    def nextState(self, tincr):
        # To adopt this function to work in three dimensions should only need to add a z, zA, and zVel. Note to self - Do you know how to name vars?
        x, y, xA, yA, xVel, yVel = self.nState
        VXOut = xVel+xA*tincr
        VYOut = yVel+yA*tincr
        xPosOut = x+VXOut*tincr
        yPosOut = y+VYOut*tincr
        self.nState = [xPosOut, yPosOut, 0, 0, VXOut, VYOut]
        self.Xs.append(xPosOut)
        self.Ys.append(yPosOut)

    def updateA(self, p):
        x, y, xA, yA, a, b = self.nState
        pX, pY, _, _, _, _ = p.nState
        dist = (x-pX)**2 + (y-pY)**2
        AXOut = -(G*(x-pX)*p.mass)/dist**1.5
        AYOut = -(G*(y-pY)*p.mass)/dist**1.5
        self.nState = [x, y, xA+AXOut, yA+AYOut, a, b]

# Updates planet locs over timeIncr
def update(planets, timeIncr):
    for p, h in permutations(planets, 2):
        p.updateA(h)
    for p in planets:
        p.nextState(timeIncr)


def plot(planets):
    fig, ax = plt.subplots(figsize=(5, 5), layout='constrained')
    for p in planets:
        if p.color:
            ax.plot(p.Xs, p.Ys, label = p.name, color=p.color)
            ax.plot(p.Xs[-1], p.Ys[-1], "ro", markeredgecolor=p.color, markerfacecolor=p.color)
        else:
            ax.plot(p.Xs, p.Ys, label = p.name)
            ax.plot(p.Xs[-1], p.Ys[-1], "ro")
    plt.axis('equal')
    plt.legend()
    # plt.axis([-2e11, 2e11, -2e11, 2e11])
    plt.show()







def live(planets, steps, tincr, inter, focus=None, focusSize=2e11, tailSize=1e9):
    global f
    global genD
    global s
    s = focusSize
    f = focus
    genD = True
    def on_press(event):
        global f
        global genD
        global s
        if event.key == " ":
            genD = not genD
        elif event.key == "=":
            s = s * 0.8
        elif event.key == "-":
            s = s * 1.2
        else:
            try:
                key = int(event.key)
                if key == 0:
                    f = None
                else:
                    f = planets[key-1]
            except:
                pass
    

    def animate(i):
        global f
        global genD
        global s
        if genD:
            for i in range(steps):
                update(planets, tincr)
            plt.cla()
            for i, p in enumerate(planets):
                if p.color:
                    plt.plot(p.Xs[int(-tailSize):], p.Ys[int(-tailSize):], label = p.name + " - " + str(i+1), color=p.color)
                    plt.plot(p.Xs[-1], p.Ys[-1], "ro", markeredgecolor=p.color, markerfacecolor=p.color)
                else:
                    plt.plot(p.Xs[int(-tailSize):], p.Ys[int(-tailSize):], label = p.name + " - " + str(i+1))
                    plt.plot(p.Xs[-1], p.Ys[-1], "ro")
            plt.axis('equal')
            plt.legend()
            if f:
                plt.axis([f.Xs[-1]-s, f.Xs[-1]+s, f.Ys[-1]-s, f.Ys[-1]+s])
            
            # taken from online - cite before submitting
            ###############################################################
            fmt = '{0.days} days {0.hours} hours {0.minutes} minutes {0.seconds} seconds elapsed - focus size: ' + "{:e} - focused on: ".format(s) + (f.name if f else "None")
            
            plt.title(fmt.format(rd(seconds=tincr*len(p.Xs))))
            ##############################################################

    fig, ax = plt.subplots()
    ani = FuncAnimation(plt.gcf(), animate, interval=inter)
    fig.canvas.mpl_connect('key_press_event', on_press)
    plt.tight_layout()
    plt.show()