file = open("puzzle-1-input.txt", "r")

pos = 50
pwd = 0

for line in file:
    direction = line[0]
    match direction:
        case 'R':
            pos += int(line[1:])
        case 'L':
            pos -= int(line[1:])
            
    pos %= 100
    
    if pos == 0:
        pwd += 1
        
print(pwd)