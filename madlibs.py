# string concatenation in Python
youtuber = "Dot DamnIt"

# a few ways to do this
print("Subscribe to " + youtuber)
# places the value of youtuber into the curly braces - string.format
print("Subscribe to {}".format(youtuber))
# f string format - prpend the f in front of the string - inside the curly braces, add variable name
print(f"Subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person name: ")

madlibs = f"Computer programming is so {adj}. I get so excited about it. I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}."

print(madlibs)