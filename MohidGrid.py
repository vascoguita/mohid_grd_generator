from qgis.core import QgsPoint, QgsLineString, QgsMultiLineString, QgsFeature, QgsVectorLayer
import math

class MohidGrid:
    def __init__(self, origin, nColumns, nRows, dX, dY, angle):
        self.setOrigin(origin)
        self.setNColumns(nColumns)
        self.setNRows(nRows)
        self.setDX(dX)
        self.setDY(dY)
        self.setAngle(angle)

    def setOrigin(self, origin: QgsPoint):
        self.__origin = origin

    def getOrigin(self) -> QgsPoint:
        return self.__origin

    def setNColumns(self, nColumns: int):
        if(nColumns < 1):
            raise Exception("Number of Columns lower than 1")
        self.__nColumns = nColumns

    def getNColumns(self) -> int:
        return self.__nColumns

    def setNRows(self, nRows: int):
        if(nRows < 1):
            raise Exception("Number of rows lower than 1")
        self.__nRows = nRows

    def getNRows(self) -> int:
        return self.__nRows

    def setDX(self, dX: float):
        if(dX < 0):
            raise Exception("dX lower than 0")
        self.__dX = dX

    def getDX(self) -> float:
        return self.__dX

    def setDY(self, dY: float):
        if(dY < 0):
            raise Exception("dX lower than 0")
        self.__dY = dY

    def getDY(self) -> float:
        return self.__dY

    def setAngle(self, angle: float):
        self.__angle = angle

    def getAngle(self) -> float:
        return self.__angle

    def getWidth(self) -> float:
        return self.getNColumns() * self.getDX()
    
    def getHeight(self) -> float:
        return self.getNRows() * self.getDY()
    
    def toQgsVectorLayer(self) -> QgsVectorLayer:
        layer = QgsVectorLayer("MultiLineString?crs=epsg:3857", "MOHID grid", "memory")
        provider = layer.dataProvider()
        feature = QgsFeature()
        feature.setGeometry(self.toQgsMultiLineString())
        provider.addFeatures([feature])
        layer.updateExtents()
        return layer

    def toQgsMultiLineString(self) -> QgsMultiLineString:
        multiLine = QgsMultiLineString()
        originX = self.getOrigin().x()
        originY = self.getOrigin().y()
        cos = math.cos(math.radians(self.getAngle()))
        sin = math.sin(math.radians(self.getAngle()))

        nVerticalLines = self.getNColumns() + 1
        dX = self.getDX()
        height = self.getHeight()

        for verticalLine in range(nVerticalLines):
            offsetX = dX * verticalLine
            a = QgsPoint(originX + (offsetX * cos), originY + (offsetX * sin))
            b = QgsPoint(originX + (offsetX * cos) - (height * sin), originY + (offsetX * sin) + (height * cos))
            line = QgsLineString([a, b])
            multiLine.addGeometry(line)

        nHorizontalLines = self.getNRows() + 1
        dY = self.getDY()
        width = self.getWidth()

        for horizontalLine in range(nHorizontalLines):
            offsetY = dY * horizontalLine
            a = QgsPoint(originX - (offsetY * sin), originY + (offsetY * cos))
            b = QgsPoint(originX + (width * cos) - (offsetY * sin), originY + (width * sin) + (offsetY * cos))
            line = QgsLineString([a, b])
            multiLine.addGeometry(line)

        return multiLine