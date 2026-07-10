def make_car(manufacturer, model, **details):
    car = {}
    car["car_manufacturer"] = manufacturer
    car["car_model"] = model
    for key, value in details.items():
        car[key] = value

    print(car)

car = make_car('subaru', 'outback', color='blue', tow_package=True)
