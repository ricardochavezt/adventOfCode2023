import fileinput
import re

def convert_numbers(numbers, map):
    dest_numbers = []
    for number in numbers:
        dest_number = number
        for (src_range, dest_difference) in map:
            if number in src_range:
                dest_number += dest_difference
                break
        dest_numbers.append(dest_number)
    return dest_numbers

def convert_ranges(ranges, map):
    dest_ranges = []
    for (orig_start, orig_length) in ranges:
        start, length = orig_start, orig_length
        for (src_range, dest_difference) in map:
            if start in src_range:
                if (start+length-1) in src_range:
                    # add transformed range
                    dest_ranges.append((start + dest_difference, length))
                    break
                else:
                    # split and add first part of the range
                    dest_ranges.append((start + dest_difference, src_range.stop - start))
                    length -= (src_range.stop - start)
                    start = src_range.stop
            elif start < src_range.start:
                if (start+length-1) in src_range:
                    # split and add first part of the range untransformed
                    dest_ranges.append((start, src_range.start - start))
                    # add transformed range
                    dest_ranges.append((src_range.start + dest_difference, length - (src_range.start - start)))
                    break
                elif (start+length-1) < src_range.start:
                    dest_ranges.append((start, length))
                    break
                else:
                    # split and add first part of the range untransformed
                    dest_ranges.append((start, src_range.start - start))
                    # add transformed range
                    dest_ranges.append((src_range.start + dest_difference, src_range.stop - src_range.start))
                    length = src_range.stop - start
                    start = src_range.stop
        else:
            dest_ranges.append((start, length))
    
    return dest_ranges

seeds_pattern = re.compile(r'seeds:\s+(.+)')
map_name_pattern = re.compile(r'([a-z-]+)\s+map:')
range_pattern = re.compile(r'(\d+)\s+(\d+)\s+(\d+)')

seeds = []
seed_ranges = []
current_map, current_map_name = None, None
for line in fileinput.input():
    if (seeds_match := seeds_pattern.match(line.strip())):
        seeds = [int(s) for s in seeds_match[1].split()]
        seed_ranges = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
        print('Seeds:', seeds, ', seed ranges:', seed_ranges)
    elif (map_name_match := map_name_pattern.match(line.strip())):
        # print('Found', map_name_match[1], 'map')
        if current_map is not None:
            print('Processing map', current_map_name)
            current_map.sort(key=lambda x: x[0].start)
            print(current_map)
            seeds = convert_numbers(seeds, current_map)
            print('Numbers:', seeds)
            seed_ranges = convert_ranges(seed_ranges, current_map)
            print('Ranges:', seed_ranges)
            current_map = None
        current_map_name = map_name_match[1]
    elif (range_match := range_pattern.match(line.strip())):
        dest_range_start, src_range_start, range_len = int(range_match[1]), int(range_match[2]), int(range_match[3])
        src_range = range(src_range_start, src_range_start+range_len)
        dest_difference = dest_range_start - src_range_start
        if current_map is None:
            current_map = []
        current_map.append((src_range, dest_difference))
    else:
        pass

if current_map is not None:
    print('Processing map', current_map_name)
    print(current_map)
    seeds = convert_numbers(seeds, current_map)
    print('Numbers:', seeds)
    seed_ranges = convert_ranges(seed_ranges, current_map)
    print('Ranges:', seed_ranges)

print('Part 1:', min(seeds))
print('Part 2:', min([x[0] for x in seed_ranges]))