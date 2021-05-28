from sdr33_structure import units, options, instrOpts

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
    
    def parseSDR(
        self, 
        defineSurveyParamsFunction, 
        defineJobFunction, 
        defineInstrumentFunction):
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
            elif line[:2] == '10':
                defineJobFunction(
                    line[4:20].split(' ')[0],
                    {
                        'pidType': options['pidType'][line[20]],
                        'includeElev': options['inclElev'][line[21]],
                        'atmosCorr': options['atmCor'][line[22]],
                        'crCor': options['crCor'][line[23]],
                        'refrConst': options['refrConst'][line[24]],
                        'seaLevCor': options['seaLevCor'][line[25]]
                    }
                )
            elif line[:2] == '01':
                defineInstrumentFunction(
                    line[5:21].split(' ')[0],
                    line[5:21].split(' ')[1],
                    line[21:27],
                    {
                        'mountType': instrOpts['mountType'][line[49]],
                        'vangleOpt': instrOpts['vangleOpt'][line[50]],
                        'EDMoffset': float(line[51:67].strip()) if line[51:67].strip() else None,
                        'reflOffset': float(line[67:83].strip()) if line[67:83].strip() else None,
                        'prizmConst': float(line[83:99].strip()) if line[83:99].strip() else None
                    }
                )
    
    def print(self):
        print(self.sdrLines)

