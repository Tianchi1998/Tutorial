mathStudents = ['Audrey','Ben','Julia','Paul','Gerry',
                'Sue','Helena','Harry','Marco','Rachel',
                'Tina','Mark','Jackson']

csStudents = ['William','Melissa','Sue','Ben','Audrey',
              'Susan','Mark','Hemi','Brendan',
              'Paul','Barry','Julia']

print("There are %d students in the Maths class."%(len(mathStudents)))
print("There are %d students in the Compsci class."%(len(csStudents)))
print()

sum=0
for student in mathStudents:
    if student in csStudents:
        sum=sum+1
        print("Student: %s is enrolled in both classes"%(student))

print()
print("%d students are enrolled in Computer Science and Maths"%(sum))

