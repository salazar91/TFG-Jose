import matplotlib.pyplot as plt
import matplotlib.pylab as P
import pickle
import numpy as np

dir_fig = "./"


Counted=[]
CError=[]
with open("./simulaciones.txt") as f:
    content = f.readlines()
for line in content[2:-2]:
    #print(line.split())
    Counted.append(float(line.split()[2]))
    CError.append(float(line.split()[3]))
total = list(zip(CError, Counted))
total.sort(key = lambda x:x[0])
total.sort(key = lambda x:x[1])
d = dict()
for par in total:
    if par[1] not in d:
        d[par[1]] = [par[0]]
    else:
        d[par[1]].append(par[0])
CError = [i[0] for i in total]
Counted = [i[1] for i in total]
print(CError)
print(Counted)

print(d)

left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
rect_scatter = [left, bottom, width, height]
plt.figure(1, figsize=(8,8))
axScatter = plt.axes(rect_scatter)
ax = plt.gca()


axScatter.scatter( Counted,CError, color="blue",s=1, label="Estimated Lenght")
Percentil95=[np.percentile(d[i],95) for i in d]
Percentil5=[np.percentile(d[i],5) for i in d]
plt.plot([i for i in d],Percentil95)
plt.plot([i for i in d],Percentil5)
ax.fill_between(d.keys(),Percentil5, Percentil95, facecolor='lightgrey', alpha=0.5)
plt.savefig(dir_fig+"TFG_JOSE")
