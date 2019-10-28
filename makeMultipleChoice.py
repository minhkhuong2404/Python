import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':'Springfield',
'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka', 'Kentucky': 'Frankfort',
'Louisiana': 'Baton Rouge', 'Maine':'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
'Michigan':'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(1):
    quizFile = open('capitalquiz%s.txt' %(quizNum + 1), 'w')
    answerKeysFile = open('capitalquiz_answer%s.txt' %(quizNum + 1), 'w')

    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' '* 20) + 'State Capital Quiz (Form %s)' %(quizNum + 1))
    quizFile.write('\n\n')

    #shuffle order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]] # stored as a value of capital dictionary
        wrongAnswers = list(capitals.values()) #list of possible wrong answer by duplicate all the capitals
        del wrongAnswers[wrongAnswers.index(correctAnswer)] # deleting correctAnswer
        wrongAnswers = random.sample(wrongAnswers,3) # select three random values from list
        answerOptions = wrongAnswers + [correctAnswer] #this is a list that's why we have [correctAnswer]
        random.shuffle(answerOptions)

        # write question and answer options
        quizFile.write('%s. What is the capital of %s?\n' %(questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n' %('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        #write the answer key to the file
        answerKeysFile.write('%s. %s\n' %(questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeysFile.close()
