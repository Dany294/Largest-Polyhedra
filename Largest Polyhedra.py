# BY DANIEL ARANDA, JIMENA CAMPOS AND HANCEL BORREGO
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
plt.rcParams["figure.figsize"] = (15, 5)


#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------


# Generates n points on the unit sphere
def n_random_sphere_points(npoints):
    list_of_points = []

    angle_theta = np.pi * np.random.rand(npoints)
    angle_phi = 2 * np.pi * np.random.rand(npoints)
    
    for i in range(npoints):
        provisional = []
        provisional.append(np.sin(angle_theta[i]) * np.cos(angle_phi[i]))
        provisional.append(np.sin(angle_theta[i]) * np.sin(angle_phi[i]))
        provisional.append(np.cos(angle_theta[i]))
        list_of_points.append(provisional)
        
    return np.array(list_of_points)

# Calculates volume 
def volume_calculator(points):
    vol = sp.spatial.ConvexHull(points).volume
    return vol

# Calculates area
def area_calculator(points):
    area = sp.spatial.ConvexHull(points).area
    return area

# Perturbs the points slightly (still on the unit sphere)
def perturb(points, scale):
    perturbed_points = []
    for point in points:
        noise = np.random.normal(0, scale, 3) # add noise that can be big or small depending on "scale", in 3 dimensions
        new_point = point + noise
        new_point /= np.linalg.norm(new_point)  # divide by the norm to make sure the new point is in the unit sphere
        perturbed_points.append(new_point)
    return np.array(perturbed_points)


#--------------------------------------------------------------------------------------------------------------

# Initial Parameters 
initial = n_random_sphere_points(10)
num_iter = 10000 #number of iterations for the method of simmulated annealing
initial_temperature = 1
cooling_rate = 0.9
scale = 0.005 # measure of the magnitude of the perturbations


#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------


# Searching for configurations with largest volume using simmulated annealing
def find_max_vol(num_iter, initial, initial_temperature,cooling_rate): 
    temperature = initial_temperature 
    
    current_best_points = initial
    current_best_volume = volume_calculator(initial)
    volumes_track = [current_best_volume]

    for i in range(num_iter):
        # perturbs initial points
        pertubed_points = perturb(current_best_points, scale)
        new_volume = volume_calculator(pertubed_points)
        
        delta_vol = new_volume - current_best_volume

        # chooses the options with more volume, and sometimes (depending on the temperature) chooses nonoptimal configurations so it does not get stuck
        if (delta_vol > 0) or (np.random.rand() < np.exp(delta_vol/temperature)):
            current_best_volume = new_volume
            current_best_points = pertubed_points
            volumes_track.append(current_best_volume)
        temperature *= cooling_rate # the tempeture decreases so each time it is more probable to choose a good configuration

    return current_best_points, current_best_volume, volumes_track


# Results for volume
solution = find_max_vol(num_iter,initial,initial_temperature,cooling_rate)
volumes_track = solution[2]
current_best_points, current_best_volume = solution[0],solution[1]

print("best volume:",current_best_volume)
print("best points:", current_best_points)

#--------------------------------------------------------------------------------------------------------------

# First plot, for the volume
plt.subplot(121)
plt.plot(range(len(volumes_track)), volumes_track, label='volume')
plt.grid(True)
plt.xlabel("Number of iterations")
plt.ylabel("Volume of the configuration")
plt.title("Search for the largest 8-point polyhedra")


#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------


# Searching for configurations with the most area using simmulated annealing
def find_max_area(num_iter, initial, initial_temperature,cooling_rate):
    temperature = initial_temperature
    
    current_best_points = initial
    current_best_area = area_calculator(initial)
    areas_track = [current_best_area]

    for i in range(num_iter):

        # perturb initial points
        pertubed_points = perturb(current_best_points, scale)
        new_area = area_calculator(pertubed_points)
        
        delta_area = new_area - current_best_area

        if (delta_area > 0) or (np.random.rand() < np.exp(delta_area/temperature)):
            current_best_area = new_area
            current_best_points = pertubed_points
            areas_track.append(current_best_area)
            
        temperature *= cooling_rate

    return current_best_points, current_best_area, areas_track

# Results for the area
solution_area = find_max_area(num_iter,initial,initial_temperature,cooling_rate)
areas_track = solution_area[2]
current_best_points_area, current_best_area = solution_area[0],solution_area[1]

print("best area:",current_best_area)
print("best points for area:",current_best_points_area)

#--------------------------------------------------------------------------------------------------------------

# Second plot, for the area
plt.subplot(122) 
plt.plot(range(len(areas_track)), areas_track, label='area')
plt.xlabel("Number of iterations")
plt.ylabel("Area of the configuration")
plt.title("Search for the 8-point polyhedron with the most area")
plt.grid(True)
plt.show()
