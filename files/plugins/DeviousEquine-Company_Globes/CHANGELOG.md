- 1.2.2
  - Actually fixed the client joining issue now (for some reason joining clients would load a level called TestAllEnemies when joining)

- 1.2.1
  - Fixed the furniture completely breaking for clients upon joining

- 1.2.0
  - Added a standing globe furniture - Model is a WIP and I'm still bug testing it currently
  - Potentially fixed the globe models disappearing under certain circumstances when reloading a save (Experimentation globes keep turning into other types of globe though, I need to look into that)
  - Embrion and Adamance should no longer be tiny if using Chameleon

- 1.1.1
  - Removed some debug stuff
  - Fixed a small loaded type error
  - Remembered to save the changelog before I published the update this time

- 1.1.0
  - Recompiled for v80

- 1.0.6
  - Fixed weird offset
  - Fixed changelog

- 1.0.5
  - Updated for version 0.7.3 of Dawnlib
  - Various backend changes, some of it due to me having to remake the Unity project after the old one got corrupted. Hopefully nothing has broken
 
- 1.0.4
  - After waiting about 14 hours for samboy.dev to stop error 502'ing, I've finally updated the mod
  - Updated the mod to work with 0.4.10 of DawnLib - This might break compatibility with with earlier versions of DL. Custom configs will also need to be updated.
  - Rewrote a lot of the code
  - More special case moons - Eventually I'm going to look into adding a config for this, or a smarter prefab lookup.
  - Now compatible with Celestial Tint's non-vanilla mode - Celestial Tint overrides the planet preview prefabs so its awkward to get the original prefab, so I've done the next best thing and have globe textures assigned by content tags
  - Globe spinning now syncs between players, I think?

- 1.0.3
  - Config update
  - Artifice and Embrion globes are now consistent with the planet preview if Chameleon is enabled
  - Added a couple new moons to the special conditions list
  - Fixed a bug where globes would appear empty if they spawned in certain mansion drawers

- 1.0.2
  - Saving and loading hopefully works now
  - Now with spinning

- 1.0.1
  - Fixed unregistered Network object
  - Added some special condition moons

- 1.0.0  
  - Initial Release.