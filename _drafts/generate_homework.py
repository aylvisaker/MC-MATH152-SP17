import csv

hw_markup = open('homework.md', 'w')
assignments = list(csv.reader(open('homework.csv', 'rU')))

hw_markup.write('---\nlayout: post\ntitle: "Homework Problems"\n')
hw_markup.write('categories: [syllabus]\ntags: [syllabus]\n')
hw_markup.write('description: MC-MATH-152\n---\n\n')

hw_markup.write('* [Chapter 5](#chapter-5)\n')
hw_markup.write('* [Chapter 6](#chapter-6)\n')
hw_markup.write('* [Chapter 7](#chapter-7)\n')
hw_markup.write('* [Chapter 8](#chapter-8)\n')
hw_markup.write('* [Chapter 9](#chapter-9)\n')
hw_markup.write('* [Chapter 10](#chapter-10)\n')
hw_markup.write('* [Chapter 11](#chapter-11)\n')

current_chapter = 5
hw_markup.write('\n' + '## Chapter 5' + '\n')
for hw in assignments[1:]:
    chap = hw[0].replace('Section ','').split('.')
    if not str(chap[0]) == str(current_chapter):
        current_chapter += 1
	chapter = '\n\n' + '## Chapter ' + str(current_chapter) + '\n'
    else:
        chapter = ''
    section  = '* ' + str(hw[0]) + ' homework:\n'
    practice = '    * practice problems: '     + str(hw[1]) + '\n'
    easy     = '    * easy problems: '         + str(hw[2]) + '\n'
    hard     = '    * hard problems: '         + str(hw[3]) + '\n'
    xcr      = '    * extra credit problems: ' + str(hw[4]) + '\n'
    hw_markup.write(chapter + section + practice + easy + hard + xcr)
