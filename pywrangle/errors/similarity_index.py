

##########
# Similary index
##########

def calculate_similarity_index(ratios_dict: dict) -> float:
    """Returns index representing string similarity from ratios_dict.
    Index drops the lowest 2 matching balues to place emphasis on high values.
    NOTE: Likely one of these is metaphone.

    Args:
        ratios_dict (dict): dictionary of ratio values

    Returns:
        float: index representing similarity b/w 2 strings
    """
    vals = [ v for v in ratios_dict.values() if isinstance(v, (int, float))]
    for _ in range(2):
        vals.remove(min(vals))
    return round(sum(vals) / len(vals), 2)
