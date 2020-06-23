cities = []

st_charles = ("54.6430", "39.8412")
lagrange = ("34.5420", "38.5420")
naperville = ("40.5309", "38.0003")

cities.append(st_charles)
cities.append(lagrange)
cities.append(naperville)
print(cities)


my_dict = {"height": "5'11",
           "color": "blue",
           "number": "41"
            }
print(my_dict["height"])

x = input("Ask me about myself: ")
if x in my_dict:
    fact = my_dict[x]
    print(fact)
else:
    print("Ask something else")


songs = {"Ben Folds": "Still",
         "Snow Patrol": "Olive Grove Facing the Sea",
         "Guster": "This Could All Be Yours",
         "Gareth Coker": "Ori"
         }
for x in songs:
    print(x)








