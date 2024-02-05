from classifiedOrbitCalculator import planet, plot, update, live
import tqdm

tI = 60

earth = planet("Earth", 5.97219e24, 1.495978707e11, 0, 0, 29784, "Green")
venus = planet("Venus", 6.39e23, 114e9, 0, 0, 34500, "Pink")
mercury = planet("Mercury", 3.285e23, 69.814e9, 0, 0, 47000, "Silver")
sun = planet("Sun", 1.989E+30, 0, 0, 0, 0, "Orange")
# mars = planet("Mars", )


moon = planet("Moon", 7.3476e22, 3.84317695e8+1.495978707e11, 0, 0, 29784+1023, "Grey")
# moonsMoon = planet("Moon's Moon", 0, 3.84317695e8+1.495978707e11+1e7, 0, 0, 29784+1023+350, "Purple")

# satellite = planet("Satellite")

oliver = planet("Oliver", 0, 1400, 0, 0, 50)


ps = [sun, moon, earth, mercury, venus]



# ps = [sun, earth, oliver]


live(planets=ps, steps=1000, tincr=500, inter=200 , focus=sun, focusSize=2e11)