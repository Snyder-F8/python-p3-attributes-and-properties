#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name=None, job=None):

        # validate name ONLY if provided
        if name is not None:
            if not isinstance(name, str) or not (1 <= len(name) <= 25):
                print("Name must be string between 1 and 25 characters.")
                self._name = None
            else:
                self._name = name.title()
        else:
            self._name = None

        # validate job ONLY if provided
        if job is not None:
            if job not in APPROVED_JOBS:
                print("Job must be in list of approved jobs.")
                self._job = None
            else:
                self._job = job
        else:
            self._job = None

    @property
    def name(self):
        return self._name

    @property
    def job(self):
        return self._job
