class NationalPark:
    
    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []
        
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and not hasattr(self, "name"):
            self._name = value
        else: raise Exception("404 Not Found")
        return self._name
    

    def trips(self, new_trip=None):
        from classes.trip import Trip
        if isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return self._trips
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        if isinstance(new_visitor, Visitor) and new_visitor not in self._visitors:
            self._visitors.append(new_visitor)
        return self._visitors
    
    def total_visits(self):
        return len(self._trips)
    
    def best_visitor(self):
        trip_dict = {}
        currentmax = 0
        currentmaxkey = None
        for trip in self._trips:
            trip_dict[trip.visitor] = trip_dict.get(trip.visitor, 0) +1
        # print(trip_dict)
        for key in trip_dict:
            if currentmax < trip_dict[key]:
                currentmax = trip_dict[key]
                currentmaxkey = key
        return currentmaxkey