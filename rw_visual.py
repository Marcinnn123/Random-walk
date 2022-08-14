import matplotlib.pyplot as plt
from random_walk import RandomWalk


rw = RandomWalk(1000)
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15,9), dpi=218)
points_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c= points_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
ax.scatter(rw.x_values[0], rw.y_values[0], c= "Green", s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c= 'red', s=100)

plt.show()
  