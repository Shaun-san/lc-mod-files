### *1.0.8**
- Updated for v70+
- Updated the method to pass another parameter to match the new update's method so suits unlock properly again.
- Added a small fix to see if this also stops unlocked suits from appearing in the shop rotation. I haven't tested this thoroughly, let me know if you still see them in there.

### **1.0.7**
- Updated for v50
- Added bee suit
- Added bunny suit
- Suit spawning method rewrote to iterate through the list of unlockables and no longer be hard coded for IDs.
- Lethal Fashion now creates a LethalFashion.cfg file in your BepInEx\config folder. This allows you to select which suits to unlock in both the base game and in suit mods if you know the suit name.
-- This also means you can use this mod in future game updates and it should let you spawn new suits without updating the mod, if you know the suit name.

### **1.0.6**  
- Added purple suit (ID 24)  

### **1.0.5**  
- Updated to work on v47 by changing the way the plugin checks who is the host
- Minor bug: Clients may see the suits synced in a different order than the host. Investigating.

### **1.0.4**  
- Works with newest update out of the box as far as I can tell, nothing should break. If it breaks, please check the LC Modding Discord and leave a message in the Lethal Fashion thread and I'll look into it.
- Removed debug code so it spams the console logs less
- Added Manual installation notes to this README on where the DLL goes
- Apparently there's issues with my mod when you install with R2Modman but I think it's a folder location issue. Please see manual installation notes.

### **1.0.3**   
- Fixed mod page formatting  
- Fixed an issue where if you quit a game and then went back into it, it would spawn duplicates of the suits and could push other suits off the rack
- Added more error handling and debugging code to make my life easier

### **1.0.2**   
- Fixed the suit disappearing issue.  
- Added logic to prevent the suits from spawning multiple times.  
- Added logic to handle when the game resets the ship (on loss; when you don't meet the quota and get fired)  
- Added logic to unlock existing suits that were spawned and reposition them on the rack  

### **1.0.1**  
- Fixed the folder structure, should now work with mod installer. Sorry for the mistake!  

### **1.0.0**
- Initial version, code reworked from my old bad implementation using a much better method from Mama Llama.  