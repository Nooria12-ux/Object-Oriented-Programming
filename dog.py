class Dog:
    
    species = "dog"
    
    def __init__(self, name, age, breed, angerlevel, color):
        self.name  = name
        self.age = age
        self.breed = breed
        self.angerlevel = angerlevel
        self.color = color
        
stella = Dog("Stella", 10, "bulldog", "7.5 out of 10", "golden")
layla = Dog("Layla", 11, "border collie", "5 out of 10", "golden and white")
gaeul = Dog("Gaeul", 5, "french poodle", "2.1 out of 10", "white" )
maeumi  = Dog("Maeumi", 3, "maltese", "4.5 out of 10", "white")
bisco = Dog("Bisco", 2, "poodle", "4.6 out of 10", "light brown" )


print(f"Stella is a {stella.species}")
print(f"Layla is a {layla.species}")
print(f"Gaeul is a {gaeul.species}")
print(f"Maeumi is a {maeumi.species}")
print(f"Bisco is a {bisco.species}")

print(f"{stella.name} is {stella.age} years old. Her breed is {stella.breed}. Her anger level is {stella.angerlevel} and she is {stella.color} color!")
print(f"{layla.name} is {layla.age} years old. Her breed is {layla.breed}. Her anger level is {layla.angerlevel} and she is {layla.color} color!")
print(f"{gaeul.name} is {gaeul.age} years old. His breed is {gaeul.breed}. His anger level is {gaeul.angerlevel} and he is {gaeul.color} color!")
print(f"{maeumi.name} is {maeumi.age} years old. His breed is {maeumi.breed}. His anger level is {maeumi.angerlevel} and he is {maeumi.color} color!")
print(f"{bisco.name} is {bisco.age} years old. His breed is {bisco.breed}. His anger level is {bisco.angerlevel} and he is {bisco.color} color!")    