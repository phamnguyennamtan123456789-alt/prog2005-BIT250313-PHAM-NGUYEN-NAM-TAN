import matplotlib.pyplot as plt

cities = ['Los Angeles', 'San Diego', 'San Jose', 'San Francisco',
          'Fresno', 'Sacramento', 'Long Beach', 'Oakland',
          'Bakersfield', 'Anaheim']

areas = [1302, 964, 466, 600, 298, 259, 133, 202, 372, 131]

plt.barh(cities, areas)
plt.gca().invert_yaxis()

plt.title('Top 10 thành phố lớn nhất California (diện tích)')
plt.xlabel('Diện tích (km2)')
plt.ylabel('Thành phố')

plt.show()