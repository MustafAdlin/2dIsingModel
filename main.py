import random
import math
import matplotlib.pyplot as plt

# Set up the lattice size
N = 30
# Set the temperature
kT = 1
# Set the number of steps to run the simulation
num_steps = 10000

# Set up the initial lattice configuration
lattice = [[random.choice([-1, 1]) for i in range(N)] for j in range(N)]

# Plot the Initial Lattice
plt.imshow(lattice, cmap="hot", interpolation="nearest")
plt.title("Initial Lattice")
plt.show()

# Calculate the energy of the system
def calculate_energy(lattice):
    energy = 0
    for i in range(N):
        for j in range(N):
            spin = lattice[i][j]
            neighbors = [lattice[(i+1)%N][j], lattice[i][(j+1)%N], lattice[(i-1)%N][j], lattice[i][(j-1)%N]]
            for neighbor in neighbors:
                energy += -1 * spin * neighbor
    return energy/2

# Print the initial energy
print("Initial Energy", calculate_energy(lattice))

initial_energy = calculate_energy(lattice)

def metropolis_step(lattice, kT):
    # Choose a random lattice site
    i = random.randint(0, N-1)
    j = random.randint(0, N-1)

    # Calculate the energy change if the spin is flipped
    spin = lattice[i][j]
    neighbors = [lattice[(i+1)%N][j], lattice[i][(j+1)%N], lattice[(i-1)%N][j], lattice[i][(j-1)%N]]
    energy_diff = 2 * spin * sum(neighbors)

    # If the energy change is negative, accept the new configuration
    if energy_diff < 0:
        lattice[i][j] = -spin
    # If the energy change is positive, accept with a probability based on the temperature
    elif random.random() < math.exp(-energy_diff / kT):
        lattice[i][j] = -spin

# Perform the simulation
energies = [initial_energy]
for step in range(num_steps):
    metropolis_step(lattice, kT)
    energies.append(calculate_energy(lattice))

# Print the final lattice configuration and energy
print("Final lattice:")
for row in lattice:
    print(row)
print("Final energy:", energies[-1])

plt.imshow(lattice, cmap="hot", interpolation="nearest")
plt.title("Final Lattice")
plt.show()

plt.plot(energies)
plt.xlabel('Time')
plt.ylabel('Energy')
plt.title('Energy vs. Time')
plt.show()