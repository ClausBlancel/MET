import matplotlib.pyplot as plt

# Read the values from the text file
with open('results.txt', 'r') as file:
    lines = file.readlines()

# Convert the lines to a list of float values
values = [float(line.strip()) for line in lines]

# Create a list of hours from 0 to 23
hours = list(range(24))

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(hours, values, marker='o', linestyle='-')
plt.title('Mean Response Time Over the Day')
plt.xlabel('Time')
plt.ylabel('Mean Response Time (seconds)')
plt.xlim(0, 23)
plt.ylim(0, 1)
plt.grid(True)

# Enregistre la figure au format png
plt.savefig('response_time_plot_quantic.png')