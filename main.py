from __future__ import barry_as_FLUFL
from this import s
import turtle
from wsgiref.util import guess_scheme
screen = turtle.Screen()
screen.title("Kosovo cities")

map = "kosovo41.gif"
turtle.addshape(map)

turtle.shape(map)
import turtle
import pandas

data = pandas.read_csv("qytetet.csv")
krejt_qytet = data.state.to_list()
guess_cities = []


while len(guess_cities)<30: 
    answer_cities = screen.textinput(title=f"{len(guess_cities)}/30 Qytetet Korrekt", prompt="Cilli eshte qyteti tjeter?").title()
    print(answer_cities)
    if answer_cities == "Exit":
        missing_city = []
        for city in krejt_qytet:
            if city not in guess_cities:
                missing_city.append(city)
        new_data = pandas.DataFrame(missing_city)
        new_data.to_csv("Qytetet_Qe_duhet_msuar.csv")      
        break


    if answer_cities in krejt_qytet:
        guess_cities.append(answer_cities)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = data[data.state == answer_cities]
        t.goto(int(state.x), int(state.y))
        t.write(answer_cities)
    