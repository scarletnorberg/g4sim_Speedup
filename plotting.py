import uproot			# to access rootfiles
import matplotlib.pyplot as plt	# to edit plots
import re			# to match strings
import numpy as np		# to obtain the np.histogram() objects
import mplhep as hep		# to plot the histograms
from collections import OrderedDict   # to avoid dict() random order when plotting

## Branch Ordered dictionaries 
Dict_EcalHitsEBenergyEM = OrderedDict()
Dict_EcalHitsEBenergy = OrderedDict()
Dict_EcalHitsEBenergyHad = OrderedDict()
Dict_EcalHitsEEenergyEM = OrderedDict()
Dict_EcalHitsEEenergy = OrderedDict()
Dict_EcalHitsEEenergyHad = OrderedDict()
Dict_HcalHitsenergy = OrderedDict()
Dict_HcalHitsenergyEM = OrderedDict()
Dict_HcalHitsenergyHad = OrderedDict()

## Branch dictionaries list
Dict_list = [Dict_EcalHitsEBenergyEM, Dict_EcalHitsEBenergy, Dict_EcalHitsEBenergyHad, Dict_EcalHitsEEenergyEM, Dict_EcalHitsEEenergy, Dict_EcalHitsEEenergyHad, Dict_HcalHitsenergy, Dict_HcalHitsenergyEM, Dict_HcalHitsenergyHad]

## list for the parameters and their respective value (this will be used for plotting)
param_val_list = [] 

param_val_branch_list = []

with open('edm_rootfiles.txt') as f:    # read desired text file with rootfiles' path; change when needed
	rootfiles = f.readlines()
	for rootfile in rootfiles:       # loops the rootfiles in .txt file
		rootfile = rootfile.replace('\n','')  # eliminates 'new line' 
		## file in someone's path
		#rootfile_name = rootfile.replace("/uscms_data/d3/snorberg/Geant_Runs/CMSSW_11_0_0/src/g4sim_Speedup/EDM_Ntuple/bin/Run7","").replace("/","_").replace(".root","").replace('\n','')
		## file in my path
		rootfile_name = rootfile.replace("/uscms/home/bcruz/nobackup/YOURWORKINGAREA/CMSSW_11_0_0/src/g4sim_Speedup/EDM_Ntuple/bin","").replace("/","_").replace(".root","").replace("\n","")
		param_val = rootfile_name.replace("_sim_","").replace('\n','')
		param_val_list.append(param_val)

		print(param_val)
		print(" ")

		with uproot.open(rootfile) as file:
			#print(file.keys()) = ECAL_HCAL_Geant_Check; T; Ecal_Hcal_Geant_Check (depends on "run#")
			Tree = file["Ecal_Hcal_Geant_Check"]	# accessing the TTree
			Branches = list(Tree.keys())		# accessing and listing the Tree's TBranches

			for branch in Branches:
				branch = branch.decode('utf8').strip()			# decode the utf8 byte from the string
				param_val_branch = str(branch) + str("_") + param_val	# Branch's parameter_value (to be used as Dict key) 

				branch_vals = np.histogram(Tree[str(branch)].array(), bins=20)	# Branch's array-value (to be used as Dict value)	
				branch_pattern = re.compile(str(branch))			# set the Branch string as a pattern for matching
			
				## verifying file's Hits amount
				#print(param_val_branch," hist sum = ",branch_vals[0].sum())
				#print()
	
				## Match the branh_pattern to add the current Branch's parameter and value as key
				## and the Branch's array-value as value to the appropriate dictionary

				if re.fullmatch(branch_pattern, "EcalHitsEBenergyEM"):
					Dict_EcalHitsEBenergyEM[str(param_val_branch)] = branch_vals
					continue
				elif re.fullmatch(branch_pattern, "EcalHitsEBenergy"):
					Dict_EcalHitsEBenergy[str(param_val_branch)] = branch_vals
					continue 
				elif re.fullmatch(branch_pattern, "EcalHitsEBenergyHad"):
					Dict_EcalHitsEBenergyHad[str(param_val_branch)] = branch_vals
					continue
				elif re.fullmatch(branch_pattern, "EcalHitsEEenergyEM"):
					Dict_EcalHitsEEenergyEM[str(param_val_branch)] = branch_vals
					continue
				elif re.fullmatch(branch_pattern, "EcalHitsEEenergy"):
					Dict_EcalHitsEEenergy[str(param_val_branch)] = branch_vals
					continue
				elif re.fullmatch(branch_pattern, "EcalHitsEEenergyHad"):
					Dict_EcalHitsEEenergyHad[str(param_val_branch)] = branch_vals
					continue
				elif re.fullmatch(branch_pattern, "HcalHitsenergy"):
					Dict_HcalHitsenergy[str(param_val_branch)] = branch_vals
					continue
				elif re.fullmatch(branch_pattern, "HcalHitsenergyEM"):
					Dict_HcalHitsenergyEM[str(param_val_branch)] = branch_vals
					continue
				elif re.fullmatch(branch_pattern, "HcalHitsenergyHad"):
					Dict_HcalHitsenergyHad[str(param_val_branch)] = branch_vals
					continue
				else:
					continue
		

## Lists to add respective Branch's values from all the rootfiles
EcalHitsEBenergyEM_data = []
EcalHitsEBenergy_data = []
EcalHitsEBenergyHad_data = []
EcalHitsEEenergyEM_data = []
EcalHitsEEenergy_data = []
EcalHitsEEenergyHad_data = []
HcalHitsenergy_data = []
HcalHitsenergyEM_data = []
HcalHitsenergyHad_data = []

Value_list = [EcalHitsEBenergyEM_data, EcalHitsEBenergy_data, EcalHitsEBenergyHad_data, EcalHitsEEenergyEM_data, EcalHitsEEenergy_data, EcalHitsEEenergyHad_data, HcalHitsenergy_data, HcalHitsenergyEM_data, HcalHitsenergyHad_data]

## Plot styling
colors = ["#9c9ca1", "#e42536", "#5790fc", "#964a8b"]
styles = ['solid', 'dotted', 'dashed', 'dashdot']

## Histogram plotting function, with ratioplots to the baseline
def plotting(x,y,z):
	hep.histplot(x, histtype='step', color=colors, linestyle=styles, label=param_val_list)
	plt.title(y)
	plt.xlabel(z+" [MeV]")
	plt.ylabel("Hits")
	plt.yscale("log")
	plt.legend(loc='upper right')
	plt.savefig(y+".png")
	plt.close()

## Loop to add the Branch value to their respective Value list
for D in Dict_list:	# loop Branches dictionaries list
	for b,v in D.items():	# goes through items of the current dictionary

		## remove the parameter and value from the string, and set the branch_name as pattern for matching
		branch_name = b.replace("ProductionCut","").strip("__-0.123456789")	# change the first string when needed
		branch_param = b.strip("__-0.123456789")
		pattern = re.compile(str(branch_name))
		
		if re.fullmatch(pattern, "EcalHitsEBenergyEM"):
			EcalHitsEBenergyEM_data.append(v[0])
			continue

		elif re.fullmatch(pattern, "EcalHitsEBenergy"):
			EcalHitsEBenergy_data.append(v[0])
			continue

		elif re.fullmatch(pattern, "EcalHitsEBenergyHad"):
			EcalHitsEBenergyHad_data.append(v[0])
			continue

		elif re.fullmatch(pattern, "EcalHitsEEenergyEM"):
			EcalHitsEEenergyEM_data.append(v[0])
			continue

		elif re.fullmatch(pattern, "EcalHitsEEenergy"):
			EcalHitsEEenergy_data.append(v[0])
			continue

		elif re.fullmatch(pattern, "EcalHitsEEenergyHad"):
			EcalHitsEEenergyHad_data.append(v[0])
			continue

		elif re.fullmatch(pattern, "HcalHitsenergy"):
			HcalHitsenergy_data.append(v[0])
			continue

		elif re.fullmatch(pattern, "HcalHitsenergyEM"):
			HcalHitsenergyEM_data.append(v[0])
			continue

		elif re.fullmatch(pattern, "HcalHitsenergyHad"):
			HcalHitsenergyHad_data.append(v[0])
			continue

		else:
			continue

## Ordered Dictionaries for the Branches to be plotted 

EcalHitsEBenergyEM_toplot = OrderedDict()
EcalHitsEBenergy_toplot = OrderedDict()
EcalHitsEBenergyHad_toplot = OrderedDict()
EcalHitsEEenergyEM_toplot = OrderedDict()
EcalHitsEEenergy_toplot = OrderedDict()
EcalHitsEEenergyHad_toplot = OrderedDict()
HcalHitsenergy_toplot = OrderedDict()
HcalHitsenergyEM_toplot = OrderedDict()
HcalHitsenergyHad_toplot = OrderedDict()

## Dictionaries to be plotted list
DictList_toPlot = [EcalHitsEBenergyEM_toplot, EcalHitsEBenergy_toplot, EcalHitsEBenergyHad_toplot, EcalHitsEEenergyEM_toplot, EcalHitsEEenergy_toplot, EcalHitsEEenergyHad_toplot, HcalHitsenergy_toplot, HcalHitsenergyEM_toplot, HcalHitsenergyHad_toplot]


#print(len(HcalHitsenergyHad_data)) = 4
#print(len(Value_list)) = 9 
#print(len(Dict_list)) = 9 
#print(len(Dict_HcalHitsenergyHad)) = 4

## Loop to add to the OrderedDict the Branch as the 'key' and the respective values list as the 'value' 
for D in Dict_list:    # 9 dictionaries

	key_list = D.keys()

	for k in key_list:  # 4 keys 

		branch_name = k.replace("ProductionCut","").strip("__-0.123456789")   # change the first string when needed
		branch_param = k.strip("__-0.123456789")
		pattern = re.compile(str(branch_name))

	if re.fullmatch(pattern, "EcalHitsEBenergyEM"):
		EcalHitsEBenergyEM_toplot[str(branch_param)] = Value_list[0]
		continue
	elif re.fullmatch(pattern, "EcalHitsEBenergy"):
		EcalHitsEBenergy_toplot[str(branch_param)] = Value_list[1]
		continue
	elif re.fullmatch(pattern, "EcalHitsEBenergyHad"):
		EcalHitsEBenergyHad_toplot[str(branch_param)] = Value_list[2]
		continue
	elif re.fullmatch(pattern, "EcalHitsEEenergyEM"):
		EcalHitsEEenergyEM_toplot[str(branch_param)] = Value_list[3]
		continue
	elif re.fullmatch(pattern, "EcalHitsEEenergy"):
		EcalHitsEEenergy_toplot[str(branch_param)] = Value_list[4]
		continue
	elif re.fullmatch(pattern, "EcalHitsEEenergyHad"):
		EcalHitsEEenergyHad_toplot[str(branch_param)] = Value_list[5]
		continue
	elif re.fullmatch(pattern, "HcalHitsenergy"):
		HcalHitsenergy_toplot[str(branch_param)] = Value_list[6]
		continue
	elif re.fullmatch(pattern, "HcalHitsenergyEM"):
		HcalHitsenergyEM_toplot[str(branch_param)] = Value_list[7]
		continue
	elif re.fullmatch(pattern, "HcalHitsenergyHad"):
		HcalHitsenergyHad_toplot[str(branch_param)] = Value_list[8]
		continue

	else:
		continue

## Plotting Loop for the Ordered Dictionaries
for P in DictList_toPlot:
	for k,v in P.items():
		branch_name = k.replace("ProductionCut","").strip("_")  # change the first string when neeeded
		print("plotting ", k)
		plotting(v,k,branch_name)
		print(" ")	

print("The End!")

