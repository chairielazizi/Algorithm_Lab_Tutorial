
def find_prefix(pattern, patt_len, temp_array):
    length = 0
    temp_array[0] = 0

    for i in range(1,patt_len):
        if(pattern[i] == pattern[length]):
            length += 1
            temp_array[i] = length
        else:
            if length != 0:
                length = temp_array[length-1]
                i -= 1
            else:
                temp_array[i] = 0

    # for i in range(len[temp_array]):
    #     print[]
    print(temp_array)

def kmp(text,pattern):
    text_size = len(text)
    p_size = len(pattern)
    lps = [0] * p_size
    # location = 0
    # final_arr = [0] * text_size

    find_prefix(pattern, p_size, lps)

    i,j = 0,0
    while i < text_size:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == p_size:
            # final_arr[location] = i-j
            # print("The pattern occurs at index %d", str(i-j))
            print("The pattern occurs at index %d" % (i - j))
            j = lps[j-1]
        elif(i < text_size and pattern[j] != text[i]):
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

text = "abxabcabcaby"
pattern = "abcaby"
arr = [0] * len(pattern)
kmp(text, pattern)


