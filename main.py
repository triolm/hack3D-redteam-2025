import prepareMap
import temperatureMap
import detectEdges

scalePath = "data/scale2.png"
imgPath = "data/cylinder.png"
minTemp = 26.0
maxTemp = 195

normalizedMap = temperatureMap.getNormalizedData(scalePath, minTemp, maxTemp)

tempMap = prepareMap.getTemperatureMap(imgPath, normalizedMap)

edge = detectEdges.detect_cube_outline(tempMap)