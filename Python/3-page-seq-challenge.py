""""
Problem: Please provide a solution in Python

You are running a small Website.
Input: simplified apache-style log file of activity

timestamp user_id page_id
101 1 1
103 1 7
105 2 3
107 3 1
111 1 14
120 1 20
121 3 7
122 3 14
130 1 22
133 2 1
134 2 20
145 10 1
146 9 1
...
...
24 hours

Output: the most popular 3-page-sequence in 24 hours
Example: 3-page-sequence: 1,7,14 (3 pages visitedList in a in sequence by the same user). In this small example, this is also the most popular sequence as 2 users have visitedList it.
Note: 7,14,20 is another 3-page sequence

"""


class PopularPages :
    def __init__(self, logFileName , numOfSeq):
        self.logFileName = logFileName
        self.numOfSeq = numOfSeq

    def readFromFileAndSearch(self) :
        visitedList = {}
        userBrowsedList = {}
        with open(self.logFileName) as fp:
            for cnt, line in enumerate(fp):
                content = list(map(lambda x : x.strip(), line.split(" ")))
                if content[1] in userBrowsedList.keys() :
                    userBrowsedList[content[1]].append(content[2])
                else :
                    userBrowsedList[content[1]] = [content[2]]

                if len(userBrowsedList[content[1]]) > self.numOfSeq - 1:
                    # get last seq and find in existing visited list
                    seqStr = ','.join(userBrowsedList[content[1]][(len(userBrowsedList[content[1]]) - self.numOfSeq) : ])
                    if seqStr in visitedList.keys() :
                        visitedList[seqStr] += 1
                    else :
                        visitedList[seqStr] = 1

        max = 0
        seqStr = ""
        for seqKey in visitedList.keys() :
            if max < visitedList[seqKey] :
                max = visitedList[seqKey]
                seqStr = seqKey

        return max , seqStr

# Driver code
if __name__ == '__main__':
    maxSeq = PopularPages("apache-style.txt" , 3).readFromFileAndSearch()
    print("Seq :" , maxSeq[1] , ", Max Visited : " , maxSeq[0])
