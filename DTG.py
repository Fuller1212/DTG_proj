
import random

destinations = ['Florida', 'United Kingdom', 'New York City', 'France']

restaurants = ['Broadway Pizza', 'Ocean Prime', 'ASPIC', 'Pizza by the Sea']

transportations = ['Rental car', 'Train', 'Uber', 'Biking',]

entertainments = ['Golfing at TPC', 'Disneyworld', 'Tour a museum', 'Visit central park']



def choose_random_destination():
    print(f'We have selected {random.choice(destinations)} for your destination! Does this sound good?')
    answer = None
    while answer != 'yes': 
        answer = input('yes or no ') 
        if answer == 'yes' or answer == 'Yes' or answer == 'y':
            print(f'Great choice! Now lets move on!')
        elif answer == 'no' or answer == 'No' or answer == 'n':
            print(f'Sorry you were not pleased with that option, let us try a different option. How does {random.choice(destinations)} sound?')
           
            

def choose_random_restaurant():
    print(f'We have selected {random.choice(restaurants)} for your restaurant! Does this sound good?')
    answer = None
    while answer != 'yes':
        answer = input('yes or no ')
        if answer == 'yes' or answer == 'Yes' or answer == 'y':
            print(f'Great choice! Now lets move on!')
        elif answer == 'no' or answer == 'No' or answer == 'n':
            print(f'Sorry you were not pleased with that option, let us try a different option. How does {random.choice(restaurants)} sound?')
            
            
    

def choose_random_transportation():
    print(f'We have selected {random.choice(transportations)} for your transportation! Does this sound good?')
    answer = None
    while answer != 'yes':
        answer = input('yes or no ')
        if answer == 'yes' or answer == 'Yes' or answer == 'y':
            print('Great choice! Now lets move on!')
        elif answer == 'no' or answer == 'No' or answer == 'n':
            print(f'Sorry you were not pleased with that option, let us try a different option. How does {random.choice(transportations)} sound?')
            
    

def choose_random_entertainment():
    print(f'We have selected {random.choice(entertainments)} for your entertainment! Does this sound good?')
    answer = None
    while answer != 'yes':
        answer = input('yes or no ')       
        if answer == 'yes' or answer == 'Yes' or answer == 'y':
            print(f'Great choice! Now lets move on!')
        elif answer == 'no' or answer == 'No' or answer == 'n':
            print(f'Sorry you were not pleased with that option, let us try a different option. How does {random.choice(entertainments)} sound?')
            
            
    
        

intro = 'Welcome to Day Trip Generator! If you are unsure or can not agree on where to vacation, then we can help fix that!'
print(intro)

choose_random_destination()

choose_random_restaurant()

choose_random_transportation()

choose_random_entertainment()


outro = "Congrats! Your day trip vacation has been planned. Let's just confirm that the trip information is correct."
print(outro)

print('The trip we have generated for you is:')
