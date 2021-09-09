#!/bin/bash

## The following works by having all the parameters in one list
## and all the desired values (assiming all parameters share them) in another.
## The other script calls each list and loops over their entries.

## list of paramters to run
#parameters=(RusRoEcalGamma RusRoHcalGamma RusRoMuonIronGamma RusRoHcalNeutron RusRoEcalNeutron RusRoMuonIronNeutron)

## list of values to run for each parameter
#values=(0.1 0.2 0.3 0.4 0.5 0.7 0.8 0.9 1.0)


## using associative arrays so that you can loop over different values for each parameter if needed

# declare the array
declare -A parameters

# declare the list of values
Energy_vals=(200 250 300 350 400 450 500 550 800)
Mag_Values=(0.01 0.015 0.05 0.1 0.15 0.2 0.25 0.3 0.35)
#RusRo_vals=(0.1 0.01 0.001 0.0001 0.00001)

# assigning array elements a specific value list
parameters[RusRoGammaEnergyLimit]=Energy_vals[@]
parameters[RusRoNeutronEnergyLimit]=Energy_vals[@]
parameters[EnergyThSimple]=Mag_Values[@]
parameters[DeltaOneStepSimple]=Mag_Values[@]
parameters[DeltaChordSimple]=Mag_Values[@]

#parameters[RusRoEcalGamma]=RusRo_vals[@]
#parameters[RusRoHcalGamma]=RusRo_vals[@]
#parameters[RusRoMuonIronGamma]=RusRo_vals[@]
#parameters[RusRoHcalNeutron]=RusRo_vals[@]  
#parameters[RusRoEcalNeutron]=RusRo_vals[@] 
#parameters[RusRoMuonIronNeutron]=RusRo_vals[@]



## Testing 

# echo to show the key and value; it shows them in the order they were added, bottom to top, on a single line
#echo ${!parameters[@]} ${parameters[@]}

# for loop to test what values each parameter loops over 
#for par in "${!parameters[@]}"; do
#    for val in "${!parameters[$par]}"; do
#        echo $par $val
#   done
#done

#for par in "${!parameters[@]}"; do
#    echo $par ${parameters[@]}
#done
