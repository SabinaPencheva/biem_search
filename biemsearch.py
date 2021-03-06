def generate_filters(data, attributes, seed=None):
    filters = []
    # Discard the last attribute match
    for (attr_index, (name, values)) in enumerate(attributes[:-1]):
        if values == 'NUMERIC':
            continue
        for value in values:
            if value is None:
                continue
            filter = []
            if seed is None:
                for (entry_index, entry) in enumerate(data):
                    if entry[attr_index] == value:
                        filter.append(entry_index)
                # filters.append(("{0}({1})".format(name, value), filter))
                filters.append(([name], [value], filter))
            else:
                for seed_index in seed[2]:
                    if data[seed_index][attr_index] == value:
                        filter.append(seed_index)
                if name not in seed[0]:
                    filters.append(([name]+seed[0], [value]+seed[1], filter))
    return filters

"""
data, attributes are as extracted from arff
search_width = w
search_depth = d
seed list of indices in data that are in the subgroup
"""


def biem_search(data, attributes, search_width, search_depth, evaluator, seed=None):
    if search_depth == 0:
        return [seed]
    filters = generate_filters(data, attributes, seed)
    filters.sort(key=evaluator.evaluate, reverse=True)
    next_level = []
    for filtr in filters[:search_width]:
        ns = biem_search(data, attributes, search_width, search_depth-1, evaluator, filtr)
        next_level.extend(ns)
    next_level.sort(key=evaluator.evaluate, reverse=True)
    return next_level[:search_width]
