import csv

#Challenge 1
"""
this works with importing os module because
this file is in the same folder as "Chapter6Challenges.py"
"""

with open("Chapter6Challenges.py", "r") as new:
    print(new.read())


#Challenge 2
with open("q.txt", "w") as question1:
    question1.write(input("How old are you? "))

ages = list()
with open("q.txt", "r") as first_age:
    ages.append(first_age.read())

with open("q.txt", "w") as question2:
    question2.write(input("How old is your spouse? "))

with open("q.txt", "r") as second_age:
    ages.append(second_age.read())

print(ages)


#Challenge 3
a_listers = [["Top Gun",
         "Risky Business",
         "Minority Report"],
        ["Titanic",
         "The Revenant",
         "Inception"],
        ["Training Day",
         "Man on Fire",
         "Flight"]]
actors = list()
with open("actors.csv", "w") as csvfile:
    w = csv.writer(csvfile,
                   delimiter=",")
    for actor_list in a_listers:
        w.writerow(actor_list)
    
with open("actors.csv", "r") as x:
    actors.append(x.read())
print(actors)
