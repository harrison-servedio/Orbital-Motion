from classifiedOrbitCalculator import planet, plot, update
import tqdm

tI = 60

earth = planet("Earth", 5.97219e24, 149597870700, 0, 0, 29784, "Green")
mars = planet("Mars", 6.39e23, 114e9, 0, 0, 34500, "Red")
mercury = planet("Mercury", 3.285e23, 69.814e9, 0, 0, 47000, "Silver")
sun = planet("Sun", 1.989E+30, 0, 0, 0, 0, "Orange")
moon = planet("Moon", 7.3476e22, 384317695+149597870700, 0, 0, 29784+1023, "Grey")
moonsMoon = planet("Moon's Moon", 0, 384317695+149597870700+10000000, 0, 0, 29784+1023+350, "Purple")


ps = [sun, moonsMoon, moon, earth, mercury, mars]


oliver = planet("Oliver", 0, 2800, 0, 0, 100)
# ps = [sun, earth, oliver]



for i in tqdm.tqdm(range(226974)):
    update(ps, tI)

plot(ps)