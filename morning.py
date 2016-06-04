
#1. Waking Up
def wake_up(day_of_week):
    if (day_of_week.lower() == "saturday"):
        instructions = "Go back to bed"
    elif (day_of_week.lower() == "sunday"):
        instructions = "Go back to bed"
    else:
        instructions = "Stop hitting snooze"

    return instructions
day_request = raw_input("What day is it?")
print wake_up(day_request)


#2. The Commute
def commute(weather,mins_until_work):
    if (weather.lower() == "rainy"):
        instructions = "Better take the car"
    elif (mins_until_work <= 10):
        instructions = "Better take the car"
    elif (mins_until_work > 30):
        instructions = "Enjoy a bike ride"
    else:
        "Hop on the bus"
    return instructions

weather = raw_input("What's the weather?")
mins_until_work = raw_input("How much time until work?")
print commute(weather,mins_until_work)





#3. Coffee Buzz
def coffee(number_of_emails):
    if (number_of_emails >= 100):
        instructions = "Time for a triple shot espresso"
    elif (number_of_emails >= 50):
        instructions = "Go for a large black coffee"
    elif (number_of_emails > 0):
        instructions = "A latte will serve you well"
    elif (number_of_emails == 0):
        instructions = "You have reached the Nirvana of 21st century communication!"
    elif (number_of_emails < 0):
        instructions = "Is this a new Gmail feature?"
    else:
        instructions = "Please enter a number!"
    return instructions

number_of_emails = raw_input("Number of emails?")
print coffee(number_of_emails)
