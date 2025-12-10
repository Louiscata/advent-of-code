with open('puzzle-1-input.txt', 'r') as file:
    input = file.read()

intervals = input.replace('\n', '').split(',')

sum = 0

for interval in intervals:
    bounds = interval.split('-')
    lower = int(bounds[0])
    upper = int(bounds[1]) + 1
    for id in range(lower, upper):
        digits = len(str(id))
        if digits % 2 == 0:
            id_str = str(id)
            half_digits = int(digits / 2)
            if id_str[:half_digits] == id_str[-half_digits:]:
                sum += id
                
print(sum)