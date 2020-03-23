import pygal

from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

hist = pygal.Bar()

hist.title = "Crazy numbers without reason."
hist.x_labels = list(range(rw.num_points))
hist.x_title = "Step"
hist.y_title = "Random decision."

hist.add("X", rw.x_values)
hist.add("Y", rw.y_values)
hist.render_to_file("rw_visual.svg")
