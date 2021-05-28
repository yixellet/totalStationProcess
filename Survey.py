class Survey:
    """
    Класс для данных съемки
    Здесь хранятся проанализированные и разобранные данные SDR-файла
    """

    def __init__(self):
        pass

    def defineParams(self, fileType, fileTypeVersion, date, time, units):
        self.fileFormat = {'type': fileType, 'version': fileTypeVersion}
        self.surveyDate = date
        self.surveyTime = time
        self.units = units
    
    def defineJob(self, jobName, options):
        self.job = {'name': jobName, 'options': options}

    def defineInstrument(self, type, version, serialNum, options):
        self.instrument = {
            'type': type,
            'version': version,
            'serialNum': serialNum,
            'options': options
        }
    
    def print(self):
        print('Формат файла: ', self.fileFormat)
        print('Дата и время: ', self.surveyDate, ' ', self.surveyTime)
        print('Файл: ', self.job)
        print('Инструмент: ', self.instrument)