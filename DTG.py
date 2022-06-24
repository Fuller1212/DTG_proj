
import random

destinations = ['Florida', 'United Kingdom', 'New York City', 'France']

restaurants = ['Broadway Pizza', 'Ocean Prime', 'ASPIC', 'Pizza by the Sea']

transportations = ['Rental car', 'Train', 'Uber', 'Biking',]

entertainments = ['Golfing at TPC', 'Disneyworld', 'Tour a museum', 'Visit central park']



def get_random_destination():
    # move original print statement into this function
    print(f'We have selected {random.choice(destinations)} for your destination! Does this sound good?')
    answer = None
    while answer != 'yes': 
        answer = input('yes or no ') 
        if answer == 'yes' or answer == 'Yes' or answer == 'y':
            print(f'Great choice! Now lets move on!')
        elif answer == 'no' or answer == 'No' or answer == 'n':
            print(f'Sorry you were not pleased with that option, let us try a different option. How does {random.choice(destinations)} sound?')
           
            

def get_random_restaurant(restaurant):
    restaurant = None
    while restaurant not in ('yes' , 'no'):
        restaurant = input('yes or no ')
        if restaurant == 'yes' or 'Yes' or 'y':
            print(f'Great choice! Now lets move on!')
        elif restaurant == 'no' or 'No' or 'n':
            print(f'Sorry you were not pleased with that option, let us try a different option. How does {random.choice(restaurants)} sound?')
            input('yes or no')
            
    

def get_random_transportation(transportation):
    transportation = None
    while transportation not in ('yes' , 'no'):
        transportation = input('yes or no ')
        if transportation == 'yes' or 'Yes' or 'y':
            print('Great choice! Now lets move on!')
        elif transportation == 'no' or 'No' or 'n':
            print(f'Sorry you were not pleased with that option, let us try a different option. How does {random.choice(transportations)} sound?')
            input('yes or no')
    

def get_random_entertainment(entertainment):
    entertainment = None
    while entertainment not in ('yes' , 'no'):
        entertainment = input('yes or no ')       
        if entertainment == 'yes' or 'Yes' or 'y':
            print(f'Great choice! Now lets move on!')
        elif entertainment == 'no' or 'No' or 'n':
            print(f'Sorry you were not pleased with that option, let us try a different option. How does {random.choice(entertainments)} sound?')
            input('yes or no')
            
    
        

intro = 'Welcome to Day Trip Generator! If you are unsure or can not agree on where to vacation, then we can help fix that!'
print(intro)



# print(f'We have selected {random.choice(destinations)} for your destination! Does this sound good?')

get_random_destination()

food = restaurants
print(f'We have selected {random.choice(food)} for your restaurant! Does this sound good?')

get_random_restaurant({random.choice(food)})

trans = transportations
print(f'We have selected {random.choice(trans)} for your transportation! Does this sound good?')

get_random_transportation({random.choice(trans)})

fun = entertainments
print(f'We have selected {random.choice(fun)} for your entertainment! Does this sound good?')

get_random_entertainment({random.choice(fun)})


outro = "Congrats! Your day trip vacation has been planned. Let's just confirm that the trip information is correct."
print(outro)

print('The trip we have generated for you is:')

Destination = destinations
print('Destination:' + Destination)

Restaurant = restaurants
print('Restaurant:' + Restaurant )

Transportation = trans
print('Transportation:' + Transportation)

Entertainment = fun
print('Entertainment' + Entertainment)
