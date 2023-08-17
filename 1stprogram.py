with open('animal.txt', 'r') as file:
    lines = file.readlines()
    
data = []

for line in lines:
    row = line.strip().split(',')
    data.append(row)

array_2d = data
# for chhecking the array from the text file
# for rrow in array_2d:
#     pepepeperrint(row)

distances = []

for i in range(len(array_2d)):
    for col in range(len(array_2d[i])):
        if array_2d[i][col] == 'NA':
            array_2d[i][col] = '1'

for i in range(1, len(array_2d) - 1):
    lists = []
    distance = 0
    for k in range(i + 1, len(array_2d)):
        for j in range(1, len(array_2d[k])):
            distance += abs(int(array_2d[i][j]) - int(array_2d[k][j]))
        lists.append(distance)
    distances.append(lists)


for row in distances:
    print(row)

dictionary = {}


for row in range(len(distances)):
    for col in range(len(distances[row])):
        key = f"d{row+1}-d{col+2}"
        val = distances[row][col]
        dictionary[key] = val


sorted_mat = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
count = 0
for key, val in sorted_mat.items():
    print(key + " : " + str(val))
    count += 1
    if count == 10:
        break
