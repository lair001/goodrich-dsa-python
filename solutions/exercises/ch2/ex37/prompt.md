Write a simulator, as in the previous project, but add a Boolean gender
field and a floating-point strength field to each animal, using an Animal
class as a base class. If two animals of the same type try to collide, then
they only create a new instance of that type of animal if they are of different genders. Otherwise, if two animals of the same type and gender try to
collide, then only the one of larger strength survives.