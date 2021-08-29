class AttributeInitType(type):
    def __call__(self, *args, **kwargs):
        """Create a new instance."""

        # First, create the object in the normal default way.
        obj = type.__call__(self, *args)

        # Additionally, set attributes on the new object.
        for name, value in kwargs.items():
            setattr(obj, name, value)

        # Return the new object.
        return obj


class Car(object, metaclass=AttributeInitType):

    @property
    def description(self) -> str:
        """Return a description of this car."""
        return " ".join(str(value) for value in self.__dict__.values())


new_car = Car('foo',make='Toyota', model='Prius', year=2005, color='Green', engine='Hybrid')
print(new_car.description)