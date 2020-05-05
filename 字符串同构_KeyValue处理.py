# 6. 字符串同构
def isIsomorphic(self, s: str, t: str) -> bool:

    maps = {}

    for k, v in zip(s, t):

        if k in maps and v != maps[k]:
            return False
        elif k not in maps and v in maps.values():
            return False
        else:
            maps[k] = v