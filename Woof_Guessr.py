import random
from woof import Woof

dog_breeds_file = open("dog_breed_list.txt", "r")
dog_breeds = dog_breeds_file.readlines()
woof = Woof(dog_breeds[random.randint(0,len(dog_breeds)-1)].strip())
woof.guess_word()
