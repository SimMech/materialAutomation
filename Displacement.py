#########################Displacment.py########################################
###############################################################################
import pandas as pd
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
###############################################################################
def Disp(node,curve,Test):
    n='rotation'
    Time,Disp=[],[]
    fnodout=open(path+runs+'/'+curve+'/output_420_'+Test+'_'+curve+'/nodout','r') 
    for line in fnodout: 
        lineList=line.split()
        for i in range(0,len(lineList),1): 
            if ('time' in line): 
                time0=lineList[len(lineList)-2]
                n='displacement'
            if (n=='displacement' and lineList[0]==node and len(lineList)==13):
                Time.append(time0)
                Disp.append(lineList[2])
                n='rotation'
    fnodout.close()
    return(Time,Disp)
############Main function###############
seperator=','
runList=input('Use commas as seperator\nWhat is the run numbers? ')
runList=runList.split(seperator)
plt.figure(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
for run in runList:
    runs=str(run)
    if runs[0]=='1': Test='Uniaxial'
    if runs[0]=='2': Test='Punch'
    if runs[0]=='3': Test='Shear'
    if runs[0]=='5': Test='NR05' 
    if runs[0]=='6': Test='NR80'
    plt.figure(num=runs, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
    labels=[]
    writer=pd.ExcelWriter(path+runs+'/caeDisp'+runs+'.xlsx')
    print('Written: {}'.format(path+runs+'/caeDisp'+runs+'.xlsx'))
    for model in extrapolate:
        Diff=[]
        node1=test[Test][1]
        node2=test[Test][2]
        curve=runs[:5]+str(extrapolate[model])+runs[-2:]
        labels.append(curve)
        time1,disp1=Disp(node1,curve,Test)
        time2,disp2=Disp(node2,curve,Test)
        time1=pd.DataFrame(time1).astype(float)
        disp1=pd.DataFrame(disp1).astype(float)
        disp2=pd.DataFrame(disp2).astype(float)
        diff=disp1-disp2
        dfm='df'+model
        df=pd.concat([time1,disp1,disp2,diff],axis=1)
        dfm=pd.concat([time1,disp1,disp2,diff],axis=1)
        df.columns =['Time','Y_'+test[Test][1],'Y_'+test[Test][2],'Y_Diff']
        dfm.columns=['Time','Y_'+test[Test][1],'Y_'+test[Test][2],'Y_Diff']
        writerCurve=pd.ExcelWriter(path+runs+'/'+curve+'/output_420_'+Test+'_'+curve+'/caeDisp'+curve+'.xlsx')
        print('Written: {}'.format(path+runs+'/'+curve+'/output_420_'+Test+'_'+curve+'/caeDisp'+curve+'.xlsx'))
        df.to_excel(writerCurve, sheet_name=curve, index=False, freeze_panes=(1,5))
        dfm.to_excel(writer, sheet_name=curve, index=False, freeze_panes=(1,5))
        writerCurve.save() 
        writerCurve.close()
        plt.plot(time1,disp1, label=labels[-1],linewidth=0.7)
        plt.plot(time1,disp2, label=labels[-1],linewidth=0.7)
        plt.plot(time1,diff, label=labels[-1],linewidth=0.7)
    plt.xlabel('Time [s]')
    plt.ylabel('Displacement [mm]')
    plt.title('Extensometer Length For Trial {}'.format(runs)) 
    writer.save()
    writer.close()
    plt.grid(b=True, which='both', color='C7',linestyle='--')
    plt.savefig(path+runs+'/disp'+runs+'.pdf',dpi=100)
    plt.figure(run)
    plt.show()