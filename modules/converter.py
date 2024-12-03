class Converter:
    def __init__(self, pxs: tuple[int]|list[int], mms: tuple[int]|list[int]):
        self.pxx, self.pxy = pxs
        self.mmx, self.mmy = mms
        
        self.coefx = self.pxx / self.mmx
        self.coefy = self.pxy / self.mmy
    
    def pxs_to_mms(self, pxs: tuple[int]|list[int]) -> list[int]:
        px, py = pxs
        mx = px * self.coefx
        my = py * self.coefx
        return [mx, my]
    
    def mms_to_pxs(self, mms: tuple[int]|list[int]) -> list[int]:
        mx, my = mms
        px = mx / self.coefx
        py = my / self.coefy
        return [px, py]

    def list_pxs_to_mms(self, pxsl: list[tuple[int]|list[int]]) -> list[list[int]]:
        ml = [] # ml - not maskine learning, it is mm list
        for pxs in pxsl:
            ml.append(self.pxs_to_mms(pxs))
        return ml
    
    def list_mms_to_pxs(self, mmsl: list[tuple[int]|list[int]]) -> list[list[int]]:
        px = []
        for mms in mmsl:
            px.append(self.mms_to_pxs(mms))
        return px


if __name__ == "__main__":
    c = Converter((100, 2), (2, 4))
    print(c.mms_to_pxs(c.pxs_to_mms((100, 100))))