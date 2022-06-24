
import random

destinations = ['Florida', 'United Kingdom', 'New York City', 'France']

restaurants = ['Broadway Pizza', 'Ocean Prime', 'ASPIC', 'Pizza by the Sea']

transportation = ['Rental car', 'Train', 'Uber', 'Biking',]

entertainment = ['Golfing at TPC', 'Disneyworld', 'Tour a museum', 'Go to central park']


def get_random_destination(destination):
    destination = input('yes or no ')           #need to create a loop that will continue until the answer is yes
    if destination == 'yes':
        print(f'Great choice! Now lets move on!')
    elif destination == 'no':
        print(f'Sorry you were not pleased with that option, let us try a different option. How does {destinations} sound?')



def get_random_restaurant(restaurant):
    restaurant = input('yes or no ')
    if restaurant == 'yes':
        print(f'Great choice! Now lets move on!')
    elif restaurant == 'no':
        print(f'Sorry you were not pleased with that option, let us try a different option. How does {restaurant} sound?')


def get_random_transportation(transportation):
    transportation = input('yes or no ')
    if transportation == 'yes':
        print('Great choice! Now lets move on!')
    elif transportation == 'no':
        print(f'Sorry you were not pleased with that option, let us try a different option. How does {transportation} sound?')


def get_random_entertainment(entertainment):
    entertainment = input('yes or no ')         
    if entertainment == 'yes':
        print(f'Great choice! Now lets move on!')
    elif entertainment == 'no':
        print(f'Sorry you were not pleased with that option, let us try a different option. How does {entertainment} sound?')



intro = 'Welcome to Day Trip Generator! If you are unsure or can not agree on where to vacation, then we can help fix that!'
print(intro)


location = destinations
print(f'We have selected {random.choice(location)} for your destination! Does this sound good?')

get_random_destination({random.choice(location)})

food = restaurants
print(f'We have selected {random.choice(food)} for your restaurant! Does this sound good?')

get_random_restaurant({random.choice(food)})

trans = transportation
print(f'We have selected {random.choice(trans)} for your transportation! Does this sound good?')

get_random_transportation({random.choice(trans)})

fun = entertainment
print(f'We have selected {random.choice(fun)} for your entertainment! Does this sound good?')

get_random_entertainment({random.choice(fun)})


outro = "Congrats! Your day trip vacation has been planned. Let's just confirm that the trip information is correct."
print(outro)

print('The trip we have generated for you is:')

