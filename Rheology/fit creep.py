# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:55:38 2023

@author: rmcgorty
"""

import numpy as np
import pandas as pd
import glob
import scipy
from scipy import special
import matplotlib
from matplotlib import pyplot as plt


filenames = glob.glob("*5.x*")
print(filenames)

dataframe1 = pd.read_excel(filenames[1], sheet_name = 'Creep - 1')
numpydf = dataframe1.to_numpy()
compliance_50 = numpydf[2:,7].astype(float)
steptime_50 = numpydf[2:,2].astype(float)

dataframe7 = pd.read_excel(filenames[1], sheet_name = 'Creep - 7')
numpydf = dataframe7.to_numpy()
compliance_200 = numpydf[2:,7].astype(float)
steptime_200 = numpydf[2:,2].astype(float)

dataframe3 = pd.read_excel(filenames[1], sheet_name = 'Creep - 3')
numpydf = dataframe3.to_numpy()
compliance_100 = numpydf[2:,7].astype(float)
steptime_100 = numpydf[2:,2].astype(float)


stress = 50

def creep_compliance_response(t, alpha, beta, bigV, bigG):
    comp = (stress * t**alpha) / (bigV * special.gamma(1+alpha))
    comp = comp + (stress * t**beta) / (bigG * special.gamma(1+beta))
    return comp


def creep_compliance_response_burgers(t, G1, G2, eta1, eta2):
    comp = (1./G1) + (t/eta1)
    comp = comp + (1./G2)*(1 - np.exp(-1*G2*t/eta2))
    return comp


stress = 50
params50 = scipy.optimize.curve_fit(creep_compliance_response, steptime_50, 
                                compliance_50, p0=np.array([0.8, 0.1, 10000e3, 500e3]))
params50_burger = scipy.optimize.curve_fit(creep_compliance_response_burgers, steptime_50, 
                                compliance_50, p0=np.array([3e4, 5e5, 2e6, 7e4]))

stress = 200
params200 = scipy.optimize.curve_fit(creep_compliance_response, steptime_200, 
                                compliance_200, p0=np.array([0.8, 0.1, 10000e3, 500e3]))
params200_burger = scipy.optimize.curve_fit(creep_compliance_response_burgers, steptime_200, 
                                compliance_200, p0=np.array([3e4, 5e5, 2e7, 1e2]))


stress = 100
params100 = scipy.optimize.curve_fit(creep_compliance_response, steptime_100, 
                                compliance_100, p0=np.array([0.8, 0.1, 10000e3, 500e3]))
params100_burger = scipy.optimize.curve_fit(creep_compliance_response_burgers, steptime_100, 
                                compliance_100, p0=np.array([3e4, 5e5, 2e7, 1e2]))


plt.figure()
plt.plot(steptime_50, compliance_50, 'bo')
stress = 50
plt.plot(steptime_50, creep_compliance_response(steptime_50, params50[0][0], params50[0][1], params50[0][2], params50[0][3]), '-r')
characteristic_time50 = (params50[0][2]/params50[0][3])**(1./(params50[0][0]-params50[0][1]))
plt.plot(steptime_50, creep_compliance_response_burgers(steptime_50, params50_burger[0][0], params50_burger[0][1], 
                                                        params50_burger[0][2],params50_burger[0][3]), 
         '--r', alpha=0.5)
plt.ylim(0, 7.5e-5)
plt.title("Stress of %i Pa" % stress)
plt.xlabel("Time (s)")
plt.ylabel("Compliance, J")

plt.figure()
plt.plot(steptime_100, compliance_100, 'go')
stress = 100
plt.plot(steptime_100, creep_compliance_response(steptime_100, params100[0][0], params100[0][1], params100[0][2], params100[0][3]), '-r')
characteristic_time100 = (params100[0][2]/params100[0][3])**(1./(params100[0][0]-params100[0][1]))
plt.plot(steptime_100, creep_compliance_response_burgers(steptime_100, params100_burger[0][0], params100_burger[0][1], 
                                                        params100_burger[0][2],params100_burger[0][3]), 
         '--r', alpha=0.5)
plt.title("Stress of %i Pa" % stress)
plt.xlabel("Time (s)")
plt.ylabel("Compliance, J")


plt.figure()
plt.plot(steptime_200, compliance_200, 'mo')
stress = 200
plt.plot(steptime_200, creep_compliance_response(steptime_200, params200[0][0], params200[0][1], params200[0][2], params200[0][3]), '-r')
characteristic_time200 = (params200[0][2]/params200[0][3])**(1./(params200[0][0]-params200[0][1]))
plt.plot(steptime_200, creep_compliance_response_burgers(steptime_200, params200_burger[0][0], params200_burger[0][1], 
                                                        params200_burger[0][2],params200_burger[0][3]), 
         '--r', alpha=0.5)
plt.title("Stress of %i Pa" % stress)
plt.xlabel("Time (s)")
plt.ylabel("Compliance, J")