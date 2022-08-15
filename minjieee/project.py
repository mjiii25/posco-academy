#!/usr/bin/env python
# coding: utf-8

# # 성적 관리 프로그램
# 
# C1조 성민지
# 
# ---

# In[ ]:


import sys
import copy

try :
    readfile = sys.argv[1]
except IndexError :
    readfile = 'students.txt'
    

stud = open(readfile, "r")
# stud = open("students.txt", "r")
stud_dic = {}




def grading(avg) :
    if avg >= 90 :
        grade = "A"
    elif avg >= 80 :
        grade = "B"
    elif avg >= 70 :
        grade = "C"
    elif avg >= 60 :
        grade = "D"
    else :
        grade = "F"
    return grade






for x in stud :
    num, name, mid, fin = x.split("\t")
    num, mid, fin = int(num), int(mid), int(fin)
    avg = (mid + fin) / 2
    grade = grading(avg)
    stud_dic[num] = [name, mid, fin, avg, grade]
       
sort_stud_dic = dict(sorted(stud_dic.items(), key = lambda a: a[1][3], reverse = True))

print("{0:>13} {1:^13} {2:^13} {3:^13} {4:^13} {5:^13}".format("Student", "Name", "Midterm", "Final", "Average", "Grade"))
print("-----------------------------------------------------------------------------------")

for x in sort_stud_dic.keys() :
    print("{0:>13} {1:^13} {2:^13} {3:^13} {4:^13} {5:^13}".format(x, 
                                                                   sort_stud_dic[x][0], 
                                                                   sort_stud_dic[x][1], 
                                                                   sort_stud_dic[x][2], 
                                                                   sort_stud_dic[x][3],
                                                                   sort_stud_dic[x][4]))



        
        
        
        
        


def show() :
           
    
    print("{0:>13} {1:^13} {2:^13} {3:^13} {4:^13} {5:^13}".format("Student", "Name", "Midterm", "Final", "Average", "Grade"))
    print("-----------------------------------------------------------------------------------")

    sort_stud_dic = dict(sorted(stud_dic.items(), key = lambda a: a[1][3], reverse = True))
          
    for x in sort_stud_dic.keys() :
        print("{0:>13} {1:^13} {2:^13} {3:^13} {4:^13} {5:^13}".format(x, 
                                                                       sort_stud_dic[x][0], 
                                                                       sort_stud_dic[x][1], 
                                                                       sort_stud_dic[x][2], 
                                                                       sort_stud_dic[x][3],
                                                                       sort_stud_dic[x][4]))










def search() :
    
    val = int(input("Student ID: "))
    
    
    if val in stud_dic.keys() :
        print("{0:>13} {1:^13} {2:^13} {3:^13} {4:^13} {5:^13}".format("Student", "Name", "Midterm", "Final", "Average", "Grade"))
        print("-----------------------------------------------------------------------------------")
        print("{0:>13} {1:^13} {2:^13} {3:^13} {4:^13} {5:^13}".format(x, 
                                                                       stud_dic[val][0], 
                                                                       stud_dic[val][1], 
                                                                       stud_dic[val][2], 
                                                                       stud_dic[val][3],
                                                                       stud_dic[val][4]))
    else :
        print("NO SUCH PERSON.")



        
        
        
        
        
        

        

def changescore() :
    
    
    
    val = int(input("Student ID: "))
    
    if val not in stud_dic.keys() :
        print("NO SUCH PERSON.")    
    else :        
        val1 = input("Mid/Final? ")
        
        if val1 == "mid" :      
            
            val2 = int(input("Input new score: "))
            if val2 >= 0 and val2 <= 100 :
                
                print("{0:>13} {1:^13} {2:^13} {3:^13} {4:^13} {5:^13}".format("Student", "Name", "Midterm", "Final", "Average", "Grade"))
                print("-----------------------------------------------------------------------------------")
                print("{0:>13} {1:^13} {2:^13} {3:^13} {4:^13} {5:^13}".format(val, 
                                                                               stud_dic[val][0], 
                                                                               stud_dic[val][1], 
                                                                               stud_dic[val][2], 
                                                                               stud_dic[val][3],
                                                                               stud_dic[val][4]))

                
                stud_dic[val][1] = val2
                stud_dic[val][3] = (stud_dic[val][1] + stud_dic[val][2]) / 2
                stud_dic[val][4] = grading(stud_dic[val][3])
                
                print("Score changed.")
                print("{0:>13} {1:^13} {2:^13} {3:^13} {4:^13} {5:^13}".format(val, 
                                                                               stud_dic[val][0], 
                                                                               stud_dic[val][1], 
                                                                               stud_dic[val][2], 
                                                                               stud_dic[val][3],
                                                                               stud_dic[val][4]))
        
                
        if val1 == "Final" :
            val2 = int(input("Input new score: "))
            if val2 >= 0 and val2 <= 100 :
                
                print("{0:>13} {1:^13} {2:^13} {3:^13} {4:^13} {5:^13}".format("Student", "Name", "Midterm", "Final", "Average", "Grade"))
                print("-----------------------------------------------------------------------------------")
                print("{0:>13} {1:^13} {2:^13} {3:^13} {4:^13} {5:^13}".format(val, 
                                                                               stud_dic[val][0], 
                                                                               stud_dic[val][1], 
                                                                               stud_dic[val][2], 
                                                                               stud_dic[val][3],
                                                                               stud_dic[val][4]))
                
                stud_dic[val][2] = val2
                stud_dic[val][3] = (stud_dic[val][1] + stud_dic[val][2]) / 2
                stud_dic[val][4] = grading(stud_dic[val][3])
                
                print("Score changed.")        
                print("{0:>13} {1:^13} {2:^13} {3:^13} {4:^13} {5:^13}".format(val, 
                                                                               stud_dic[val][0], 
                                                                               stud_dic[val][1], 
                                                                               stud_dic[val][2], 
                                                                               stud_dic[val][3],
                                                                               stud_dic[val][4]))
                
                
                stud_dic.update({val : [stud_dic[val][0], 
                                        stud_dic[val][1],
                                        stud_dic[val][2], 
                                        stud_dic[val][3], 
                                        stud_dic[val][4]]})
                
                
                
                
                
                
                
                

                


def add() :
     
    val = int(input("Student ID: "))
    
    if val in stud_dic.keys() :
        print("ALREADY EXISTS.")
    else :
        val1 = input("Name: ")
        val2 = int(input("Midterm Score: "))
        val3 = int(input("Final Score: "))        
        val4 = (val2 + val3) / 2
        val5 = grading(val4)
        
        stud_dic[val] = [val1, val2, val3, val4, val5]
        print("Student added.")

        
        
        
        
        
        


def searchgrade() :
    k = 0
    val = input("Grade to search: ")
    
    
    if val not in ["A", "B", "C", "D", "F"] :
        pass
    else : 
        for x in stud_dic.keys() : 
            if val == stud_dic[x][4] :
                print("{0:>13} {1:^13} {2:^13} {3:^13} {4:^13} {5:^13}".format("Student", "Name", "Midterm", "Final", "Average", "Grade"))
                print("-----------------------------------------------------------------------------------")
                print("{0:>13} {1:^13} {2:^13} {3:^13} {4:^13} {5:^13}".format(x,
                                                                               stud_dic[x][0],
                                                                               stud_dic[x][1], 
                                                                               stud_dic[x][2], 
                                                                               stud_dic[x][3],
                                                                               stud_dic[x][4]))
            else :
                k += 1
                
    if k == len(stud_dic.keys()) :
        print("NO RESULTS.")
    
    
    
    
    
    
    
    




def remove() :
    
    if stud_dic == {} :
        print("List is empty.")
    else :
        val = int(input("Student ID: "))
        if val not in stud_dic.keys() :
            print("NO SUCH PERSON.")
        else:
            del stud_dic[val]
            print("Student removed.")




            
            
            
            
            



def quit() :
    
    q1 = input("Save data?[yes/no] ")
    
    if q1 == "yes" :
        file_name = input("File name: ")
        fw = open(file_name, "w")
        
        sort_stud_dic = dict(sorted(stud_dic.items(), key = lambda a: a[1][3], reverse = True))
        
        for x in sort_stud_dic.keys() :
            data = "%d\t %s\t %d\t %d\t %1.f\t %s\n" % (x, sort_stud_dic[x][0], 
                                                        sort_stud_dic[x][1], 
                                                        sort_stud_dic[x][2], 
                                                        sort_stud_dic[x][3], 
                                                        sort_stud_dic[x][4])
            fw.write(data)
        fw.close()


        



        
        
    

while True :
    command = input("# ")
    command = command.casefold()
    
    if command == "show" :
        show()
    elif command == "search" :
        search()
    elif command == "changescore" :
        changescore()
    elif command == "searchgrade" :
        searchgrade()
    elif command == "add" :
        add()
    elif command == "remove" :
        remove()
    elif command == "quit" :
        quit()
        break

    
stud.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




