import itertools

result = []
with open('data.txt', 'r') as file:
    for line in file:
        line = line.split()
        result.append(line)

for L in range(1):
    with open('result.txt', 'w') as file:
        for subset in itertools.combinations(result, 2):
            # print(subset)
            name = f"{subset[0][0]} - {subset[1][0]}"
            delta_x = round(float(subset[1][1]) - float(subset[0][1]), 4)
            delta_y = round(float(subset[1][2]) - float(subset[0][2]), 4)
            delta_z = round(float(subset[1][3]) - float(subset[0][2]), 3)
            print(delta_x, delta_y)
            file.write(str(name) + '    ' + str(delta_x) + '    ' + str(delta_y) + '    ' + str(delta_z) + "\n")
