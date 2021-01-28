def CountToWord():
  fileName = input('Enter The File Name: ')
  file = open(fileName,'r')
  numberOfWords = 0
  for line in file:
    word = line.split()
    numberOfWords = numberOfWords+len(word)
    print(numberOfWords)

CountToWord()  