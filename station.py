class Station:
    """
    Съёмочная станция.
    """
    def __init__(self, name, height, orientation):
        self.name = name
        self.height = height
        self.orientation = orientation
        self.observations = []