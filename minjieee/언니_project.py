import sys
import copy


try:
    readfile = sys.argv[1] 
except IndexError:
    readfile = "students.txt"

stud = open(readfile,"r")

stud_dic = {}

# print("%7s %15s %10s %10s %10s %10s" % ("Student","Name","Midterm","Final","Average","Grade"))
# print("----------------------------------------------------------------------")


def stud_grade(stud_avg) :
    if stud_avg >= 90:
        grade = "A"
    elif stud_avg >= 80:
        grade = "B"
    elif stud_avg >= 70:
        grade = "C"
    elif stud_avg >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade


for i in stud:
    number, name, mid, fin = i.split("\t")
    number = int(number)
    mid = int(mid)
    fin = int(fin)
    stud_avg = (int(mid) + int(fin)) / 2
    grade = stud_grade(stud_avg)
    stud_dic[number] = [name, mid, fin, stud_avg, grade]
    
stud_sorted_avg = dict(sorted(stud_dic.items(), key = lambda a: a[1][3], reverse = True))

# for i in stud_sorted_avg.keys() :
#         print(i, "\t", stud_sorted_avg[i][0], "\t",stud_sorted_avg[i][1], "\t",stud_sorted_avg[i][2], 
#               "\t",stud_sorted_avg[i][3], "\t",stud_sorted_avg[i][4])
        
        
def show():
    
    print("Student","\t","Name","\t","Midterm","\t","Final","\t","Average","\t","Grade","\t")
    print("----------------------------------------------------------------------")
    
    stud_sorted_avg = dict(sorted(stud_dic.items(), key = lambda a: a[1][3], reverse = True))
    
    for i in stud_sorted_avg.keys() :
        print(i, "\t", stud_sorted_avg[i][0], "\t",stud_sorted_avg[i][1], "\t",stud_sorted_avg[i][2], 
              "\t",stud_sorted_avg[i][3], "\t",stud_sorted_avg[i][4])



def search():
    
    s_name = int(input("Student ID: "))
    
    if s_name in stud_dic.keys():
        print("Student","\t","Name","\t","Midterm","\t","Final","\t","Average","\t","Grade","\t")
        print("----------------------------------------------------------------------")
        print(s_name, "\t", stud_sorted_avg[s_name][0], "\t",stud_sorted_avg[s_name][1], "\t",
              stud_sorted_avg[s_name][2], "\t",stud_sorted_avg[s_name][3], "\t",stud_sorted_avg[s_name][4])
    else:
        print("NO SUCH PERSON")
        


def changescore():
    
    s_name = int(input("Student ID: "))
    
    if s_name not in stud_dic.keys():
        print("NO SUCH PERSON")
    else:
        c_score = input("Mid/Final? ")
                      
        if c_score == "mid":
            ch_score = int(input("Input new score: "))
            
            if ch_score >= 0 and ch_score <= 100:
                print("Student","\t","Name","\t","Midterm","\t","Final","\t","Average","\t","Grade","\t")
                print("----------------------------------------------------------------------")
                print(s_name, "\t", stud_sorted_avg[s_name][0], "\t",stud_sorted_avg[s_name][1], 
                      "\t",stud_sorted_avg[s_name][2], "\t",stud_sorted_avg[s_name][3],
                      "\t",stud_sorted_avg[s_name][4])
                
                stud_sorted_avg[s_name][1] = ch_score
                stud_sorted_avg[s_name][3] = (stud_sorted_avg[s_name][1] + stud_sorted_avg[s_name][2]) / 2
                stud_sorted_avg[s_name][4] = stud_grade(stud_sorted_avg[s_name][3])
                
                print("Score changed")
                print("Student","\t","Name","\t","Midterm","\t","Final","\t","Average","\t","Grade","\t")
                print("----------------------------------------------------------------------")
                print(s_name, "\t", stud_sorted_avg[s_name][0], "\t",stud_sorted_avg[s_name][1], 
                      "\t",stud_sorted_avg[s_name][2], "\t",stud_sorted_avg[s_name][3],
                      "\t",stud_sorted_avg[s_name][4])
                
        if c_score == "fin":
            ch_score = int(input("Input new score: "))
            
            if ch_score >= 0 and ch_score <= 100:
                print("Student","\t","Name","\t","Midterm","\t","Final","\t","Average","\t","Grade","\t")
                print("----------------------------------------------------------------------")
                print(s_name, "\t", stud_sorted_avg[s_name][0], "\t",stud_sorted_avg[s_name][1], 
                      "\t",stud_sorted_avg[s_name][2], "\t",stud_sorted_avg[s_name][3],
                      "\t",stud_sorted_avg[s_name][4])
                
                stud_sorted_avg[s_name][2] = ch_score
                stud_sorted_avg[s_name][3] = (stud_sorted_avg[s_name][1] + stud_sorted_avg[s_name][2]) / 2
                stud_sorted_avg[s_name][4] = stud_grade(stud_sorted_avg[s_name][3])
                
                print("Score changed")
                print("Student","\t","Name","\t","Midterm","\t","Final","\t","Average","\t","Grade","\t")
                print("----------------------------------------------------------------------")
                print(s_name, "\t", stud_sorted_avg[s_name][0], "\t",stud_sorted_avg[s_name][1], 
                      "\t",stud_sorted_avg[s_name][2], "\t",stud_sorted_avg[s_name][3],
                      "\t",stud_sorted_avg[s_name][4])
                
                stud_sorted_avg({s_name : [stud_sorted_avg[s_name][0],stud_sorted_avg[s_name][1],
                                           stud_sorted_avg[s_name][2],stud_sorted_avg[s_name][3],
                                           stud_sorted_avg[s_name][4]]})



def add():
    s_name = int(input("Student ID: "))
    
    if s_name in stud_dic.keys():
        print("ALREADY EXISTS")
    else:
        a_name = input("Name: ")
        a_mid = int(input("Midterm Score: "))
        a_fin = int(input("Final Score: "))
        a_avg = (a_mid + a_fin) / 2
        a_grd = stud_grade(a_avg)
        
        stud_sorted_avg[s_name] = [a_name, a_mid, a_fin, a_avg, a_grd]
        print("Student  added")
        


def searchgrade():
    s_grade = input("Grade to search: ")

    if s_grade in ['A','B','C','D','F']:
        print("Student","\t","Name","\t","Midterm","\t","Final","\t","Average","\t","Grade","\t")
        print("----------------------------------------------------------------------")
        
        for i in stud_sorted_avg.keys():
            if s_grade == stud_sorted_avg[i][4]:
                
                print(i, "\t", stud_sorted_avg[i][0], "\t",stud_sorted_avg[i][1], 
                      "\t",stud_sorted_avg[i][2], "\t",stud_sorted_avg[i][3],
                      "\t",stud_sorted_avg[i][4])   
    else:
        print("NO RESULTS")
        


def remove():
    re_stud = int(input("Student ID: "))
    
    if stud_sorted_avg == {}:
        print("List id empty.")
    else:
        if re_stud not in stud_sorted_avg.keys():
            print("NO SUCH PERSON.")
        else:
            del stud_sorted_avg[re_stud]
            print("Student removed.")
            

def quit():
    q = input("Save data?[yes/no] ")
    
    if q == "yes":
        filename = input("File name: ")
        file_o = open(filename, "w")
        
        stud_sorted_name = dict(sorted(stud_sorted_avg.items(), key = lambda a: a[1][3], reverse = True))
        
        for i in stud_sorted_name.keys():
            list_c = "%d\t%s\t%d\t%d\t%1.f\t%s\n" %(i,stud_sorted_name[i][0],stud_sorted_name[i][1], 
                      stud_sorted_name[i][2],stud_sorted_name[i][3],
                      stud_sorted_name[i][4])
            
            file_o.write(list_c)
        file_o.close()
        
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
    else :
        print("wrong input!")
        
stud.close()