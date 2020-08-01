word = input()
word_len = len(word)

def print_line1(word_len):
    output = [".", "."]
    for i in range(1, word_len + 1):
        if i % 3 == 0:
            output.append('*')
        else:
            output.append('#')
        
        if i != (word_len):
            output.extend([".",".","."])

    output.extend([".", "."])
    print(' '.join(output))

def print_line2(word_len):
    output = ["."]
    for i in range(1, word_len + 1):
        if i % 3 == 0:
            output.extend(["*", ".", "*", "."])
        else:
            output.extend(["#", ".", "#", "."])
    print(' '.join(output))
        
def print_word(word, word_len):
    output = []

    for i in range(1, word_len + 1):
        if i % 3 == 0:
            output.extend(['*', '.', word[i-1], '.'])
        elif (i % 3 == 1) and (i>3):
            output.extend(['*', '.', word[i-1], '.'])
        else:
            output.extend(['#', '.', word[i-1], '.'])

    if word_len % 3 == 0:
        output.append("*")
    else:
        output.append("#")
    print(' '.join(output))


    
print_line1(word_len)
print_line2(word_len)
print_word(word, word_len)
print_line2(word_len)
print_line1(word_len)
