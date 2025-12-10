with open('puzzle-1-input.txt', 'r') as file:
    input = file.read()

intervals = input.replace('\n', '').split(',')

sum = 0

for interval in intervals:
    bounds = interval.split('-')
    lower = int(bounds[0])
    upper = int(bounds[1]) + 1
    for id in range(lower, upper):
        id_str = str(id)
        digits = len(id_str)
        for pattern_length in range(1, digits // 2 + 1):
            if digits % pattern_length == 0:
                flag = 1
                for i in range(0, digits - pattern_length, pattern_length):
                    i_p1 = i + pattern_length
                    i_p2 = i_p1 + pattern_length
                    if id_str[i:i_p1] != id_str[i_p1:i_p2]:
                        flag = 0
                        break
                if flag == 1:
                    sum += id
                    break
                
print(sum)