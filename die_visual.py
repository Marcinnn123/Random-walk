from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

die_1 = Die(6)
die_2 = Die(6)

results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result):
    frequency = results.count(value)
    frequencies.append(frequency)
    
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequencies'}
my_layout = Layout(title="2 x D6 frequency", xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')