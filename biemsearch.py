def generate_filters(data, attributes, seed=None):
    filters = []
    # Discard the last attribute match
    for (attr_index, (name, values)) in enumerate(attributes[:-1]):
        for value in values:
            filter = []
            if seed is None:
                for (entry_index, entry) in enumerate(data):
                    if entry[attr_index] == value:
                        filter.append(entry_index)
                filters.append(("{0}({1})".format(name, value), filter))
            else:
                for seed_index in seed[1]:
                    if data[seed_index][attr_index] == value:
                        filter.append(seed_index)
                filters.append(("{0}+{1}({2})".format(seed[0], name, value), filter))
    return filters


def is_match(entry):
    return entry[-1] == '1'


def default_eval(filter, data):
    if len(filter[1]) / len(data) < 0.01:
        return 0
    score = 0
    for index in filter[1]:
        entry = data[index]
        if is_match(entry):
            score += 1
    return score/len(filter[1])


"""
data, attributes are as extracted from arff
search_width = w
search_depth = d
seed list of indices in data that are in the subgroup
"""


def biem_search(data, attributes, search_width, search_depth, evaluator=default_eval, seed=None):
    if search_depth == 0:
        return seed
    filters = generate_filters(data, attributes, seed)
    filters.sort(key=lambda f: evaluator(f, data), reverse=True)
    next_level = []
    for filtr in filters[:search_width]:
        next_level.append(biem_search(data, attributes, search_width, search_depth-1, evaluator, filtr))
    return next_level[:search_width]
