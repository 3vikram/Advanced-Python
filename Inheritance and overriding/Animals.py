class Animal:

    # Animal class constructor

    def __init__(self, eyes, legs, hands, tail, skin_pattern, origin_type):
        self.eyes = eyes
        self.legs = legs
        self.hands = hands
        self.tail = tail
        self.skin_pattern = skin_pattern
        self.origin_type = origin_type

    def get_eyes(self):
        return self.eyes

    def set_legs(self, no_legs):
        self.legs = no_legs

    def set_hands(self, no_hands):
        self.hands = no_hands

    def get_tail(self):
        return self.tail

    def get_legs(self):
        return self.legs

    def get_hands(self):
        return self.hands

    def get_skin_pattern(self):
        return self.skin_pattern

    def get_type_animal(self):
        return self.origin_type

    def get_animal_info(self):
        animal_info = "Animal has {} eyes,\n {} legs, {} hands, {} tail,\n it's skin pattern looks like {}, and it's origin is {}".format(self.eyes, self.legs, self.hands,
                                                                                                                                          self.tail, self.skin_pattern,self.origin_type)
        return animal_info

if __name__ == '__main__':
    instance = Animal(2, 2, 2, 1, 'stripes', 'indian')
    print(instance.get_animal_info())


