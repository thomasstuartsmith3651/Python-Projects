import numpy as np
import matplotlib.pyplot as plt
from primefactors import primefactors
from scipy.optimize import curve_fit

primefactors(11302)
#times = []
#numbers = []
#x = np.arange(0,15000,500)
# for i in x:
#      times.append(primefactors(i)[0])
#      numbers.append(primefactors(i)[1])
# print(times)
# print(numbers)

#plt.plot(numbers,times,'x')
#plt.xlabel('Number')
#plt.ylabel('time,s')

# def xsq(x,A):
#     y = []
#     for i in range(len(x)):
#         y.append(A*((x[i])**2))
#     return y
# initial_guess = [10]
# params,params_cov = curve_fit(xsq,numbers,times,initial_guess,maxfev=100000)
# plt.plot(numbers,xsq(numbers,params[0]))
# plt.show()
# print(params[0])
