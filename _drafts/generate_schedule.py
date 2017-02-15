import datetime, csv

academic_calendar = [[1] * 5] * 6 + [[1,1,1,1,0]] + [[0] * 5] 
academic_calendar += [[1] * 5] * 4 + [[1,1,1,1,0]] + [[0,1,1,1,1]] 
academic_calendar += [[1,0,1,1,1]] + [[1,1,1,0,0]]
start = datetime.date(2017,1,16)

schedule_markup = open('schedule.md', 'w')
source = csv.reader(open('schedule.csv', 'rU'))
discussions = [item[1] for item in source]

schedule_markup.write('---\nlayout: post\ntitle: "Course Schedule"\n')
schedule_markup.write('categories: [syllabus]\ntags: [syllabus]\n')
schedule_markup.write('description: MC-MATH-152\n---\n\n')
schedule_markup.write('|Week|Start Date|Monday|Tuesday|Wednesday|Thursday|Friday|\n')
schedule_markup.write('|:---:|:---:|:---:|:---:|:---:|:---:|:---: |\n')
iterator = 0
lab_iterator = 0
for week in range(len(academic_calendar)):
    row = '|' + str(week + 1) + '|' + str(start + datetime.timedelta(days = 7 * week))[-5:] + '|'
    if academic_calendar[week][3]:
        lab_iterator += 1
    for day in [0,1,2,3,4]:
        current_day = start + datetime.timedelta(days = 7 * week + day)
        if not academic_calendar[week][day]:
            row += 'NO CLASS' + '|'
        else:
            iterator += 1
            row += discussions[iterator] + '|'
    schedule_markup.write(row + '\n')

print(iterator)
print(lab_iterator)
