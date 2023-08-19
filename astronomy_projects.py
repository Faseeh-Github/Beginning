"""
class weight_calculater:
    def __init__(self,weight_on_earth,gravity_of_planet):#constuctor of class with 3 arguments
        self.weight=weight_on_earth                      #initializig two variables
        self.gravity=gravity_of_planet

    def calculate(self):  #Function to calculate weight
        weight=self.weight * self.gravity/9.8  #Formula

        print("The gravity of person on planet is:",weight,"N")

W=float(input("Enter the weight of person on Earth in kg: " )) #This line will get the weight of person on Earth in float or integer
g=float(input("Enter the gravity of planet on which you want to calculate the weight: "))#This line will get the gravity of desired planet from user 

obj=weight_calculater(W,g)

print(obj.calculate())
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

class Star:
    def __init__(self, mass, temperature, luminosity):
        self.mass = mass
        self.temperature = temperature
        self.luminosity = luminosity

def stellar_evolution(time, star):
    # Constants
    solar_mass = 1.989e30  # kg
    solar_luminosity = 3.828e26  # W

    # Stellar evolution equations
    dMdt = -1e-11 * star.mass * solar_mass  # Mass loss rate
    dTdt = -1e6 * (star.luminosity / solar_luminosity) * (star.mass * solar_mass)**(-0.7)  # Temperature change rate
    dLdt = -dMdt * star.luminosity / (star.mass * solar_mass)  # Luminosity change rate

    return [dMdt, dTdt, dLdt]

# Initial conditions
initial_mass = 1.0  # Solar masses
initial_temperature = 5778  # Kelvin (Sun's temperature)
initial_luminosity = 3.828e26  # Watts (Sun's luminosity)

initial_star = Star(initial_mass, initial_temperature, initial_luminosity)

# Time span for simulation (in years)
t_span = (0, 1e10)  # From 0 to 10 billion years

# Solving the differential equations
solution = solve_ivp(stellar_evolution, t_span, [initial_mass, initial_temperature, initial_luminosity],
                    args=(initial_star,), method='RK45', dense_output=True)

# Extracting simulation results
time_values = np.linspace(0, 1e10, num=1000)
mass_values, temperature_values, luminosity_values = solution.sol(time_values)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(time_values, mass_values, label='Mass')
plt.plot(time_values, temperature_values, label='Temperature')
plt.plot(time_values, luminosity_values, label='Luminosity')
plt.xlabel('Time (years)')
plt.ylabel('Values')
plt.title('Stellar Evolution Simulation')
plt.legend()
plt.semilogy()
plt.show()