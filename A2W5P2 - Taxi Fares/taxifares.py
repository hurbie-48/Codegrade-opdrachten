def calculate_fare(distance: float) -> float:
    total_price = 4
    distance = distance*1000
    meter_amount = 0
    while distance > 0:
        meter_amount += 1
        distance -= 140
    meter_calculated = meter_amount * 0.25
    total_price += meter_calculated
    return total_price


if __name__ == "__main__":
    print(calculate_fare(float(input("Distance: "))))