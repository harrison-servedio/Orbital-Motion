from classifiedOrbitCalculator import planet, plot, live


horizontalSpeed = 0

ps = [
    planet("Moon", 7.3476e22, 3.84317695e8+1.495978707e11, 0, horizontalSpeed, 29784+1023, "Grey"),
    planet("Earth", 5.97219e24, 1.495978707e11, 0, horizontalSpeed, 29784, "Green"),
    planet("Venus", 6.39e23, 114e9, 0, horizontalSpeed, 34500, "Pink"),
    planet("Mercury", 3.285e23, 69.814e9, 0, horizontalSpeed, 47000, "Silver"),
    planet("Sun", 1.989E+30, 0, 0, horizontalSpeed, 0, "Orange"),
    # oddMoon = planet("Moon's Moon", 0, 3.84317695e8+1.495978707e11+1e7, 0, horizontalSpeed, 29784+1023+350, "Purple"), 
]



live(planets=ps, steps=1000, tincr=60, inter=1 , focus=ps[-1], focusSize=2e11)
# plot(ps, 100, 50000)