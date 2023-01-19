import re
from collections import Counter

# Notice: do not change these function name
def is_palindrome(x):

    
    temp = x
    #assign value
    result = 0
   #check Conditions
    if x<0:
        return False
    else:
        while(x>0):
            r=x%10
            result = result*10 + r
            x = x//10
    if(temp == result):
        return True
    else:
        return False
        
    
       
def is_anagrams(s, t):
 
 # Declare a empty dictionary for s and t
    d1={}
    d2={}
 # check length  
    if len(s)!=len(t):
        return False
    else:
        for char_s in s:
            d1[char_s] = s.count(char_s)
        #print(d1)
        for char_t in t:
            d2[char_t] = t.count(char_t)
        #print(d2)
        
        if d1==d2:
            return True
        else:
            return False



def top_k_words(s, k):
    
    #remove the spaces and special characters 
    new_word = re.sub(r'[^a-zA-Z0-9]',' ',s).split()
    #print("List:",new_word)
    count_word = Counter(new_word)
    #store two most common words 
    temp =  count_word.most_common(2)
    #Declare empty list
    res = []
    for i in temp:
        res.append(i[0])
    return res
    

def gradient_descent(x, y, m, c, epochs, L=0.001):
    for i in range(epochs):
    #Assign the values
     dm = 0
     dc = 0
     #Declare the empty list
     Dm=[]
     Dc=[]
     for i in range(len(x)):
        Ypred = m*x[i][0] + c
        a = x[i][0]*(Ypred-y[i])
        Dm.append(a)
        b = (Ypred-y[i])
        Dc.append(b)
     dm_sum=0
     for i in Dm:
        dm_sum = dm_sum+i
     dm = dm_sum/len(Dm)

     dc_sum=0
     for i in Dc:
        dc_sum = dc_sum+i
     dc = dc_sum/len(Dc)

     m = m - L * dm
     c = c - L * dc
    #return m and c
    return m,c
    


if __name__ == "__main__":  
    
    # Test Question 1
    
    print("\nQ1")
    q1_test1 = 121
    q1_test2 = -121
    q1_test3 = 0
    q1_answer1 = is_palindrome(q1_test1)
    q1_answer2 = is_palindrome(q1_test2)
    q1_answer3 = is_palindrome(q1_test3)
    print(q1_answer1)
    print("right answer: True")
    print("--------------")
    print(q1_answer2)
    print("right answer: False")
    print("--------------")
    print(q1_answer3)
    print("right answer: True")

    
    print("\nQ2")
    q2_test1_s = "anagram"
    q2_test1_t = "nagaram"
    q2_answer1 =  is_anagrams(q2_test1_s,  q2_test1_t)
    print(q2_answer1)
    print("right answer: True")

    print("--------------")
    q2_test2_s = "python"
    q2_test2_t = "py"
    q2_answer2 =  is_anagrams(q2_test2_s, q2_test2_t)
    print(q2_answer2)
    print("right answer: False")
    print("--------------")

    # test question 3
    print("\nQ3")
    q3_test1_s = "   i love python, he    love coding python. the course is about python. "
    q3_test1_k = 2
    q3_answer = top_k_words(q3_test1_s, q3_test1_k)
    print(q3_answer)
    print("right: answer:")
    print("['python', 'love']")

    print ("\nQ4")

    x = [[0.18], [1.0], [0.92], [0.07], [0.85], [0.99], [0.87]]
    y = [109.85, 155.72, 137.66, 76.17, 139.75, 162.6, 151.77]
    m = 0
    c = 0
    q4_epochs200 = 200
    q4_epochs500 = 500
    q4_epochs1000 = 1000
    q4_epochs2000 = 2000
    q4_epochs3000 = 3000
    q4_answer1 = gradient_descent(x,y,m,c,q4_epochs200)
    q4_answer2 = gradient_descent(x,y,m,c,q4_epochs500)
    q4_answer3 = gradient_descent(x,y,m,c,q4_epochs1000)
    q4_answer4 = gradient_descent(x,y,m,c,q4_epochs2000)
    q4_answer5 = gradient_descent(x,y,m,c,q4_epochs3000)
    print(q4_answer1)
    print("right answer:")
    print("17.724810647355827, 22.97599012903927")
    print("--------------")
    print(q4_answer2)
    print("right answer:")
    print("35.97890301691016, 46.54235227399102")
    print("--------------")
    print(q4_answer3)
    print("right answer:")
    print("52.816639894324545, 68.05971340716786")
    print("--------------")
    print(q4_answer4)
    print("right answer:")
    print("64.56549666509812, 82.46678636085996")
    print("--------------")
    print(q4_answer5)
    print("right answer:")
    print("67.42648874428104, 85.32444456113602")
    print("--------------")