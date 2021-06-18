inputString=input('enter string')
characterCount=0
wordCount=1
for i in inputString:
    characterCount=characterCount+1
    if (i==' '):
        wordCount=wordCount+1

print(characterCount)
print(wordCount)