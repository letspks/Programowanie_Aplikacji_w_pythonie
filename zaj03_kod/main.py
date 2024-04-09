from random import randint  # Import funkcji randint do generowania losowych priorytetów
from fleet.ambulance import Ambulance
from fleet.station import Station
from operations import *
from personnel import *
def run_application():
    # Zdefiniowanie naszych zasobów
    ambulance1 = Ambulance("Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    ambulance2 = Ambulance("Type B", "on mission", (50.095340, 19.920282), ["Stretcher", "First Aid Kit"])

    employee1 = Employee("John", "Doe", 12000.0)
    employee2 = Employee("Jane", "Smith", 8000.0)

    driver1 = Driver("Mike", "Johnson", 10000.0, "DL12345", ["BLS"])
    driver2 = Driver("Anna", "Brown", 11500.0, "DL12346", ["ALS", "PHTLS"])

    # Sprawdzenie czy to czasem nie są te same karetki
    if ambulance1 == ambulance2:
        raise ValueError("To są te same karetki!")

    # Sprawdzenie ile mamy karetek
    print(Ambulance.get_instances_count())


    # Daj kierowcy podwyżkę za super zasługi
    print(f"Przed podwyżką: {driver1.display_info()}")
    driver1.update_salary(5000.12)
    print(f"Po podwyżce: {driver1.display_info()}")
    # Stworzenie kolejki incydentów
    queue = IncidentQueue()

    # Zaraportowanie 2 zgłoszeń
    # Generowanie losowego priorytetu
    priority1 = randint(1, 10)
    priority2 = randint(1, 10)
    reporter1 = "John Doe"
    reporter2 = "Jadwiga Hymel"
    incident1 = Incident("Power outage in sector 4", (51, 20), priority1, "12:00", reporter1)
    incident2 = Incident("Fire alarm in building 21", (50, 20), priority2, "13:00", reporter2)
    queue += incident1
    queue += incident2

    print("Aktualne zgłoszenia:")
    print(queue)
    
    station1 = Station((50.5, 18.5), ambulance1, driver1, employee1)
    print(f'Station one: {station1}')

   

    incident1.add_ambulance(ambulance1)  # Dodanie karetki do incydentu pierwszego 
    incident2.add_ambulance(ambulance1)  # Dodanie karetki do incydentu drugiego 


    assert queue[0].ambulance is not None
    assert ambulance1.incident is not None


    ambulance1.ambulancee()


    # Sprawdzenie czy wszystkie incydenty zostały zakończone
    for incident in queue:
        assert incident.status == "done"


if __name__ == "__main__":
    run_application()