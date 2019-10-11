'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
count = 0

def count_th(word):

    global count

    if len(word) == 0:
        return count
    elif word[:2] == 'th':
        count += 1
        word = word[1:len(word)]
        return count_th(word)
    elif word[:2] != 'th':
        word = word[1:len(word)]
        return count_th(word)
    return count