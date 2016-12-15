import csv

hw_markup = open('homework.md', 'w')
assignments = list(csv.reader(open('homework.csv', 'rU')))

hw_markup.write('---\nlayout: post\ntitle: "Homework Problems"\n')
hw_markup.write('categories: [syllabus]\ntags: [syllabus]\n')
hw_markup.write('description: MC-MATH-141\n---\n\n')

hw_markup.write('* [Chapter 1](#chapter-1)\n')
hw_markup.write('* [Chapter 2](#chapter-2)\n')
hw_markup.write('* [Chapter 3](#chapter-3)\n')
hw_markup.write('* [Chapter 4](#chapter-4)\n')
hw_markup.write('* [Chapter 5](#chapter-5)\n')

current_chapter = '1'
hw_markup.write('\n' + '## Chapter 1' + '\n')
for hw in assignments[1:]:
	if not str(hw[0][0]) == current_chapter:
		current_chapter = hw[0][0]
		chapter = '\n\n' + '## Chapter ' + str(current_chapter) + '\n'
	else:
		chapter = ''
	section  = '* Section ' + str(hw[0]) + ' homework:\n'
	practice = '    * practice problems: '     + str(hw[1]) + '\n'
	easy     = '    * easy problems: '         + str(hw[2]) + '\n'
	hard     = '    * hard problems: '         + str(hw[3]) + '\n'
	xcr      = '    * extra credit problems: ' + str(hw[4]) + '\n'
	hw_markup.write(chapter + section + practice + easy + hard + xcr)