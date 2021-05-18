file = open('total_station.sdr', 'r')

while True:
    line = file.readline()
    if not line:
        break
    print(line)

file.close()