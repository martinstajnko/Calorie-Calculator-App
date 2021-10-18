from flask import Flask, render_template, request
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from wtforms.fields.core import SelectField
from calorie import Calorie
from temperature import Temperature

app = Flask(__name__)

"""
ADD COMMENT!
"""


class HomePage(MethodView):
    
    def get(self):
        return render_template('index.html')


class CaloriesFormPage(MethodView):
    
    """
    ADD COMMENT!
    """

    def get(self):
        calories_form = CaloriesForm()
        return render_template('calories_form_page.html',
                                caloriesform=calories_form) 
                                

    def post(self):
        calories_form = CaloriesForm(request.form)

        temperature = Temperature(country=calories_form.country.data,
                                  city= calories_form.city.data)

        current_temp = temperature.get_temperature()
        if current_temp != 'Error':
            calorie = Calorie(weight=float(calories_form.weight.data), 
                              height=float(calories_form.height.data),
                              age=float(calories_form.age.data), 
                              sex=calories_form.sex.data,
                              temperature=current_temp)

            calories_kcal, calorie_kJ = calorie.calculate()

            return render_template('calories_form_page.html',
                                   caloriesform=calories_form,
                                   city=temperature.city.upper(),
                                   country=temperature.country.upper(),
                                   current_temperature=current_temp,                               
                                   calories=calories_kcal,
                                   calories2=calorie_kJ,
                                   result=True)
        else:
            return render_template('calories_form_page.html',
                        caloriesform=calories_form,
                        city=temperature.city.upper(),
                        country=temperature.country.upper(),
                        current_temperature=False,                     
                        result=True)


class CaloriesForm(Form):

    """
    ADD COMMENT!
    """
    
    # Widgets
    city = StringField("City: ", default="Ljubljana")
    country = StringField("Country: ", default="Slovenia")
    weight = StringField("Weight: ", default=70)
    height = StringField("Height: ", default=175)
    age = StringField("Age: ", default=30)
    #sex = StringField("Gender: ", default="Woman")
    sex = SelectField("Gender: ", choices=["man", "woman"]) 
    button = SubmitField("Calculate")


#app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
#app.add_url_rule('/calories_form', view_func=CaloriesFormPage.as_view('calories_form_page'))
app.add_url_rule('/', view_func=CaloriesFormPage.as_view('calories_form_page'))

app.run(debug=True)