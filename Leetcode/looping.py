#https://leetcode.com/problems/find-words-containing-character/

words = ["leet", "code", "text"]
x = str("e")      

index1 = [ ]
for i in range(len(words)):

    single_word = list(words[i])

    if x in single_word:

        index1.append(i)

        print(index1)