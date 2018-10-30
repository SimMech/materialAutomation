​################################inputPoints.py#################################
###############################################################################
path='T:/Mat/420/'

def inputPoints():
    for line in fr:
        lineList=line.split()
        if ('maxPlasticStrain' in line):
            break
        if (len(lineList)==3):
            fw.write('{0} {1}\n'.format(lineList[1],lineList[2]))
    fr.close() 
###############################################################################
#####################Curve Fit Results Comparison##############################
fw=open(path+'/inputPoints.txt', 'w')
seperator=','
runList=input('Use commas as seperator\nWhat are the run numbers?')
runList=runList.split(seperator)
for run in runList:
    runs=str(run)
    fw.write('Curve'+runs[:6]+runs[-2:]+'\n')
    fr=open(path+runs+'/metal_extrapolate/Hoc-She_yield_curve-extrap.key','r') 
    inputPoints()
fw.write('end')
fw.close()