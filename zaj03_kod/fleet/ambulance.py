from datetime import datetime, timedelta
class Ambulance:
    __slots__ = ['id', 'vehicle_type', 'status', 'location', 'medical_equipment', 'incident', 'state']
    __instances_count = 0
    __max_id = 1

    def __init__(self, vehicle_type, status, location, medical_equipment):
        self.id = Ambulance.__max_id
        self.vehicle_type = vehicle_type
        self.status = status  # e.g., "available", "on_mission", "servicing"
        self.location = location # as (northing, easting)
        self.medical_equipment = medical_equipment  # List of medical equipment names
        self.incident = []
        self.state = 'rest'
        Ambulance.__instances_count += 1
        Ambulance.__max_id += 1

    def update_location(self, new_location):
        self.state = 'drives'
        self.location = new_location

    def add_incident(self, incident):
        self.incident.append(incident)
        print(f'Added incident{self.incident[-1].id} to ambulance{self.id}')
        self.state = 'got incident'
        print(f'ambulance{self.id} got incident')

    def sort_incident(self):
        self.incident = sorted(self.incident, key=lambda x: (x.priority, x.time))
        self.state = 'thinks'
        print(f'Sorted incident: {self.incident}')

    def time_from_incident_happend(self, incident):
        aktualny_czas = datetime.now()
        aktualny_czas = aktualny_czas.strftime("%H:%M")

        czas_incydentu = datetime.strptime(incident.time, '%H:%M')
        czas_incydentu = czas_incydentu.strftime("%H:%M")

        print(f'time right now: {aktualny_czas}, incident time: {czas_incydentu}')

        dh = int(aktualny_czas[0:2]) - int(czas_incydentu[0:2])
        dm = int(aktualny_czas[3:5]) - int(czas_incydentu[3:5])
        dt = timedelta(hours=dh, minutes=dm)

        print(f'time difference: {dt}')

    def distance_from_incident(self, incident):
        x = abs(self.location[0] - incident.location[0])
        y = abs(self.location[1] - incident.location[1])
        print(f'Geodesic location difference x: {x}, y: {y}')

    def ambulancee(self):
        self.sort_incident()
        assert self.state == "thinks"
        for accident in self.incident:
            self.time_from_incident_happend(accident)
            self.distance_from_incident(accident)
            self.update_location(accident.location)
            assert self.state == "drives"
            accident.status = "done"
            self.state = "done"
            assert self.state == "done"
            print("incident done")

    def __eq__(self, other):
        if not isinstance(other, Ambulance):
            return NotImplemented
        return self.id == other.id and self.vehicle_type == other.vehicle_type
    
    def __str__(self):
        return (f"Ambulance ID: {self.id}, Type: {self.vehicle_type}, "
                f"Status: {self.status}, Location: {self.location}, "
                f"Equipment: {', '.join(self.medical_equipment)}")
    
    @staticmethod
    def validate_id(ambulance_id):
        return isinstance(ambulance_id, int) and ambulance_id > 0

    @classmethod
    def get_instances_count(cls):
        return f"Number of working ambulances: {cls.__instances_count}"

if __name__ == "__main__":
    ambulance1 = Ambulance(
        #id=0,
        vehicle_type="AZ124",
        status="Available",
        location=(50.095340, 19.920282),
        medical_equipment = ["defibrillator", "stretcher"]
    )
    ambulance2 = Ambulance(
        #id=1,
        vehicle_type="AZ2000",
        status="Available",
        location=(50.095340, 19.920282),
        medical_equipment = ["defibrillator", "stretcher"]
    )

    print(ambulance1 == ambulance2)
    print(ambulance1)

# slajd 17 - sloty - odkomentować __slots__
    # ambulance1.whatever = "123"
    # print(ambulance1.whatever)

# slajd 17 - metody statyczne i metody klasy - odkomentować 3 rzeczy u góry
    print(Ambulance.validate_id(123))
    print(Ambulance.validate_id("123"))

    print(Ambulance.get_instances_count())