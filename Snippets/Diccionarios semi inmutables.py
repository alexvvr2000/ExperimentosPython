from types import MappingProxyType

d: MappingProxyType = MappingProxyType({1: 2, 3: 4})
d[3] = 5
