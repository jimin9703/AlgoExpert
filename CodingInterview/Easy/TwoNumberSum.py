# solution 1
def twoNumberSum(array, targetSum):
    # Write your code here.
    for i in array:
        for j in array:
            if i != j:
                if i + j == targetSum:
                    return [i, j]
    return []

# solution 2
def twoNumberSum(array, targetSum):
    # Write your code here.
    se = set(array)
    for i in se:
        if i != targetSum - i:
            if targetSum - i in se:
                return [i, targetSum - i]
    return []