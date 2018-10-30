
#######################cleanup.py###########################
Folder='T:/E2SC-K'
folder='T:/E2SC-K'
import os

print('The list of files which will be removed:\n')
fcleanup=open(Folder+'/'+'cleanup.txt','w')
fcleanup.write('The list of files which will be removed:\n')
for Folder,dirs,files in os.walk(Folder): 
    for filename in files:
##########################DYNA################## 
        if 'metal_extrapolate' in Folder: continue
        if 'referral' in Folder: continue
        if 'original' in Folder: continue
        if filename[-5:]=='.xlsx': continue 
        if filename[-4:]=='.key': continue
        if filename[-4:]=='.dyn': continue
        if filename[-3:]=='.py': continue
        if filename[:11]=='inputPoints': continue
        if filename[:7]=='secforc': continue
        if filename[:6]=='nodout': continue 
        if filename[:4]=='test': continue 
        if filename[:4]=='disp': continue
        if filename[:3]=='cae': continue
##########################ABAQUS################## 
        if filename[-4:]=='.cae': continue 
        if filename[-4:]=='.jnl': continue
        if filename[-4:]=='.inp': continue 
        if filename[-4:]=='.dat': continue
        if filename[-4:]=='.msg': continue 
##########################OTHERS##################
        if filename[-5:]=='.pptx': continue 
        if filename[-5:]=='.html': continue 
        if filename[-5:]=='.iges': continue
        if filename[-4:]=='.doc': continue 
        if filename[-4:]=='.ppt': continue 
        if filename[-4:]=='.tif': continue
        if filename[-4:]=='.gif': continue
        if filename[-4:]=='.jpg': continue
        if filename[-4:]=='.JPG': continue
        if filename[-4:]=='.png': continue 
        if filename[-4:]=='.PNG': continue 
        if filename[-4:]=='.avi': continue
        if filename[-4:]=='.fem': continue
        if filename[-4:]=='.x_t': continue 
        if filename[-4:]=='.stp': continue 
        if filename[-4:]=='.fdb': continue
        if filename[-4:]=='.flo': continue
        if filename[-4:]=='.xls': continue 
        if filename[-4:]=='.csv': continue 
        if filename[-4:]=='.log': continue
        if filename[-3:]=='.hm': continue 
        if filename=='cleanup.txt': continue
################################################ 
        remfile=os.path.join(Folder,filename)
        fcleanup.write('{0}\n'.format(remfile))
fcleanup.close()
print('Check the cleanup.txt for files which will be removed\n')
yesNo=input('Are you sure you want to delete all the files?\n y for Yes\n ...')
if yesNo=='y':
  for folder,dirs,files in os.walk(folder): 
    for filename in files:
##########################DYNA################## 
        if 'metal_extrapolate' in folder: continue
        if 'referral' in folder: continue
        if 'original' in folder: continue
        if filename[-5:]=='.xlsx': continue 
        if filename[-4:]=='.key': continue
        if filename[-4:]=='.dyn': continue
        if filename[-3:]=='.py': continue
        if filename[:11]=='inputPoints': continue
        if filename[:7]=='secforc': continue
        if filename[:6]=='nodout': continue 
        if filename[:4]=='test': continue 
        if filename[:4]=='disp': continue
        if filename[:3]=='cae': continue
##########################ABAQUS################## 
        if filename[-4:]=='.cae': continue 
        if filename[-4:]=='.jnl': continue
        if filename[-4:]=='.inp': continue 
        if filename[-4:]=='.dat': continue
        if filename[-4:]=='.msg': continue 
##########################OTHERS##################
        if filename[-5:]=='.pptx': continue 
        if filename[-5:]=='.html': continue 
        if filename[-5:]=='.iges': continue
        if filename[-4:]=='.doc': continue 
        if filename[-4:]=='.ppt': continue 
        if filename[-4:]=='.tif': continue 
        if filename[-4:]=='.gif': continue
        if filename[-4:]=='.jpg': continue
        if filename[-4:]=='.JPG': continue
        if filename[-4:]=='.png': continue 
        if filename[-4:]=='.PNG': continue 
        if filename[-4:]=='.avi': continue
        if filename[-4:]=='.fem': continue
        if filename[-4:]=='.x_t': continue 
        if filename[-4:]=='.stp': continue 
        if filename[-4:]=='.fdb': continue
        if filename[-4:]=='.flo': continue
        if filename[-4:]=='.xls': continue 
        if filename[-4:]=='.csv': continue 
        if filename[-4:]=='.log': continue
        if filename[-3:]=='.hm': continue 
        if filename=='cleanup.txt': continue
################################################ 
        remfile=os.path.join(folder,filename)
        os.remove(remfile)
print('done')