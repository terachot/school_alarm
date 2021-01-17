file = open('scores_file.txt')

#อ่านทั้งหมด
#print(file.read())

#อ่านทีละบรรทัด
print(file.readline())
print(file.readline())

#ค่าที่อ่านจะเป็นข้อความ
for score in file:
    print(int(score))

file.close()

file_group = open('scores_group_file.txt')

for group_scores in file_group:
    group_scores_list = group_scores.split(' ')
    for score in group_scores_list:
        print(score)

file_group.close()



