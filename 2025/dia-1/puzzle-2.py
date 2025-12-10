file = open('puzzle-1-input.txt', 'r')

pos = 50
pwd = 0

for line in file:
    dir = line[0]
    dist = int(line[1:])
    match dir:
        case 'R':
            pos += dist
            pwd += pos // 100
        case 'L':
            first = pos if pos != 0 else 100
            if dist >= first:
                pwd += (dist - first) // 100 + 1
            pos -= dist
                
    pos %= 100
            
print(pwd)