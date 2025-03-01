import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import scipy.signal

class AntColonySimulation:
    def __init__(self, width=50, height=50, n_ants=20, evaporation_rate=0.05, diffusion_rate=0.1):
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

        # Preallocate visualization data
        self.rgb_data = np.zeros((height, width, 3))

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
        # Process ant movement (only update a subset of ants per frame)
        for ant in self.ants[:10]:  # Only update 10 ants per frame
            self._move_ant(ant)

        # Update pheromones
        self._update_pheromones()

    def _move_ant(self, ant):
        # Extract ant properties to local variables
        pos = ant['pos']
        direction = ant['direction']
        has_food = ant['has_food']
        state = ant['state']
        i, j = pos

        # Deposit pheromone
        deposit = 2.0 * self.pheromone_deposit if has_food else 0.5 * self.pheromone_deposit
        self.pheromone[i, j] += deposit

        # Check if at nest with food
        if has_food and pos == self.nest:
            has_food = False
            state = 'exploring'
            self.food_found += 1

        # Check if found food
        elif not has_food and self.food[i, j]:
            has_food = True
            state = 'returning'
            direction = (direction + 4) % 8  # Immediate U-turn

        # Choose next direction
        if state == 'returning':
            direction = self._calculate_nest_direction(pos, direction)
        else:
            if random.random() < 0.8:
                direction = self._follow_pheromones(pos, direction)
            else:
                direction = (direction + random.randint(-1, 1)) % 8

        # Move ant
        di, dj = self.directions[direction]
        new_i = i + di
        new_j = j + dj

        # Boundary checking
        if 0 <= new_i < self.height and 0 <= new_j < self.width:
            pos = (new_i, new_j)

        # Update ant properties
        ant.update({
            'pos': pos,
            'direction': direction,
            'has_food': has_food,
            'state': state
        })

    def _calculate_nest_direction(self, pos, current_dir):
        """Returns new direction instead of modifying ant dict"""
        i, j = pos
        nest_i, nest_j = self.nest
        di = nest_i - i
        dj = nest_j - j

        # Determine best direction based on di, dj
        if di == 0:
            base_dir = 2 if dj > 0 else 6
        elif dj == 0:
            base_dir = 4 if di > 0 else 0
        else:
            if di > 0:
                base_dir = 3 if dj > 0 else 5
            else:
                base_dir = 1 if dj > 0 else 7

        # Add randomness
        if random.random() < 0.2:
            base_dir = (base_dir + random.randint(-1, 1)) % 8

        return base_dir

    def _follow_pheromones(self, pos, current_dir):
        """Returns new direction instead of modifying ant dict"""
        i, j = pos
        max_phero = -1
        best_dir = current_dir

        for dir_idx, (di, dj) in enumerate(self.directions):
            ni, nj = i + di, j + dj
            if 0 <= ni < self.height and 0 <= nj < self.width:
                if self.pheromone[ni, nj] > max_phero:
                    max_phero = self.pheromone[ni, nj]
                    best_dir = dir_idx

        return best_dir if (max_phero > 0 and random.random() < 0.8) else \
               (current_dir + random.randint(-1, 1)) % 8

    def _update_pheromones(self):
        # Evaporation
        self.pheromone *= (1 - self.evaporation_rate)

        # Simplified diffusion (average with immediate neighbors)
        kernel = np.array([[0, 1, 0],
                           [1, 0, 1],
                           [0, 1, 0]]) / 4.0
        self.pheromone = (1 - self.diffusion_rate) * self.pheromone + \
                         self.diffusion_rate * scipy.signal.convolve2d(
                             self.pheromone, kernel, mode='same', boundary='wrap')

    def get_visualization_data(self):
        # Reset to black
        self.rgb_data[:, :, :] = 0

        # Add pheromone as blue channel
        normalized_pheromone = self.pheromone / (np.max(self.pheromone) + 0.01)
        self.rgb_data[:, :, 2] = normalized_pheromone

        # Add food as green
        self.rgb_data[:, :, 1] = self.food.astype(float)

        # Add nest as red
        self.rgb_data[self.nest[0], self.nest[1], 0] = 1.0

        # Add ants
        for ant in self.ants:
            i, j = ant['pos']
            if ant['has_food']:
                self.rgb_data[i, j, :2] = 1.0  # Yellow
            else:
                self.rgb_data[i, j, 0] = 1.0  # Red

        return self.rgb_data


# Run simulation with animation
def run_simulation():
    # Parameters
    width, height = 50, 50  # Reduced grid size
    n_ants = 20  # Reduced number of ants
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
        simulation.update()
        img.set_array(simulation.get_visualization_data())
        food_text.set_text(f'Food collected: {simulation.food_found}')
        return img, food_text

    # Create animation
    ani = FuncAnimation(fig, update, frames=200, interval=100, blit=True)  # Slower but smoother
    plt.tight_layout()
    plt.show()

    return simulation


if __name__ == "__main__":
    run_simulation()