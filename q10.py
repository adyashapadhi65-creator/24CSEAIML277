#Write a function that accepts a list and returns sum of its elements
def sum_of_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

lst = list(map(int, input().split()))
print(sum_of_list(lst))