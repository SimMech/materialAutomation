from scipy.signal import lfilter
#IIR #vs Kamlan Fliter
n = 30 # the larger n is, the smoother curve will be
b = [1.0 / n] * n
a = 1
gradientsFiltered = lfilter(b,a,gradients)

plt.figure(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
plt.plot(disps,gradientsFiltered, linewidth=2, linestyle="-", c="b") # smooth by filter
plt.xlim(2,12)
plt.ylim(-300,500)
plt.xlabel('Disp')
plt.ylabel('Gradient')
plt.title('Filtered Test Stress/Strain Gradient')
plt.grid(b=True, which='both',color='C7',linestyle='--')
plt.savefig(path+'Filtered Gradient.pdf',dpi=100)
plt.show()