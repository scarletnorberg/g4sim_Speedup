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

#include "XrdCl/XrdClURL.hh"
#include "XrdCl/XrdClFileSystem.hh"


// Root includes
#include "TROOT.h"
#include "TTree.h"
#include <boost/filesystem.hpp>
#include <iostream>

using namespace boost::filesystem;
using namespace std;
using namespace cms;
using namespace edm;
using namespace std;

int main(int argc,char**argv) {
     //char *directory="root://cmseos.fnal.gov//store/user/pedrok/g4speedup//run5/";
     //const std::filesystem::path sandbox{"root://cmseos.fnal.gov//store/user/pedrok/g4speedup//run5/"};
     //for(auto const& dir_entry: std::filesystem::directory_iterator{sandbox}) std::cout << dir_entry << '\n'; 
     // path p = "/uscms_data/d3/snorberg/Geant_Test/CMSSW_11_0_0/src";//current_path();
    // directory_iterator it{p};
    //    while (it != directory_iterator{})
    //            std::cout << *it++ << '\n';
    //TFile file("TOP-RunIISummer19UL18SIM-00034_nominal.root");
          int file_count(0);
          std::string url_string = "root://cmseos.fnal.gov/";
          std::string input = "/store/user/pedrok/g4speedup/run5/";
          if (argc==2) {
              input=argv[1];
              cout<<"input= "<<input<<endl;
          }else{
              cout<<"Unknown number of arguments ( "<<argc<<" )"<<endl;
              cout<<argv[0]<<" <path>"<<endl;
          }
          XrdCl::DirectoryList *response;
          XrdCl::DirListFlags::Flags flags = XrdCl::DirListFlags::None;
          XrdCl::URL url(url_string);
          XrdCl::FileSystem fs(url);
          fs.DirList(input,flags,response);
          for(auto iresp=response->Begin(); iresp!=response->End(); iresp++) {
              if((*iresp)->GetName().find(".root")!=std::string::npos) {
                  cout << "\tAdding " << url_string << input << (*iresp)->GetName() << endl;
                  cout << input<< endl;
                  std::string rootfileend = (*iresp)->GetName();
                  std::string root_file_name = url_string+input+rootfileend;
                  cout<<root_file_name<< endl;
                  TFile* file = TFile::Open(root_file_name.c_str(), "READ");
         //TFile ofile(rootfileend.c_str(),"RECREATE");
         fwlite::Event ev(&*file);
         TH1F EcalHitsEB_energyEM("EcalHitsEB_energyEM","EcalHitsEB energyEM",100,0.,5.);
         TH1F EcalHitsEB_energy("EcalHitsEB_energy","EcalHitsEB energy",100,0.,1000);
         TH1F EcalHitsEE_energyEM("EcalHitsEE_energyEM","EcalHitsEE energyEM",100,0.,5.);
         TH1F EcalHitsEE_energy("EcalHitsEE_energy","EcalHitsEE energy",100,0.,1000);
         fwlite::Handle<std::vector<PCaloHit>> obj;
         fwlite::Handle<std::vector<PCaloHit>> obj1;
         fwlite::Handle<std::vector<PCaloHit>> HH;
         //https://github.com/cms-sw/cmssw/blob/master/SimDataFormats/CaloHit/interface/PCaloHit.h information to extract 
         TFile *hfile = hfile = TFile::Open(rootfileend.c_str(),"RECREATE");
         TTree *tree = new TTree("Ecal_Hcal_Geant_Check","GeantV");
         Float_t EcalHitsEBenergyEM;
         Float_t EcalHitsEBenergy;
         Float_t EcalHitsEBenergyHad;
         Float_t EcalHitsEEenergyEM;
         Float_t EcalHitsEEenergy;
         Float_t EcalHitsEEenergyHad;
         Float_t HcalHitsenergy;
         Float_t HcalHitsenergyEM;
         Float_t HcalHitsenergyHad;
         tree->Branch("EcalHitsEBenergyEM",&EcalHitsEBenergyEM,"EcalHitsEBenergyEM/F");
         tree->Branch("EcalHitsEBenergy",&EcalHitsEBenergy,"EcalHitsEBenergy/F"); 
         tree->Branch("EcalHitsEBenergyHad",&EcalHitsEBenergyHad,"EcalHitsEBenergyHad/F");  
         tree->Branch("EcalHitsEEenergyEM",&EcalHitsEEenergyEM,"EcalHitsEEenergyEM/F");
         tree->Branch("EcalHitsEEenergy",&EcalHitsEEenergy,"EcalHitsEEenergy/F");
         tree->Branch("EcalHitsEEenergyHad",&EcalHitsEEenergyHad,"EcalHitsEEenergyHad/F");
         tree->Branch("HcalHitsenergy",&HcalHitsenergy,"HcalHitsenergy/F");
         tree->Branch("HcalHitsenergyEM",&HcalHitsenergyEM,"HcalHitsenergyEM/F");
         tree->Branch("HcalHitsenergyHad",&HcalHitsenergyHad,"HcalHitsenergyHad/F");
         for( ev.toBegin(); ! ev.atEnd(); ++ev) {
                obj.getByLabel(ev, "g4SimHits","EcalHitsEB");  
                obj1.getByLabel(ev, "g4SimHits", "EcalHitsEE");
                HH.getByLabel(ev, "g4SimHits", "HcalHits");
                //CaloHitsTk BeamHits
               for( auto const& ecee: *obj1) {
                     EcalHitsEE_energyEM.Fill(ecee.energyEM());
                     EcalHitsEE_energy.Fill(ecee.energy());
                     EcalHitsEEenergyEM=ecee.energy();
                     EcalHitsEEenergy=ecee.energyEM();
                     EcalHitsEEenergyHad=ecee.energyHad();
                     tree->Fill();
               } 
                for( auto const& hit: *obj) {
                      EcalHitsEB_energyEM.Fill(hit.energyEM());
                      EcalHitsEB_energy.Fill(hit.energy());
                      EcalHitsEBenergy=hit.energy();
                      EcalHitsEBenergyEM=hit.energyEM();
                      EcalHitsEBenergyHad=hit.energyHad();
                      tree->Fill();
                      //std::cout <<"size "<<hit.energyEM()<<std::endl;
                   }   
                for( auto const& hc: *HH) {
                       HcalHitsenergy=hc.energy();
                       HcalHitsenergyEM=hc.energyEM();
                       HcalHitsenergyHad=hc.energyHad();
                       tree->Fill();
                }
                  
           }
            //EcalHitsEB_energyEM.Write();
            //EcalHitsEB_energy.Write();
            //EcalHitsEE_energyEM.Write();
            //EcalHitsEE_energy.Write();
            //ofile.Close();
            tree->Print();
            tree->Write();
            delete hfile;
              }
          }
            return 0;
}
