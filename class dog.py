class Dog:
    # Class variable
    animal = "Dog"

    def __init__(self, breed, colour):
        # Instance variables
        self.breed = breed
        self.colour = colour

    def display_details(self):
        print(f"Animal: {Dog.animal}")
        print(f"Breed: {self.breed}")
        print(f"Colour: {self.colour}")
        print("-" * 20)

# Creating two objects with different breeds and colours
dog1 = Dog("Labrador", "Yellow")
dog2 = Dog("German Shepherd", "Black and Tan")

# Displaying details of both dogs
dog1.display_details()
dog2.display_details()