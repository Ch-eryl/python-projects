
# Base class representing a planet with common astronomical properties
class Planet:
    def __init__(self, name, diameter, distance_from_sun, number_of_moons, gravity_strength, 
                 high_temperature, low_temperature, orbital_period):
        self.__name = name
        self.__diameter = diameter
        self.__distance_from_sun = distance_from_sun
        self.__number_of_moons = number_of_moons
        self.__gravity_strength = gravity_strength
        self.__high_temperature = high_temperature
        self.__low_temperature = low_temperature
        self.__orbital_period = orbital_period

# Getters
    def get_name(self):
        return self.__name

    def get_diameter(self):
        return self.__diameter

    def get_distance_from_sun(self):
        return self.__distance_from_sun

    def get_number_of_moons(self):
        return self.__number_of_moons

    def get_gravity_strength(self):
        return self.__gravity_strength

    def get_high_temperature(self):
        return self.__high_temperature

    def get_low_temperature(self):
        return self.__low_temperature

    def get_orbital_period(self):
        return self.__orbital_period

# Setters
    def set_name(self, new_name):
        self.__name = new_name

    def set_diameter(self, new_diameter):
        if new_diameter > 0:
            self.__diameter = new_diameter

    def set_distance_from_sun(self, new_distance):
        if new_distance > 0:
            self.__distance_from_sun = new_distance

    def set_number_of_moons(self, new_moons):
        if new_moons >= 0:
            self.__number_of_moons = new_moons

    def set_gravity_strength(self, new_gravity):
        if new_gravity > 0:
            self.__gravity_strength = new_gravity

    def set_high_temperature(self, new_high_temp):
        self.__high_temperature = new_high_temp

    def set_low_temperature(self, new_low_temp):
        self.__low_temperature = new_low_temp

    def set_orbital_period(self, new_period):
        if new_period > 0:
            self.__orbital_period = new_period

# Methods
    def orbit(self):
        return f"{self.__name} orbits the sun in {self.__orbital_period} Earth days."

    def rotate(self):
        return f"{self.__name} is rotating on its axis."

    def support_life(self):
        return f"{self.__name} may or may not support life."

    def __str__(self):
        return (f"Planet {self.__name}: {self.__diameter} km diameter, "
                f"{self.__distance_from_sun} AU from sun, {self.__number_of_moons} moons")

# Class representing rocky, Earth-like planets
class TerrestrialPlanet(Planet):
    def __init__(self, name, diameter, distance_from_sun, number_of_moons, gravity_strength, 
                 high_temperature, low_temperature, orbital_period, surface_type):
        super().__init__(name, diameter, distance_from_sun, number_of_moons, gravity_strength,
                        high_temperature, low_temperature, orbital_period)
        self.__surface_type = surface_type

    def get_surface_type(self):
        return self.__surface_type

    def set_surface_type(self, new_surface_type):
        if new_surface_type.lower() in ['rocky', 'volcanic', 'barren', 'icy']:
            self.__surface_type = new_surface_type

    def break_down_rocks(self):
        return f"{self.get_name()}'s {self.__surface_type} surface is weathering over time."

    def __str__(self):
        return super().__str__() + f", Surface: {self.__surface_type}"

# Class representing planets in the habitable zone capable of supporting life
class GoldilocksPlanet(TerrestrialPlanet):
    def __init__(self, name, diameter, distance_from_sun, number_of_moons, gravity_strength, 
                 high_temperature, low_temperature, orbital_period, surface_type, current_population):
        super().__init__(name, diameter, distance_from_sun, number_of_moons, gravity_strength,
                        high_temperature, low_temperature, orbital_period, surface_type)
        self.__current_population = current_population

    def get_current_population(self):
        return self.__current_population

    def set_current_population(self, new_population):
        if new_population >= 0:
            self.__current_population = new_population

    def sustain_human_life(self):
        if -50 <= self.get_low_temperature() <= 50 and -50 <= self.get_high_temperature() <= 50:
            return (f"{self.get_name()} can sustain human life with ideal conditions. "
                    f"Current population: {self.__current_population:,}")
        return f"{self.get_name()} has borderline habitable conditions."

    def __str__(self):
        return super().__str__() + f", Population: {self.__current_population:,}"

# Class representing gas giant planets
class GasGiant(Planet):
    def __init__(self, name, diameter, distance_from_sun, number_of_moons, gravity_strength, 
                 high_temperature, low_temperature, orbital_period, atmospheric_composition):
        super().__init__(name, diameter, distance_from_sun, number_of_moons, gravity_strength,
                        high_temperature, low_temperature, orbital_period)
        self.__atmospheric_composition = atmospheric_composition

    def get_atmospheric_composition(self):
        return self.__atmospheric_composition

    def set_atmospheric_composition(self, new_composition):
        self.__atmospheric_composition = new_composition

    def generate_gravity(self):
        return f"{self.get_name()} generates strong gravity with {self.__gravity_strength}g force."

    def __str__(self):
        return super().__str__() + f", Atmosphere: {self.__atmospheric_composition}"

# Class representing ice giant planets
class IceGiant(Planet):
    def __init__(self, name, diameter, distance_from_sun, number_of_moons, gravity_strength, 
                 high_temperature, low_temperature, orbital_period, core_composition):
        super().__init__(name, diameter, distance_from_sun, number_of_moons, gravity_strength,
                        high_temperature, low_temperature, orbital_period)
        self.__core_composition = core_composition

    def get_core_composition(self):
        return self.__core_composition

    def set_core_composition(self, new_core):
        self.__core_composition = new_core

    def have_extreme_weather(self):
        return f"{self.get_name()} experiences extreme weather with its {self.__core_composition} core."

    def __str__(self):
        return super().__str__() + f", Core: {self.__core_composition}"

# Class representing dwarf planets
class DwarfPlanet(Planet):
    def __init__(self, name, diameter, distance_from_sun, number_of_moons, gravity_strength, 
                 high_temperature, low_temperature, orbital_period, orbit_type):
        super().__init__(name, diameter, distance_from_sun, number_of_moons, gravity_strength,
                        high_temperature, low_temperature, orbital_period)
        self.__orbit_type = orbit_type

    def get_orbit_type(self):
        return self.__orbit_type

    def set_orbit_type(self, new_orbit_type):
        if new_orbit_type.lower() in ['eccentric', 'resonant', 'classical']:
            self.__orbit_type = new_orbit_type

    def __str__(self):
        return super().__str__() + f", Orbit: {self.__orbit_type}"

# Class representing terrestrial planets with active exploration
class ExploredTerrestrialPlanet(TerrestrialPlanet):
    def __init__(self, name, diameter, distance_from_sun, number_of_moons, gravity_strength, 
                 high_temperature, low_temperature, orbital_period, surface_type, current_rover_count):
        super().__init__(name, diameter, distance_from_sun, number_of_moons, gravity_strength,
                        high_temperature, low_temperature, orbital_period, surface_type)
        self.__current_rover_count = current_rover_count

    def get_current_rover_count(self):
        return self.__current_rover_count

    def set_current_rover_count(self, new_count):
        if new_count >= 0:
            self.__current_rover_count = new_count

    def receive_rover(self):
        self.__current_rover_count += 1
        return f"New rover deployed to {self.get_name()}. Total rovers: {self.__current_rover_count}"

    def __str__(self):
        return super().__str__() + f", Rovers: {self.__current_rover_count}"

# Helper function to validate user input
def get_valid_input(prompt, input_type=float, min_val=None, max_val=None):
    while True:
        try:
            value = input_type(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be at most {max_val}")
                continue
            return value
        except ValueError:
            print(f"Please enter a valid {input_type.__name__}")

# Create a planet instance based on user input
def create_planet():
    print("\nPlanet Creation System")
    print("1. Generic Planet")
    print("2. Terrestrial Planet")
    print("3. Goldilocks Planet")
    print("4. Gas Giant")
    print("5. Ice Giant")
    print("6. Dwarf Planet")
    print("7. Explored Terrestrial Planet")
    
    choice = get_valid_input("Select planet type (1-7): ", int, 1, 7)
    
    print("\nEnter planet details:")
    name = input("Name: ").strip()
    diameter = get_valid_input("Diameter (km): ", float, 100)
    distance = get_valid_input("Distance from sun (AU): ", float, 0.1)
    moons = get_valid_input("Number of moons: ", int, 0)
    gravity = get_valid_input("Gravity strength (Earth=1): ", float, 0.01)
    high_temp = get_valid_input("High temperature (°C): ", float)
    low_temp = get_valid_input("Low temperature (°C): ", float)
    orbital_period = get_valid_input("Orbital period (Earth days): ", float, 0.1)

# Generic Planet
    if choice == 1:
        return Planet(name, diameter, distance, moons, gravity, high_temp, low_temp, orbital_period)
        
# Terrestrial Planet
    elif choice == 2: 
        surface = input("Surface type (rocky/volcanic/barren/icy): ").lower()
        while surface not in ['rocky', 'volcanic', 'barren', 'icy']:
            print("Invalid surface type")
            surface = input("Surface type (rocky/volcanic/barren/icy): ").lower()
        return TerrestrialPlanet(name, diameter, distance, moons, gravity, high_temp, 
                               low_temp, orbital_period, surface)
        
 # Goldilocks Planet
    elif choice == 3:
        surface = input("Surface type (rocky/volcanic/barren/icy): ").lower()
        while surface not in ['rocky', 'volcanic', 'barren', 'icy']:
            print("Invalid surface type")
            surface = input("Surface type (rocky/volcanic/barren/icy): ").lower()
        population = get_valid_input("Current population: ", int, 0)
        return GoldilocksPlanet(name, diameter, distance, moons, gravity, high_temp,
                              low_temp, orbital_period, surface, population)
# Gas Giant
    elif choice == 4:  
        atmosphere = input("Atmospheric composition: ").strip()
        return GasGiant(name, diameter, distance, moons, gravity, high_temp,
                      low_temp, orbital_period, atmosphere)
# Ice Giant    
    elif choice == 5: 
        core = input("Core composition: ").strip()
        return IceGiant(name, diameter, distance, moons, gravity, high_temp,
                      low_temp, orbital_period, core)
# Dwarf Planet    
    elif choice == 6:  
        orbit = input("Orbit type (eccentric/resonant/classical): ").lower()
        while orbit not in ['eccentric', 'resonant', 'classical']:
            print("Invalid orbit type")
            orbit = input("Orbit type (eccentric/resonant/classical): ").lower()
        return DwarfPlanet(name, diameter, distance, moons, gravity, high_temp,
                         low_temp, orbital_period, orbit)
    
# Explored Terrestrial Planet   
    elif choice == 7: 
        surface = input("Surface type (rocky/volcanic/barren/icy): ").lower()
        while surface not in ['rocky', 'volcanic', 'barren', 'icy']:
            print("Invalid surface type")
            surface = input("Surface type (rocky/volcanic/barren/icy): ").lower()
        rovers = get_valid_input("Current rover count: ", int, 0)
        return ExploredTerrestrialPlanet(name, diameter, distance, moons, gravity, high_temp,
                                       low_temp, orbital_period, surface, rovers)


# Return a list of available actions for the planet
def get_available_actions(planet):

    actions = {
        1: ("Orbit", planet.orbit),
        2: ("Rotate", planet.rotate),
        3: ("Check life support", planet.support_life)
    }
    
    if isinstance(planet, TerrestrialPlanet):
        actions[4] = ("Break down rocks", planet.break_down_rocks)
    if isinstance(planet, GoldilocksPlanet):
        actions[5] = ("Sustain human life", planet.sustain_human_life)
    if isinstance(planet, GasGiant):
        actions[6] = ("Generate gravity", planet.generate_gravity)
    if isinstance(planet, IceGiant):
        actions[7] = ("Experience extreme weather", planet.have_extreme_weather)
    if isinstance(planet, ExploredTerrestrialPlanet):
        actions[8] = ("Receive rover", planet.receive_rover)
    
    return actions


# Perform selected action on the planet
def perform_planet_action(planet):

    actions = get_available_actions(planet)
    
    print(f"\nAvailable actions for {planet.get_name()}:")
    for num, (desc, _) in sorted(actions.items()):
        print(f"{num}. {desc}")
    
    choice = get_valid_input("\nSelect action: ", int, 1, max(actions.keys()))
    
    if choice in actions:
        _, action_func = actions[choice]
        print("\n" + action_func())
    else:
        print("Invalid action for this planet type.")
        

# Main program function
# Commented-out instances from previous weeks
#proxima_centauri_b = Planet("Proxima Centauri b", 15000, 4.24, 0, 1.2, 30, -30, 11.2)
#venus = TerrestrialPlanet("Venus", 12104, 0.72, 0, 0.9, 464, -45, 225, "Rocky")
#jupiter = GasGiant("Jupiter", 139820, 5.20, 79, 2.5, -145, -145, 4333, "Hydrogen and Helium")
#neptune = IceGiant("Neptune", 49244, 30.07, 14, 1.1, -200, -200, 60190, "Rock and Ice")
#pluto = DwarfPlanet("Pluto", 2376, 39.48, 5, 0.62, -225, -225, 90560, "Eccentric")
#mars = ExploredTerrestrialPlanet("Mars", 6779, 1.52, 2, 0.38, 20, -153, 687, "Rocky", 3)
def main():
    
    print("\n" + "="*50)
    print("PLANET SYSTEM SIMULATOR".center(50))
    print("="*50)
    
    while True:
        planet = create_planet()
        if planet is None:
            continue
        
        print(f"\nCreated planet:\n{planet}")
        
        while True:
            perform_planet_action(planet)
            
            another = input("\nPerform another action? (y/n): ").lower()
            if another != 'y':
                break
        
        another = input("\nCreate another planet? (y/n): ").lower()
        if another != 'y':
            print("\nExiting Planet System Simulator. Goodbye!")
            break


if __name__ == "__main__":
    main()
