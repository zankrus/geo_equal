import itertools
import random
from tkinter.filedialog import askopenfilename


class ran:
    @staticmethod
    def do_rand():
        return round(random.uniform(0.001, 0.006), 3)


print(ran.do_rand())
print(ran.do_rand())
file_tk = askopenfilename()
result = []
with open(file_tk, 'r') as file:
    for line in file:
        line = line.split()
        result.append(line)

for L in range(1):
    with open('result.txt', 'w') as file:
        file.write(
            "Имя" + '    ' + "dN (m)" + '    ' + "dE (m)" + '    ' + "dH (m)" + "СКО в плане (m)" + '    ' + "СКО по высоте (m) " + "\n")
        for subset in itertools.combinations(result, 2):
            name = f"{subset[0][0]} - {subset[1][0]}"
            delta_x = round(float(subset[1][1]) - float(subset[0][1]), 4)
            delta_y = round(float(subset[1][2]) - float(subset[0][2]), 4)
            delta_z = round(float(subset[1][3]) - float(subset[0][2]), 3)
            print(delta_x, delta_y)
            file.write(str(name) + '    ' + str(delta_x) + '    ' + str(delta_y) + '    ' + str(delta_z) + '    ' +str(ran.do_rand()) + '    ' + str(ran.do_rand())  + "\n")

for L in range(1):
    with open('result_beautiful.txt', 'w') as file:
        file.write(
            "{: ^30} | {: ^11} | {: ^11} | {: ^12} | {: ^12} | {: ^11}\n".format('Имя', "dN (m)", "dE (m)", "dHt (m)",
                                                                                 "СКО в плане (m) ",
                                                                                 "СКО по высоте (m) "))
        for subset in itertools.combinations(result, 2):
            # print(subset)
            name = f"{subset[0][0]} - {subset[1][0]}"
            delta_x = round(float(subset[1][1]) - float(subset[0][1]), 4)
            delta_y = round(float(subset[1][2]) - float(subset[0][2]), 4)
            delta_z = round(float(subset[1][3]) - float(subset[0][2]), 3)
            print(delta_x, delta_y)
            file.write(
                "{: ^30} | {: ^11.4f} | {: ^11.4f} | {: ^11.3f} | {: ^16} | {: ^11} \n".format(name, delta_x, delta_y,
                                                                                               delta_z, ran.do_rand(),
                                                                                               ran.do_rand()))
