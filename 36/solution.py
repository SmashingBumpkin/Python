def es36(dictionariesList):
    # I have to find the set of keys that appear in all dictionaries
    # I initialize it with the keys of the first dictionary
    keys = set(dictionariesList[0].keys())
    # and I update it by making the intersection with the key set of each of the other dictionaries
    for d in dictionariesList[1:]:
        keys = keys.intersection(d.keys())
    # so I repeat on the values the same mechanism only for the obtained keys
    # I initialize all the key values with the value sets of the first dictionary
    diz = {k: set(v) for k, v in dictionariesList[0].items() if k in keys}
    # and then for each dictionary and for each key
    for d in dictionariesList[1:]:
        for k, v in d.items():
            if k in diz:
                # I update the values keeping only the common values (intersection)
                diz[k] = diz[k].intersection(v)
    # at the end I order the values associated to each key (obtaining ordered lists)
    return {k: sorted(v) for k, v in diz.items()}
