'''
Latin vocab parser
uses top 1000 latin words. 
'''

from bs4 import BeautifulSoup
import random


class LatinParser:
    def __init__(self):
        with open("/Users/macuser/Desktop/projects/latin/latinTop1000Data.html") as fp:
            soup = BeautifulSoup(fp, "lxml")
        self.information = [text for text in soup.stripped_strings]
        self.num_words = int(self.information.__len__()/5)

    def createDataLists(self):
        i = 0
        self.latList,self.defList,self.posList,self.semList,self.rnkList = ([],[],[],[],[])
        for elem in self.information:
            if i%5 == 0:
                self.latList.append(elem)
            if i%5 == 1:
                self.defList.append(elem)
            if i%5 == 2:
                self.posList.append(elem)
            if i%5 == 3:
                self.semList.append(elem)
            if i%5 == 4:
                self.rnkList.append(elem)
            i+=1

    def createDict(self):    
        self.createDataLists()
        self.word_tuples = []
        for j in range(self.num_words):
            self.word_tuples.append((self.latList[j], self.defList[j], self.posList[j], self.semList[j], self.rnkList[j]))
    
    def printDict(self):
        print(self.word_tuples)

    def getEnglish(self, index):
        return self.word_tuples[index][1]

    def subsetByRnk(self, low, high): # both high and low are inclusive
        subset = []
        if low==1 and high==997: return self.word_tuples
        for tuple in self.word_tuples:
            rank = int(tuple[4])
            if rank>=low and rank<=high: subset.append(tuple)
        return subset

    def randomize(self, subset):
        random.shuffle(subset)
        return subset

    def quizLToE_basic(self, low = 1, high = 997):
        subset = self.randomize(self.subsetByRnk(low, high))
        for tuple in subset:
            print("--------------------------------------------------------------------")
            print(tuple[0])
            trans = input("\nWhat is your Translation? ")
            print("\nCompare yours: {"+ trans+ "} and mine: {"+ tuple[1]+"}")

    def quizLToE_studying(self, low = 1, high = 997):
        subset = self.randomize(self.subsetByRnk(low, high))
        while subset.__len__()>=1:
            for tuple in subset:
                print("--------------------------------------------------------------------")
                print(tuple[0])
                trans = input("\nWhat is your Translation? ")
                print("\nCompare yours: {"+ trans+ "} and mine: {"+ tuple[1]+"}")
                goodbye = input("Were you right? (Y/N) ")
                if goodbye=='Y' or goodbye=='y': subset.remove(tuple)

    def quizEToL_basic(self, low = 1, high = 997):
        subset = self.randomize(self.subsetByRnk(low, high))
        for tuple in subset:
            print("--------------------------------------------------------------------")
            print(tuple[1])
            trans = input("\nWhat is your Translation? ")
            print("\nCompare yours: {"+ trans+ "} and mine: {"+ tuple[0]+"}")

    def quizEToL_studying(self, low = 1, high = 997):
        subset = self.randomize(self.subsetByRnk(low, high))
        while subset.__len__()>=1:
            for tuple in subset:
                print("--------------------------------------------------------------------")
                print(tuple[1])
                trans = input("\nWhat is your Translation? ")
                print("\nCompare yours: {"+ trans+ "} and mine: {"+ tuple[0]+"}")
                goodbye = input("Were you right? (Y/N) ")
                if goodbye=='Y' or goodbye=='y': subset.remove(tuple)


lp = LatinParser()
lp.createDict()
lp.quizLToE_studying(1,4)