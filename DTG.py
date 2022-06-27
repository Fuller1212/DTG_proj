
import random

destinations = ['Florida', 'United Kingdom', 'New York City', 'France']

restaurants = ['Broadway Pizza', 'Ocean Prime', 'ASPIC', 'Pizza by the Sea']

transportations = ['Rental car', 'Train', 'Uber', 'Biking',]

entertainments = ['Golfing at TPC', 'Disneyworld', 'Tour a museum', 'Visit central park']

result = ['', '', '', '']
destination =''
restaurant = ''
transportation = ''
entertainment = ''



def choose_random_destination():
    answer = None
    destination = random.choice(destinations)
    print(f'We have selected {destination} for your destination! Does this sound good?')
    result[0] = destination
    while answer != 'yes': 
        answer = input('yes or no ') 
        if answer == 'yes' or answer == 'Yes' or answer == 'y':
            print(f'Great choice! Now lets move on!')
        elif answer == 'no' or answer == 'No' or answer == 'n':
            destination = random.choice(destinations)
            print(f'Sorry you were not pleased with that option, let us try a different option. How does {destination} sound?')
    return destination
           
            

def choose_random_restaurant():
    answer = None
    restaurant = random.choice(restaurants)
    result[1] = restaurant
    print(f'We have selected {restaurant} for your restaurant! Does this sound good?')
    while answer != 'yes':
        answer = input('yes or no ')
        if answer == 'yes' or answer == 'Yes' or answer == 'y':
            print(f'Great choice! Now lets move on!')
        elif answer == 'no' or answer == 'No' or answer == 'n':
            print(f'Sorry you were not pleased with that option, let us try a different option. How does {restaurant} sound?')
    return restaurant 
            
            
    

def choose_random_transportation():
    answer = None
    transportation = random.choice(transportations)
    result[2] = transportation
    print(f'We have selected {random.choice(transportations)} for your transportation! Does this sound good?')
    while answer != 'yes':
        answer = input('yes or no ')
        if answer == 'yes' or answer == 'Yes' or answer == 'y':
            print('Great choice! Now lets move on!')
        elif answer == 'no' or answer == 'No' or answer == 'n':
            print(f'Sorry you were not pleased with that option, let us try a different option. How does {transportation} sound?')
    return transportation 
            
    

def choose_random_entertainment():
    answer = None
    entertainment = random.choice(entertainments)
    result[3] = entertainment
    print(f'We have selected {random.choice(entertainments)} for your entertainment! Does this sound good?')
    while answer != 'yes':
        answer = input('yes or no ')       
        if answer == 'yes' or answer == 'Yes' or answer == 'y':
            print(f'Great choice! Now lets move on!')
        elif answer == 'no' or answer == 'No' or answer == 'n':
            print(f'Sorry you were not pleased with that option, let us try a different option. How does {entertainment} sound?')
    return entertainment
            
            
    
        
intro = 'Welcome to Day Trip Generator! If you are unsure or can not agree on where to vacation, then we can help fix that!'
print(intro)

destination = choose_random_destination()

restaurant = choose_random_restaurant()

transportation = choose_random_transportation()

entertainment = choose_random_entertainment()


outro = "Congrats! Your day trip vacation has been planned. Let's just confirm that the trip information is correct."
print(outro)

print('The trip we have generated for you is:')

print(f'Destination: {destination}')

print(f'Restaurant: {restaurant}')

print(f'Transportation: {transportation}')

print(f'Entertainment: {entertainment}')

print(f'Prepare for the time of your life as you visit {destination} while traveling by {transportation}. Enjoying a nice dinner at {restaurant} and having a blast while {entertainment}')

