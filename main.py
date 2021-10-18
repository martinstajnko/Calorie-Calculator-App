from temperature import Temperature
from calorie import Calorie


"""
Main function has program executed in terminal, where you have to input different parameters.
Then calculation of calories is done and printed.
In the end you can repeat program or you can finish it with answer "NO". 
Because program exists of while loop.
"""


while True:

    country = input("Select country: ")
    city = input("Select city: ")
    weight = float(input("Input your weight: "))
    height = float(input("Input your height: "))
    age = int(input("Input your age: "))
    sex = ''
    while True: 
        sex = input("Input your gender (man/woman): ").upper()
        if sex == 'MAN' or sex == 'WOMAN':
            break
        else:
            print('Wrong input, input can be man or woman!')

    place = Temperature(country=country, city=city)
    current_temp = place.get_temperature()

    print(f'In {place.city} - {place.country}  is now {current_temp} °C.')
    calories = Calorie(weight=weight, height=height, age=age, sex=sex, temperature=current_temp)

    print(f'For your body is good to ingest {calories.calculate()}')

    _continue = input("Do you want to continue (YES/NO)? ").upper()
    if _continue == 'NO':
        break