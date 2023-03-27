from enum import Enum


class CRIME_TYPE(Enum):
    """Enum of types of possible crimes"""

    MURDER = "Murder"
    THEFT = "Theft"
    KIDNAPPING = "Kidnapping"
    DRUG_DEALING = "Drug Dealing"
    ARSON = "Arson"
    UNDEFINED = "Undefined"
