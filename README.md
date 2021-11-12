# Setup and Running the Script

```bash
cmsrel CMSSW_11_0_0
cd CMSSW_11_0_0/src
cmsenv
git cms-init
git clone git@github.com:scarletnorberg/g4sim_Speedup.git
scram b
cd g4SimHit_SpeedUp/VarParameters
xrdcp root://cmseos.fnal.gov//store/user/snorberg/GEANT/PPD-RunIISummer20UL17GEN-00001.root .
python RunGeantSettings.sh
#./Script_RunGeantSettings.sh
```
```bash
To graph
cd EDM_Ntuple/bin/
scram b -j4
OutputEDMtoNtuple /store/user/pedrok/g4speedup/run5/ 
```
*Script_RunGeantSettings.sh* calls a second script, *RunEverything.sh*, which contains two lists, 
one for the desired parameters and the other for the values.

The first script iterates all the values for each parameter, does **cmsRun PPD_RunIISummer20UL17SIM_0_cfg.py**,
logs the summary of the run, and outputs the parameter, the value and the time it took to run through all the events.
Additionally, it produces a root file for each parameter and value.

We have had three runs so far which I will add some more information on.

Run 5 will be ProductionCuts which means that the DefaultCutValue changes 

Run 6 combined EnergyTH, RusRoNeutronEnergyLimit just 0.05,0.25 and 0, 100
