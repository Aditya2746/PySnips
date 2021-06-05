from matplotlib import pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')

# ages from 25 to 35
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_indexes = np.arange(len(ages_x))
width = 0.25
# median Salaries for the people of age group in ages_x
dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
# median Salaries for the people of age group in ages_x (of python devs)
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
# median Salaries for the people of age group in ages_x (of js devs)
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.title('Median Salary (USD) by Age') # title of chart
plt.xlabel('Age') # label for x axis
plt.ylabel('Median Salary (USD)') # label for y axis

plt.bar(x_indexes - width,
        py_dev_y, width=width, color='#5a7d9a',
        linestyle='-.', linewidth=2, label='Python Devs')
plt.bar(x_indexes,
        js_dev_y, width=width, color='#adad3b',
        linestyle='-.', linewidth=2, label='Javascript Devs')
plt.bar(x_indexes + width,
        dev_y, width=width, color='#444444',
        linestyle='-', linewidth=1, label='All Devs')
plt.legend()

plt.xticks(ticks=x_indexes, labels=ages_x)

plt.grid(True)
plt.tight_layout()

plt.show()
