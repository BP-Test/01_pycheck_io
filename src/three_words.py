def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def checkio(words: str) -> bool:
    words_list = words.split() # split words
    words_bool = [not is_number(i) for i in words_list] # if i is not a number it returns Ture, else False
    words_bool_series = pd.Series(words_bool) # conver to pd.Series
    words_bool_rolling = words_bool_series.rolling(3).sum() # get rolling sum. If it is 3 it means there was a sequence of three words
    words_bool_rolling = words_bool_rolling.isin([3]) # extract the occation that has 3 consecutive words
    three_sequences_counts = words_bool_rolling.sum() # count how many combination of 3 sequence happened
    if three_sequences_counts !=0:
        return True
    else:
        return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))
    
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")