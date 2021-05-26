from sdr33_structure import units

class Parser:
    """
    Парсер SDR33-файла
    """
    def __init__(self):
        """Constructor"""
        pass

    def readSDR(self, file):
        """Выполняет чтение файла и создает массив строк"""
        with open(file, 'r') as sdr:
            self.sdrLines = sdr.readlines()
    
    def parseSDR(self, defineSurveyParamsFunction):
        """Парсит строки из массива и 
        создает экземпляры классов Survey, Station и Observation"""
        for line in self.sdrLines:
            if line[:2] == '00':
                defineSurveyParamsFunction(
                    line[4:20].split(' ')[0], 
                    line[4:20].split(' ')[1], 
                    line[24:40].split(' ')[0], 
                    line[24:40].split(' ')[1],
                    {
                        'angle': units['angle'][line[40]],
                        'distance': units['distance'][line[41]],
                        'pressure': units['pressure'][line[42]],
                        'temperature': units['temperature'][line[43]],
                        'coordPrompt': units['coordPrompt'][line[44]],
                        'angleLeftRight': units['angleLeftRight'][line[45]]
                    })
    
    def print(self):
        print(self.sdrLines)


if __name__ == "__main__":
    parser = Parser('survey')
    parser.parseSDR('total_station.sdr')
    parser.print()