class Survey:
    """
    Класс для данных съемки
    Здесь хранятся проанализированные и разобранные данные SDR-файла
    """

    def __init__(self, sdrFormat, date, settings, job, instr, observations):
        """Constructor"""
        self.sdrFormat = sdrFormat
        self.date = date
        self.settings = settings
        self.job = job
        self.instr = instr
        self.observations = observations