import datetime, random

def getBirthdays(n):
    """Returns a list of n random date objects for birthdays."""
    birthdays = []
    startOfYear = datetime.date(2001, 1, 1)
    for _ in range(n):
        randomDays = datetime.timedelta(random.randint(0, 364))
        birthdays.append(startOfYear + randomDays)
    return birthdays


def getMatch(birthdays):
    """Returns the date object of a birthday that appears more than once."""
    if len(birthdays) == len(set(birthdays)):
        return None
    
    # Check for duplicates
    seen = set()
    for bday in birthdays:
        if bday in seen:
            return bday
        seen.add(bday)
    return None


# Display intro
print('This is the Birthday Paradox Problem')

MONTHS = ('Jan', 'Feb','Mar','Apr','May','Jun',
          'Jul','Aug','Sep','Oct','Nov','Dec')

# Ask user for number
while True:
    response = input("How many birthdays shall I generate? (Max 100)\n>")
    if response.isdecimal() and (0 < int(response) <= 100):
        numBdays = int(response)
        break
print()

# Generate and display birthdays
print('Here are', numBdays, 'birthdays:')
birthdays = getBirthdays(numBdays)

for i, bday in enumerate(birthdays):
    if i > 0:
        print(", ", end="")
    print(f"{MONTHS[bday.month - 1]} {bday.day}", end="")

print("\n")

# Determine if matches exist
match = getMatch(birthdays)

# Display results
print("In this simulation,", end=" ")
if match is not None:
    monthName = MONTHS[match.month - 1]
    print(f"multiple people have a birthday on {monthName} {match.day}.")
else:
    print("there are no matching birthdays.")
print()
