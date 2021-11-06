from collections import Counter
from itertools import groupby

# Task №1
def arr_filter(arr):
    filtered = [num for num in arr if isinstance(num, (int))]
    return filtered

def Task1():
    print("--- TASK 1 ---")
    list_1 = [1, 2, "a", "b"]
    list_2 = [1, "a", "b", 0, 15]
    list_3 = [1, 2, "aasf", '1', "123", 123]
    print(arr_filter(list_1))
    print(arr_filter(list_2))
    print(arr_filter(list_3))

# Task №2
def first_non_repeating_letter():
    print("\n--- TASK 2 ---")
    string = input("Input text like 'sTreSS': ")
    dict = {}
    lowercase_string = string.lower()

    for ch in lowercase_string:
        if ch in dict:
            dict[ch] = dict[ch] + 1
        else:
            dict[ch] = 1

    for ch in lowercase_string:
        if ch in dict and dict[ch] == 1:
            index = lowercase_string.find(ch)
            return print("First non-repeated letter: ",string[index])

# Task №3
def digital_root(n):
    print("\n--- TASK 3 ---")
    while n >= 10:
        n = sum(int(i) for i in str(n))
    return print("Result: ",n)

# Task №4
def Task4():
    print("\n--- TASK 4 ---")
    arr = [1, 3, 6, 2, 2, 0, 4, 5]
    n = len(arr)
    sum = 5
    count = 0
    list = []
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                list += (arr[i],arr[j])
                count += 1
    return print("Количество полученых пар: ", count,"\n",
          [(list[i],list[i+1]) for i in range(0,len(list),2)] )

# Task №5
def meeting():
    s = "Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
    Task5(s)

def Task5(s):
    print("\n--- TASK 5 ---")
    sorted_list = ["({}, {})".format(*reversed(name.split(":"))).upper()
                            for name in s.split(";")]

    return print("".join(sorted(sorted_list)))


# Extra tasks
# ---Extra №1
def Extra_task1(num):
    print("\n--- Extra TASK 1 ---")
    digits = [int(i) for i in str(num)]
    idx = len(digits) - 1

    while idx >= 1 and digits[idx - 1] >= digits[idx]:
        idx -= 1

    if idx == 0:
        return print(-1)

    pivot = digits[idx - 1]
    swap_idx = len(digits) - 1

    while pivot >= digits[swap_idx]:
        swap_idx -= 1

    digits[swap_idx], digits[idx - 1] = digits[idx - 1], digits[swap_idx]
    digits[idx:] = digits[:idx - 1:-1]

    return print(int(''.join(str(x) for x in digits)))

def Extra_task2(num):
    print("\n--- Extra TASK 2 ---")
    try:
        bin_a = bin(num)[2:].zfill(32)
        list_a = [bin_a[i:i + 8] for i in range(0, 31, 8)]
        z = [str(int(i, base=2)) for i in list_a]
        return print('.'.join(z))
    except ValueError:
        return print("Incorrect input")



if __name__ == '__main__':
    Task1()                         #1
    first_non_repeating_letter()    #2
    digital_root(132189)            #3
    Task4()                         #4
    meeting()                       #5
    # Extra---------------------------
    Extra_task1(2071)              #*1
    Extra_task2(2149583361)        #*2
