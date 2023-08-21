
class asteroid:
    def __init__(self, diameter, speed, angle):
        self.diameter = diameter
        self.speed = speed
        self.angle = angle

    def asteroid_density(self, asteroid_material):
        if asteroid_material == "metallic":
            asteroid_density = 6000
        elif asteroid_material == "rocky":
            asteroid_density = 2500
        else:
            print("This type of asteroids do not exist")
            return None
        return asteroid_density
    
    def asteroid_mass(self,asteroid_material):
        asteroid_density = self.asteroid_density(asteroid_material)
        if asteroid_density is not None:
    
           asteroid_radius = self.diameter / 2
           asteroid_volume = (4 / 3) * 3.14159 * (asteroid_radius ** 3)
           return asteroid_volume * asteroid_density
        return None

    def kinetic_energy(self,asteroid_material):
        asteroid_mass = self.asteroid_mass(asteroid_material)
        if asteroid_mass is not None:
            kinetic_energy = 0.5 * asteroid_mass * (self.speed ** 2)
            return kinetic_energy
        return None

    def crater_diameter(self,asteroid_material, k=1.2):
        asteroid_density = self.asteroid_density(asteroid_material)
        if asteroid_density is not None:
            asteroid_volume = (4 / 3) * 3.14159 * ((self.diameter / 2) ** 3)
            crater_diameter = k * (asteroid_density ** (2 / 3)) * (asteroid_volume ** 0.4)
            return crater_diameter
        return None


d = float(input("Enter the diameter of the asteroid in meters : "))
s = float(input("Enter the speed of the asteroid in kilometers per second: "))
a = float(input("Enter the angle at which the asteroid hit the Earth: "))

obj = asteroid(d, s, a)

asteroid_material = input("What type of asteroid is this? Is this metallic or rocky?")

# Call the asteroid_density() method to get the density of the asteroid
obj.asteroid_density(asteroid_material)

# Call the other methods to get the mass, kinetic energy, and crater diameter of the asteroid
asteroid_mass = obj.asteroid_mass(asteroid_material)
kinetic_energy = obj.kinetic_energy(asteroid_material)
crater_diameter = obj.crater_diameter(asteroid_material)

if d<25 and a>45:
    print("That asteroid's size is too small and angle is shallow it will probably burn in air and will not cause any damage")
elif 25>d<30 and a>45:
  print("The asteroid's size is small however it will probably cause any minor distruction such as breaking windows or knocking down power lines.") 

elif asteroid_mass is not None and kinetic_energy is not None and crater_diameter is not None:
        print("The asteroid's size is large and its angle is steeper it will cause too much damage. On hiiting in ocean it might cause a tsunami")
        print("The mass of the asteroid is:", asteroid_mass, "kg")
        print("The kinetic energy release when asteroid hit the Earth is:", kinetic_energy, "Joule")
        print("The diameter of the carter form when asteroid hits the Earth is:", crater_diameter, "meters")


