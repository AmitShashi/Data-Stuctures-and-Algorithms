#Uncommon characters

#Given two strings A and B. Find the characters that are not common in the two strings. 

class Solution:
    def UncommonChars(self,A, B):
        
        #step1: remove duplicate characters in each string using set
        #step2: count no. of each characters present in both set using same dictionary
        #step3: if count is 1 then that character is uncommon so add it to ans string
        #step4: return answer string
        
        x=set(A)                    #step1
        y=set(B)
        
        Map=dict()
        temp=[]
        res=""
        
        for i in x:                 #Step2
            if i in Map:
                Map[i]+=1
            else:
                Map[i]=1
                
        for i in y:
            if i in Map:
                Map[i]+=1
            else:
                Map[i]=1
                
        for k,v in Map.items():     #Step3: Part1
            if v == 1 :
                temp.append(k)
        
        temp.sort()       
        
        for i in temp:              #Step3: Part2
            res+=i
        
        if res=="":                 #Step4
            return -1
        return res
