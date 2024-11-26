from sensor import Sensor
from display import Display

class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []  # Prevent mutable default argument
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):
        return f"The car location {self.location}, with the capacity of {self.capacity}."

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)

        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()

    @property
    def available_bays(self):
        if (self.capacity - len(self.plates)) >= 0:
            return self.capacity - len(self.plates)
        elif (self.capacity - len(self.plates)) < 0:
            return 0

    def update_displays(self):
        # dictionary to send information to the displays
        data = {"available_bays": self.available_bays,
                "temperature": 25}
        for display in self.displays:
            display.update(data)

