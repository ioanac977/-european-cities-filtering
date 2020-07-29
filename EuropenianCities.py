import json
from collections import OrderedDict


class EuropeanianCities(object):
    cities = []

    def __init__(self, cities):
        self.cities = cities;

    def __str__(self):
        return "Europenian cities: " + str(self.cities)

    def oddLenghts(self):
        oddLengthCities = [x for x in self.cities if len(x) % 2]
        return oddLengthCities

    def evenLenghts(self):
        evenLengthCities = [x for x in self.cities if len(x) % 2 == 0]
        return evenLengthCities

    def generateDictionary(self, oddLengthCities, evenLengthCities):
        dictionary = {"oddLengthCities": oddLengthCities, "evenLengthCities": evenLengthCities}
        return dictionary

    def saveToJSONFile(self, listContent):
        with open("content.json", 'a') as json_file:
            json.dump(listContent, json_file)
            json_file.write('\n')
            # json.dump(dictionaryContent, json_file)
            # json_file.write('\n')


class SomeEuropeanianCities(EuropeanianCities):
    someCities = []

    def __init__(self, someCities):
        self.someCities = someCities;

    def __str__(self):
        return "Some europenian cities: " + str(self.someCities)

    def sortByAmount(self):
        return " ".join(sorted(self.someCities, key=len))

    def removeDuplicateStrings(self):
        return " ".join(["".join(OrderedDict.fromkeys(x)) for x in self.someCities])


listOfCities = ["Paris", "Cluj-Napoca", "Timisoara", "Berlin", "Madrid", "Londra", "Barcelona", "Venetia", "Viena",
                "Iasi"]

cities = EuropeanianCities(listOfCities)
print(cities)
print("methods from parent class : ")
print("met 1: {}".format(cities.oddLenghts()))
print("met 2: {}".format(cities.evenLenghts()))
print("met 3: {}".format(cities.generateDictionary(cities.oddLenghts(), cities.evenLenghts())))
dictionaryContent = cities.generateDictionary(cities.oddLenghts(), cities.evenLenghts())
print("met 4: look at content.json file from the current directory")
cities.saveToJSONFile(cities.oddLenghts())
cities.saveToJSONFile(cities.evenLenghts())
cities.saveToJSONFile(dictionaryContent)

print("methods from child class : ")
someCities = SomeEuropeanianCities(listOfCities)
print("met 1: {}".format(someCities.sortByAmount()))
print("met 2: {}".format(someCities.removeDuplicateStrings()))
listContentForChild = someCities.sortByAmount() + someCities.removeDuplicateStrings()
print("met 4: look at content.json file from the current directory")
someCities.saveToJSONFile(someCities.sortByAmount())
someCities.saveToJSONFile(someCities.removeDuplicateStrings())
