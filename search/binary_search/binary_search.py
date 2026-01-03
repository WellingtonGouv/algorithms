def binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] > target:
            right = mid - 1

        elif nums[mid] < target:
            left = mid + 1

        else:
            # number found
            return mid
    return -1

def recursive_binary_search(nums: list[int], target: int, left: int, right: int) -> int:
    if right >= left:

        mid = left + (right - left) // 2

        if nums[mid] > target:
            return recursive_binary_search(nums,target,left,mid-1)
        
        elif nums[mid] < target:
            return recursive_binary_search(nums,target,mid+1,right)
        else:
            # number found
            return mid
    return -1

if __name__ == '__main__':
    array = []

    for i in range(1000):
        array.append(i)

    array.sort()
    print(recursive_binary_search(array, 800, 0, len(array)-1))
