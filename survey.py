class Survey:
    """
    Класс для данных съемки
    Здесь хранятся проанализированные и разобранные данные SDR-файла
    """

    def __init__(self, sdrFormat, date, settings, job, instrument, observations):
        """Constructor"""
        self.sdrFormat = sdrFormat
        self.date = date
        self.settings = settings
        self.job = job
        self.instrument = instrument
        self.observations = observations