from Animals import Animal

class Elephant(Animal):

    # constructor method overriden
    def __init__(self, trunk):
        self.trunk = trunk
        self.eyes = 2
        self.legs = 4
        self.hands = None
        self.tail = 1
        self.skin_pattern = 'hard and thick'
        self.origin_type = 'African'
        
        #calling Animal super class constructor method
        super().__init__(self.eyes, self.legs, self.hands, self.tail, self.skin_pattern, self.origin_type)

    def get_elephant_info(self):
        # Calling Animal parent class get_animal_info() method inside child class method
        return super().get_animal_info()

    # Overriden method of Animal class
    def get_animal_info(self):
        animal_info = "Animal has {} eyes,\n {} legs, {} hands, {} tail,\n it has {} trunks it's skin pattern looks like {}, and it's origin is {}".format(self.eyes, self.legs, self.hands,
                                                                                                                                          self.tail, self.trunk, self.skin_pattern,self.origin_type)
        return animal_info


if __name__ == "__main__":
    instance = Elephant(2)
    print(instance.get_animal_info())
    print(instance.get_elephant_info())

