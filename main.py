from GOL_Simulation import GOL_Simulation

newSim = GOL_Simulation(30, 5, 5, 50)
for i in range(50):
    print '\nIteration #' + str(i + 1)
    newSim.evaluate()
    newSim.stats()
    newSim.evolve_population()
