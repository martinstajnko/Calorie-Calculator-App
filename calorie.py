from temperature import Temperature

class Calorie:

    """
    Class Calorie calculate how many kilo jouls - calories needs person to use in specific day.
    There are different formulas for men and women.
    """


    def __init__(self, weight, height, age, sex, temperature):       
        self.weight = weight
        self.height = height 
        self.age = age
        self.sex = sex
        self.temperature = temperature

    
    def calculate(self): 
        if self.sex == 'woman':
            result_kcal = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161 - self.temperature * 10
        elif self.sex == 'man':
            result_kcal = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5 - self.temperature * 10

        # kilo joul: 1kJ = 0.239kcal
        result_kJ = result_kcal * 4.184

        return round(result_kcal,2), round(result_kJ, 2)


if  __name__ == "__main__":
    temperature =  Temperature(country='Italy', city='Rome').get_temperature()
    calorie = Calorie(weight=85, height=185, age=45, sex='MAN', temperature=temperature)
    print(calorie.calculate())