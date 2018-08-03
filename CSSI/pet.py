dog  = {
"name": "Doggy McDogface",
"breed": "Terrier",
"age": 2,
"hungry": True,
"sleepy": False,
}

class Dog(object):
    def __init__(self, name , age):
        self.name = name
        self.age = age
        self.is_hungry = True
        self.needs_a_walk = True
        self.is_sleepy = False

    def feed(self):
        self.is_hungry = False
        print("Nomomomom")

    def walk(self):
        if self.needs_a_walk and not self.is_sleepy:
            self.needs_a_walk = False
            self.is_sleepy = True
            print("Wakakakkakakakk")

    def sleep(self):
        if self.is_sleepy:
            self.is_hungry = True
            print("Dog is sleepy")

    def play(self, other_dog):
        print("%s is playing." % (self.name))

    def __str__(self):
        return "%s who is %s" % (self.name, self.age)

dog1 = Dog("Doggy McDogface", 2)
dog2 = Dog("Buster", 1)

dog1.name = "Ruff"

print(dog1.name)
print("%s is %s years old" % (dog1.name, dog1.age))
print(type(dog1))

dog1.feed()
dog1.walk()
dog1.sleep()
dog1.feed()
dog1.walk()
dog1.sleep()
print dog1.is_hungry

print(dog1)
print(dog2)
dog1.play(dog2)
