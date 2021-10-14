#if !defined(__CINT__) && !defined(__MAKECINT__)
#include "DataFormats/FWLite/interface/Handle.h"
#include "DataFormats/FWLite/interface/Event.h"
//Headers for the data items

#include "DQMServices/Core/interface/DQMStore.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "Validation/EcalHits/interface/EcalSimHitsValidation.h"
#include <DataFormats/EcalDetId/interface/EBDetId.h>
#include <DataFormats/EcalDetId/interface/EEDetId.h>
#include <DataFormats/EcalDetId/interface/ESDetId.h>

#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Photon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/TrackReco/interface/Track.h"

#include "PhysicsTools/FWLite/interface/EventContainer.h"
#include "PhysicsTools/FWLite/interface/CommandLineParser.h"
#include <filesystem>
#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <experimental/filesystem> // http://en.cppreference.com/w/cpp/experimental/fs


// Root includes
#include "TROOT.h"

#include <boost/filesystem.hpp>
#include <iostream>

using namespace boost::filesystem;

using namespace std;

using namespace cms;
using namespace edm;
using namespace std;

#endif
void print_data() {
     //char *directory="root://cmseos.fnal.gov//store/user/pedrok/g4speedup//run5/";
     //const std::filesystem::path sandbox{"root://cmseos.fnal.gov//store/user/pedrok/g4speedup//run5/"};
     //for(auto const& dir_entry: std::filesystem::directory_iterator{sandbox}) std::cout << dir_entry << '\n'; 
      path p = "/uscms_data/d3/snorberg/Geant_Test/CMSSW_11_0_0/src";//current_path();
        directory_iterator it{p};
          while (it != directory_iterator{})
                  std::cout << *it++ << '\n';
    TFile file("TOP-RunIISummer19UL18SIM-00034_nominal.root");
      TFile ofile("Top_nominal.root","RECREATE");
         fwlite::Event ev(&file);
         TH1F ECHBB_EEM("ECHBB_EEM","EcalHitsEB energyEM",100,0.,5.);
         TH1F ECHBB_E("ECHBB_E","EcalHitsEB energy",100,0.,1000);
         TH1F ECHEE_EEM("ECHEE_EEM","EcalHitsEE energyEM",100,0.,5.);
         TH1F ECHEE_E("ECHEE_E","EcalHitsEE energy",100,0.,1000);
         fwlite::Handle<std::vector<PCaloHit>> obj;
         fwlite::Handle<std::vector<PCaloHit>> obj1;
         fwlite::Handle<std::vector<PCaloHit>> HH;
         //https://github.com/cms-sw/cmssw/blob/master/SimDataFormats/CaloHit/interface/PCaloHit.h information to extract 
         TFile *hfile = hfile = TFile::Open("Top_nominal.root","RECREATE");
         TTree *tree = new TTree("T","GeantV");
         Float_t ECHBBEEM;
         Float_t ECHBBE;
         Float_t ECHBEEEM;
         Float_t ECHBEE;
         tree->Branch("ECHBBEEM",&ECHBBEEM,"ECHBBEEM/F");
         tree->Branch("ECHBBE",&ECHBBE,"ECHBBE/F");   
         tree->Branch("ECHBEEEM",&ECHBEEEM,"ECHBEEEM/F");
         tree->Branch("ECHBEE",&ECHBEE,"ECHBEE/F");
         for( ev.toBegin(); ! ev.atEnd(); ++ev) {
                obj.getByLabel(ev, "g4SimHits","EcalHitsEB");  
                obj1.getByLabel(ev, "g4SimHits", "EcalHitsEE");
                HH.getByLabel(ev, "g4SimHits", "HcalHits");
                //CaloHitsTk BeamHits
               for( auto const& ecee: *obj1) {
                     ECHEE_EEM.Fill(ecee.energyEM());
                     ECHEE_E.Fill(ecee.energy());
                     ECHBEE=ecee.energy();
                     ECHBEEEM=ecee.energyEM();
                     tree->Fill();
               } 
                for( auto const& hit: *obj) {
                      ECHBB_EEM.Fill(hit.energyEM());
                      ECHBB_E.Fill(hit.energy());
                      ECHBBE=hit.energy();
                      ECHBBEEM=hit.energyEM();
                      tree->Fill();
                      //std::cout <<"size "<<hit.energyEM()<<std::endl;
                   }   
                  
           }
            ECHBB_EEM.Write();
            ECHBB_E.Write();
            ECHEE_EEM.Write();
            ECHEE_E.Write();
            ofile.Close();
            tree->Print();
            tree->Write();
            delete hfile;
}
