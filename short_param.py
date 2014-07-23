# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 14:16:57 2014

@author: paulinkenbrandt
"""

def shortdict(param):
    param = param.lower()
    chemdict = {'conductivity @ 25 c umhos/cm': \
    'Cond', 'ammonia-nitrogen as n':'N', \
    'bicarbonate as hco3': 'HCO3', 'tds':'TDS', \
    'inorganic nitrogen (nitrate and nitrite) as N':'N', \
    'inorganic nitrogen (nitrate and nitrite)':'N', \
    'kjeldahl nitrogen':'N','total dissolved solids':'TDS', \
    'sulfate as so4':'SO4', 'ph':'pH', 'ph, lab':'pH', \
    'temperature, water':'Temp_C','arsenic':'As', \
    'bromide':'Br','carbon dioxide':'CO2', 'specific conductance':'Cond', \
    'conductivity':'Cond', 'sulfate':'SO4', 'nitrate':'NO3', \
    'nitrite':'NO2','magnesium':'Mg', 'calcium':'Ca', 'potassium':'K', \
    'sodium':'Na', 'sodium plus potassium':'NaK', \
    'bicarbonate':'HCO3', 'carbonate':'CO3', 'chloride':'Cl', \
    'silica':'Si','fluoride':'F', 'total hardness':'Hard', \
    'hardness, non-carbonate':'Hard', }
    return chemdict.get(param)    