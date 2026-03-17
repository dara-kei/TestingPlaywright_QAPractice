import enum


class States(enum.Enum):
    """ It is used in practice form testing"""
    NCR = "NCR"
    UTTAR_PRADESH = "Uttar Pradesh"
    HARYANA = "Haryana"
    RAJASTHAN = "Rajasthan"

class CityOfNCRState(enum.Enum):
    """ It is used in practice form testing"""

    DELHI = "Delhi"
    GURGAON = "Gurgaon"
    NOIDA = "Noida"

class CityOfUttarPradeshState(enum.Enum):
    """ It is used in practice form testing"""

    AGRA = "Agra"
    LUCKNOW = "Lucknow"
    MERRUT = "Merrut"

class CityOfHaryana(enum.Enum):
    """ It is used in practice form testing"""

    KARNAL = "Karnal"
    PANIPAT = "Panipat"


class CityOfRajasthan(enum.Enum):
    """ It is used in practice form testing"""

    JAIPUR = "Jaipur"
    JAISELMER = "Jaiselmer"

