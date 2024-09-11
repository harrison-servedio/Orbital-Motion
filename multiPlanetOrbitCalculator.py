# Used to iterate through the planets
from itertools import permutations 

# Used to graph and animate the data
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Used in formatting time
from dateutil.relativedelta import relativedelta as rd

# Used to create loading bar
from tqdm import tqdm


# G constant defined and unchanging
G = 6.67E-11

# Planet Class
#   Tracks location of a planet and its velo+accel
#   Updates the planet with the gravity from other planets
class planet:
    def __init__(self, name, mass, x, y, VX, VY, color=""):
        # Used for legend
        self.name = name
        self.mass = mass
        # Keeps track of the history of Xs and Ys for graphing purposes
        self.Xs = [x]
        self.Ys = [y]
        self.nState = [x, y, 0, 0, VX, VY]
        self.color = color
    
    # Preps the planet class for accel computations with other planets
    def nextState(self, tincr):
        # This calculates the future position of the planet after its acceleration has been calculated with the other planets
        x, y, xA, yA, xVel, yVel = self.nState

        VXOut = xVel+xA*tincr
        VYOut = yVel+yA*tincr
        xPosOut = x+VXOut*tincr
        yPosOut = y+VYOut*tincr

        self.nState = [xPosOut, yPosOut, 0, 0, VXOut, VYOut]

        # Saves the position of the planet in order to create a trail
        self.Xs.append(xPosOut)
        self.Ys.append(yPosOut)

    # Update calculates the acceleration between self and another planet 
    # Keeps track of the cumulative sum of the force from all other planets before running the update function
    def updateA(self, p):
        x, y, xA, yA, a, b = self.nState
        pX, pY = p.nState[:2]


        dist = (x-pX)**2 + (y-pY)**2
        AXOut = -(G*(x-pX)*p.mass)/dist**1.5
        AYOut = -(G*(y-pY)*p.mass)/dist**1.5
        self.nState = [x, y, xA+AXOut, yA+AYOut, a, b]

# Updates planet locs over timeIncr
# Uses permutations to run the update function for every planet with every other planet
def update(planets, timeIncr):
    for p, h in permutations(planets, 2):
        p.updateA(h)
    # After updating the accelerations of the planets, it runs update to compute the positions of the planets with the calculated
    for p in planets:
        p.nextState(timeIncr)

# Plots the position of the planets after a certain number of steps
# Takes a list of planet classes, the time increment between calculation steps, and the number of steps to simulate
# print info prints major and minor axis information for the planet number specified
def plot(planets, timeIncr, steps, printInfo = False, planetNum = 0):
    # Uses a tqdm loading bar and simulates the number of steps specified by repeatedly running the update function
    for _ in tqdm(range(steps)):
        update(planets, timeIncr)

    # Creates the figure
    fig, ax = plt.subplots(figsize=(5, 5), layout='constrained')
    # For each planet, plots it with its color if it has a color specified
    for p in planets:
        if p.color:
            # plots trail
            ax.plot(p.Xs, p.Ys, label = p.name, color=p.color)
            # Plots a point at end of trail
            ax.plot(p.Xs[-1], p.Ys[-1], "o", markeredgecolor=p.color, markerfacecolor=p.color)
        else:
            # plots trail
            ax.plot(p.Xs, p.Ys, label = p.name)
            # Plots a point at end of trail
            ax.plot(p.Xs[-1], p.Ys[-1], "o")
    
    # Sets the axis equal so the scale is the same for x and y
    plt.axis('equal')
    # creates a legend and displays the created graph
    plt.legend(loc='upper right')
    if printInfo:
        print(f"X min: {str(min(planets[planetNum].Xs))}\nX max: {str(max(planets[planetNum].Xs))}")
        print(f"Y min: {str(min(planets[planetNum].Ys))}\nY max: {str(max(planets[planetNum].Ys))}")
    plt.show()


# Lives takes various arguments in order to display a live simulation of the planets
#   planets - A list of instances of the planet class
#   steps - the steps between each frame
#   tincr - the time that each time step simulates in seconds
#   inter - the minimum time between frame(There might be more time between frame if the computer is too slow)
#   focus - the planet the animation focuses on
#   focusSize - the size of the window of the animation to be displayed
#   tailSize - The amount of points of the tail to display
# The poor use of global variables and of functions inside functions was needed because of the way matplotlib function animate works
def live(planets, steps, tincr, inter, focus=None, focusSize=2e11, tailSize=1e9):
    # f: Planet focused on
    # genD: Generate data, basically pauses the simulation if no data is being generated
    # s: size of focus window for animation 
    global f
    global genD
    global s
    s = focusSize
    f = focus
    genD = True
    # On press is triggered when there is user input
    def on_press(event):
        global f
        global genD
        global s
        # The space key pauses and unpauses the simulation
        if event.key == " ":
            genD = not genD
        # The equals key zooms in by decreasing the focus and the minus key zooms out by increasing the focus
        elif event.key == "=":
            s = s * 0.8
        elif event.key == "-":
            s = s * 1.2
        # check if the key pressed was a number and if it is set the focus to be the planet that correlates with that number
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
        # If simulation is not paused then animate otherwise the simulation doesn't change
        if genD:
            # Generates more data
            for i in range(steps):
                update(planets, tincr)
            # Clears the plot and completely replots the data
            plt.cla()
            for i, p in enumerate(planets):
                if p.color:
                    plt.plot(p.Xs[int(-tailSize):], p.Ys[int(-tailSize):], label = p.name + " - " + str(i+1), color=p.color)
                    plt.plot(p.Xs[-1], p.Ys[-1], "o", markeredgecolor=p.color, markerfacecolor=p.color)
                else:
                    plt.plot(p.Xs[int(-tailSize):], p.Ys[int(-tailSize):], label = p.name + " - " + str(i+1))
                    plt.plot(p.Xs[-1], p.Ys[-1], "o")
            plt.axis('equal')
            # If there is a focus then the graph is focused on that point
            if f:
                plt.axis([f.Xs[-1]-s, f.Xs[-1]+s, f.Ys[-1]-s, f.Ys[-1]+s])
            
            # sets the legend to the top right because having the legend be automatic slows down the simulation
            plt.legend(loc='upper right')
            
            # Next two lines were found online - they format the time in day hour minute second format
            fmt = '{0.days} days {0.hours} hours {0.minutes} minutes {0.seconds} seconds elapsed - focus size: ' + "{:e} - focused on: ".format(s) + (f.name if f else "None")
            plt.title(fmt.format(rd(seconds=tincr*len(p.Xs))))

    # Creates the plot
    fig, ax = plt.subplots()

    # Creates the animation object and sets up keypress events
    ani = FuncAnimation(plt.gcf(), animate, interval=inter, cache_frame_data=False)
    fig.canvas.mpl_connect('key_press_event', on_press)

    # Begins the animation
    plt.show()