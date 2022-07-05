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
	for rootfile in rootfiles:      # loops the rootfiles in .txt file
		rootfile = rootfile.replace('\n','')  # eliminates 'new line' 
		## file in someone's path
		#rootfile_name = rootfile.replace("/uscms_data/d3/snorberg/Geant_Runs/CMSSW_11_0_0/src/g4sim_Speedup/EDM_Ntuple/bin/Run7","").replace("/","_").replace(".root","").replace('\n','')
		## file in my path
		rootfile_name = rootfile.replace("/uscms/home/bcruz/nobackup/YOURWORKINGAREA/CMSSW_11_0_0/src/Scarlet_g4sim_Speedup/EDM_Ntuple/bin","").replace("/","_").replace(".root","").replace("\n","")
		param_val = rootfile_name.replace("_sim_","").replace('\n','')
		param_val_list.append(param_val)

		print(param_val) # prints current paramater_value being read
		print(" ")

		with uproot.open(rootfile) as file:
			### print(file.keys()) = ECAL_HCAL_Geant_Check; T; Ecal_Hcal_Geant_Check (depends on "run#")
			Tree = file["Ecal_Hcal_Geant_Check"]	# accessing the TTree
			Branches = list(Tree.keys())		# accessing and listing the Tree's TBranches

			for branch in Branches:
				branch = branch.decode('utf8').strip()			# decode the utf8 byte from the string
				param_val_branch = str(branch) + str("_") + param_val	# Branch's parameter_value (to be used as Dict key) 
				data = Tree[str(branch)].array()
				
				# make a sequence (for binning) from the data
				edges_seq = np.linspace(min(data),max(data), num=20, dtype=int, endpoint=True)
				
				branch_vals = np.histogram(data, bins=edges_seq)	# Branch's array-value (to be used as Dict value)	
				branch_pattern = re.compile(str(branch))		# set the Branch string as a pattern for matching
				
				# fill the appropriate dictionary
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

## Lists to add the respective Branch's binning from all the rootfiles
EcalHitsEBenergyEM_bins = []
EcalHitsEBenergy_bins = []
EcalHitsEBenergyHad_bins = []
EcalHitsEEenergyEM_bins = []
EcalHitsEEenergy_bins = []
EcalHitsEEenergyHad_bins = []
HcalHitsenergy_bins = []
HcalHitsenergyEM_bins = []
HcalHitsenergyHad_bins = []

Bins_list = [EcalHitsEBenergyEM_bins, EcalHitsEBenergy_bins, EcalHitsEBenergyHad_bins, EcalHitsEEenergyEM_bins, EcalHitsEEenergy_bins, EcalHitsEEenergyHad_bins, HcalHitsenergy_bins, HcalHitsenergyEM_bins, HcalHitsenergyHad_bins]


## Loop to add the Branch value to their respective Value list
for D in Dict_list:	# loop Branches dictionaries list
	for b,v in D.items():	# goes through items of the current dictionary

		## remove the parameter and value from the string, and set the branch_name as pattern for matching
		branch_name = b.replace("ProductionCut","").strip("__-0.123456789")	# change the first string when needed
		branch_param = b.strip("__-0.123456789")
		pattern = re.compile(str(branch_name))

		## getting the bin-center for ratio plot
		edges = v[1]
		bin_centers = edges[:-1] + np.diff(edges,n=1)/2		

		# fill the respective data and binning dictionaries
		if re.fullmatch(pattern, "EcalHitsEBenergyEM"):
			EcalHitsEBenergyEM_data.append(v[0])
			EcalHitsEBenergyEM_bins.append(bin_centers)
			continue

		elif re.fullmatch(pattern, "EcalHitsEBenergy"):
			EcalHitsEBenergy_data.append(v[0])
			EcalHitsEBenergy_bins.append(bin_centers)
			continue

		elif re.fullmatch(pattern, "EcalHitsEBenergyHad"):
			EcalHitsEBenergyHad_data.append(v[0])
			EcalHitsEBenergyHad_bins.append(bin_centers)
			continue

		elif re.fullmatch(pattern, "EcalHitsEEenergyEM"):
			EcalHitsEEenergyEM_data.append(v[0])
			EcalHitsEEenergyEM_bins.append(bin_centers)
			continue

		elif re.fullmatch(pattern, "EcalHitsEEenergy"):
			EcalHitsEEenergy_data.append(v[0])
			EcalHitsEEenergy_bins.append(bin_centers)
			continue

		elif re.fullmatch(pattern, "EcalHitsEEenergyHad"):
			EcalHitsEEenergyHad_data.append(v[0])
			EcalHitsEEenergyHad_bins.append(bin_centers)
			continue

		elif re.fullmatch(pattern, "HcalHitsenergy"):
			HcalHitsenergy_data.append(v[0])
			HcalHitsenergy_bins.append(bin_centers)
			continue

		elif re.fullmatch(pattern, "HcalHitsenergyEM"):
			HcalHitsenergyEM_data.append(v[0])
			HcalHitsenergyEM_bins.append(bin_centers)
			continue

		elif re.fullmatch(pattern, "HcalHitsenergyHad"):
			HcalHitsenergyHad_data.append(v[0])
			HcalHitsenergyHad_bins.append(bin_centers)
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


## Ordered Dictionaries for the centered-bins for ratio plot
EcalHitsEBenergyEM_binning = OrderedDict()
EcalHitsEBenergy_binning = OrderedDict()
EcalHitsEBenergyHad_binning = OrderedDict()
EcalHitsEEenergyEM_binning = OrderedDict()
EcalHitsEEenergy_binning = OrderedDict()
EcalHitsEEenergyHad_binning = OrderedDict()
HcalHitsenergy_binning = OrderedDict()
HcalHitsenergyEM_binning = OrderedDict()
HcalHitsenergyHad_binning = OrderedDict()

## Ratio plots centered-bins to be plotted list
BinningList_toPlot = [EcalHitsEBenergyEM_binning, EcalHitsEBenergy_binning, EcalHitsEBenergyHad_binning, EcalHitsEEenergyEM_binning, EcalHitsEEenergy_binning, EcalHitsEEenergyHad_binning, HcalHitsenergy_binning, HcalHitsenergyEM_binning, HcalHitsenergyHad_binning]


###print(len(HcalHitsenergyHad_data)) = 4
###print(len(Value_list)) = 9 
###print(len(Dict_list)) = 9 
###print(len(Dict_HcalHitsenergyHad)) = 4

## Loop to add to the OrderedDict the Branch as the 'key' and the respective values list as the 'value' 
for D in Dict_list:    # 9 dictionaries
	key_list = D.keys()

	for k in key_list:  # 4 keys in each dictionary
		branch_name = k.replace("ProductionCut","").strip("__-0.123456789")   # change the first string when needed
		branch_param = k.strip("__-0.123456789")
		pattern = re.compile(str(branch_name))

	# fill the respective value and binning plotting-Dictionary
	if re.fullmatch(pattern, "EcalHitsEBenergyEM"):
		EcalHitsEBenergyEM_toplot[str(branch_param)] = Value_list[0]
		EcalHitsEBenergyEM_binning[str(branch_param)] = Bins_list[0]
		continue
	elif re.fullmatch(pattern, "EcalHitsEBenergy"):
		EcalHitsEBenergy_toplot[str(branch_param)] = Value_list[1]
		EcalHitsEBenergy_binning[str(branch_param)] = Bins_list[1]
		continue
	elif re.fullmatch(pattern, "EcalHitsEBenergyHad"):
		EcalHitsEBenergyHad_toplot[str(branch_param)] = Value_list[2]
		EcalHitsEBenergyHad_binning[str(branch_param)] = Bins_list[2]
		continue
	elif re.fullmatch(pattern, "EcalHitsEEenergyEM"):
		EcalHitsEEenergyEM_toplot[str(branch_param)] = Value_list[3]
		EcalHitsEEenergyEM_binning[str(branch_param)] = Bins_list[3]
		continue
	elif re.fullmatch(pattern, "EcalHitsEEenergy"):
		EcalHitsEEenergy_toplot[str(branch_param)] = Value_list[4]
		EcalHitsEEenergy_binning[str(branch_param)] = Bins_list[4]
		continue
	elif re.fullmatch(pattern, "EcalHitsEEenergyHad"):
		EcalHitsEEenergyHad_toplot[str(branch_param)] = Value_list[5]
		EcalHitsEEenergyHad_binning[str(branch_param)] = Bins_list[5]
		continue
	elif re.fullmatch(pattern, "HcalHitsenergy"):
		HcalHitsenergy_toplot[str(branch_param)] = Value_list[6]
		HcalHitsenergy_binning[str(branch_param)] = Bins_list[6]
		continue
	elif re.fullmatch(pattern, "HcalHitsenergyEM"):
		HcalHitsenergyEM_toplot[str(branch_param)] = Value_list[7]
		HcalHitsenergyEM_binning[str(branch_param)] = Bins_list[7]
		continue
	elif re.fullmatch(pattern, "HcalHitsenergyHad"):
		HcalHitsenergyHad_toplot[str(branch_param)] = Value_list[8]
		HcalHitsenergyHad_binning[str(branch_param)] = Bins_list[8]
		continue
	else:
		continue

## Plot styling
colors = ["#9c9ca1", "#e42536", "#5790fc", "#964a8b"]
styles = ['solid', 'dotted', 'dashed', 'dashdot']

## Histogram-plotting function, with ratioplots to the baseline
def plotting(x,y,z,x1,x2,x3,c1,c2,c3):
	fig, axs = plt.subplots(2,1, sharex='all', figsize=(10,8),
				gridspec_kw={'width_ratios': [1],
						'height_ratios':[2,1],
						'wspace': 0.2,
						'hspace': 0.2} )
	# make the histogram
	hep.histplot(x, histtype='step', color=colors, linestyle=styles, label=param_val_list, ax=axs[0])
	plt.suptitle(y, fontsize=20)
	axs[0].set(yscale="log")
	axs[0].set_ylabel("Hits", fontsize=15)
	axs[0].legend(loc='upper right')
	

	# make the ratio plots' y-scale logarithmic if the maximum value is greater than 10
	if max(x1)>10:
		axs[1].scatter(c1,x1, color="#e42536", marker='o')
		axs[1].set(yscale='log')
	else:
		axs[1].scatter(c1,x1, color="#e42536", marker='o')
	
	if max(x2)>10:
		axs[1].scatter(c2,x2, color="#5790fc", marker='s')
		axs[1].set(yscale='log')
	else:
		axs[1].scatter(c2,x2, color="#5790fc", marker='s' )
	
	if max(x3)>10:
		axs[1].scatter(c3,x3, color="#964a8b", marker='^')
		axs[1].set(yscale='log')
	else:
		axs[1].scatter(c3,x3, color="#964a8b", marker='^')

	# make the ratio plot
	axs[1].set_xlabel(z+" [MeV]", fontsize=15)
	axs[1].set_ylabel(r'$\frac{Parameter change}{Baseline}$', fontsize=16)
	plt.savefig(y+".png")  # save figure at the current directory
	plt.close()

## Plotting Loop for the Ordered Dictionaries
for P,C in zip(DictList_toPlot,BinningList_toPlot):
	for ec in C.values(): # loop the binning dictionary; get the second, third, and fourth values to use in  ratio plot binning
		ec1 = ec[1]
		ec2 = ec[2]
		ec3 = ec[3]
		continue # to the next for-loop

	for k,v in P.items(): # loop the values dictionary
		branch_name = k.replace("ProductionCut","").strip("_")  # change the first string when neeeded
		baseline=v[0]
		val2=v[1]
		val3=v[2]
		val4=v[3]
			
		# perform the ratio between the changed parameter values to the baseline value;
		# make any zero or infinity values NAN	
		ratio1=val2/baseline
		ratio1=np.nan_to_num(ratio1, nan=0.0, posinf=0.0)

		ratio2=val3/baseline
		ratio2=np.nan_to_num(ratio2, nan=0.0, posinf=0.0)

		ratio3=val4/baseline
		ratio3=np.nan_to_num(ratio3, nan=0.0, posinf=0.0)
		
		# plot current parameter dictionary
		print("plotting ", k)
		plotting(v,k,branch_name,ratio1,ratio2,ratio3,ec1,ec2,ec3) 
		print(" ")
		continue # to next P,C iteration	

print("Done!")

