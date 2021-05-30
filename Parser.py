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
        defineInstrumentFunction,
        createStationFunction,
        addOrientationFunction):
        """Парсит строки из массива и 
        создает экземпляры классов Survey, Station и Observation"""
        for line in self.sdrLines:
            if line[:2] == '00':
                defineSurveyParamsFunction(
                    line[4:20].split(' ')[0], 
                    line[4:20].split(' ')[1], 
                    line[24:40].split(' ')[0], 
                    line[24:40].split(' ')[1],
                    units['angle'][line[40]],
                    units['distance'][line[41]],
                    units['pressure'][line[42]],
                    units['temperature'][line[43]],
                    units['coordPrompt'][line[44]],
                    units['angleLeftRight'][line[45]]
                )
            elif line[:2] == '10':
                defineJobFunction(
                    line[4:20].split(' ')[0],
                    options['pidType'][line[20]],
                    options['inclElev'][line[21]],
                    options['atmCor'][line[22]],
                    options['crCor'][line[23]],
                    options['refrConst'][line[24]],
                    options['seaLevCor'][line[25]]
                )
            elif line[:2] == '01':
                defineInstrumentFunction(
                    line[5:21].split(' ')[0],
                    line[5:21].split(' ')[1],
                    line[21:27],
                    instrOpts['mountType'][line[49]],
                    instrOpts['vangleOpt'][line[50]],
                    float(line[51:67].strip()) if line[51:67].strip() else None,
                    float(line[67:83].strip()) if line[67:83].strip() else None,
                    float(line[83:99].strip()) if line[83:99].strip() else None
                )
            elif line[:2] == '02':
                createStationFunction(
                    line[4:20].strip(),
                    float(line[20:36].strip()) if line[20:36].strip() else None,
                    float(line[36:52].strip()) if line[36:52].strip() else None,
                    float(line[52:68].strip()) if line[52:68].strip() else None,
                    float(line[68:84].strip()) if line[68:84].strip() else None,
                    line[84:100].strip(),
                )
            elif line[:2] == '07':
                addOrientationFunction(
                    line[4:20].strip(),
                    line[20:36].strip(),
                    float(line[36:52].strip()) if line[36:52].strip() else None,
                    float(line[52:68].strip()) if line[52:68].strip() else None,
                )
            elif line[:2] == '03':
                self.targetHeight = float(line[4:20].strip())
            elif line[:2] == '09':
                pass
