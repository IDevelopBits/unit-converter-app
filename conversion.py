length_factors = {
    "millimeter": 0.001,
    "centimeter": 0.01,
    "meter": 1.0,
    "kilometer": 1000.0,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "mile": 1609.344,
}

weight_factors = {
    "milligram": 0.001,
    "gram": 1.0,
    "kilogram": 1000.0,
    "ounce": 28.3495,
    "pound": 453.592,
}

unit_labels = {
    "length": {
        "millimeter": "mm",
        "centimeter": "cm",
        "meter": "m",
        "kilometer": "km",
        "inch": "in",
        "foot": "ft",
        "yard": "yd",
        "mile": "mi"
    },
    "weight": {
        "milligram": "mg",
        "gram": "g",
        "kilogram": "kg",
        "ounce": "oz",
        "pound": "lb"
    },
    "temperature": {
        "Celsius": "°C",
        "Fahrenheit": "°F",
        "Kelvin": "K"
    }
}

# Functions to convert from each unit TO Celsius
to_celsius = {
    "Celsius": lambda x: x,
    "Fahrenheit": lambda x: (x - 32) * 5 / 9,
    "Kelvin": lambda x: x - 273.15,
}

# Functions to convert from Celsius TO each unit
from_celsius = {
    "Celsius": lambda x: x,
    "Fahrenheit": lambda x: (x * 9 / 5) + 32,
    "Kelvin": lambda x: x + 273.15,
}


def convert_length(value, from_unit, to_unit):
    length = value * length_factors[from_unit]
    return length / length_factors[to_unit]


def convert_weight(value, from_unit, to_unit):
    weight = value * weight_factors[from_unit]
    return weight / weight_factors[to_unit]


def convert_temperature(value, from_unit, to_unit):
    celsius = to_celsius[from_unit](value)
    return from_celsius[to_unit](celsius)
