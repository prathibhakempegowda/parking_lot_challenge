
import logging
import numpy as np
import random
import json
# import boto3

class ParkingLot:
    """
        ParkingLot class that takes in a square footage size as input
        and creates an array of empty values based on the input square footage size

        methods:
            calulate_parking_spot_size
                - params: square_footage(int)
            map_vehicles
                - params: None

    """
    def __init__(self, square_footage):
        self.square_footage = square_footage
        self.parking_spot = self.calulate_parking_spot_size(96)

    def calulate_parking_spot_size(self, spot_size):
        return np.array([None] * int(self.square_footage/spot_size))
    
    def map_vehicles(self):
        # method for the parking lot class that maps vehicles to parked spots in a JSON object
        car_parked_in_spot = []
        for index, license_plate in enumerate(self.parking_spot):
            car_parked_in_spot.append({index: license_plate})
        print(car_parked_in_spot)
        with open('parking_lot_map.json', 'w') as f:
            json.dump(car_parked_in_spot, f)
        # s3_client = boto3.resource('s3')
        # s3_client.upload_file('parking_lot_map.json', 'bucket_name', 'parking_lot_map.json')


    class Car:
        """
            Car class that takes in a 7 digit license plate and sets it as a property

            methods:
            park
                - params: parking spot (class instance)
                          spot (int)

        """
        def __init__(self, license_plate):
            self.license_plate = license_plate
    
        # Magic method to output the license plate when converting the class instance to a string.
        def __str__(self):
            return self.license_plate
    
        # Method to park the car in a given spot in the parking lot
        def park(self, parking_lot, spot):
            # Check if spot is already occupied
            if parking_lot[spot] is None:
                # Park the car
                parking_lot[spot] = self
                return "Car with license plate {} parked successfully in spot {}".format(self.license_plate, spot)
            else:
                return "Car with license plate {} was not parked successfully".format(self.license_plate)
class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        print(self.license_plate)
        return self.license_plate
    
    def park(self, parking_lot, parking_spot):
        if parking_lot.parking_spot[parking_spot] is None:
            parking_lot.parking_spot[parking_spot] = self.license_plate
            print(f"Car with license plate {self.license_plate} parked successfully in spot {parking_spot}")
            return f"Car with license plate {self.license_plate} parked successfully in spot {parking_spot}"
        else:
            print(f'Car with license plate {self.license_plate} was not parked successfully')
            return f'Car with license plate {self.license_plate} was not parked successfully'
        
def main(parking_lot, cars):
    try:
        for car in cars:
            random_spot = random.randint(0, len(parking_lot.parking_spot) - 1)
            if not parking_lot.parking_spot[random_spot]:
                car.park(parking_lot, random_spot)
            else:
                available_spot = np.where(parking_lot.parking_spot==None)[0][0]
                car.park(parking_lot, available_spot)
            if None not in parking_lot.parking_spot:
                break
    except Exception as e:
        logging.error(e)


if __name__ == "__main__":
    parking_lot = ParkingLot(2000)
    cars = []
    for car in range(0, 16):
        license_no = random.randrange(1111111, 9999999, 7)
        cars.append(Car(license_no))
    main(parking_lot, cars)
    parking_lot.map_vehicles()
