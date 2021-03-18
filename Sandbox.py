# hours = raw_input("Enter hours:")
# rate = float(raw_input("Enter rate:"))
# print float(hours) * rate

# Exercise from the video
# friends = ["John","Glenn","Sally"]
# for friend in friends :
#     print "Happy New Year ", friend
# print "Done!"


# looking for the smallest. It is an exercise from the video week7 Largest and Smaller (2nd video)
# smallest = None
# print "Before"
# for value in [9,41,12,3,74,15]:
#     if smallest is None:
#         smallest = value
#     elif smallest > value:
#         smallest = value
#     print smallest, value
#     break
#     print "Otra vuelta"
# print "After ",smallest

# Exercise 5.10 of the book the one in the quiz of the assignment.
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
    if smallest is None:
        largest = num
        smallest = num
    elif smallest > num:
        smallest = num
    elif largest < num:
        largest = num

print("Maximum is {}".format(largest))
print("Minimum is {}".format(smallest))

# Exercise from the video
friends = ["John","Glenn","Sally"]
for friend in friends :
    print ("Happy New Year {}.".format(friend))
print("Done!")