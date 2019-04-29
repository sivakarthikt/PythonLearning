

# Impelementing Custom Iterator
class Sentence():
    def __init__(self,sentence):
        self.sentence=sentence
        self.index=0
        self.words=self.sentence.split()
    def __iter__(self):
        return self
    def __next__(self):
        if self.index>=len(self.words):
            raise StopIteration
        idx=self.index
        self.index+=1
        return self.words[idx]

st=Sentence("This is fun!!!!")

for word in st:
    print(word)