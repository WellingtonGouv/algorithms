def linear_search(nums: list[int], target: int) -> int:
    for i in range(len(nums)):
        if (nums[i] == target):
            return i
    return -1

if __name__ == '__main__':
    array = []

    for i in range(1000):
        array.append(i)

    array.sort()
    print(linear_search(array, 800))
