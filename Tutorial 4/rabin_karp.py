d = 256

def rabin_karp(text, pattern, prime):
    text_len = len(text)
    pattern_len = len(pattern)
    i = 0
    j = 0
    pattern_hash = 0
    text_hash = 0
    h = 1  # d^(m-1)


    # calculate h value
    for i in range(pattern_len-1):
        h = (h*d) % prime

    # compute hash value of pattern and text first window
    for i in range(pattern_len):
        pattern_hash = (d * pattern_hash + ord(pattern[i]))%prime
        text_hash = (d * text_hash + ord(text[i]))%prime

    # slide pattern to the next window
    for i in range(text_len - pattern_len + 1):
        if(pattern_hash == text_hash):
            for j in range(pattern_len):
                if(text[i+j] != pattern[j]):
                    break
            j += 1

            if j == pattern_len:
                print("Pattern found at index "+str(i+1))

        # remove trailing character, add leading character
        if i < text_len - pattern_len:
            text_hash = (d*(text_hash-ord(text[i])*h)+ord(text[i+pattern_len]))%prime

            if text_hash < 0:
                text_hash = text_hash + prime

text = "algorithmisfun"
pattern = "fun"
prime = 13
rabin_karp(text, pattern, prime)