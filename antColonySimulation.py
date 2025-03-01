import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random


class AntColonySimulation:
    def __init__(self, width=50, height=50, n_ants=50, evaporation_rate=0.05, diffusion_rate=0.1):
        # Environment
        self.width = width
        self.height = height
        self.pheromone = np.zeros((height, width))
        self.food = np.zeros((height, width), dtype=bool)
        self.nest = None

        # Ants
        self.n_ants = n_ants
        self.ants = []

        # Parameters
        self.evaporation_rate = evaporation_rate
        self.diffusion_rate = diffusion_rate
        self.pheromone_deposit = 1.0
        self.food_found = 0

        # Directions: N, NE, E, SE, S, SW, W, NW
        self.directions = [
            (-1, 0), (-1, 1), (0, 1), (1, 1),
            (1, 0), (1, -1), (0, -1), (-1, -1)
        ]

    def setup(self):
        # Create nest at center
        self.nest = (self.height // 2, self.width // 2)

        # Create food sources
        food_radius = 5
        # Food source 1 - upper right
        center1 = (self.height // 4, 3 * self.width // 4)
        for i in range(self.height):
            for j in range(self.width):
                if ((i - center1[0]) ** 2 + (j - center1[1]) ** 2) < food_radius ** 2:
                    self.food[i, j] = True

        # Food source 2 - lower left
        center2 = (3 * self.height // 4, self.width // 4)
        for i in range(self.height):
            for j in range(self.width):
                if ((i - center2[0]) ** 2 + (j - center2[1]) ** 2) < food_radius ** 2:
                    self.food[i, j] = True

        # Initialize ants
        for _ in range(self.n_ants):
            self.ants.append({
                'pos': self.nest,
                'direction': random.randint(0, 7),  # Random initial direction
                'has_food': False,
                'state': 'exploring'  # 'exploring' or 'returning'
            })

    def update(self):
        # Process ant movement
        for ant in self.ants:
            self._move_ant(ant)

        # Update pheromones
        self._update_pheromones()

    def _move_ant(self, ant):
        i, j = ant['pos']

        # Deposit pheromone
        if ant['has_food']:
            self.pheromone[i, j] += self.pheromone_deposit * 2  # Stronger trail when carrying food
        else:
            self.pheromone[i, j] += self.pheromone_deposit * 0.5

        # Check if at nest with food
        if ant['has_food'] and ant['pos'] == self.nest:
            ant['has_food'] = False
            ant['state'] = 'exploring'
            self.food_found += 1

        # Check if found food
        elif not ant['has_food'] and self.food[i, j]:
            ant['has_food'] = True
            ant['state'] = 'returning'
            # Turn around when food is found
            ant['direction'] = (ant['direction'] + 4) % 8

        # Choose next direction
        if ant['state'] == 'returning':
            # When returning, head towards nest with some randomness
            self._head_towards_nest(ant)
        else:  # exploring
            # Follow pheromones or explore randomly
            if random.random() < 0.8:  # 80% chance to follow pheromones
                self._follow_pheromones(ant)
            else:
                # Random direction change
                ant['direction'] = (ant['direction'] + random.randint(-1, 1)) % 8

        # Move ant
        new_i = i + self.directions[ant['direction']][0]
        new_j = j + self.directions[ant['direction']][1]

        # Boundary checking
        if 0 <= new_i < self.height and 0 <= new_j < self.width:
            ant['pos'] = (new_i, new_j)

    def _head_towards_nest(self, ant):
        i, j = ant['pos']
        nest_i, nest_j = self.nest

        # Determine best direction to head towards nest
        di = nest_i - i
        dj = nest_j - j

        # Determine best direction based on di, dj
        if di == 0 and dj > 0:  # East
            best_dir = 2
        elif di == 0 and dj < 0:  # West
            best_dir = 6
        elif di > 0 and dj == 0:  # South
            best_dir = 4
        elif di < 0 and dj == 0:  # North
            best_dir = 0
        elif di > 0 and dj > 0:  # Southeast
            best_dir = 3
        elif di > 0 and dj < 0:  # Southwest
            best_dir = 5
        elif di < 0 and dj > 0:  # Northeast
            best_dir = 1
        else:  # Northwest
            best_dir = 7

        # Add some randomness (20% chance to deviate)
        if random.random() < 0.2:
            best_dir = (best_dir + random.randint(-1, 1)) % 8

        ant['direction'] = best_dir

    def _follow_pheromones(self, ant):
        i, j = ant['pos']
        max_pheromone = 0
        best_dir = ant['direction']

        # Check pheromone levels in neighboring cells
        for dir_idx, (di, dj) in enumerate(self.directions):
            ni, nj = i + di, j + dj
            if 0 <= ni < self.height and 0 <= nj < self.width:
                if self.pheromone[ni, nj] > max_pheromone:
                    max_pheromone = self.pheromone[ni, nj]
                    best_dir = dir_idx

        # If pheromone found, 80% chance to follow, otherwise continue current direction
        if max_pheromone > 0 and random.random() < 0.8:
            ant['direction'] = best_dir
        else:
            # Random direction change
            ant['direction'] = (ant['direction'] + random.randint(-1, 1)) % 8

    def _update_pheromones(self):
        # Evaporation
        self.pheromone *= (1 - self.evaporation_rate)

        # Diffusion (simple averaging with neighbors)
        new_pheromone = self.pheromone.copy()
        for i in range(1, self.height - 1):
            for j in range(1, self.width - 1):
                # Average with neighbors
                neighbors_avg = (
                                        self.pheromone[i - 1, j] + self.pheromone[i + 1, j] +
                                        self.pheromone[i, j - 1] + self.pheromone[i, j + 1]
                                ) / 4
                # Apply diffusion
                new_pheromone[i, j] = (1 - self.diffusion_rate) * self.pheromone[
                    i, j] + self.diffusion_rate * neighbors_avg

        self.pheromone = new_pheromone

    def get_visualization_data(self):
        # Create RGB representation for visualization
        rgb_data = np.zeros((self.height, self.width, 3))

        # Add pheromone as blue channel
        normalized_pheromone = self.pheromone / (np.max(self.pheromone) + 0.01)  # Avoid div by zero
        rgb_data[:, :, 2] = normalized_pheromone

        # Add food as green
        rgb_data[:, :, 1] = self.food.astype(float)

        # Add nest as red
        nest_i, nest_j = self.nest
        rgb_data[nest_i, nest_j, 0] = 1.0

        # Add ants
        for ant in self.ants:
            i, j = ant['pos']
            if ant['has_food']:
                # Yellow ant (carrying food)
                rgb_data[i, j, 0] = 1.0
                rgb_data[i, j, 1] = 1.0
                rgb_data[i, j, 2] = 0.0
            else:
                # Red ant (searching)
                rgb_data[i, j, 0] = 1.0
                rgb_data[i, j, 1] = 0.0
                rgb_data[i, j, 2] = 0.0

        return rgb_data


# Run simulation with animation
def run_simulation():
    # Add this variable near the parameters
    render_every = 2  # Only render every 2nd simulation update
    frame_counter = 0
    # Parameters
    width, height = 100, 100
    n_ants = 50
    simulation = AntColonySimulation(width, height, n_ants)
    simulation.setup()

    # Setup plot
    fig, ax = plt.subplots(figsize=(8, 8))
    img = ax.imshow(np.zeros((height, width, 3)), origin='upper')
    ax.set_title('Ant Colony Simulation')
    ax.set_axis_off()

    # Text for food count
    food_text = ax.text(0.02, 0.95, '', transform=ax.transAxes, color='white', fontsize=10)

    # Animation function
    def update(frame):
        nonlocal frame_counter
        for _ in range(10):  # Higher steps per frame
         for _ in range(20):  # Run multiple steps per frame for faster simulation
            simulation.update()
            frame_counter += 1

        # Update visualization
        if frame_counter % render_every == 0:
            img.set_array(simulation.get_visualization_data())
            food_text.set_text(f'Food collected: {simulation.food_found}')
        return img, food_text

    # Create animation
    ani = FuncAnimation(fig, update, frames=200, interval=10, blit=True)
    plt.tight_layout()
    plt.show()

    return simulation


if __name__ == "__main__":
    run_simulation()