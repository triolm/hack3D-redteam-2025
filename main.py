import prepareMap
import temperatureMap
import detectEdges

scalePath = "data/scale.png"
imgPath = "data/cube.png"
minTemp = 24.6
maxTemp = 153

normalizedMap = temperatureMap.getNormalizedData(scalePath, minTemp, maxTemp)

tempMap = prepareMap.getTemperatureMap(imgPath, normalizedMap)

edge = detectEdges.detect_cube_outline(tempMap)