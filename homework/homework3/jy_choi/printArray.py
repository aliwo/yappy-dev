import collections

def frequency_sort(items):
    counts = collections.Counter(items)
    new_items = sorted(items, key=lambda x: (counts[x], x), reverse=True)
    print(new_items)



print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))