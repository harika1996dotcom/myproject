import re
dict = {}
def uniqueWord(Word):
    if Word in dict:
        dict[words] += 1
    else:
        dict.update({words: 1})
if __name__ == '__main__':
      string = "Java is to JavaScript what car is to Carpet"
      ListOfWords = re.split("[\W]+", string)
      for words in ListOfWords:
          uniqueWord(words)
      for elements in dict:
              if dict[elements] == 1:
                 print(elements)  
