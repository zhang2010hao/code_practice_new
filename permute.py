

def permute(nums):
    def dfs(arr, visted):
        if len(arr) == n:
            rsts.append([t for t in arr])
        else:
            for i in range(n):
                if visted[i] == 0:
                    arr.append(nums[i])
                    visted[i] = 1
                    dfs(arr, visted)
                    arr.pop(-1)
                    visted[i] = 0

    n = len(nums)
    rsts = []
    visted = [0] * n
    dfs([], visted)

    return rsts

nums = [1]
print(permute(nums))