from classifiedOrbitCalculator import planet, plot, live

ps = [
    planet("Earth", 1E+20, 384400000, 0, 0, 416635.0542985352, "Green"),
    planet("Sun", 1E+30, 0, 0, 0, 0, "Orange"),
    # oddMoon = planet("Moon's Moon", 0, 3.84317695e8+1.495978707e11+1e7, 0, horizontalSpeed, 29784+1023+350, "Purple"), 
]



live(planets=ps, steps=5, tincr=1, inter=1 , focus=ps[-1], focusSize=2e11, tailSize=400)
# plot(ps, 100, 50000)