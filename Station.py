class Station:
    """
    Съёмочная станция
    """
    def __init__(self):
        self.coords = {'north': None, 'east': None, 'elev': None}
        self.height = None
        self.note = None
        self.orientation = {'targetName': None, 'azimuth': None,
                            'horObs': None, 'vObs': None, 'face': None}
        self.observations = []
    
    def defineNXYZH(self, name, north, east, elev, height, note):
        self.name = name
        self.coords = {'north': north, 'east': east, 'elev': elev}
        self.height = height
        self.note = note
    
    def defineOrientation(self, targetName, azimuth, horObs):
        self.orientation = {
            'targetName': targetName,
            'azimuth': azimuth,
            'horObs': horObs
        }
    
    def correctOrientation(self, vObs, horObs, face):
        self.orientation['horObs'] = horObs,
        self.orientation['vObs'] = vObs,
        self.orientation['face'] = face
    
    def addObservation(self, targetName, face, slopeDist, vObs, horObs, desc):
        observation = {
            'targetName': targetName,
            'face': face,
            'slopeDist': slopeDist,
            'vObs': vObs,
            'horObs': horObs,
            'desc': desc
        }
        self.observations.append(observation)
    
    def print(self):
        print(self.name)