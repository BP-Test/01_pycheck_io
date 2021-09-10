
#You are given an array of integers. 
#You should find the sum of the integers with even indexes (0th, 2nd, 4th...). 
#Then multiply this summed number and the final element of the array together. 
#Don't forget that the first element has an index of 0.
#
#For an empty array, the result will always be 0 (zero).
#
#Input: A list of integers.
#
#Output: The number as an integer.
#checkio([0, 1, 2, 3, 4, 5]) == 30
#checkio([1, 3, 5]) == 30
#checkio([6]) == 36
#checkio([]) == 0

# My Original Answer
def checkio(array: list) -> int:
    """
        sums even-indexes elements and multiply at the last
    """
    a = 0
    for i in range(0,len(array)):
        if i%2==1:
            a += 0
        else:
            a += array[i]            
     
    if len(array) ==0:
        return 0
    else:
        return array[len(array)-1] * a

# Soemeone else's answer 1
checkio=lambda x: sum(x[::2])*x[-1] if x else 0
# Soemeone else's answer 2
def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    if len(array) == 0: return 0
    return sum(array[0::2]) * array[-1]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))
    
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
