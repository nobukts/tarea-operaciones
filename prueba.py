import random as r

sol = [0,1,2,3]
sol2 = sol.copy()
j1,j2 = r.sample(sol, 2)

aux = sol2[j1]
sol2[j1] = sol2[j2]
sol2[j2] = aux

print(sol)
print(sol2)