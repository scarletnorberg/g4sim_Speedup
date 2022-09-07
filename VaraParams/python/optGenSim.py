import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
import g4SimHit_SpeedUp.VarParameters.ParamModifier as pm


params = pm.getAllClasses(pm)

#opt = VarParsing.VarParsing ('analysis')
options = VarParsing('analysis')
#options = VarParsing()

options.register("paramNames", "", VarParsing.multiplicity.list, VarParsing.varType.string, "Geant4 parameters to modify (choices: {})".format(','.join(sorted(params))))
options.register("paramValues", "", VarParsing.multiplicity.list, VarParsing.varType.float, "values for modified Geant4 parameters".format(','.join(sorted(params))))
options.register("dump", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool)
<<<<<<< HEAD
#options.register("filename","", VarParsing.multiplicity.list, VarParsing.varType.string, "Geant4 parameters to modify (choices: {})".format(','.join(sorted(params))))
=======
options.register("inputroot", "", VarParsing.multiplicity.singleton, VarParsing.varType.string)
>>>>>>> 2cd9e7699b601e55bb299e5150c7b7aa68aae3c4

options.parseArguments()

# handle parameters
paramValueCounter = 0
options._params = []
options._inFiles =[]
# create parameter classes, assign values, assemble name
_pnames = []
print ("AHAHAHA", options.paramNames)
for p in options.paramNames:
    if p not in params:
        raise ValueError("Unsupported param: "+p)
    else:
        options._params.append(getattr(pm,p)())
        options._params[-1].setValues(options.paramValues[paramValueCounter:paramValueCounter+options._params[-1].nparams])
        _pnames.append(p+','.join(str(pp) for pp in options._params[-1].params))
        paramValueCounter += options._params[-1].nparams
if paramValueCounter != len(options.paramValues):
    raise ValueError("Used {} paramValues, but {} were provided".format(paramValueCounter,len(options.paramValues)))
_pnametmp = '_'.join(_pnames)

options._root = "sim_"+str(options.paramNames).strip("[']").replace("', '","_")+"_"+str(options.paramValues).strip("[']").replace(", ","_")
<<<<<<< HEAD
print("ROOT options", options._root)
=======
#print("ROOT options", options._root)

>>>>>>> 2cd9e7699b601e55bb299e5150c7b7aa68aae3c4

def resetSeeds(process,options):
    # reset all random numbers to ensure statistically distinct but reproducible jobs
    from IOMC.RandomEngine.RandomServiceHelper import RandomNumberServiceHelper
    randHelper = RandomNumberServiceHelper(process.RandomNumberGeneratorService)
    randHelper.resetSeeds(options.maxEvents+options.part)
    if process.source.type_()=='EmptySource' and options.part>0: process.source.firstEvent = cms.untracked.uint32((options.part-1)*options.maxEvents+1)
    return process


