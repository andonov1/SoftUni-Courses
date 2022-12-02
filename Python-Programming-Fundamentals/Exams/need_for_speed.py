n = int(input())
cars = {}
max_fuel = 75

for i in range(n):
    car, mileage, fuel = input().split('|')
    mileage = int(mileage)
    fuel = int(fuel)
    cars[car] = [mileage, fuel]

while True:
    command = input().split(" : ")
    if command[0] == 'Stop':
        break
    elif command[0] == 'Drive':
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        if cars[car][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car][0] += distance
            cars[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car][0] >= 100000:
                cars.pop(car)
                print(f"Time to sell the {car}!")
    elif command[0] == 'Refuel':
        car = command[1]
        fuel = int(command[2])
        needed_fuel = 75 - cars[car][1]
        bought_fuel = 0
        if fuel <= needed_fuel:
            bought_fuel = fuel
        else:
            bought_fuel = needed_fuel
        cars[car][1] += bought_fuel
        print(f"{car} refueled with {bought_fuel} liters")
    else:
        car = command[1]
        kilometers = int(command[2])
        cars[car][0] -= kilometers
        if cars[car][0] < 10000:
            cars[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

for key, value in cars.items():
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")