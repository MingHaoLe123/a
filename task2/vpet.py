class VirtualPet:
    def __init__(self, name):
        """
        Initialize a VirtualPet instance with a name, default energy of 10, and default hunger of 0.
        :param name: The name of the pet.
        """
        self.name = name
        self.energy = 10
        self.hunger = 0

    def play(self):
        """
        Simulate playing by reducing energy by 2 and increasing hunger by 2.
        If energy is less than 2, prints "Too tired to play".
        """
        if self.energy < 2:
            print("Too tired to play")
        else:
            self.energy -= 2
            self.hunger += 2

    def feed(self):
        """
        Simulate feeding the pet by reducing hunger using the formula:
        hunger = max(0, hunger - 3).
        """
        self.hunger = max(0, self.hunger - 3)

    def sleep(self):
        """
        Simulate sleeping to restore energy by increasing energy by 10.
        """
        self.energy += 10

    def __str__(self):
        """
        Return the details of the pet in the format:
        "pet_name with x energy points and y hunger level".
        """
        return f"{self.name} with {self.energy} energy points and {self.hunger} hunger level"
