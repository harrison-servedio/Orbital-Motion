from classifiedOrbitCalculator import planet, plot, live

# With lots of testing, binary star system works a little
# The suns are still moving very fast and they are very close to each other
# Most likely not realistic but visually functional
# The binary star set up makes it so the planet is not elliptical in orbit
v = 577480
ps = [
    planet("Sun 1", 1e30, 1E8, 0, 0, v, "Red"),
    planet("Sun 2", 1E30, 0, 0, 0, -v, "Orange"),
    planet("Planet", 0, 4E8, 0, 0, 700000, "Green"),
]

orbits= 1
live(ps, 100, 0.5, 100, None)