def Reverse(str):
   word=str.split()
   reversed=word[::-1]
   new_sentence=" ".join(reversed)
   return new_sentence

str=raw_input("Enter a sentence:")
print(Reverse(str))
