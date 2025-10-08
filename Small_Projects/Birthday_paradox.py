import datetime, random


def getBirthdays(NosOfBdays):
    """Returns a list of number random date objs for bdays"""
    birthdays = []
    for i in range(NosOfBdays):
        startOfYear = datetime.date(2001,1,1)

        #getting a random day into the year
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """Returns the date obj of a bday that occurs more than once in the bdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None # All birthdays are unique, so return None.
    
    #compare each bday to every other bday
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA #Return the matching bday
            

#display the intro
print('This is the Birthday Paradox Problem')


#Setting up a tuple of month names in order
MONTHS = ('Jan', 'Feb','Mar','Apr','May','Jun',
          'Jul','Aug','Sep','Oct','Nov','Dec')

while True:
    print("How many birthday shall I generate ? (Max 100)")
    response = input('>')
    if response.isdecimal() and (0 < int(response)<=100):
        numBdays = int(response)
        break
print()

#generate and display the bdays
print('Here are', numBdays, 'birthdays:'):
birthdays = getBirthdays(numBdays)
for i, birthdays in enumerate(birthdays):
    if i != 0:
        print(',', end = '')