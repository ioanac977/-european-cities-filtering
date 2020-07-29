# -european-cities-filtering
european cities filtering and generating an output file with results

# FEATURES 
1. Handle different operations with an array including cities from Europe: [Paris, Cluj-Napoca, Timisoara, Berlin, Madrid, Londra, Barcelona, Venetia, Viena, Iasi]
2. Define a parent class which has 4 methods We will make different filtering operations:

* met1 - find out all cities with an odd number of characters
* met2 - find out all cities with an even number of characters
* met3- generate a dictionary with two groups:

* first group the list of cities with even number of characters
* second group the list of cities with odd number of characters

* met4 - Generate an output fie, txt, json, xml, (just one format it’s enough) with the results after calling met1, met2, met3

3. Define a new class which should be inherited from the parent one. 2 new methods must be implemented:

* met 1 - sort the array so in the end we will have it ordered by the amount of characters
* met 2 - remove all the duplicate characters from each string from the same array
* In the end, reuse the met4 from parent class in order to generate the output from met1 and met2 into a txt, json or xml file

# CONFIGURATIONS 
- install python version > 3.0
- install pip 
- install PyCharm 

# RUN
- download repository
- open project using PyCharm
- run EuropenianCities.py
