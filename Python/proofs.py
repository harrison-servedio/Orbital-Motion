from classifiedOrbitCalculator import planet, plot, live


# Simulation used to prove Kepler's 1st law
ps = [
    planet("Planet", 0, 784400000, 0, 0, 216635.0542985352, "Green"),
    planet("Host", 1E+30, 0, 0, 0, 0, "Orange"),
]
# plot(ps, 1, 10000, printInfo= True)


# Simulation 1 to prove Kepler's 3rd law
ps = [
    planet("Planet 1", 0, 784400000, 0, 0, 291661.2308568036, "Green"),
    planet("Host", 1E+30, 0, 0, 0, 0, "Orange"),
]
plot(ps, 1, 16912, printInfo=True)

# Simulation 2 to prove Kepler's 3rd law
ps = [
    planet("Planet 2", 0, 484400000, 0, 0, 371146.55136872607, "Green"),
    planet("Host", 1E+30, 0, 0, 0, 0, "Orange"),
]
# plot(ps, 1, 8207, printInfo=True)

# Simulation for investigation
# Altered the amount of orbits and the mass of "planet 2"
ps = [
    planet("Planet 2", 1e27, 484400000, 0, 0, 371146.55136872607, "Green"),
    planet("Host", 1E+30, 0, 0, 0, 0, "Orange"),
]

orbits= 90
# plot(ps, 1, 8207*orbits, printInfo=True)
live(ps, 100, 0.5, 100, None)