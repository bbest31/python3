class WaterBottle:
    def __init__(self, color, volume=0, max_volume=500):
        if volume > max_volume:
            raise AttributeError("Volume can't be larger than the max volume held by the bottle!")
        self._color = color
        self._volume = volume
        self._max_volume = max_volume
    
    def __repr__(self):
        return f"A {self._color} {self._max_volume}mL water bottle with {self._volume}mL"

    # Properties
    # Getters
    @property
    def volume(self):
        """This method returns the current volume of fluid in the water bottle"""
        return self._volume

    @property
    def color(self):
        """This method returns the current volume of fluid in the water bottle"""
        return self._color
    
    @property
    def max_volume(self):
        return self._max_volume

    def add_volume(self, vol):
        if type(vol) != int:
            raise TypeError("Invalid volume type")
        elif vol <= 0:
            raise AttributeError("Volume to add can't be less than 0mL")
        elif self._volume + vol > self._max_volume:
            raise Exception("Bottle overflowing!")
        else:
            self._volume += vol
    
    def empty_bottle(self):
        self._volume = 0
    
    def fill_water_bottle(self):
        self._volume = self._max_volume
    
    def drink(self, vol):
        """
        Drinks a determined amount of fluid from the current volume.

        """
        if type(vol) != int:
            raise TypeError("Invalid volume type")
        elif vol <= 0:
            raise AttributeError("Volume to drink can't be less than 0mL")
        elif self._volume - vol < 0:
            self._volume = 0
        else:
            self._volume -= vol


# Inline Testing using assertion statements.


