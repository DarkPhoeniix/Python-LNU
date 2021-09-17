
import point_forecasting
import matplotlib.pyplot as plt

database_UDS = open("database_USD.txt", "r")
content = database_UDS.readlines()
my_map = {}
for i in range(0, len(content), 4):
    my_map[content[i][0:10]] = {content[i + 1][0:10]: [content[i + 1][11:17], content[i + 1][18:24]],
                                content[i + 2][0:10]: [content[i + 2][11:17], content[i + 2][18:24]],
                                content[i + 3][0:15]: [content[i + 3][16:22], content[i + 3][23:29]]}
names = []
data_1 = []
data_2 = []
data_3 = []
for i in my_map:
    names.append(i[0:5])
    data_1.append(float(my_map.get(i).get('PrivatBank')[0]))
    data_2.append(float(my_map.get(i).get('PrivatBank')[1]))
    data_3.append([i[0:2], float(my_map.get(i).get('PrivatBank')[0])])

k, b = point_forecasting.line_by_least_squares_method(data_3)
r = point_forecasting.forecast_next_point(k, b, 9)

plt.scatter(names, data_1, color='red')
plt.scatter(names, data_2, color='blue')
plt.scatter(names, data_3, color='yellow')

plt.ylim(26, 27.5)
plt.show()
