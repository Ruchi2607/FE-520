#!/usr/bin/env python
# coding: utf-8

# In[21]:



                                                                        # Question 1:

def split(endYear,startYear=2012):
    
    import pandas as pd
    import numpy as np
    from datetime import datetime

    #Importing dataset
    df_energy = pd.read_excel(r"D:\Ruchi Folder\Python\Assignment5\Energy.xlsx")
    
 
    # Column columns  "Accumulated Other Comprehensive Income (Loss)" to "Selling, General and Administrative Expenses"]

    df_selected=df_energy.loc[:,"Accumulated Other Comprehensive Income (Loss)": "Selling, General and Administrative Expenses"]
   
    
    date_dataf=df_energy.loc[:,"Data Date":"Fiscal Year"]

    
    # Joining df_Selected with df_Dates
    new_dataf=date_dataf.join(df_selected)
    


    
    
    if endYear==None:
        
           Test=new_dataf[new_dataf["Fiscal Year"]==startYear]
        
           Train=new_dataf[new_dataf["Fiscal Year"]!=startYear]
    
    elif endYear!=None:
        
           Test= new_dataf[(new_dataf["Fiscal Year"] >= startYear) & (new_dataf["Fiscal Year"] <= endYear)]
        
           Train=new_dataf[~((new_dataf["Fiscal Year"] >= startYear) & (new_dataf["Fiscal Year"] <= endYear))]
        
        
    
    return(Test, Train)


split(2013)


# In[37]:


                                                                                # Question 3:


import sklearn
from sklearn import linear_model
from sklearn import preprocessing
from sklearn import datasets
from sklearn import svm
import numpy as np

from sklearn import linear_model
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import mean_squared_error, r2_score


# In[38]:


                                                                                #Question 3 - 1

#Load the dataset
diabets_df=datasets.load_diabetes()


# In[39]:


#Display the data
diabets_df


# In[40]:


                                                                                    #Question3 - 2:
new_df= diabets_df.data[:,np.newaxis,2]

atest=new_df[-20:]
atrain=new_df[:-20]

btest=diabets_df.target[-20:]
btrain=diabets_df.target[:-20]


# In[41]:


                                                                                    #Question3 - 3:

var_lm=linear_model.LinearRegression()

var_lm.fit(atrain,btrain)
model_y= var_lm.predict(atest)
model_y
coef=var_lm.coef_
ms_error=mean_squared_error(btest,model_y)
r_square=r2_score(btest,model_y)
print(coef)
print(ms_error)
print(r_square)


# In[46]:


                                                                                        #Question3 - 4:

var_fold=10

new_var_lm=var_lm.fit(atrain,btrain)

rang=list(range(1,11))

#use For Loop 
for res_data in rang:
    
    res_data=cross_val_score(new_var_lm,atrain, btrain,cv=10)
    #print the result
    print(res_data)
    


# In[48]:


                                                                                #Question3 - 5

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score

regressor = RandomForestRegressor(max_depth = 7,random_state = 0)


# In[49]:


regressor.fit(atrain,btrain)
pred = regressor.predict(atest)
print(pred)


# In[50]:


regressor.score(atrain,btrain)


# In[51]:


                                                                            #Question3 - 6

from sklearn.model_selection import GridSearchCV


# In[52]:


hy_parameters = {'max_depth': [None,7,4],'min_samples_split':[2,10,20]}


# In[53]:


grid_GBR = GridSearchCV(estimator = regressor,param_grid = hy_parameters,cv = 2,n_jobs = 1)


# In[54]:


grid_GBR.fit(atrain,btrain)


# In[56]:


print('Results')
print('\nThe best estimator:',grid_GBR.best_estimator_)
print('\nThe best score :',grid_GBR.best_score_)
print('\nThe best parameter:',grid_GBR.best_params_)


# In[57]:


                                                                                    # Question 2 


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt


# In[59]:


data = pd.read_excel('D:\Ruchi Folder\Python\Assignment5\ResearchDatasetV2.0.xlsx',parse_dates= True)


# In[63]:


data['Date'] = pd.to_datetime(data['Date'], format='%Y%m%d')
data.describe()


# In[62]:


y = data['Signal'].tolist()
x = data['ClosePrice'].tolist()


# In[64]:


plt.plot(data['Date'].tolist(), y, color='r', label='signal')
plt.plot(data['Date'].tolist(), x, color='g', label='closeprice')
plt.show()


# In[65]:


data['signal_return'] = data['Signal'].pct_change()
data['price_return'] = data['ClosePrice'].pct_change()
data.describe()


# In[67]:


plt.plot(data['Date'].tolist(), data['signal_return'], color='r', label='signalreturn')
plt.plot(data['Date'].tolist(), data['price_return'], color='g', label='closepricereturn')
plt.title('Plotting of Price and Signal returns vs Time')
plt.show()


# In[68]:


def cross_correlate(x, y, lag):
    return x.corr(y.shift(lag))


# In[70]:


cross_corrs = []
for lag in range(1, 11):
    cross_corrs.append(cross_correlate(data['price_return'],
                                      data['signal_return'], lag))
plt.plot(range(1,11), cross_corrs, marker='o')
plt.xlabel('Lags')
plt.ylabel('Correlation')
plt.title('Correlation of price returns and signal returns with lagk')
plt.show()


# In[72]:


grp_1 = []
grp_1_idx = []
grp_2 = []
grp_2_idx = []
grp_3 = []
grp_3_idx = []
grp_4 = []
grp_4_idx = []
for index in range(len(data['signal_return'])):
    if data['signal_return'][index] < -0.01:
        grp_1.append(data['signal_return'][index])
        grp_1_idx.append(index)
    elif data['signal_return'][index] >= -0.01 and data['signal_return'][index] < 0:
        grp_2.append(data['signal_return'][index])
        grp_2_idx.append(index)
    elif data['signal_return'][index] >= 0 and data['signal_return'][index] < 0.01:
        grp_3.append(data['signal_return'][index])
        grp_3_idx.append(index)
    elif data['signal_return'][index] >= 0.01:
        grp_4.append(data['signal_return'][index])
        grp_4_idx.append(index)
grp_1_idx = [x+3 for x in grp1_idx if x+3 < len(data.index)]
grp_2_idx = [x+3 for x in grp2_idx if x+3 < len(data.index)]
grp_3_idx = [x+3 for x in grp3_idx if x+3 < len(data.index)]
grp_4_idx = [x+3 for x in grp4_idx if x+3 < len(data.index)]

#calculate the average return
average_returns = [np.mean(data['price_return'][grp_1_idx]),
                  np.mean(data['price_return'][grp_2_idx]),
                  np.mean(data['price_return'][grp_3_idx]),
                  np.mean(data['price_return'][grp_4_idx])]
grps = ['<-0.01', '-0.01:0', '0:0.01', '>0.01']


# In[73]:


average_returns


# In[78]:


plt.bar(grps, average_returns)
plt.title('Plot of average return')
plt.xlabel('Groups of singal return')
plt.ylabel('Average returns across group')
plt.show()


# In[ ]:


value = [100]
investment_available = 100
data['buy_signal'] = pd.Series(np.zeros(len(data.index)))
data['sell_signal'] = pd.Series(np.zeros(len(data.index)))
invested = False
for i in range(len(data.index)):
    
    if data['buy_signal'][i] == 1:
        shares = investment_available/data['ClosePrice'][i]
        invested = True
        
    if data['sell_signal'][i] == 1:
        investment_available = shares * data['ClosePrice'][i]
        
    if data['signal_return'][i] < 0 and invested == False:
        data['buy_signal'][i+3] = 1
        
        
    if invested == False:
        value.append(value[i-1])
        
    if invested == True:
        value.append(shares*data['ClosePrice'][i])
        
    if data['sell_signal'][i] == 1:
        invested = False
        
    if data['signal_return'][i] > 0.01 and invested == True:
        data['sell_signal'][i+3] = 1


# In[79]:


plt.plot(data['Date'], value[1:])
plt.xlabel('Date')
plt.ylabel('value of portfolio')
plt.title('Change in value of portfolio')
plt.show()


# In[80]:


total_return = value[-1]/value[0] -1 
total_return
plt.plot(data['ClosePrice'], data['buy_signal'])
risk_free = 0.01 #1% rate of return on risk free asset
portfolio_return = total_return # Calculated above
std = np.std(pd.Series(value).pct_change())
sharpe = (total_return - risk_free) / std
sharpe


# In[ ]:




