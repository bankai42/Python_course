def sortByOrderNum(elems):
    sorted_elems = sorted(elems, key= lambda x: x[1])
    return sorted_elems

elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]
print(f"Elements: {elements}\n")
print(f"Sorted Elements: {sortByOrderNum(elements)}")