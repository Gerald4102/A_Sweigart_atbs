#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with answer key.
import random

# The quiz data. Keys are English counties and values are the headquarters.
hqs = {'Bedfordshire': 'Bedford', 
       'Berkshire': 'Reading',
       'Buckinghamshire': 'Aylesbury',
       'Dorset': 'Dorchester',
       'Cambridgeshire': 'Cambridge',
       'Cambridgeshire': 'March',
       'Cheshire': 'Chester ',
       'Cornwall': 'Truro',
       'County Durham': 'Durham',
       'Cumberland': 'Carlisle',
       'Derbyshire': 'Matlock',
       'Devon': 'Exeter',
       'East Riding of Yorkshire': 'Beverley',
       'Essex': 'Chelmsford',
       'Gloucestershire': 'Gloucester',
       'Hampshire': 'Winchester',
       'Hampshire': 'Newport',
       'Herefordshire': 'Hereford',
       'Hertfordshire': 'Hertford',
       'Huntingdonshire': 'Huntingdon',
       'Kent': 'Maidstone',
       'Lancashire': 'Preston',
       'Leicestershire': 'Glenfield',
       'Lincolnshire': 'Boston',
       'Lincolnshire': 'Sleaford',
       'Lincolnshire': 'Lincoln',
       'London': 'Lambeth',
       'Middlesex': 'Westminster',
       'Monmouthshire': 'Newport',
       'Norfolk': 'Norwich',
       'North Riding of Yorkshire': 'Northallerton',
       'Northamptonshire': 'Northampton',
       'Northamptonshire': 'Peterborough',
       'Northumberland': 'Morpeth',
       'Nottinghamshire': 'West Bridgford',
       'Oxfordshire': 'Oxford',
       'Rutland': 'Oakham',
       'Shropshire': 'Shrewsbury',
       'Somerset': 'Taunton',
       'Staffordshire': 'Stafford',
       'Suffolk': 'Ipswich',
       'Suffolk': 'Bury St Edmunds',
       'Surrey': 'Kingston upon Thames',
       'Sussex': 'Lewes',
       'Sussex': 'Chichester',
       'Warwickshire': 'Warwick',
       'Westmorland': 'Kendal',
       'West Riding of Yorkshire': 'Wakefield',
       'Wiltshire': 'Trowbridge',
       'Worcestershire': 'Worcester'}

for quizNum in range(35):
       # Create the quiz and answer key files.
       quizFile = open(f'countiesquiz{quizNum + 1}.txt', 'w')
       answerFile = open(f'countiesquiz_answer{quizNum + 1}.txt', 'w')
       # Write the header for the quiz.
       quizFile.write('Name:\n\nDate:\n\n')
       quizFile.write(' ' * 20 + f'English Counties HQ quiz (Form {quizNum + 1})')
       quizFile.write('\n\n')
       # Shuffle order of counties.
       counties = list(hqs.keys())
       random.shuffle(counties)
       # Loop through counties to make a question for each county.
       for questionNum in range(len(hqs.keys())):
              correctAnswer = hqs[counties[questionNum]]
              wrongAnswers = list(hqs.values())
              del wrongAnswers[wrongAnswers.index(correctAnswer)]
       # Close the files.
       quizFile.close()
       answerFile.close()