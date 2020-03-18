#Read in Words from a dictionary 
words = []
dict = open("dictionary.txt", 'r')
for line in dict:
    word = node(line.strip())
    words.append(word)

word1 = input("What is the starting word?")
word2 = input("What is the ending word?")

def BFS(nodelist, start, goal):
    # path = BFS(words, index1, index2)

def compareWords(word1, word2):
    if len(word) != len(word2):
        return False
        numdifferent = 0
        for i in range(len(word)):
            for j in range(i+1, len(words)):
                if compareWords(words[i].getWord(), words[j].getWord()):
                    addLink(words, i, j)
                if word1[i] != word2[i]:
                    numdifferent += 1
    if numdifferent == 1:
        return True
    else:
        return False
### Display ### 
print(words)
