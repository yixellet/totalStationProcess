from math import pow, sin, cos, radians

class Observation:
    """
    Наблюдение при тахеометрической съемке
    """
    def __init__(self, name, slopeDist, vertAngle, horAngle, height, note):
        """Constructor"""
        self.name = name
        self.slopeDist = slopeDist
        self.vertAngle = vertAngle
        self.horAngle = horAngle
        self.height = height
        self.note = note
        self.coordinates = {'north': None, 'east': None, 'height': None}
    
    def calcHorDist(self):
        """Расчет горизонтального проложения"""
        self.horDist = self.slopeDist * pow(cos(radians(self.vertAngle)), 2)
    
    def calcElevation(self, instrHeight):
        """Расчет превышения пикета над станцией"""
        self.elevation = 0.5 * self.slopeDist * sin(
            radians(self.vertAngle) * 2) + instrHeight - self.height
    
    def calcCoordinates(self, stationNorthCoord, stationEastCoord, stationAzimuth):
        """Расчет координат пикета. 

        А ЧТО ЕСЛИ ДИРЕКЦИОННЫЙ УГОЛ БОЛЬШЕ 360?

        """
        self.coordinates['north'] = stationNorthCoord + (
            self.horDist * cos(radians(stationAzimuth + self.horAngle)))
        
        self.coordinates['east'] = stationEastCoord + (
            self.horDist * sin(radians(stationAzimuth + self.horAngle)))

    def calcHeight(self, stationHeight):
        """Расчет отметки пикета"""
        self.coordinates['height'] = stationHeight + self.elevation

if __name__ == "__main__":
    obs = Observation('1', 8.131, 2.48139, 306.78639, 0, '')
    obs.calcHorDist()
    obs.calcElevation(1.529)
    obs.calcCoordinates(422062.12, 2236268.35, 16.85088)
    obs.calcHeight(-23.01)
    print(obs.coordinates)