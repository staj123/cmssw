import FWCore.ParameterSet.Config as cms
from RecoEgamma.ElectronIdentification.Identification.mvaElectronID_tools import *
from os import path

# Egamma presentation on this ID
# https://indico.cern.ch/event/732971/contributions/3022864/attachments/1658765/2656595/180530_egamma.pdf

mvaTag = "Win22IsoV2"

weightFileDir = "RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Win22IsoV2"

mvaWeightFiles = [
     path.join(weightFileDir, "EB1_5.weights.root"), # EB1_5
     path.join(weightFileDir, "EB2_5.weights.root"), # EB2_5
     path.join(weightFileDir, "EE_5.weights.root"), # EE_5
     path.join(weightFileDir, "EB1_10.weights.root"), # EB1_10
     path.join(weightFileDir, "EB2_10.weights.root"), # EB2_10
     path.join(weightFileDir, "EE_10.weights.root"), # EE_10
     ]

#mvaEleID_Win22_iso_V2_wpHZZ_container = EleMVARaw_WP(
#    idName = "mvaEleID-Fall17-iso-V2-wpHZZ", mvaTag = mvaTag,
#    cutCategory0 = "1.26402092475", # EB1_5
#    cutCategory1 = "1.17808089508", # EB2_5
#    cutCategory2 = "1.33051972806", # EE_5
#    cutCategory3 = "2.36464785939", # EB1_10
#    cutCategory4 = "2.07880614597", # EB2_10
#    cutCategory5 = "1.08080644615", # EE_10
#    )

mvaEleID_Win22_iso_V2_wp80_container = EleMVARaw_WP(
    idName = "mvaEleID-Fall17-iso-V2-wp80", mvaTag = mvaTag,
    cutCategory0 = "0.956654715538025", # EB1_5
    cutCategory1 = "0.9244146823883057", # EB2_5
    cutCategory2 = "0.8489419341087341", # EE_5
    cutCategory3 = "0.9934913158416748", # EB1_10
    cutCategory4 = "0.9874098300933838", # EB2_10
    cutCategory5 = "0.9670001745223998", # EE_10
    )

#mvaEleID_Win22_iso_V2_wpLoose_container = EleMVARaw_WP(
#    idName = "mvaEleID-Fall17-iso-V2-wpLoose", mvaTag = mvaTag,
#    cutCategory0 = "0.700642584415", # EB1_5
#    cutCategory1 = "0.739335420875", # EB2_5
#    cutCategory2 = "1.45390456109", # EE_5
#    cutCategory3 = "-0.146270871164", # EB1_10
#    cutCategory4 = "-0.0315850882679", # EB2_10
#    cutCategory5 = "-0.0321841194737", # EE_10
#    )

mvaEleID_Win22_iso_V2_wp90_container = EleMVARaw_WP(
    idName = "mvaEleID-Fall17-iso-V2-wp90", mvaTag = mvaTag,
    cutCategory0 = "0.9001831412315369", # EB1_5
    cutCategory1 = "0.8278245985507964", # EB2_5
    cutCategory2 = "0.672588300704956", # EE_5
    cutCategory3 = "0.9818042814731598", # EB1_10
    cutCategory4 = "0.9656652748584746", # EB2_10
    cutCategory5 = "0.9055343508720398", # EE_10
    )


workingPoints = dict(
#    wpHZZ = mvaEleID_Win22_iso_V2_wpHZZ_container,
    wp80 = mvaEleID_Win22_iso_V2_wp80_container,
#    wpLoose = mvaEleID_Win22_iso_V2_wpLoose_container,
    wp90 = mvaEleID_Win22_iso_V2_wp90_container
)

mvaEleID_Win22_iso_V2_producer_config = cms.PSet(
    mvaName             = cms.string(mvaClassName),
    mvaTag              = cms.string(mvaTag),
    nCategories         = cms.int32(6),
    categoryCuts        = cms.vstring(*EleMVA_6CategoriesCuts),
    weightFileNames     = cms.vstring(*mvaWeightFiles),
    variableDefinition  = cms.string(mvaVariablesFile)
    )

#mvaEleID_Win22_iso_V2_wpHZZ = configureVIDMVAEleID( mvaEleID_Win22_iso_V2_wpHZZ_container )
mvaEleID_Win22_iso_V2_wp80 = configureVIDMVAEleID( mvaEleID_Win22_iso_V2_wp80_container )
#mvaEleID_Win22_iso_V2_wpLoose = configureVIDMVAEleID( mvaEleID_Win22_iso_V2_wpLoose_container )
mvaEleID_Win22_iso_V2_wp90 = configureVIDMVAEleID( mvaEleID_Win22_iso_V2_wp90_container )

#mvaEleID_Win22_iso_V2_wpHZZ.isPOGApproved = cms.untracked.bool(True)
mvaEleID_Win22_iso_V2_wp80.isPOGApproved = cms.untracked.bool(True)
#mvaEleID_Win22_iso_V2_wpLoose.isPOGApproved = cms.untracked.bool(True)
mvaEleID_Win22_iso_V2_wp90.isPOGApproved = cms.untracked.bool(True)
