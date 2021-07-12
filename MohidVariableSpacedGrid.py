from qgis.core import QgsPoint, QgsLineString, QgsMultiLineString, QgsFeature, QgsVectorLayer, QgsMultiPolygon, QgsPolygon
import math
from typing import List

class MohidVariableGrid:
    def __init__(self, origin, XX, YY, angle):
        self.setOrigin(origin)
        self.setAngle(angle)
        self.setXX(XX)
        self.setYY(YY)

    def setOrigin(self, origin: QgsPoint):
        self.__origin = origin

    def getOrigin(self) -> QgsPoint:
        return self.__origin

    def setXX(self, XX: List[float]):
        if(len(XX) < 1):
            raise Exception("Number of Columns lower than 1")
        self.__XX = XX

    def getXX(self) -> List[float]:
        return self.__XX

    def setYY(self, YY: List[float]):
        if(len(YY) < 1):
            raise Exception("Number of Columns lower than 1")
        self.__YY = YY

    def getYY(self) -> List[float]:
        return self.__YY

    def setAngle(self, angle: float):
        self.__angle = angle

    def getAngle(self) -> float:
        return self.__angle

    
    def toQgsVectorLayer(self) -> QgsVectorLayer:
        layer = QgsVectorLayer("MultiPolygon?crs=epsg:4327", "MOHID variable spaced grid", "memory")
        provider = layer.dataProvider()
        feature = QgsFeature()
        feature.setGeometry(self.toQgsMultiPolygon())
        provider.addFeatures([feature])
        layer.updateExtents()
        return layer

    #Is generating too many vertexes
    def toQgsMultiPolygon(self) -> QgsMultiPolygon:
        multiPoly = QgsMultiPolygon()
        originX = self.getOrigin().x()
        originY = self.getOrigin().y()
        XX = self.getXX()
        YY = self.getYY()
        cos = math.cos(math.radians(self.getAngle()))
        sin = math.sin(math.radians(self.getAngle()))
        sumX = 0
        for x in range(len(XX)):
            sumY = 0
            for y in range(len(YY)):
                a = QgsPoint(originX + (sumX * cos), originY + (sumX * sin))
                b = QgsPoint(originX + (sumX + XX[x]) * cos, originY + (sumX + XX[x]) * sin)
                c = QgsPoint(originX - (sumY + YY[y]) * sin + (sumX + XX[x]) * cos, originY + (sumY + YY[y]) * cos + (sumX + XX[x]) * sin)
                d = QgsPoint(originX - (sumY + YY[y]) * sin, originY + (sumY + YY[y]) * cos)
                line = QgsLineString([a, b, c, d])
                square = QgsPolygon(line)
                multiPoly.addGeometry(square)
                sumY += YY[y]
            sumX += XX[x]

        return multiPoly