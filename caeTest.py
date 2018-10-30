###############################################################################
############################### caeTest.py#####################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path='T:/Mat/420/'
test={'Uniaxial': ['1', '35563', '1364', 'Displacement (Extensometer 1)'],
         'Punch': ['2', '2', '1', 'Max Out of Plane Displ'],
         'Shear': ['3', '187703', '187693', 'Relative Displacement'],
          'NR05': ['5', '15699', '3503', 'Displacement (Extensometer 1)'],
          'NR80': ['6', '21094', '6319', 'Displacement (Extensometer 1)']}
extrapolate={'Hockett-Sherby':0,
             'Modified-Hockett-Sherby':1,
             'Elmagd1':2,
             'Elmagd2':3,
             'Voce':4,
             'Swift':5,
             'Johnson-Cook':6,
             'Mix':7,
             'Optimum':8}
#############inputPoints###########################
def inputPoints(run):
    runs='Curve'+str(run)
    point={}
    point.setdefault('curve',[]) 
    point.setdefault('strain',[])
    point.setdefault('stress',[])
    point['curve'].append(run)
    f=open(path+'inputPoints.txt', 'r')
    find=False
    for line in f: 
        lineList=line.split()
        if (lineList[0]=='end'): break 
        if (len(lineList)==1 and lineList[0]!=runs):
            find=False
            continue
        if (len(lineList)==2 and find==False): 
            continue
        if (lineList[0]==runs):
            find=True
            continue
        if (len(lineList)==2 and find==True): 
            point['strain'].append(float(lineList[0]))
            point['stress'].append(float(lineList[1])) 
            continue
    f.close()
    return(point)
#############Test Plot###########################
def testPlot(runs,labels,Test):
    testData=pd.read_excel(path+'ref_test/'+'XX-'+Test+'.xlsx', sheetname='QS-UT') 
    if (Test=='Uniaxial'):
        forc=testData.iloc[61:,1].dropna(axis=0,how='any',inplace=False)
        disp=testData.iloc[61:,7].dropna(axis=0,how='any',inplace=False)
    if (Test=='Punch'):
        forc=testData.iloc[61:,35].dropna(axis=0,how='any',inplace=False)
        disp=testData.iloc[61:,41].dropna(axis=0,how='any',inplace=False)
    if (Test=='Shear'):
        forc=testData.iloc[61:,45].dropna(axis=0,how='any',inplace=False)
        disp=testData.iloc[61:,51].dropna(axis=0,how='any',inplace=False)
    if (Test=='NR05'):
        forc=testData.iloc[61:,55].dropna(axis=0,how='any',inplace=False)
        disp=testData.iloc[61:,61].dropna(axis=0,how='any',inplace=False)
    if (Test=='NR80'):
        forc=testData.iloc[61:,65].dropna(axis=0,how='any',inplace=False)
        disp=testData.iloc[61:,71].dropna(axis=0,how='any',inplace=False)
    forcScale=[x*.001 for x in forc] 
    plt.plot(disp,forcScale,label=labels[-1], linewidth=1.5, color='red')
    disp=[x for x in disp] 
    area=np.trapz(forcScale,disp)
    print('The area is {0:6.2f} kNmm for Test{1}'.format(area,runs[1]))
###################CAE Plot######################
def caePlot(runs,curve,labels,Test,model):
    forc=disp=[]
    labels.append(model)
    caeData=pd.read_excel(path+runs+'/'+curve+'/output_420_'+Test+'_'+curve+'/caeData'+curve+'.xlsx') 
    disp=caeData.iloc[3:-3,3].astype(float)
    forc=caeData.iloc[3:-3,4].astype(float)
    plt.plot(disp,forc,label=labels[-1],linewidth=0.7)
    disp=[x for x in disp]
    forc=[x for x in forc]
    area=np.trapz(forc,disp)
    print('The area is {0:6.2f} kNmm for {1}'.format(area,model))
###################################################
seperator=','
runList=input('Use commas as seperator\nWhich runs?')
print('\n')
runList=runList.split(seperator)
plt.close('all')

for run in runList:
    runs=str(run)
    if runs[0]=='1': Test='Uniaxial'
    if runs[0]=='2': Test='Punch'
    if runs[0]=='3': Test='Shear'
    if runs[0]=='5': Test='NR05' 
    if runs[0]=='6': Test='NR80' 
    labels=[]
    labels.append(runs)
    inputPoints(runs)
    plt.figure(num=run, figsize=(12,10),dpi=80,facecolor='w',edgecolor='k')
    testPlot(runs,labels,Test)
    for model in extrapolate:
        curve=runs[:5]+str(extrapolate[model])+runs[-2:]
        caePlot(runs,curve,labels,Test,model)
    x=inputPoints(run)
    plt.text(0, 0, x, fontsize=12)
    plt.xlabel('Displacement [mm]')
    plt.ylabel('Force [kN]')
    plt.axis('tight')
    plt.title('Hardening Curves For Trial {}'.format(runs))
    plt.grid(b=True, which='both', color='C7',linestyle='--')
    plt.legend(bbox_to_anchor=(0.11, 0.8),loc=2)
    plt.savefig(path+'caeTest'+runs+'.pdf',dpi=100)
    plt.show(run)