class Survey:
    """
    Класс для данных съемки
    Здесь хранятся проанализированные и разобранные данные SDR-файла
    """

    def __init__(self):
        self.stations = []

    def defineParams(self, fileType, fileTypeVersion, date, time, angle, 
                        distance, pressure, temp, coorPr, anLR):
        self.fileFormat = {'type': fileType, 'version': fileTypeVersion}
        self.surveyDate = date
        self.surveyTime = time
        self.units = {
            'angle': angle,
            'distance': distance,
            'pressure': pressure,
            'temperature': temp,
            'coordPrompt': coorPr,
            'angleLeftRight': anLR
        }
    
    def defineJob(self, jobName, pidType, includeElev, atmCorr, crCorr,
                    refrConst, seaLevCorr):
        self.job = {
            'name': jobName,
            'options': {
                'pidType': pidType,
                'includeElev': includeElev,
                'atmosCorr': atmCorr,
                'crCor': crCorr,
                'refrConst': refrConst,
                'seaLevCor': seaLevCorr
            }
        }

    def defineInstrument(self, type, version, serialNum, mountType, vangleOpt,
                            EDMoffset, reflOffset, prizmConst):
        self.instrument = {
            'type': type,
            'version': version,
            'serialNum': serialNum,
            'options': {
                'mountType': mountType,
                'vangleOpt': vangleOpt,
                'EDMoffset': EDMoffset,
                'reflOffset': reflOffset,
                'prizmConst': prizmConst
            }
        }
    
    def createStation(self, station):
        self.stations.append(station)
    
    def addOrientation(self, stationName, targetName, azimuth, horObs):
        for station in self.stations:
            if station.name == stationName:
                station.defineOrientation(targetName, azimuth, horObs)

    def addObservation(self, stationName, targetName, slopeDist, vObs, horObs, face, desc):
        for station in self.stations:
            if station.name == stationName:
                if station.orientation['targetName'] == targetName:
                    station.correctOrientation(vObs, horObs, face)
                station.addObservation(targetName, face, slopeDist, vObs, horObs, desc)
    
    def print(self):
        for i in self.stations:
            print(i.name)
            for obs in i.observations:
                print(obs)