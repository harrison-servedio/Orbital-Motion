from classifiedOrbitCalculator import planet, plot, live


ps = [
    planet("Earth", 5.97219e24, 1.495978707e11, 0, 0, 29784, "Green"),
    planet("Moon", 7.3476e22, 3.84317695e8+1.495978707e11, 0, 0, 29784+1023, "Grey"),
    planet("Venus", 6.39e23, 114e9, 0, 0, 34500, "Pink"),
    planet("Mercury", 3.285e23, 69.814e9, 0, 0, 47000, "Silver"),
    planet("Sun", 1.989E+30, 0, 0, 0, 0, "Orange"),
    # oddMoon = planet("Moon's Moon", 0, 3.84317695e8+1.495978707e11+1e7, 0, 0, 29784+1023+350, "Purple"), 
]



live(planets=ps, steps=20, tincr=500, inter=100 , focus=ps[-1], focusSize=2e11)
# plot(ps, 100, 20000)