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


def combine(a: any, b: any) -> any:
    """
    Combines two objects of the same type. Currently implemented are: list, set, dict, tuple.
    :param a: an object
    :param b: an object of the same type as 'a'
    :return: a combined with b
    """
    if type(a) != type(b):
        raise NotImplementedError
    if isinstance(a, list):
        r = a.copy()
        r.extend(b)
    elif isinstance(a, set):
        r = a.union(b)
    elif isinstance(a, dict):
        r = a.copy()
        r.update(b)
    elif isinstance(a, tuple):
        r = a + b
    else:
        raise NotImplementedError
    return r
