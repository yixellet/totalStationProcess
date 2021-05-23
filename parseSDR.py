class Parser:
    """
    Парсер SDR33-файла
    """
    def __init__(self, survey):
        """Constructor"""
        self.survey = survey

    def parseSDR(self, file):
        with open(file, 'r') as sdr:
            self.sdrLines = sdr.readlines()
    
    def print(self):
        print(self.sdrLines)


if __name__ == "__main__":
    parser = Parser('survey')
    parser.parseSDR('total_station.sdr')
    parser.print()