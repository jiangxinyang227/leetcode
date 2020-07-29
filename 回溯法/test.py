import copy


def subset(nums):
    result = []
    path = []
    nums.sort()
    back_track(nums, path, result, 0)
    return result


def back_track(nums, path, result, index):
    temp = copy.deepcopy(path)
    result.append(temp)
    for i in range(index, len(nums)):
        if nums[i] == nums[i - 1] and i > index:
            continue
        path.append(nums[i])
        back_track(nums, path, result, i + 1)
        path.pop()


res = subset([1, 2, 2])
print(res)


def all_set(nums):
    result = []
    path = []
    back_path(nums, path, result)
    return result


def back_path(nums, path, result):
    for i in range(len(nums)):
        path.append(nums[i])
        if len(path) < 3:
            back_path(nums[:i] + nums[i + 1:], path, result)
        else:
            result.append(copy.deepcopy(path))
        path.pop()  # 写在判断条件外面，否则无法回溯上去


res = all_set([1, 2, 3])
print(res)
