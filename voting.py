# Part 4
from collections import Counter


class Candidate(object):
    votes = []

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def setVotes(self, vote):
        self.votes.append(vote)

    def getVotes(self):
        return dict(Counter(self.votes))

candi1 = Candidate('John Doe', 'President')

for x in range(10):
    voteCast = int(input('Enter code to cast your vote'))
    candi1.setVotes(voteCast)

print(candi1.getVotes())