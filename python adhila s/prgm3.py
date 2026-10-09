s=input("enter a sentence:")
print(s)
Wordslist=s.split()
print(Wordslist)
uniquewords=set(Wordslist)
for word in uniquewords:
   print(f"{word}occurs{Wordslist.count(word)}times")
