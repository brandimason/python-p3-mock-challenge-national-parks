class Visitor:

    def __init__(self, name):
        self.name = name

        self._new_trip = []
        self._national_parks =[]

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15 and not hasattr(self, "name"):
            self._name = value
        else: raise Exception("404 Not Found")
        return self._name
        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        if isinstance(new_trip, Trip):
            self._new_trip.append(new_trip)
        return self._new_trip
    
    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        if isinstance(new_national_park, NationalPark) and new_national_park not in self._national_parks:
            self._national_parks.append(new_national_park)
        return self._national_parks
