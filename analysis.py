"""
Simple data analysis script for reproducibility demonstration.
"""

import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(42)
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.1, 100)

# Create visualization
plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.6, label='Data points')
plt.plot(x, np.sin(x), 'r-', linewidth=2, label='True function')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Reproducible Data Analysis')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('output.png', dpi=100, bbox_inches='tight')
print("Analysis complete! Plot saved as output.png")
