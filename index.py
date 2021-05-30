from Parser import Parser
from Survey import Survey
from Station import Station
from Observation import Observation

survey = Survey()
parser = Parser()

def defineSurveyParams(fileType, fileTypeVersion, date, time, angle, 
                        distance, pressure, temp, coorPr, anLR):
    survey.defineParams(fileType, fileTypeVersion, date, time, angle, 
                        distance, pressure, temp, coorPr, anLR)

def defineSurveyJob(jobName, pidType, includeElev, atmCorr, crCorr,
                    refrConst, seaLevCorr):
    survey.defineJob(jobName, pidType, includeElev, atmCorr, crCorr,
                    refrConst, seaLevCorr)

def defineInstrument(type, version, serialNum, mountType, vangleOpt,
                        EDMoffset, reflOffset, prizmConst):
    survey.defineInstrument(type, version, serialNum, mountType, vangleOpt,
                            EDMoffset, reflOffset, prizmConst)

def createStation(name, north, east, elev, height, note):
    station = Station()
    station.defineNXYZH(name, north, east, elev, height, note)
    survey.createStation(station)

def addOrientation(station, targetName, azimuth, horObs):
    survey.addOrientation(station, targetName, azimuth, horObs)


def createObservation(name, slopeDist, vertAngle, horAngle, height, note):
    return Observation(name, slopeDist, vertAngle, horAngle, height, note)

parser.readSDR('total_station.sdr')
parser.parseSDR(defineSurveyParams,
                defineSurveyJob,
                defineInstrument,
                createStation,
                addOrientation)


survey.print()