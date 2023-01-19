import re
import pandas as pd
import numpy as np



#QUESTION 2
ctdf = pd.read_csv('res_purchase_2014.csv') #Import file
print('\n There are',ctdf.shape[0],'rows and',ctdf.shape[1],'columns\n')

#Define a function to clean 'Amount' Column
def amt_cln(amt):
    if '$' in str(amt):
        amt = amt.replace('$','')
    if '(' in str(amt):
        amt = amt.replace('(','-')
    if ')' in str(amt):
        amt = amt.replace(')','')
    amt = re.sub("[^-.0-9]", "", str(amt))
    return float(amt)

ctdf['Amount'] = ctdf.Amount.apply(amt_cln)

#1. 
print('\n Total Amt: ',round(sum(ctdf['Amount']),2),'dollars\n')

#2. 
garinger = ctdf.loc[ctdf['Vendor']=='WW GRAINGER']
print('\n Amt "WW GRAINGER" :' ,round(sum(garinger['Amount']),2),'dollars\n')

#3.
supercenter = ctdf.loc[ctdf['Vendor']=='WM SUPERCENTER']
print('\n Amt "WM SUPERCENTER" : ',round(sum(supercenter['Amount']),2),'dollars\n')

#4.
grocery_stores = ctdf.loc[ctdf['Merchant Category Code (MCC)'] =='GROCERY STORES,AND SUPERMARKETS']
print('\n Amount "GROCERY STORES" : ',round(sum(grocery_stores['Amount']),2),'dollars\n')


#QUESTION 3    - Data Processing with Pandas

#1 Question
Energy = 'Energy.xlsx'
BalanceSheet = pd.read_excel(Energy)

Rating = 'EnergyRating.xlsx'
Ratings  = pd.read_excel(Rating)

#2. drop the column if more than 30% value in this colnmn is 0 (or missing value).
BalanceSheet = BalanceSheet.fillna(0)
BalanceSheet = BalanceSheet.replace({0:np.nan})
BalanceSheet = BalanceSheet.dropna( axis=1, thresh=BalanceSheet.shape[1]*0.3)

Ratings = Ratings.fillna(0)
Ratings = Ratings.replace({0:np.nan})
Ratings = Ratings.dropna(axis=1, thresh=Ratings.shape[1]*0.3)

print('2 question Balancesheet',BalanceSheet.head(10))
print('2 question Rating',Ratings.head(10))

#3. drop the column if more than 90% value in this colnmn is 0 (or missing value).
BalanceSheet = BalanceSheet.fillna(0)
BalanceSheet = BalanceSheet.replace({0:np.nan})
BalanceSheet = BalanceSheet.dropna( axis=1, thresh=BalanceSheet.shape[1]*0.9)

Ratings = Ratings.fillna(0)
Ratings = Ratings.replace({0:np.nan})
Ratings = Ratings.dropna(axis=1, thresh=Ratings.shape[1]*0.9)

print('3 question Balancesheet',BalanceSheet.head(10))
print('3 question Rating',Ratings.head(10))


#4. replace all None or NaN with average value of each column.

BalanceSheet_clean = BalanceSheet.fillna(BalanceSheet.mean()) #fill numeric empty spaces with the average of their column
Ratings_clean = Ratings.fillna(Ratings.mean()) #fill numeric empty spaces with the average of their column



#5. Question
def normalize(x,column_min,column_max):
    if column_max == column_min:
        return x
    x = x-column_min/(column_max-column_min)
    return x


#Apply Normalization formula
#For BalanceSheet
for feature in BalanceSheet_clean.select_dtypes(include=[np.number]).columns:
    BalanceSheet_clean[feature] = BalanceSheet_clean[feature].apply(normalize,args=(BalanceSheet_clean[feature].min(),BalanceSheet_clean[feature].max()))

#For Ratings
for feature in Ratings_clean.select_dtypes(include=[np.number]).columns:
    Ratings_clean[feature] = Ratings_clean[feature].apply(normalize,args=(Ratings_clean[feature].min(),Ratings_clean[feature].max()))   

#6.find Correlation matrix
Energy = 'Energy.xlsx'
newBalanceSheet = pd.read_excel(Energy) #needed to make a new balance sheet since 'Assets Netting & Other Adjustments' was dropped earlier
b_Cols = newBalanceSheet[['Current Assets - Other - Total', 'Current Assets - Total', 'Other Long-term Assets', 'Assets Netting & Other Adjustments']]
print(b_Cols.corr())


#7. Merge
Matched_BR = pd.merge(BalanceSheet_clean,Ratings_clean,on=['Data Date','Global Company Key'],how='inner')
#print(Matched_BR.head(10))

#8. Mapping
match_maping = {'AAA':0,'AA+':1,'AA':2,'AA-':3,'A+':4,'A':5,'A-':6,'BBB+':7,
                                        'BBB':8,'BBB-':9,'BB+':10,'BB':11,'others':12}

Matched_BR['Rate'] = Matched_BR['S&P Domestic Long Term Issuer Credit Rating'].map(match_maping)       
#print('88888',Matched_BR['Rate'].head())




#Question 1:



class Linear_regression:
      
  #initialize a value 
    c=0 
    epochs = 0
    L=0.001
    def __init__(self,m, epochs, L,x,y):
        self.m = m
        self.epochs = epochs
        self.L = L
        self.c = 0
        self.x=x
        self.y=y
        
    def gradient_descent(self):
        for i in range(self.epochs):
            for i in range(len(self.x)):
             arr_result = self.m * self.x
             Ypred = arr_result + self.c
             δm = - self.x[i]*(Ypred-arr_result-self.c)
             δc = - 1 * (Ypred-arr_result-self.c),
            self.m = self.m-δm * self.L
            self.c = self.c- δc*self.L 
        return self.m,self.c
    
    def predict(self,x_new):
        #Declare a empty list
        y = []
        # for loop for finding the value y
        for i in range(len(x_new)):
         Ypred = self.m*x_new + self.c
         y.append(Ypred)
        return y
        
 
 

# Question 1
M=[0,0,0,0,0]
N=[0.18, 1.0, 0.92, 0.07, 0.85]
m=np.array([M], dtype = float)
x=np.array([N,M], dtype = float)
y = np.array([109.85, 155.72, 137.66, 76.17, 139.75, 162.6, 151.77],dtype = float)
x_new = [0.9,0.8,0.40,0.7]
Linear_model = Linear_regression(m,500,0.001,x,y)
print("I use m=0, c=0, epochs=500, L=0.001")
print("my m and c: ",Linear_model.gradient_descent())
print("right m and c:(35.97890301691016, 46.54235227399102)")    
print("--------------") 
# print("my predict: ", Linear_model.predict(x_new))
# print(" right predict: [78.92336498921017, 75.32547468751915, 60.93391348075509, 71.72758438582812]")
