from z3 import *

# possible solutions
l1 = Bool('l1') # lady in room 1
l2 = Bool('l2') # lady in room 2
l3 = Bool('l3') # lady in room 3

# the solver
s = Solver()

# only one lady appears in one room
s.add(Or(Or(l1, l2), l3)) # lady exists
s.add(Not(And(l1, l2))) # only one lady
s.add(Not(And(l1, l3)))
s.add(Not(And(l2, l3)))

# sign1 => tiger in room1 => l1 = false
# sign2 => lady in room2 => l2 = true
# sign3 => tiger in room2 => l2 = false
# at most one sign is true
s.add(Or(And(l1 == True, And(l2 == False, l2 == True)), \
	Or(And(l1 == False, And(l2 == False, l2 == True)), \
		Or(And(l1 == True, And(l2 == True, l2 == True)), \
			And(l1 == True, And(l2 == False, l2 == False))))))

#print(s.check())
#print(s.model())

# the answer is l1
# proof
s.add(Not(l1))
print(s.check())
