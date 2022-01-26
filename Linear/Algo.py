import docplex.mp.model as cpx


dataUsers = {1 : 0.10, 2 : 0.30} #utilisateurs et leur degré de suspicion
dataObj = {3 : 0.20, 4 : 0.40, 5 : 0.50} #objets et leur degré de suspicion
dataEdge = {(1,3): 0.1, (1,5):0.2, (2,4):0.3, (2,5):0.4} #arrêtes et leur degré de suspicion

user = [range(1, 3)] # {1, 2}
object = [range(3, 6)] # {3,4,5}
#yTab = range(1, 6) # {1,2,3,4,5}

m = cpx.Model(name='Detection Fraudes')
x = {(i,j): m.continuous_var(name='x_{0}_{1}'.format(i,j)) for i in user for j in object}
y = {j: m.continuous_var(name='y_{0}'.format(j), lb = 0) for j in user+object}

print(x)
print(y)

m.maximize(m.sum( x[i,j] for i in user for j in object) )

for i in user:
    m.add_constraint((x[i,j] for j in object) <= y[i])

for j in object:
    m.add_constraint((x[i,j] for i in user) <= y[j])

for j in user+object:
    m.add_constraint(m.sum(y[j]) <= 1)

#c1 = m.add_constraint((x[i,j] <= y[k]) for i,j in vals for k in valsy, ctname="const1")
#c2 = m.add_constraint(m.sum(y) <= 1, ctname="const2")

#m.set_objective("max", x)
m.print_information()
m.solve()
m.print_solution()

'''
tms = m.solve()
assert tms
tms.display()
'''




'''
opt_model = cpx.Model(name="MIP Model")

# if x is Continuous
x_vars  = {(i,j): opt_model.continuous_var(lb=l[i,j], ub= u[i,j], name="x_{0}_{1}".format(i,j)) for i in set_I for j in set_J}
# if x is Binary
x_vars  = {(i,j): opt_model.binary_var(name="x_{0}_{1}".format(i,j)) for i in set_I for j in set_J}
# if x is Integer
x_vars  = {(i,j): opt_model.integer_var(lb=l[i,j], ub= u[i,j], name="x_{0}_{1}".format(i,j)) for i in set_I for j in set_J}

# <= constraints
constraints = {j : opt_model.add_constraint( ct=opt_model.sum(a[i,j] * x_vars[i,j] for i in set_I) <= b[j], ctname="constraint_{0}".format(j))for j in set_J}

# our objective
objective = opt_model.sum(x_vars[i,j] * c[i,j] for i in set_I for j in set_J)

# for maximization
opt_model.maximize(objective)
'''

