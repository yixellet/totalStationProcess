from Parser import Parser
from Survey import Survey
from Station import Station
from Observation import Observation

survey = Survey()
parser = Parser()

def defineSurveyParams(fileType, fileTypeVersion, date, time, units):
    survey.defineParams(fileType, fileTypeVersion, date, time, units)

def defineSurveyJob(jobName, options):
    survey.defineJob(jobName, options)

def defineInstrument(type, version, serialNum, options):
    survey.defineInstrument(type, version, serialNum, options)

def createStation(name, height, orientation):
    return Station(name, height, orientation)

def createObservation(name, slopeDist, vertAngle, horAngle, height, note):
    return Observation(name, slopeDist, vertAngle, horAngle, height, note)

parser.readSDR('total_station.sdr')
parser.parseSDR(defineSurveyParams, defineSurveyJob, defineInstrument)

survey.print()
