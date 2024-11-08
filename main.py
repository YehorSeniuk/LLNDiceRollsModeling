import numpy as np
import matplotlib.pyplot as plt

# Set the number of dice rolls
num_rolls = 10000

# Generate random numbers from 1 to 6 (simulating dice rolls)
dice_rolls = np.random.randint(1, 7, size=num_rolls)

# Calculate the cumulative mean
cumulative_mean = np.cumsum(dice_rolls) / np.arange(1, num_rolls + 1)

# The theoretical expectation for a dice roll (from 1 to 6) is 3.5
expected_value = 3.5

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(cumulative_mean, label='Cumulative Mean')
plt.axhline(y=expected_value, color='r', linestyle='--', label='Theoretical Expectation')
plt.xlabel('Number of Rolls')
plt.ylabel('Mean Value')
plt.title('Law of Large Numbers for Dice Rolls')
plt.legend()
plt.grid(True)
plt.show()

