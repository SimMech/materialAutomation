###########################inputPointsPlot.py#################################
import matplotlib.pyplot as plt
path='T:/Mat/420/'
###############################################################################
###########################Input Points Plot###################################
i=0
f=open(path+'inputPoints.txt', 'r')
plt.figure(num=None, figsize=(10, 8), dpi=80, facecolor='w', edgecolor='k')
for line in f:
    lineList=line.split()
    if (len(lineList)==1 and line!='end' and i==0):
        i+=1
        point={}
        point.setdefault('strain',[])
        point.setdefault('stress',[])
        point.setdefault('curve',[])
        point['curve'].append(lineList[0])
        continue
    if (len(lineList)==2):
        point['strain'].append(float(lineList[0]))
        point['stress'].append(float(lineList[1]))
        continue
    if (len(lineList)==1 and line!='end' and i>0):
        i+=1
        plt.plot(point['strain'],point['stress'],'o-',label=point['curve'][0],linewidth=0.7)
        point={}
        point.setdefault('strain',[])
        point.setdefault('stress',[])
        point.setdefault('curve',[])
        point['curve'].append(lineList[0])
        continue
    if (line=='end'):
        i+=1
        plt.plot(point['strain'],point['stress'],'o-',label=point['curve'][0],linewidth=0.7)
        break 
f.close()
plt.xlabel('Strain []')
plt.ylabel('Stress [GPa]')
plt.title('Proposed Points')
plt.legend(bbox_to_anchor=(0.0, 1.0),loc=2)
plt.grid(b=True, which='both', color='C7',linestyle='--')
plt.savefig(path+'inputPointsPlot.pdf',dpi=100)
plt.show()