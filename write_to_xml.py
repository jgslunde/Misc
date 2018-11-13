from AST2000SolarSystemViewer import AST2000SolarSystemViewer
import numpy as np

m2AU = 6.684E-12

def write_to_xml(positions, time_array, number_of_planets, seed=666):
    if np.shape(positions) == (number_of_planets, len(time_array), 3):
        pass
    elif np.shape(positions) == (len(time_array), 3) and number_of_planets == 1:
        positions = np.array([positions,])
    else:
        raise ValueError("WRONG SHAPE!")
    SS = AST2000SolarSystemViewer(seed, number_of_planets)
    planet_pos = np.zeros((2, number_of_planets, len(time_array)))
    for i in range(2):
        for j in range(number_of_planets):
            for k in range(len(time_array)):
                planet_pos[i,j,k] = positions[j,k,i]*m2AU
    SS.orbit_xml(planet_pos, time_array)