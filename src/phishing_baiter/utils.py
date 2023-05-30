from random import uniform as rand_uniform


def rand_choice(data) -> any:
    """
    Choices a random object of the iterable given. Supports weights.
    :param data: either dict or list of tuples, second object is the weighting
    :return: a random object of the list given
    """
    if isinstance(data, dict):
        data = data.items()
    weights = {}
    total = 0.0
    for i, v in enumerate(data):
        if isinstance(v, tuple):
            if len(v) >= 2:
                total += v[1]
                weights[i] = v[1]
                continue
        weights[i] = 1.0
    index = rand_uniform(0, total)
    counter = 0.0
    for i in weights:
        counter += weights[i]
        if counter >= index:
            if isinstance(data[i], tuple):
                return data[i][0]
            return data[i]
