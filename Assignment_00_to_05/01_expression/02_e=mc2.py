# Write a program that continually reads in mass from the user and then outputs the equivalent
# energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for 
# mass, and C is the speed of light:

def calculate_energy(mass):
    # Speed of light constant (meters per second)
    C = 299792458
    # Einstein's formula: E = m * c^2
    energy = mass * (C ** 2)
    return energy

# Get user input for mass
mass = float(input("Enter kilos of mass: "))

# Calculate energy
energy = calculate_energy(mass)

# Display the result
print("e = m * C^2...\n")
print(f"m = {mass} kg")
print(f"C = {299792458} m/s")
print(f"{energy} joules of energy!")