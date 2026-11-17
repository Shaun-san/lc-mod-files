\## Changelog



\## 2.6.3 



* Commented out more debug code fornow.



\## 2.6.2



Released for V81



\## 2.6.0



\- Upgraded to v50

\- Fixed names of ai types in README.md



Known issues:

\- The Rolling Giant can't get on the ship

\- The Rolling Giant stutters when getting on top of something



\## 2.5.2



\- Fixed LLL spawning

\- Fixed daytime variant's shader being missing (somehow)

\- Fixed daytime variant, when disabled, not disabling audio



\## 2.5.1



\- Fixed timers that didn't reset when ai types changed hourly

\- Fixed some ai types slowing down dramatically due to timers not resetting



\## 2.5.0



\- Added `AiTypeChangeOnHourInterval` to the config so the ai type can change every X amount of hours

\- The `InverseCoilhead` ai type will now move towards a player if it can't see any of them, until it gets back into line of sight



\## 2.4.4



\- Added`@Headcraps` to the acknowledgments for making the original Rolling Giant model

&#x20; - I was given this by a friend so I wasn't aware that Headcraps initially made it, sorry about that!



\## 2.4.3



\- Fixes outside ai!



\## 2.4.2



\- Clients properly get targetted during the roaming phase



\## 2.4.1



\- Fixed an ownership issue that caused the Rolling Giant to spam errors

\- Fixed an ownership issue that caused the Rolling Giant to not untarget from someone

\- Fixed an ownership issue that caused the Rolling Giant to target people outside of the factory

\- Removed capsule collider and added a box collider as it was causing issues with the Rolling Giant's attack

\- Rolling Giants outside still don't work properly, but is getting worked on 🫡



\## 2.4.0



\- Fixed the Rolling Giant's bestiary entry breaking when scanning the outside versions of it

\- Fixed the Rolling Giant not being able to get on the ship

\- Fixed the latency teleportation of the Rolling Giant on clients; now moves smoothly across all clients

\- Fixed ai path issues if the player jumped or got onto a high place. Now the Rolling Giant paths to the closest point to the player if they are inaccessable

\- Fixed the Rolling Giant damaging the player when clipping into the ship and the player is in the ship. Now it won't damage the player in this case

\- Fixed ai type syncing between clients

\- Fixed various ai types by syncing shared variables between clients

\- Fixed `LookingTooLongKeepsAgro` where the Rolling Giant wouldn't move while the timer is partially completed

\- Fixed `LookingTooLongKeepsAgro` where the time would restart when it switched players, or lost the player

\- Fixed `OnceSeenAgroAfterTimer` where the time would restart when it switched players, or lost the player 

\- Fixed ai type timers resetting when the player jumped or went out of range

\- Fixed the Rolling Giant's audio stuttering if it makes quick small movements to reach a location

\- Improved the wandering speed so it will speed up to their max speed like their chasing state

\- Rolling Giants past 1.2 size can no longer get onto the ship

\- Rolling Giant scale now slightly affects their rolling audio pitch



\## 2.3.0



\- Added a config option to change the max amount of Rolling Giant's that can spawn in a level

\- Changed the config option for AiType to accept multiple values

&#x20; - This allows for a random AI type to be picked at the start of each moon

&#x20; - AI type is now synced across clients with a NetworkVariable instead of with the config sync

\- Added a new Rolling Giant model that is more optimized than the previous one

&#x20; - Thanks to `Krampus` for the help on that!

\- The Rolling Giant now properly checks line of sight to start chasing the player

\- Fixed a client bug that would complain about an invalid navmesh agent



\## 2.2.1



\- Fixed dead body shader being applied to all dead bodies and not only to the Rolling Giant player death type



\## 2.2.0



\- Added a config option to spawn the Rolling Giant on any level and a weight for that option



\## 2.1.4



\- Fixed client audio not playing due to agent speed mismatch



\## 2.1.3



\- Slightly increases the now too low default poster spawn weight



\## 2.1.2



\- Removed a multipler that was applied to the poster rarity for some reason



\## 2.1.1



\- Removed the soft dependency to LethalSettings, as it somehow broke through a try catch which broke the mod loading.

\- Increased the default spawn weights slightly.

\- Added a slight probability curve to the giant's spawning inside, outside, and outside during the day.

&#x20; - Inside will slightly more common at the start

&#x20; - Outside will be slightly more common at the start and a bit more common near the end

&#x20; - Outside during the day will be slightly more common at the start



\## 2.1.0



\- Renamed `SpawnInside` to `CanSpawnInside`, and is now just a toggle

\- Renamed `SpawnOutside` to `CanSpawnOutside`, and is now just a toggle

\- Renamed `SpawnDaytime` to `DisableOutsideAtNight` as it was too confusing for many people, and is now just a toggle

\- Added extra notes to various config options to make them more clear

\- Added the Rolling Giant to the in-game dev enemy spawn list

\- Fixed the Rolling Giant's outside AI

\- Gave the Rolling Giant, when it is a daytime type, a disabled state



\## 2.0.1



\- Removed logs from ai modes that spammed the console :(



\## 2.0.0



\- Removed Terminal API dependency

\- Converted the Rolling Giant into a completely custom enemy that can be added to the spawn pools 

\- Overhauled all AI behaviors

\- Fixed many audio and networking sync issues

\- All AI types will wander by default if all players get out of range

\- Added a new player death type for when the Rolling Giant kills the player

\- Removed wander settings

\- Added config options:

&#x20; - `GotoPreviousAiTypeKey` - The key to go to the previous AI type.

&#x20;   - This uses Unity's New Input System's key-bind names

&#x20; - `GotoNextAiTypeKey` - The key to go to the next AI type.

&#x20;   - This uses Unity's New Input System's key-bind names

&#x20; - `ReloadConfigKey` - The key to reload the config. Does not update spawn conditions.

&#x20;   - This uses Unity's New Input System's key-bind names

&#x20; - `SpawnIn` - Levels that the Rolling Giant can spawn in, separated by their chances of spawning

&#x20; - `SpawnInside` - If the Rolling Giant should spawn inside the dungeon

&#x20; - `SpawnDaytime` - If the Rolling Giant should spawn during the day

&#x20; - `SpawnOutside` - If the Rolling Giant should spawn outside

&#x20; - `MoveDeceleration` - How long it takes the Rolling Giant to stop moving in seconds

&#x20; - `SpawnPosterIn` - Where the Rolling Giant poster scrap can spawn, separated by their chances of spawning



\## 1.2.0



\- Removed unused LC\_API dependency

\- Added a config option to tell the Rolling Giant to wander again if the player goes past a certain distance

\- Added a config option to change that distance between the player and the Rolling Giant

\- Added a config option to change how long it takes the Rolling Giant to get to its movement speed

\- Added a config option to change the Rolling Giant's visual scale between two values

\- Added a config option to change the duration the player has to look at the Rolling Giant before agro for the LookingTooLongKeepsAgro AI

\- Audio volume scales based on the Rolling Giant's speed up to a cap of 1.0

\- Added new AI types for the Rolling Giant:

&#x20; - FollowOnceAgro = Once provoked, the Rolling Giant will follow the player constantly

&#x20; - OnceSeenAgroAfterTimer = Once the player sees the Rolling Giant, it will agro after a timer

\- Fixed RandomlyMoveWhileLooking AI not taking into account player viewing for timers

\- Fixed movement speed not applying to AI tick loop

\- Overhauled all settings to allow for per-AI type settings

&#x20; - AI types are now grouped with the data they need

&#x20; - Previous settings are removed automatically



\## 1.1.1



\- Made the Rolling Giant rng utilize the map seed to make results less samey



\## 1.1.0



\- Multiple AI types for the Rolling Giant:

&#x20; - Coilhead = Coilhead AI

&#x20; - MoveWhenLooking = Move when player is looking at it

&#x20; - RandomlyMoveWhileLooking = Randomly move while the player is looking at it

&#x20; - LookingTooLongKeepsAgro = If the player looks at it for too long it doesn't stop chasing

\- Can change the scale of the Rolling Giant's model

\- Can change the Rolling Giant's movement speed and wait/move random durations

\- Rolling Giants have the option to rotate to face the player if they have been still for some time

\- Rolling Giant variant is now synced visually across clients



\## 1.0.0



\- Initial release



