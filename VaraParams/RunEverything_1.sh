#!/bin/bash

## The following works calling the local variable in the other script

#parameters ()
#{
#    param1=EnergyThSimple
#}

#values ()
#{
#   vals1=(0.015 0.05)
#}

## The following works by having all the parameters in one list
## and all the desired values (assiming all parameters share them) in another.
## The other script calls each list and loops over their entries.

parameters=(RusRoEcalGamma RusRoHcalGamma RusRoMuonIronGamma RusRoHcalNeutron RusRoEcalNeutron RusRoMuonIronNeutron)

values=(0.1 0.2 0.3 0.4 0.5 0.7 0.8 0.9 1.0)
