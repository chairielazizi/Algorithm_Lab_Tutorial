string = input("Enter a string: ")

def reverse(str):
    ayat = str.split(' ')
    ayat.reverse()
    ayat = ' '.join(ayat)

    return ayat

print(reverse(string))