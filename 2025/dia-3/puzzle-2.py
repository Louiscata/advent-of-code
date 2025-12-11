with open('puzzle-1-input.txt', 'r') as input:
    total_joltage = 0
    batt_per_bank = 12
    
    for bank in input:
        bank_trim = bank.replace('\n', '')
        joltage = ''
        
        for last_valid_batt in range(-batt_per_bank + 1, 1):
            max = 0
            remove_batt_until = 0
            valid_batt = bank_trim[:last_valid_batt] if last_valid_batt != 0 else bank_trim

            for batt_index in range(len(valid_batt)):
                batt_int = int(bank_trim[batt_index])
                
                if batt_int > max:
                    max = batt_int
                    remove_batt_until = batt_index + 1

            joltage += str(max)
            bank_trim = bank_trim[remove_batt_until:]

        total_joltage += int(joltage)
        
    print(total_joltage)
