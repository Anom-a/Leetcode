nums = [0, 2, 3, 4, 6, 8, 9]

if not nums:
    print([])
else:
    ranges = []
    start = nums[0]

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:
            end = nums[i - 1]
            if start == end:
                ranges.append([start])
            else:
                ranges.append([start, end])
            start = nums[i]

    # Flush the final open range.
    end = nums[-1]
    if start == end:
        ranges.append([start])
    else:
        ranges.append([start, end])

    output = []
    for item in ranges:
        if len(item) == 1:
            output.append(str(item[0]))
        else:
            output.append(str(item[0]) + "->" + str(item[1]))

    print(output)

