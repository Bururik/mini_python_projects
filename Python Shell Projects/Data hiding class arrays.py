class Queue:
    def __init__(self,contents):
        self._hiddenlist = list(contents)

    def push(self,value):
        self._hiddenlist.insert(0,value)

    def pop(self):
        return self._hiddenlist.pop(-1) #the negative 1 is not really necessary with pop


    #This last line translates the array from a memory entry to a readable string in the output

    def __repr__(self):
        return 'Queue({})'.format(self._hiddenlist)


queue = Queue([1,2,3])
print(queue,'\n')

queue.push(0)
print(queue,'\n')

queue.pop() #default for pop is -1
print(queue,'\n')

print(queue._hiddenlist)
