from z3 import *

# define four variables
Lisa = Int('Lisa')
Bob = Int('Bob')
Jim = Int('Jim')
Mary = Int('Mary')

s = Solver()

# the domain of variables
s.add(And(Lisa >= 1, Lisa <= 4))
s.add(And(Bob >= 1, Bob <= 4))
s.add(And(Jim >= 1, Jim <=4))
s.add(And(Mary >= 1, Mary <=4))

# each one just get one rank
s.add(Not(Lisa == Bob))
s.add(Not(Lisa == Jim))
s.add(Not(Lisa == Mary))
s.add(Not(Bob == Jim))
s.add(Not(Bob == Mary))
s.add(Not(Jim == Mary))

# Lisa is not next to Bob in the ranking
s.add(Not(Lisa - Bob == 1))
s.add(Not(Bob - Lisa == 1))

# Jim is ranked immediately ahead of a biology major
# One of the women (Lisa and Mary) is a biology major
s.add(Or(Lisa - Jim == 1, Mary - Jim == 1))

# Bob is ranked immediately ahead of Jim
s.add(Jim - Bob == 1)

# One of the women is ranked first
s.add(Or(Lisa == 1, Mary == 1))

# find the solution
print(s.check())
print(s.model())
