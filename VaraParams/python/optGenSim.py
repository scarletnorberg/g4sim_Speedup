import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
import g4SimHit_SpeedUp.VarParameters.ParamModifier as pm


params = pm.getAllClasses(pm)

options = VarParsing()

options.register("paramNames", "", VarParsing.multiplicity.list, VarParsing.varType.string, "Geant4 parameters to modify (choices: {})".format(','.join(sorted(params))))
options.register("paramValues", "", VarParsing.multiplicity.list, VarParsing.varType.float, "values for modified Geant4 parameters".format(','.join(sorted(params))))
options.register("dump", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool)
options.register("inputroot", "", VarParsing.multiplicity.singleton, VarParsing.varType.string)

options.parseArguments()

# handle parameters
paramValueCounter = 0
options._params = []
# create parameter classes, assign values, assemble name
_pnames = []
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
#print("ROOT options", options._root)


def resetSeeds(process,options):
    # reset all random numbers to ensure statistically distinct but reproducible jobs
    from IOMC.RandomEngine.RandomServiceHelper import RandomNumberServiceHelper
    randHelper = RandomNumberServiceHelper(process.RandomNumberGeneratorService)
    randHelper.resetSeeds(options.maxEvents+options.part)
    if process.source.type_()=='EmptySource' and options.part>0: process.source.firstEvent = cms.untracked.uint32((options.part-1)*options.maxEvents+1)
    return process


