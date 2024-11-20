class OPath_converter:
    @staticmethod
    def export(path, start_point):
        narray = []
        narray.append(start_point)
        narray += path
        rlist = []
        for id in range(1, len(narray)):
            dx = narray[id][0] - narray[id - 1][0]
            dy = narray[id][1] - narray[id - 1][1]
            rlist.append({"task": "movemm", "value": [round(dx, 1), round(dy, 2)]})
        return rlist


if __name__ == "__main__":
    OPath_converter.export(
        [
            [753, 230],
            [732, 87],
            [367, 167],
            [295, 278],
            [434, 393],
            [737, 326],
            [873, 244],
        ],
        [469, 262],
    )
