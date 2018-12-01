from z3 import *

# possible solutions
l1 = Bool('l1') # lady in room 1
l2 = Bool('l2') # lady in room 2
l3 = Bool('l3') # lady in room 3

# all signs
sign1 = Bool('sign1')
sign2 = Bool('sign2')
sign3 = Bool('sign3')

# the solver
s = Solver()

# only one lady appears in one room
s.add(If(l1, 1, 0) + If(l2, 1, 0) + If(l3, 1, 0) == 1)

# sign1 => tiger in room1 => l1 = false
# sign2 => lady in room2 => l2 = true
# sign3 => tiger in room2 => l2 = false
s.add(sign1 == Not(l1))
s.add(sign2 == l2)
s.add(sign3 == Not(l2))

# at most one sign is true
s.add(If(sign1, 1, 0) + If(sign2, 1, 0) + If(sign3, 1, 0) <= 1)

print("=============================")
print("Solver.Check:", s.check())
print("Solver.Model:", s.model())

# the answer is l1
# proof
print("------------ Proof ----------")
sol_list = [l1, l2, l3]
answer = None
for i in range(1, len(sol_list) + 1):
	print('check whether lady is in room %d or not' % (i))
	s.push()
	s.add(Not(sol_list[i-1]))
	print('Solver.Check:', s.check())
	if s.check() == unsat:
		answer = i
	s.pop()
if answer != None:
	print("---------- Solution ---------")
	print("Lady is in room %d" % (answer))


