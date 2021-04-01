
def naive_matcher(text,pattern):
    n = len(text)
    m = len(pattern)

    for i in range(0, n-m):
        j = 0
        while(j < m and text[i+j] == pattern[j]):
            j+=1
        if(j == m):
            print("Pattern found at index " + str(i))
        # else:
        #     print("No match")


text = "cdcdabbaabbacdcdklmn"
pattern = "cdcd"

print(naive_matcher(text, pattern))