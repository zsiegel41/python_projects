# Challenge 1
tv = ["Avatar: The Last Airbender",
      "Cutthroat Kitchen",
      "House Hunters",
      "Haikyuu!"]
for show in tv:
    print(show)

#Challenge 2
for i in range(10, 16):
    print(i)
    
#Challenge 3    
students = ["Kayleon",
            "Alex",
            "Jacob",
            "Adrian"]
times = ["1pm",
         "1:30pm",
         "2pm",
         "2:30pm"]

for i, time in enumerate(times):
    print(time)

for i, student in enumerate(students):
    print(i)
    print(student)

#Challenge 4
colors = ["purple", "yellow", "red", "blue"]
while True:
    answer = input("Guess a color, or press 'q' to quit: ")
    if answer == 'q':
        break
    try:
        answer = str(answer)
    except ValueError:
        print("Enter a valid string! Or press 'q' to quit")
    if answer in colors:
        print("Good guess!")
    else:
        print("Nope, try again")

#Challenge 5
nums1 = [1, 2, 4]
nums2 = [1, 2, 6]
new = []
for x in nums1:
    for y in nums2:
        new.append(x * y)

print(new)

    





    
