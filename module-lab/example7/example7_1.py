import matplotlib.pyplot as plt
import random

class Island(object):
    def __init__(self, n, prey_count=0, predator_count=0):
        """Initialize grid to all 0's, then fill with animals"""
        self.grid_size = n
        self.grid = []
        for i in range(n):
            row = [0] * n  # row is a list of n zeros
            self.grid.append(row)
        self.init_animals(prey_count, predator_count)

    def size(self):
        """Return size of the island: one dimension."""
        return self.grid_size

    def animal(self, x, y):
        """Return animal at location (x, y)"""
        if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
            return self.grid[x][y]
        else:
            return -1  # outside island boundary

    def init_animals(self, prey_count, predator_count):
        """Put some initial animals on the island"""
        count = 0
        while count < prey_count:
            x = random.randint(0, self.grid_size - 1)
            y = random.randint(0, self.grid_size - 1)
            if not self.animal(x, y):
                new_prey = Prey(island=self, x=x, y=y)
                count += 1
                self.register(new_prey)
        count = 0
        while count < predator_count:
            x = random.randint(0, self.grid_size - 1)
            y = random.randint(0, self.grid_size - 1)
            if not self.animal(x, y):
                new_predator = Predator(island=self, x=x, y=y)
                count += 1
                self.register(new_predator)

    def register(self, animal):
        """Register animal with island, i.e., put it at the animal's coordinates"""
        x = animal.x
        y = animal.y
        self.grid[x][y] = animal

    def remove(self, animal):
        """Remove animal from the island"""
        self.grid[animal.x][animal.y] = 0

    def __str__(self):
        """String representation for printing.
        (0,0) will be in the lower-left corner.
        """
        s = ""
        for j in range(self.grid_size - 1, -1, -1):  # print row size−1 first
            for i in range(self.grid_size):  # each row starts at 0
                if not self.grid[i][j]:
                    s += "{:<2s}".format('. ')
                else:
                    s += "{:<2s}".format(str(self.grid[i][j]) + " ")
            s += "\n"
        return s


class Animal(object):
    def __init__(self, island, x=0, y=0, s="A"):
        self.island = island
        self.name = s
        self.x = x
        self.y = y

    def __str__(self):
        return self.name

    def move(self):
        """Move to an open, neighboring position."""
        offset = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
        for dx, dy in offset:
            x = self.x + dx
            y = self.y + dy
            if self.island.animal(x, y) == 0:
                self.island.remove(self)
                self.x = x
                self.y = y
                self.island.register(self)
                break


class Prey(Animal):
    breed_time = 3  # default breed time for all Prey instances

    def __init__(self, island, x=0, y=0, s="O"):
        super().__init__(island, x, y, s)
        self.breed_clock = Prey.breed_time

    def clock_tick(self):
        self.breed_clock -= 1

    def breed(self):
        if self.breed_clock <= 0:
            self.breed_clock = Prey.breed_time
            offset = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # adjacent cells
            for dx, dy in offset:
                x = self.x + dx
                y = self.y + dy
                if self.island.animal(x, y) == 0:
                    new_prey = Prey(self.island, x, y)
                    self.island.register(new_prey)
                    break

class Predator(Animal):
    breed_time = 6  # default breed time for all Predator instances
    starve_time = 3  # default starve time for all Predator instances

    def __init__(self, island, x=0, y=0, s="X"):
        super().__init__(island, x, y, s)
        self.starve_clock = Predator.starve_time
        self.breed_clock = Predator.breed_time

    def clock_tick(self):
        self.breed_clock -= 1
        self.starve_clock -= 1
        if self.starve_clock <= 0:
            self.island.remove(self)

    def check_grid(self, prey_class):
        """Check neighboring cells for prey."""
        offset = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
        for dx, dy in offset:
            x = self.x + dx
            y = self.y + dy
            if isinstance(self.island.animal(x, y), prey_class):
                return (x, y)
        return None

    def eat(self):
        """Predator looks for prey in neighboring cells to eat."""
        location = self.check_grid(Prey)
        if location:
            prey = self.island.animal(location[0], location[1])
            self.island.remove(prey)
            self.island.remove(self)
            self.x = location[0]
            self.y = location[1]
            self.island.register(self)
            self.starve_clock = Predator.starve_time

    def breed(self):
        if self.breed_clock <= 0:
            self.breed_clock = Predator.breed_time
            offset = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in offset:
                x = self.x + dx
                y = self.y + dy
                if self.island.animal(x, y) == 0:
                    new_predator = Predator(self.island, x, y)
                    self.island.register(new_predator)
                    break

def main(predator_breed_time, predator_starve_time, initial_predators,
         prey_breed_time, initial_prey, size, ticks):
    Predator.breed_time = predator_breed_time
    Predator.starve_time = predator_starve_time
    Prey.breed_time = prey_breed_time

    # Lists to store population counts
    prey_population = []
    predator_population = []

    isle = Island(size, initial_prey, initial_predators)

    initial_prey_count, initial_predator_count = initial_prey, initial_predators
    prey_population.append(initial_prey_count)
    predator_population.append(initial_predator_count)

    #    print(isle)

#    for _ in range(ticks):
#        for x in range(size):
#            for y in range(size):
#                animal = isle.animal(x, y)
    #                if animal:
    #                if isinstance(animal, Predator):
    #                   animal.eat()
    #               animal.move()
    #               animal.breed()
    #               animal.clock_tick()
    #   print(isle)

    for _ in range(1, ticks):
        prey_count = 0
        predator_count = 0

        # Iterate through each cell to update animals
        for x in range(size):
            for y in range(size):
                animal = isle.animal(x, y)
                if animal:
                    if isinstance(animal, Prey):
                        prey_count += 1
                    elif isinstance(animal, Predator):
                        predator_count += 1
                        animal.eat()  # Predator eats prey if available
                    animal.move()
                    animal.breed()
                    animal.clock_tick()

        # Store the population counts for this tick
        prey_population.append(prey_count)
        predator_population.append(predator_count)

        # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.plot(range(ticks), prey_population, color='cyan', label='Prey Population')
    plt.plot(range(ticks), predator_population, color='black', label='Predator Population')
    plt.xlabel('Time (Ticks)')
    plt.ylabel('Population Size')
    plt.title('Graph of Population Sizes Using Our Simulation')
    plt.legend()
    plt.show()

# Run the simulation with specified parameters
main(
    predator_breed_time=6,
    predator_starve_time=3,
    initial_predators=10,
    prey_breed_time=3,
    initial_prey=50,
    size=10,
    ticks=300
)
