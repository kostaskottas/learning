def find_duplicates(nums):
    duplicates = []
    seen = []
    for num in nums:
        if num in seen:
            if num not in duplicates:
                duplicates.append(num)
        if num not in seen:
            seen.append(num)
    return duplicates

x = [1,2,3,4,5,6,7,8,2,3,4,5,2,3]

print(find_duplicates(x))
