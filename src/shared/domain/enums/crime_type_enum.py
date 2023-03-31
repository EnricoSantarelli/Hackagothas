from enum import Enum


class CRIME_TYPE(Enum):
    """Enum of types of possible crimes"""

    MURDER = "MURDER"
    THEFT = "THEFT"
    KIDNAPPING = "KIDNAPPING"
    DRUG_DEALING = "DRUG_DEALING"
    ARSON = "ARSON"
    UNDEFINED = "UNDEFINED"
