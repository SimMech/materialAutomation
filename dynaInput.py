########################dynaInputs.py#############################
import shutil
import pathlib
path='T:/Mat/420/'

test={'Uniaxial':1,
      'Punch':2,
      'Shear':3,
      'Double shear':4,
      'Notched A':5,
      'Notched B':6,
      'Sub_0deg':7,
      'Sub_45deg':8,
      'Sub_90deg':9}

extrapolate={'Hockett-Sherby':0,
               'Modified-Hockett-Sherby':1,
               'Elmagd1':2,
               'Elmagd2':3,
               'Voce':4,
               'Swift':5,
               'Johnson-Cook':6,
               'Mix':7,
               'Optimum':8}
def dynaCurve(runs,model): 
        if (runs[0]=='1'): #testType=uniaxial
            shutil.copy(refFolder+'/000_BOUNDARY_PULL-NOSYM_PARAM.key',runFolder)
            shutil.copy(refFolder+'/OSU_Tensile_200.key',runFolder)
            f1=open(refFolder+'/420_uniaxial.dyn', 'r') 
            f2=open(runFolder+'/420_uniaxial_'+curve+'.dyn','w')
            for line in f1:
                f2.write(line.replace('referral',curve))
            f1.close()
            f2.close() 

        if (runs[0]=='2'): #testType=punch 
            shutil.copy(refFolder+'/000_BOUNDARY_PUNCH_PARAM.key',runFolder)
            shutil.copy(refFolder+'/OSU_Punch_0-5mm.key',runFolder)
            f1=open(refFolder+'/420_punch_0001.dyn', 'r') 
            f2=open(runFolder+'/420_punch_'+curve+'.dyn','w')
            for line in f1:
                f2.write(line.replace('referral',curve))
            f1.close()
            f2.close() 
                       
        if (runs[0]=='3'): #testType=shear
            shutil.copy(refFolder+'/000_BOUNDARY_PULL-NOSYM_PARAM.key',runFolder)
            shutil.copy(refFolder+'/Shear_Scaled_orgnl_Groove_narrow_4.key',runFolder)
            f1=open(refFolder+'/420_shear.dyn', 'r') 
            f2=open(runFolder+'/420_shear_'+curve+'_tmp.dyn','w')
            for line in f1:
                f2.write(line.replace('referral',curve))
            f1.close()
            f2.close()

        if (runs[0]=='5'): #testType=notched A
            shutil.copy(refFolder+'/000_BOUNDARY_PULL-NOSYM_PARAM.key',runFolder)
            shutil.copy(refFolder+'/NR05.key',runFolder)
            f1=open(refFolder+'/420_NR05.dyn', 'r') 
            f2=open(runFolder+'/420_NR05_'+curve+'.dyn','w')
            for line in f1:
                f2.write(line.replace('referral',curve))
            f1.close()
            f2.close() 
       
        if (runs[0]=='6'): #testType=notched B
            shutil.copy(refFolder+'/000_BOUNDARY_PULL-NOSYM_PARAM.key',runFolder)
            shutil.copy(refFolder+'/NR80.key',runFolder)
            f1=open(refFolder+'/420_NR80.dyn', 'r') 
            f2=open(runFolder+'/420_NR80_'+curve+'.dyn','w')
            for line in f1:
                f2.write(line.replace('referral',curve))
            f1.close()
            f2.close() 
       
        if (model=='Hockett-Sherby'):
            f3=open(Folder+'/metal_extrapolate/Hoc-She_yield_curve-extrap.key','r')
            f4=open(runFolder+'/'+curve+'.key','w') 
            for line in f3:
                f4.write(line.replace('122070401',' '+curve))
            f3.close()
            f4.close()

        if (model=='Modified-Hockett-Sherby'):
            f3=open(Folder+'/metal_extrapolate/Modified_Hoc-She_yield_curve-extrap.key','r')
            f4=open(runFolder+'/'+curve+'.key','w') 
            for line in f3:
                f4.write(line.replace('122070401',' '+curve))
            f3.close()
            f4.close()

        if (model=='Elmagd1'):
            f3=open(Folder+'/metal_extrapolate/elmagd_yield_curve-extrap.key','r')
            f4=open(runFolder+'/'+curve+'.key','w') 
            for line in f3:
                f4.write(line.replace('122070401',' '+curve))
            f3.close()
            f4.close()

        if (model=='Elmagd2'):
            f3=open(Folder+'/metal_extrapolate/elmagd2_yield_curve-extrap.key','r')
            f4=open(runFolder+'/'+curve+'.key','w') 
            for line in f3:
                f4.write(line.replace('122070401',' '+curve))
            f3.close()
            f4.close()

        if (model=='Voce'):
            f3=open(Folder+'/metal_extrapolate/voce_yield_curve-extrap.key','r')
            f4=open(runFolder+'/'+curve+'.key','w') 
            for line in f3:
                f4.write(line.replace('122070401',' '+curve))
            f3.close()
            f4.close()

        if (model=='Swift'):
            f3=open(Folder+'/metal_extrapolate/swift_yield_curve-extrap.key','r')
            f4=open(runFolder+'/'+curve+'.key','w') 
            for line in f3:
                f4.write(line.replace('122070401',' '+curve))
            f3.close()
            f4.close()

        if (model=='Johnson-Cook'): #yield curvee xtrapolation=johnson-Cook
            f3=open(Folder+'/metal_extrapolate/johnson-cook_yield_curve-extrap.key','r')
            f4=open(runFolder+'/'+curve+'.key','w') 
            for line in f3:
                f4.write(line.replace('122070401',' '+curve))
            f3.close()
            f4.close()

        if (model=='Mix'):
            f3=open(Folder+'/metal_extrapolate/mix_yield_curve-extrap.key','r')
            f4=open(runFolder+'/'+curve+'.key','w') 
            for line in f3:
                f4.write(line.replace('122070401',' '+curve))
            f3.close()
            f4.close()

        if (model=='Optimum'):
            f3=open(Folder+'/metal_extrapolate/optimum_yield_curve-extrap.key','r')
            f4=open(runFolder+'/'+curve+'.key','w') 
            for line in f3:
                f4.write(line.replace('122070401',' '+curve))
            f3.close()
            f4.close()
#######################Main dynaCurve#############################
seperator=','
runList=input('Use commas as seperator\nWhat is the run numbers?')
runList=runList.split(seperator)
for run in runList:
    runs=str(run)
    Folder=path+runs
    refFolder=path+'ref_cae'
    pathlib.Path(Folder).mkdir(parents=True, exist_ok=True)
    for model in extrapolate:
        curve=runs[:5]+str(extrapolate[model])+runs[-2:]
        runFolder=Folder+'/'+curve
        pathlib.Path(runFolder).mkdir(parents=True, exist_ok=True)
        shutil.copy(refFolder+'/005_CONTROL-20141028_R612_MATCHAR_0005.key',runFolder)
        shutil.copy(refFolder+'/MAT_24_PARAM.key',runFolder)
        dynaCurve(runs, model)
        print('Dyna files are created | {0} | Model:{1}'.format(runFolder,model))