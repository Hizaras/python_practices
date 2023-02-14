def counter(dictionary: str | list | tuple) -> dict:
    from collections import Counter, defaultdict
    # myvalue_dict = {}
    #
    #  myvalue_dict =defaultdict(int)
    # for item in dictionary:
    #  # if item in myvalue_dict:
        #     myvalue_dict[item] = myvalue_dict[item] + 1
        # else:
        #     myvalue_dict[item] = 1
        # myvalue_dict[item] = myvalue_dict.get(item, 0)+
        # myvalue_dict[item] = dictionary.count(item)
    #         myvalue_dict[item]+= 1
    # # return myvalue_dict
    #  return dict (counter(dictionary))


print(counter([1, 3, 2, 4, 2, 4, 2, 45, 58, ]))
