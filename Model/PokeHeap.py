from Model.pkmDB import pkmDB
import math

class PokeHeap:
    def __init__(self):
        self.heap = self.createHeap()

    def createHeap(self):
        pkmArray = pkmDB()
        qArray = []
        i = 0
        for pkm in pkmArray:
            qArray.append(pkm)
            qArray = self.maxHeapifyUp(qArray, i)
            i += 1
        return qArray
    
    # Relacionado a la inserción de elementos
    def maxHeapifyUp(self, qArray, indexCurrent):
        if qArray[indexCurrent].getNumber() > qArray[self.parentIndex(indexCurrent)].getNumber():
            x = qArray[self.parentIndex(indexCurrent)]
            qArray[self.parentIndex(indexCurrent)] = qArray[indexCurrent]
            qArray[indexCurrent] = x
            if indexCurrent != 0:
                qArray = self.maxHeapifyUp(qArray, self.parentIndex(indexCurrent))
                return qArray
            else:
                return qArray
        else:
            return qArray
    
    def deleteMax(self):
        max = self.heap[0]
        self.heap[0] = self.heap[len(self.heap)-1]
        self.heap[len(self.heap)-1] = max
        self.heap.pop()
        self.maxHeapifyDown(0)
        return max

    # Relacionado a borrar los máximos
    def maxHeapifyDown(self, indexCurrent):
        lftChildIndex = self.leftIndex(indexCurrent)
        rghtChildIndex = self.rightIndex(indexCurrent)

        if lftChildIndex and rghtChildIndex <= len(self.heap)-1: 
            if self.heap[lftChildIndex].getNumber() > self.heap[rghtChildIndex].getNumber():
                x = self.heap[indexCurrent]
                self.heap[indexCurrent] = self.heap[lftChildIndex]
                self.heap[lftChildIndex] = x
                self.maxHeapifyDown(lftChildIndex)
            else:
                x = self.heap[indexCurrent]
                self.heap[indexCurrent] = self.heap[rghtChildIndex]
                self.heap[rghtChildIndex] = x
                self.maxHeapifyDown(rghtChildIndex)
        elif lftChildIndex <= len(self.heap)-1:
            x = self.heap[indexCurrent]
            self.heap[indexCurrent] = self.heap[lftChildIndex]
            self.heap[lftChildIndex] = x

    def getMaxArray(self):
        maxPkmArray = []
        for i in range(150):
            maxPkmArray.append(self.deleteMax())
            print(maxPkmArray[i].getName())
        return maxPkmArray

    def leftIndex(self, indexParent):
        return 2*indexParent + 1
    
    def rightIndex(self, indexParent):
        return 2*indexParent + 2
    
    def parentIndex(self, indexChild):
        parentIndex = math.floor((indexChild-1)/2)
        if parentIndex < 0:
            return indexChild
        else:
            return parentIndex
