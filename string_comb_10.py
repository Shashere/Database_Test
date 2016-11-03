def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target: 
        print(partial, target)
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n]) 


if __name__ == "__main__":
    num_str="3523014"
    print("The number is:",num_str)
    result_list=subset_sum(list(map(int,num_str)),10)
    print(result_list)
