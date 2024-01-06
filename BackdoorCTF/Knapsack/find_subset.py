def find_subset_with_sum(numbers, target_sum):
    def backtrack(start, current_sum, current_subset):
        if current_sum == target_sum:
            result.append(current_subset.copy())
            return
        for i in range(start, len(numbers)):
            if current_sum + numbers[i] <= target_sum:
                current_subset.append(numbers[i])
                backtrack(i + 1, current_sum + numbers[i], current_subset)
                current_subset.pop()

    result = []
    backtrack(0, 0, [])
    return result

def check_superincreasing(arr):
    sum = 0
    arr.sort()
    for i in arr:
        if i < sum:
            print(f'Not superincreasing at {i}')
            return
        print(i)
        sum += i

# Given array and target sum
arr = [600848253359, 617370603129, 506919465064, 218995773533, 831016169202, 501743312177, 15915022145, 902217876313, 16106924577, 339484425400, 372255158657, 612977795139, 755932592051, 188931588244, 266379866558, 661628157071, 428027838199, 929094803770, 917715204448, 103431741147, 549163664804, 398306592361, 442876575930, 641158284784, 492384131229, 524027495955, 232203211652, 213223394430, 322608432478, 721091079509, 518513918024, 397397503488, 62846154328, 725196249396, 443022485079, 547194537747, 348150826751, 522851553238, 421636467374, 12712949979]
s = 7929089016814

check_superincreasing(arr)