import re
import fileinput

def count_valid_combinations(record, groups):
    pattern_str = r'\.+'.join([f'#{{{g}}}' for g in groups.split(',')])
    groups_pattern = re.compile(r'\.*'+pattern_str+r'\.*')

    possible_combinations = [record]
    for i in range(0, len(record)):
        if record[i] == '?':
            temp_list = []
            for c in possible_combinations:
                temp_list.append(c[0:i]+'.'+c[i+1:])
                temp_list.append(c[0:i]+'#'+c[i+1:])
            possible_combinations = temp_list
    
    valid_combination_count = 0
    for c in possible_combinations:
        if groups_pattern.fullmatch(c):
            valid_combination_count += 1

    return valid_combination_count

valid_combination_total, unfolded_combination_total = 0, 0
for line in fileinput.input():
    record, groups = line.strip().split()
    valid_combination_total += count_valid_combinations(record, groups)
    unfolded_record = '?'.join([record] * 5)
    unfolded_groups = ','.join([groups] * 5)
    unfolded_combination_total += count_valid_combinations(unfolded_record, unfolded_groups)

print('Part 1:', valid_combination_total)
print('Part 2:', unfolded_combination_total)