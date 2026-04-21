class Converter:
    def __init__(self, length, unit):
        self.to_meters = {
            'inches': 0.0254,
            'feet': 0.3048,
            'yards': 0.9144,
            'miles': 1609.344,
            'kilometers': 1000,
            'meters': 1,
            'centimeters': 0.01,
            'millimeters': 0.001
        }

        if unit in self.to_meters:
            self.meters_value = length * self.to_meters[unit]
        else:
            raise ValueError(f"Unit '{unit}' is not supported.")

    def inches(self):
        return self.meters_value / self.to_meters['inches']

    def feet(self):
        return self.meters_value / self.to_meters['feet']

    def yards(self):
        return self.meters_value / self.to_meters['yards']

    def miles(self):
        return self.meters_value / self.to_meters['miles']

    def kilometers(self):
        return self.meters_value / self.to_meters['kilometers']

    def meters(self):
        return self.meters_value

    def centimeters(self):
        return self.meters_value / self.to_meters['centimeters']

    def millimeters(self):
        return self.meters_value / self.to_meters['millimeters']


if __name__ == "__main__":
    convert = Converter(9, 'inches')
    print(convert.feet())
    print(convert.meters())