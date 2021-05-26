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
    
    def defineInstrument(self, type):
        pass
    
    def print(self):
        print('Формат файла: ', self.fileFormat)
        print('Дата и время: ', self.surveyDate, ' ', self.surveyTime)
        print('Единицы измерения: ', self.units)