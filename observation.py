from math import pow, sin, cos, radians

class Observation:
    """
    Наблюдение при тахеометрической съемке.
    """
    def __init__(self, name, slopeDist, vertAngle, horAngle, height, description):
        self.name = name
        self.slopeDist = slopeDist
        self.vertAngle = vertAngle
        self.horAngle = horAngle
        self.height = height
        self.description = description
        self.coordinates = {'north': None, 'east': None, 'height': None}
    
    def calcHorDist(self):
        self.horDist = self.slopeDist * pow(cos(radians(self.vertAngle)), 2)
    
    def calcElevation(self, instrHeight):
        self.elevation = 0.5 * self.slopeDist * sin(
            radians(self.vertAngle) * 2) + instrHeight - self.height
    
    def calcCoordinates(self, stationCoords, stationAzimuth):
        pass