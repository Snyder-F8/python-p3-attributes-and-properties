#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name=None, breed=None):

        # validate name ONLY if provided
        if name is not None:
            if not isinstance(name, str) or not (1 <= len(name) <= 25):
                print("Name must be string between 1 and 25 characters.")
                self._name = None
            else:
                self._name = name
        else:
            self._name = None

        # validate breed ONLY if provided
        if breed is not None:
            if breed not in APPROVED_BREEDS:
                print("Breed must be in list of approved breeds.")
                self._breed = None
            else:
                self._breed = breed
        else:
            self._breed = None

    @property
    def name(self):
        return self._name

    @property
    def breed(self):
        return self._breed
