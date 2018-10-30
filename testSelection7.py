######################Shear Tension Tests###########################
Path=path='T:/Mat/420/ref_test/'
forcColumns=[2,32,43,54,65]
dispColumns=[10,40,51,62,73]
labels=[0,30,41,52,63]
writer=pd.ExcelWriter(Path+'SHtensionDerivatives.xlsx')
plt.figure(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
for Path,dirs,files in os.walk(Path): 
    for fileName in files:
        if (fileName=='XX-SH.xlsx'):
            testData=pd.read_excel(Path+fileName, sheetname='SH-QS') 
            for i in range(0,len(forcColumns)):
                disp=[]
                forc=[]
                forc=testData.iloc[57:,forcColumns[i]].astype(float)
                disp=testData.iloc[57:,dispColumns[i]].astype(float)
                plt.plot(disp,forc, label=testData.iloc[46,labels[i]],linewidth=0.7)
                df=pd.concat([disp,forc],axis=1)
                df.columns =['Disp','Force'] 
                df.to_excel(writer, sheet_name=testData.iloc[46,labels[i]], index=False)
plt.xlabel('Displacement [mm]') 
plt.ylabel('Load [N]')
plt.title('Force-Displacement Curves For Shear Tension Tests')
plt.legend()
plt.grid(b=True, which='both', color='C7',linestyle='--')
plt.savefig(path+'testSelectionShearTension.pdf',dpi=100)
plt.show() 
writer.close()