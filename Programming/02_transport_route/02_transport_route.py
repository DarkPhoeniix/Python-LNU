
# class definition of transport route
class TransportRoute:
    # constructor
    def __init__(self, start_station, end_station, stations_num, route_length):
        self.start_station = start_station
        self.end_station = end_station
        self.stations_num = int(stations_num)
        self.route_length = int(route_length)

    # for print()
    def __repr__(self):
        return 'start station: ' + self.start_station + '\n' + \
               'end station: ' + self.end_station + '\n' + \
               'number of stations: ' + str(self.stations_num) + '\n' + \
               'length of route: ' + str(self.route_length) + '\n'


# opening file with data
file = open(r"data.txt", "r")
lines = file.readlines()

# list for all routes
routes = []

# reading routes from file
for i in lines:
    values = i.split()
    routes.append(TransportRoute(values[0], values[1], values[2], values[3]))

# sorting by route length
routes.sort(key=lambda x: x.route_length)

# finding routes with average length between stops less then <length_x>
length_x = int(input("Print number of routes with average length between stops less than "))
print("Number of routes with average length between stops less than " + str(length_x) + ": ", end='')
num = 0
for i in routes:
    if i.route_length / i.stations_num < length_x:
        num += 1
print(num)

# finding routes with start station <station_x>
station_x = input("Input start station: ")
new_list = [i for i in routes if i.start_station == station_x]
for i in new_list:
    print(i)

# finding routes with maximal number of stops
print("Routes with maximal number of stops: ")
for i in routes:
    if i.stations_num == max(routes, key=lambda x: x.stations_num).stations_num:
        print(i)
