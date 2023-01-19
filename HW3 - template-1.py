#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Notice: do not change these function name 
class MovingAverage:

    def __init__(self, size):
        self.size=size
        #The values of the input will be saved in a results list.
        self.val1=list()
                
    def next(self, val):
        self.val1.append(val)
        total=0
        #if an items in values are smaller than the original of the window
        if len(self.val1)<self.size:
                for i in self.val1:
                        total=total+i
                return round(total/len(self.val1),5)
        else:
                total=self.val1[-1]+self.val1[-2]+self.val1[-3]
                return round(total/self.size,5)
#Using the given input, put the class to the check.
result=list()
result.append(None)
movingAverage=MovingAverage(3)
#To get the moving average, execute the next() function.
result.append(movingAverage.next(1))
result.append(movingAverage.next(10))
result.append(movingAverage.next(3))
result.append(movingAverage.next(5))
print(result)
    
    
    
class subway:

    def __init__(self):
        #pass
            self.totl_time = dict()       
            self.chck_in_time = dict()
        
    def checkIn(self, id, stationName, t):
       self.chck_in_time[id] = (t, stationName)    
    
    def checkOut(self, id, stationName, t):
        # recalculate your travel times between startStation to endStation
        startStation = self.chck_in_time[id][1]
        endStation = stationName
        time_travel = t - self.chck_in_time[id][0]
        if (startStation, endStation) in self.totl_time:
            totl_time = time_travel + self.totl_time[(startStation, endStation)][0]
            num_of_check_out = self.totl_time[(startStation, endStation)][1] + 1
            self.totl_time[(startStation, endStation)] = (totl_time, num_of_check_out)
        else:
            self.totl_time[(startStation, endStation)] = (time_travel, 1)
        # Eliminate the id from the chck_in_time_dict
        self.chck_in_time.pop(id)
    
    def getAverageTime(self, startStation, endStation):
         totl_time, num_of_customers = self.totl_time[(startStation, endStation)]
         return totl_time / num_of_customers 
       # pass

    

class Linear_regression:
  
  #initialize a value 
    m=0
    c=0 
    epochs = 0
    L = 0
  
    def __init__(self, x, y, m, c, epochs, L):
    
        
        self.m = m
        self.c = c
        self.epochs = epochs
        self.L = L
        self.x = x
        self.y = y
      
       
        
        
    def gradient_descent(self):
        for i in range(self.epochs):
            #Assign the values
            dm = 0
            dc = 0
            # Declare a empty dictionary
            Dm=[]
            Dc=[]
            for i in range(len(self.x)):
             Ypred = self.m*self.x[i][0] + self.c
             a = self.x[i][0]*(Ypred-self.y[i])
             #append value
             Dm.append(a)
            
             b = (Ypred-self.y[i])
            #append value
             Dc.append(b)
             dm_sum=0
             # For loop
            for i in Dm:
                 dm_sum = dm_sum+i
                 dm = dm_sum/len(Dm)
            dc_sum=0
            for i in Dc:
                dc_sum = dc_sum+i
                dc = dc_sum/len(Dc)

            self.m = self.m - self.L * dm
            self.c = self.c - self.L * dc
        return self.m,self.c
    
    
    def predict(self,x_new):
        #Declare a empty list
        y = []
        # for loop for finding the value y
        for i in range(len(x_new)):
         Ypred = self.m*x_new[i] + self.c
         y.append(Ypred)
        return y
            
    
    
class LCG:

    def __init__(self, seed, multiplier, increment, modulus):  
        # add your code here    
        pass
        
    def get_seed(self):   
        # add your code here    
        pass
         
    def set_seed(self,new_seed):   
        # add your code here    
        pass
    
    def initialize(self):
       # add your code here    
        pass
    
    def gen(self):
        # add your code here    
        pass
        
    def seq(self, num):  
        # add your code here    
        pass

#


if __name__ == "__main__":  

    x = [[0.18], [1.0], [0.92], [0.07], [0.85], [0.99], [0.87]]
    y = [109.85, 155.72, 137.66, 76.17, 139.75, 162.6, 151.77]
    x_new = [0.9,0.8,0.40,0.7]

    
    # Test Question 1
    print("\nQ1")    
    windowsize = 3 
    moving_average = MovingAverage(windowsize)
    step1 = moving_average.next(1)  
    print("my answer: ", step1)    
    print("right answer: 1.0")    
    print("--------------")
    step2 = moving_average.next(10) 
    print("my answer: ", step2)    
    print("right answer: 5.5")    
    print("--------------")  
    step3 = moving_average.next(3) 
    print("my answer: ", step3)    
    print("right answer: 4.66667")    
    print("--------------") 
    step4 = moving_average.next(5) 
    print("my answer: ", step4)    
    print("right answer: 6.0")    
    print("--------------") 
    
    
    
    # Test Question 2
    print("\nQ2") 
    s = subway()
    s.checkIn(10,'Leyton',3)
    s.checkOut(10,'Paradise',8)
    print("my answer: ",s.getAverageTime('Leyton','Paradise'))
    print("right answer: 5.0")    
    print("--------------") 
    s.checkIn(10,'Leyton',10)
    s.checkOut(10,'Paradise',16)
    print("my answer: ",s.getAverageTime('Leyton','Paradise'))
    print("right answer: 5.5")    
    print("--------------") 
    s.checkIn(10,'Leyton',21)
    s.checkOut(10,'Paradise',30)
    print("my answer: ",s.getAverageTime('Leyton','Paradise'))
    print("right answer: 6.667")    
    print("--------------") 
    
    
    # Test Question 3
    print("\nQ3") 
    Linear_model = Linear_regression(x,y,0,0,500,0.001)
    print("I use m=0, c=0, epochs=500, L=0.001")
    print("my m and c: ",Linear_model.gradient_descent())
    print("right m and c:(35.97890301691016, 46.54235227399102)")    
    print("--------------") 
    print("my predict: ", Linear_model.predict(x_new))
    print(" right predict: [78.92336498921017, 75.32547468751915, 60.93391348075509, 71.72758438582812]")
    
    
    # Bonus Question 
    print("\nBonus") 
    print("set seed = 1, multiplier = 1103515245, increment = 12345, modulus = 2**32")
    lcg = LCG(1,1103515245,12345, 2**32 )
    print("my seed is: ", lcg.get_seed())
    print("right seed is: 1")
    print("the seed is setted with: ", lcg.set_seed(5))
    print("right seed is setted with 5")
    print("the LCG is initialized with seed: ",lcg.initialize())
    print("the LCG is initialized with seed 5")
    print("the next random number is: ", lcg.gen())
    print("right next random number is: 0.2846636981703341")
    print("the first ten sequence is: ", lcg.seq(10))
    print("the first ten sequence is: ", [0.6290451611857861, 0.16200014390051365, 0.4864134492818266, 0.655532845761627, 0.8961918593849987, 0.2762452410534024, 0.8611323081422597, 0.9970241007395089, 0.798466683132574, 0.46138259768486023])



# %%
