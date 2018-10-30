###############################################################################
############################sectionForce.py####################################
###############################################################################
import matplotlib.pyplot as plt
import pandas as pd
import os, time, datetime

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
             'Optimum':8
            }
progress=[chr(124),chr(45),chr(47),chr(92)]
p=0
now=datetime.datetime.now()
now=now.strftime("%Y-%m-%d %H:%M")
seperator=','
runList=input('Use commas as seperator\nWhat is the run numbers?')
runList=runList.split(seperator)

for run in runList:
    runs=str(run)
    if runs[0]=='1': Test='Uniaxial'
    if runs[0]=='2': Test='Punch'
    if runs[0]=='3': Test='Shear'
    if runs[0]=='5': Test='NR05' 
    if runs[0]=='6': Test='NR80' 
    plt.figure(num=runs, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
    plt.xlabel('Time')
    plt.ylabel('Load')
    plt.title('Load For Trial {}'.format(runs))
    caeData=pd.read_excel(path+runs+'/caeDisp'+runs+'.xlsx')
    writer=pd.ExcelWriter(path+runs+'/caeData'+runs+'.xlsx')
    print('Written: {}'.format(path+runs+'/caeData'+runs+'.xlsx'))
    for model in extrapolate:
        Time,Force,labels=[],[],[]
        curve=runs[:5]+str(extrapolate[model])+runs[-2:] 
        labels.append(model)
        caeDataM=pd.read_excel(path+runs+'/'+curve+'/output_420_'+Test+'_'+curve+'/caeDisp'+curve+'.xlsx') 
        caeDataM.dropna(how='any')
        if 'Load' in caeDataM:
            caeDataM.drop('Load', axis=1)
        if (Test=='Uniaxial' or test[Test]=='Shear' or test[Test]=='NR05' or test[Test][0]=='NR80'):
            f=open(path+runs+'/'+curve+'/output_420_'+Test+'_'+curve+'/secforc','r') 
            for line in f :
                p+=1
                if p>3: p=0
                print(progress[p], end='\r')
                lineList=line.split()
                if (len(lineList)==6 and lineList[0]=='1'):
                    time=lineList[1]
                    force=lineList[3]
                    Time.append(time)
                    Force.append(force)
        if (Test=='Punch'):
            f=open(path+runs+'/'+curve+'/output_420_'+curve+'/rcforc','r') 
            for line in f:
                p+=1
                if p>3: p=0
                print(progress[p], end='\r')
                lineList=line.split()
                if (len(lineList) == 18 and lineList[0])=='master' and (lineList[1]=='2'):
                    time=lineList[3]
                    force=lineList[7]
                    Time.append(time)
                    Force.append(force)
        f.close()

        plt.plot(Time,Force, label=labels[-1],linewidth=0.7) 
        ForceDataM=pd.DataFrame(Force, columns=['Load']).astype(float)
        caeDataM=pd.concat([caeDataM,ForceDataM],axis=1)
        writerM=pd.ExcelWriter(path+runs+'/'+curve+'/output_420_'+Test+'_'+curve+'/caeData'+curve+'.xlsx')
        print('Written: {}'.format(path+runs+'/'+curve+'/output_420_'+Test+'_'+curve+'/caeData'+curve+'.xlsx'))
        caeDataM.to_excel(writerM, sheet_name=curve, freeze_panes=(1,5))
        caeDataM.to_excel(writer, sheet_name=curve, freeze_panes=(1,5))
        writerM.close()
    writer.close()
    plt.legend()
    plt.grid(b=True, which='both', color='C7',linestyle='--')
    plt.savefig(path+runs+'/secforc'+runs+'.pdf')
    plt.show()