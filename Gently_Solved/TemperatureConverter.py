def convertToFahrenheit(degreesCelsius):
    Fahrenheit = degreesCelsius * (9/5) + 32
    return Fahrenheit

def convertToCelsius(DegreesFahrenheit):
    Celsius = (DegreesFahrenheit - 32) * (5/9)
    return Celsius

#assert statements stop the program if their condition is False
assert convertToCelsius(0) == -17.77777777777778 
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(100) == 212
print(convertToFahrenheit(50))

