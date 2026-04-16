def smallest(n:float, m:float) -> float:
    if n < m:
        return n #which calls below in thus statement evaluated? = n < m
    else:
        return m

first = smallest(3,2) #What is the value of first? = first = 2
second = smallest(2,2) #What is the value of second? Is this a reasonable result? Why or why not?
# = second = 2 It is reasonable because m and n are equal so returning either one gives 2.
print(first, second)

def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b #In general, when will a call to this function evaluate this statement? = When a is the largest number
    elif b > c:
        return b + c #In general, when will a call to this function evaluate this statement? = When a is not the largest and b > c
    else:
        return 2 * c #In general, when will a call to this function evaluate this statement? = When a is not the largest and b <= c

answer1 = function2(3,2,1) #What is the value of answer1? = answer1 = 1
answer2 = function2(2,3,1) #What is the value of answer2? = answer2 = 4
answer3 = function2(2,1,3) #What is the value of answer3? = answer3 = 6
print(answer1, answer2, answer3)