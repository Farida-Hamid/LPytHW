## Animal is-a object
class Animal(object):
  pass

## Dog is-a object of class animal
class Dog(Animal):
  def __init__(self, name):
    ## A dog has-a name
    self.name = name

## Cat is-a object of class animal
class Cat(Animal):
  def __init__(self, name):
    ## A cat has-a name
    self.name = name

## Person is-a object
class Person(object):
  def __init__(self, name):
    ## Person has-a name
    self.name = name
    ## Person has-a pet of some kind
    self.pet = None

## Employee is-a object of class person
class Employee(Person):
  def __init__(self, name, salary):
    ## Employee has-a name just like an object of class person
    super(Employee, self).__init__(name)
    ## Employee has-a salary
    self.salary = salary

## Fish is-a object
class Fish(object):
  pass

## Salmon is-a object of class Fish
class Salmon(Fish):
  pass

## Halibut is-a class of Fish
class Halibut(Fish):
  pass

## rober is-a Dog
rover = Dog('Rover')

## satan is-a cat
satan = Cat('Satan')

## mary is-a Person
mary = Person('Mary')

## mary has-a pet named satan
mary.pet = satan

## frank is-a Employee
frank = Employee('Frank', 120000)

## frank has-a pet name rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon Fish
crouse = Salmon()

## harry is-a Halibut Fish
harry = Halibut()