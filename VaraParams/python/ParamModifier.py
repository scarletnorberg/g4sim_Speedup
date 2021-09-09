import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

def getAllClasses(module):
    import inspect
    vm = vars(module)
    exclude = ["ParamModifier"]
    all_classes = [v for v in vm if v not in exclude and inspect.isclass(vm[v])]
    return all_classes

class ParamModifier(object):
    def __init__(self, nparams):
        self.nparams = nparams
        self.params = []
    def setValues(self, params):
        if len(params)!=self.nparams: raise RuntimeError("Expected number of params for {} is {}, but {} were provided".format(self.__class__.__name__,self.nparams,len(params)))
        self.params = params
        print ("PARAMTER",self.params)
    def apply(self, process):
        pass

class ProductionCut(ParamModifier):
    def __init__(self):
        super(ProductionCut,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.Physics.CutsPerRegion = cms.bool(False)
        process.g4SimHits.Physics.DefaultCutValue = cms.double(self.params[0])
        return process

#################################
#                               #
##  Magnetic Field parameters  ##
#                               #
#################################

class EnergyThSimple(ParamModifier):
    def __init__(self):
        super(EnergyThSimple,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.MagneticField.ConfGlobalMFM.OCMS.StepperParam.EnergyThSimple = cms.double(self.params[0])
        return process

class DeltaChordSimple(ParamModifier):
    def __init__(self):
        super(DeltaChordSimple,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.MagneticField.ConfGlobalMFM.OCMS.StepperParam.DeltaChordSimple = cms.double(self.params[0])
        return process

class DeltaOneStepSimple(ParamModifier):
    def __init__(self):
        super(DeltaOneStepSimple,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.MagneticField.ConfGlobalMFM.OCMS.StepperParam.DeltaOneStepSimple = cms.double(self.params[0])
        return process

class DeltaIntersectionSimple(ParamModifier):
    def __init__(self):
        super(DeltaIntersectionSimple,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.MagneticField.ConfGlobalMFM.OCMS.StepperParam.DeltaIntersectionSimple = cms.double(self.params[0])
        return process

##########################
#                        #  
##  Physics parameters  ##
#                        #    
##########################

class RusRoEcalElectron(ParamModifier):
    def __init__(self):
        super(RusRoEcalElectron,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.Physics.RusRoEcalElectron = cms.double(self.params[0])
        return process

class RusRoHcalElectron(ParamModifier):
    def __init__(self):
        super(RusRoHcalElectron,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.Physics.RusRoHcalElectron = cms.double(self.params[0])
        return process

class RusRoMuonIronElectron(ParamModifier):
    def __init__(self):
        super(RusRoMuonIronElectron,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.Physics.RusRoMuonIronElectron = cms.double(self.params[0])
        return process

class RusRoPreShowerElectron(ParamModifier):
    def __init__(self):
        super(RusRoPreShowerElectron,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.Physics.RusRoPreShowerElectron = cms.double(self.params[0])
        return process

class RusRoCastorElectron(ParamModifier):
    def __init__(self):
        super(RusRoCastorElectron,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.Physics.RusRoCastorElectron = cms.double(self.params[0])
        return process

class RusRoWorldElectron(ParamModifier):
    def __init__(self):
        super(RusRoWorldElectron,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.Physics.RusRoWorldElectron = cms.double(self.params[0])
        return process

class RusRoElectronEnergyLimit(ParamModifier):
    def __init__(self):
        super(RusRoElectronEnergyLimit,self).__init__(1)
    def apply(self, process):
	process.g4SimHits.Physics.RusRoEcalElectron      = cms.double(0.1)
	process.g4SimHits.Physics.RusRoHcalElectron      = cms.double(0.1)
	process.g4SimHits.Physics.RusRoMuonIronElectron  = cms.double(0.1)
	process.g4SimHits.Physics.RusRoPreShowerElectron = cms.double(0.1)
	process.g4SimHits.Physics.RusRoCastorElectron    = cms.double(0.1)
	process.g4SimHits.Physics.RusRoWorldElectron     = cms.double(0.1)
        process.g4SimHits.Physics.RusRoElectronEnergyLimit = cms.double(self.params[0])
        return process


##################################
#                                #
##  StackingAction  parameters  ##
#                                #
##################################

class RusRoGammaEnergyLimit(ParamModifier):
    def __init__(self):
        super(RusRoGammaEnergyLimit,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoGammaEnergyLimit = cms.double(self.params[0])
        return process

class RusRoEcalGamma(ParamModifier):
    def __init__(self):
        super(RusRoEcalGamma,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoEcalGamma = cms.double(self.params[0])
        return process

class RusRoHcalGamma(ParamModifier):
    def __init__(self):
        super(RusRoHcalGamma,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoHcalGamma = cms.double(self.params[0])
        return process

class RusRoMuonIronGamma(ParamModifier):
    def __init__(self):
        super(RusRoMuonIronGamma,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoMuonIronGamma = cms.double(self.params[0])
        return process

class RusRoPreShowerGamma(ParamModifier):
    def __init__(self):
        super(RusRoPreShowerGamma,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoPreShowerGamma = cms.double(self.params[0])
        return process

class RusRoCastorGamma(ParamModifier):
    def __init__(self):
        super(RusRoCastorGamma,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoCastorGamma = cms.double(self.params[0])
        return process

class RusRoWorldGamma(ParamModifier):
    def __init__(self):
        super(RusRoWorldGamma,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoWorldGamma = cms.double(self.params[0])
        return process

class RusRoHcalNeutronEnergyLimit(ParamModifier):
    def __init__(self):
        super(RusRoNeutronEnergyLimit,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoNeutronEnergyLimit = cms.double(self.params[0])
        return process

class RusRoEcalNeutron(ParamModifier):
    def __init__(self):
        super(RusRoEcalNeutron,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoEcalNeutron = cms.double(self.params[0])
        return process

class RusRoHcalNeutron(ParamModifier):
    def __init__(self):
        super(RusRoHcalNeutron,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoHcalNeutron = cms.double(self.params[0])
        return process

class RusRoMuonIronNeutron(ParamModifier):
    def __init__(self):
        super(RusRoMuonIronNeutron,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoMuonIronNeutron = cms.double(self.params[0])
        return process

class RusRoPreShowerNeutron(ParamModifier):
    def __init__(self):
        super(RusRoPreShowerNeutron,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoPreShowerNeutron = cms.double(self.params[0])
        return process

class RusRoCastorNeutron(ParamModifier):
    def __init__(self):
        super(RusRoCastorNeutron,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoCastorNeutron = cms.double(self.params[0])
        return process

class RusRoWorldNeutron(ParamModifier):
    def __init__(self):
        super(RusRoWorldNeutron,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoWorldNeutron = cms.double(self.params[0])
        return process

class RusRoProtonEnergyLimit(ParamModifier):
    def __init__(self):
        super(RusRoProtonEnergyLimit,self).__init__(1)
    def apply(self, process):
	process.g4SimHits.StackingAction.RusRoEcalProton      = cms.double(0.1)
	process.g4SimHits.StackingAction.RusRoHcalProton      = cms.double(0.1)
	process.g4SimHits.StackingAction.RusRoMuonIronProton  = cms.double(0.1)
	process.g4SimHits.StackingAction.RusRoPreShowerProton = cms.double(0.1)
	process.g4SimHits.StackingAction.RusRoCastorProton    = cms.double(0.1)
	process.g4SimHits.StackingAction.RusRoWorldProton     = cms.double(0.1)
        process.g4SimHits.StackingAction.RusRoProtonEnergyLimit = cms.double(self.params[0])
        return process

class RusRoEcalProton(ParamModifier):
    def __init__(self):
        super(RusRoEcalProton,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoEcalProton = cms.double(self.params[0])
        return process

class RusRoHcalProton(ParamModifier):
    def __init__(self):
        super(RusRoHcalProton,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoHcalProton = cms.double(self.params[0])
        return process

class RusRoMuonIronProton(ParamModifier):
    def __init__(self):
        super(RusRoMuonIronProton,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoMuonIronProton = cms.double(self.params[0])
        return process

class RusRoPreShowerProton(ParamModifier):
    def __init__(self):
        super(RusRoPreShowerProton,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoPreShowerProton = cms.double(self.params[0])
        return process
class RusRoCastorProton(ParamModifier):
    def __init__(self):
        super(RusRoCastorProton,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoCastorProton = cms.double(self.params[0])
        return process

class RusRoWorldProton(ParamModifier):
    def __init__(self):
        super(RusRoWorldProton,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoWorldProton = cms.double(self.params[0])
        return process

class RusRoGammaEnergyLimit(ParamModifier):
    def __init__(self):
        super(RusRoGammaEnergyLimit,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoGammaEnergyLimit = cms.double(self.params[0])
        return process

class RusRoNeutronEnergyLimit(ParamModifier):
    def __init__(self):
        super(RusRoNeutronEnergyLimit,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoNeutronEnergyLimit = cms.double(self.params[0])
        return process

class RusRoEcalProton(ParamModifier):
    def __init__(self):
        super(RusRoEcalProton,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoEcalProton = cms.double(self.params[0])
        return process

class RusRoHcalProton(ParamModifier):
    def __init__(self):
        super(RusRoHcalProton,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoHcalProton = cms.double(self.params[0])
        return process

class RusRoMuonIronProton(ParamModifier):
    def __init__(self):
        super(RusRoMuonIronProton,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoMuonIronProton = cms.double(self.params[0])
        return process

class RusRoPreShowerProton(ParamModifier):
    def __init__(self):
        super(RusRoPreShowerProton,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoPreShowerProton = cms.double(self.params[0])
        return process

class RusRoCastorProton(ParamModifier):
    def __init__(self):
        super(RusRoCastorProton,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoCastorProton = cms.double(self.params[0])
        return process

class RusRoWorldProton(ParamModifier):
    def __init__(self):
        super(RusRoWorldProton,self).__init__(1)
    def apply(self, process):
        process.g4SimHits.StackingAction.RusRoWorldProton = cms.double(self.params[0])
        return process



