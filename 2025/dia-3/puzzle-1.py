with open('puzzle-1-input.txt', 'r') as input:
    total_joltage = 0
    for bank in input:
        last_battery = bank[-2]
        last_battery_int = int(last_battery)
        bank_strip = bank[:-2]
        max = 0
        second_max = 0 
        for battery in bank_strip:
            battery_int = int(battery)
            if battery_int > max:
                max = battery_int
                second_max = 0
            else:
                if battery_int > second_max:
                    second_max = battery_int
        
        if last_battery_int > second_max:
            second_max = last_battery_int
     
        joltage = int(str(max) + str(second_max))
        total_joltage += joltage
        
    print(total_joltage)
