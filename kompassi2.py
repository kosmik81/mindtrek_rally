# based on
# http://blog.bitify.co.uk/2013/11/connecting-and-calibrating-hmc5883l.html

import math

class Kompassi(object):

    def __init__(self):
        self._xs = []
        self._ys = []
        self._zs = []

    def _average_x(self):
        self._xs = self._xs[-20:]
        return reduce(lambda x, y: x + y, self._xs) / len(self._xs)

    def _average_y(self):
        self._ys = self._ys[-20:]
        return reduce(lambda x, y: x + y, self._ys) / len(self._ys)

    def _average_z(self):
        self._ys = self._ys[-20:]
        return reduce(lambda x, y: x + y, self._zs) / len(self._zs)

    def bearing(self, (x, y, z)):
        self._xs.append(x)
        self._ys.append(y)
        self._zs.append(z)
        bearing  = math.atan2(self._average_x(), self._average_y())
        if (bearing < 0):
            bearing += 2 * math.pi
        return math.degrees(bearing)
