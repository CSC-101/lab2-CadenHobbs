from typing import Optional             # gain access to the Optional[X] type hint


def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)    # What is the value of test on each call? Call 1: True 9>=0, False 9 < 3, test = True and False = False
    # Call 2: True 2>=0, True 2 < 3, test = True and True = True
    if test:                            # What is this check preventing? The check prevents [IndexError]
        return L[idx]
    else:
        return None


first = checked_access([1, 0, 1], 9)     # What is the value of first? = None
second = checked_access([1, 0, 1], 2)    # What is the value of second? = 1
print()

def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])    # For which call below is this statement evaluated and what are the values being added? len(L[0]) + len(L[1]) + len(L[2]), 4 + 2 + 3 = 9
    elif len(L) > 1:
        result = len(L[0]) + len(L[1])                # For which call below is this statement evaluated and what are the values being added? len(L[0]) + len(L[1]), 7 + 4 = 11
    elif len(L) > 0:
        result = len(L[0])                            # For which call below is this statement evaluated and what are the values being added? len(L[0], = 11
    else:
        result = 0
    return result


first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()

def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
         # What is the value of words at this point? ['this', 'is', 'confusing', 'code.','AVOID', 'SUCH.']
         # What are the values of first and second at this point? ['this', 'is', 'confusing', 'code.','AVOID', 'SUCH.']
         # What happened? The function changes the original list [words] and both first and second point to the same list, so it changed one shared list rather than creating a new list
print()