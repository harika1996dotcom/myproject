from typing import NamedTuple


class item(NamedTuple):
    id: str
    name: str
    cost: int


i1 = item('one', 'ramesh', 2200)
i2 = item('two', 'suresh', 1090)
i3 = item('three', 'anil', 3597)
i4 = item('four', 'ravi', 5670)
i5 = item('five', 'chandu', 9000)

items = [i1, i2, i3, i4, i5]

items.sort(key=lambda e: e.name)

for item in items:
    print(item)
