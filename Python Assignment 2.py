# Python Assignment 2- List Operations
age_list=[24,25,26,27,28]
print(age_list)
name_list=["Malu","Aami","Arun","Dhruv","Aichu"]
print(name_list)
name_list.append("Yazhini")
print(name_list)
age_list.insert(2,30)
print(age_list)
name_list.remove("Yazhini")
print(name_list)
age_list.pop()
print(age_list)
age_list.extend([29,30,26])
print(age_list)
age_list.sort()
print(age_list)
print(max(age_list))
print(min(age_list))
print(sum(age_list))
print(name_list[0])
print(name_list[-1])
print(name_list[2:5])
print(name_list[::-1])
student_marks={"Malu":85,
               "Aami":80,
               "Arun":90,
               "Dhruv":70,
               "Aichu":45}
print(student_marks)
print(student_marks["Dhruv"])
student_marks["Janani"]=80
print(student_marks)
student_marks["Arun"]=82
print(student_marks)
print(student_marks.keys())
print(student_marks.values())
print(student_marks.items())
my_set={'a','e','i','o','u','a','a','i'}
print(my_set)
#my_set[4]='s'
print(my_set)
#Sets are unordered collections and do not supportindexing.Therefore we cannot change an element using an index.
set1={1,3,5,7,9}
set2={2,3,5,8,10}
print(set1)
print(set2)
print("union:",set1.union(set2))
print("intersection:",set1.intersection(set2))
score = int(input("enter your score(0 to 10):"))
if score<0 or score>10:
          print("Invalid score")
elif  score>7:
        print("Above Average: Excellent work")
elif score>=4:
          print("Average:Good effort!Keep practising, there's  room for improvement.")
else:
     print("Below Average:Need to improve ")
     

    
