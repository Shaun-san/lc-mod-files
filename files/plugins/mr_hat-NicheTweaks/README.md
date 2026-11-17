# NicheTweaks

### Audio
<details>

#### Silence ringing ear audio from shotgun blast
- If true, silences the ear ringing audio and muffled audio sound effect from shotgun blasts.

#### Silence lightning static audio
- If true, silences live lightning static that plays from a conductive item being targeted when entering the facility.

#### Mute fear audio
- If true, stops the fear ambience and heartbeat audio driven by the local player's fear level.
</details>

### Decals
<details>

#### Decal draw distance override
- If true, breaks the decal draw distance and causes decals to always be rendered. Will impact performance, not recommended without LethalSponge.
	- Compatibility tested with [LethalSponge](https://thunderstore.io/c/lethal-company/p/Scoops/LethalSponge/), it is highly recommended to use this mod if you want to use this setting. You can control the decal distance using 'decalDrawDist'. 100 is plenty with the amount of fog in Lethal Company.

#### Enable footprint pool override
- If true, overrides the number of footprint decals allowed to exist.

#### Footprint pool size
- Number of footprints that are allowed to be present before the oldest footprints start culling visually.

#### Enable player blood effects
- Enable blood effects when players take damage.

#### Player blood pool size
- Number of blood splatters that are allowed to be present before the oldest blood splatters start culling visually, vanilla is 50.

</details>

### Gameplay
<details>

#### Fix hoarder bug trying to grab man eater
- If true, prevents hoarder bugs from trying to pick up man eaters.

#### Fix hoarder bug trying to grab spider body
- If true, prevents hoarding bugs from trying to grab player corpses hung up by spiders.

#### Enable grabbable to enemies item blacklist
- If true, enables grabbable to enemies item blacklist.

#### Give Radmechs a larger hit collider
- If true, gives the Radmech/Old Bird enemies a larger hitbox, mainly for use with mods where they are no longer immortal. However, as an unavoidable consequence, they can now grab you far easier, making them more difficult. Can also be used to just make them more difficult.

#### Give Butlers a taller player hit collider
- If true, increases the height of Butlers player hit collider to allow them to have more vertical reach. This is to stop players sitting on the Mansion doorframe to avoid danger, amongst other high areas.

#### Give Jesters a taller player hit collider
- If true, increases the height of Jesters player hit collider to allow them to have more vertical reach. This is to stop players sitting on the Mansion doorframe to avoid danger, amongst other high areas.

#### Lower size of Butler obstacle avoidance
- If true, resizes Butler's NavMeshAgent obstacle avoidance radius from 1.6 to 1.4 to help them fit through tighter spaces and open doors properly.

#### Disable utility slot
- If true, disables the utility slot on the HUD and prevents items from using the utility slot.

#### Prevent check dead players cheese
- If true, displays the 'No one can hear you' popup when sending a chat message when everyone is dead.

#### Eject at zero days without ship loot
- If true, triggers the deadline firing sequence as soon as the crew reaches 0 days left when no ship scrap value is found.
	- Compatible with [ShipInventory](https://thunderstore.io/c/lethal-company/p/LethalCompanyModding/ShipInventoryUpdated/)
	- Compatible with [Extend Deadline](https://old.thunderstore.io/c/lethal-company/p/WhiteSpike/Extend_Deadline/)

#### Disable item inspection
- If true, disables the ability to inspect items in your hand.

#### Fix zero scale items/NaN errors
- If true, fixes NaN errors (player falling through the map randomly). Patch originally created by [Pacoito](https://thunderstore.io/c/lethal-company/p/pacoito/), thank them wholesomely for it.

#### Remove deposit desk cooldown
- If true, removes the cooldown when placing items on the company desk.

#### Unlock doors from inventory
- If true, keys can unlock doors from any inventory slot.

#### Better Flashlight Handling
- If true, improves flashlight behaviour when carrying multiple flashlights. Also fixes bulb remaining active when freshly spawned.

#### Allow pickup of items before game start
- If true, allows all items to be picked up before the game starts.

#### Remove nonscrap item values
- If true, removes scrap value from nonscrap item's scan node subtext.

#### Pick up items in order
- If true, fills inventory slots from left to right.

#### Put two handed items in slot one
- If true, places two handed items in the first inventory slot.

#### Rearrange inventory after dropping
- If true, moves inventory items left after dropping an item.

#### Hide player names
- If true, hides names above players.
</details>

### QoL
<details>

#### Enable global voice volume slider
- If true, enables the global voice volume slider in the player list.
	- Compatibility tested with [MoreCompany](https://thunderstore.io/c/lethal-company/p/notnotnotswipez/MoreCompany/).

#### Enable player volume saving
- If true, enables player volume saving
	- Compatible with global voice slider, saves the global voice slider value as well. Will overwrite any individual player volume save data.
	- This does not run every frame, it runs every 0.1 seconds as long as you are in orbit and will disable itself when landing.
	- Volume only saves to file when exiting the pause menu.

#### Restart voice chat after landing
- EXPERIMENTAL | If true, restarts voice chat once after landing on a moon. This may help with large voice chat desyncs after generating interiors.

#### Enable dropship pickup delay
- If true, adds a 1 second delay to items dropped by the dropship before they can be grabbed.

#### Enable teleporter item pickup block
- If true, block item grabbing whilst you are being teleported.
	- This is to prevent GrabInvalidated if you pick up an item just before you get teleported

#### Jester Warmup
- If true, silently plays and stops the Jester's audio clips so they are decompressed before first real playback to prevent an in-game lag spike.

#### Ambient music warmup
- If true, silently plays and stops ambient music so they are decompressed before first real playback to prevent an in-game lag spike.

#### Normalise helmet light brightness
- If true, copies the currently used flashlight's beam settings onto the helmet light when pocketed.

#### Uncap fps
- If true, removes the 250 fps cap.

#### Dead players see ghost girl
- If true, allows dead players/spectators to see Ghost Girls haunting other players
</details>

### Ship
<details>

#### Close ship doors when lever is pulled
- If true, closes the ship doors when the lever is pulled.

#### Disable planet reel video on ship monitors
- If true, disables the planet reel video on the ship monitor.

#### Disable indoor ship camera
- If true, disables the indoor ship camera.

#### Disable outdoor ship camera
- If true, disables the outdoor ship camera.

#### Disable speaker intro voice
- If true, disables the ship speaker intro voice.

#### Fix teleporter glass text
- If true, fixes the teleporter button and glass interaction text.

#### Hide ship cabinet doors
- If true, hides both ship cabinet doors.

#### Add light switch scan node
- If true, adds a scan node to the ship light switch.

#### Enable dropship item limit override
- If true, overrides the dropship item limit.

#### Dropship item limit
- Maximum number of items that can be ordered at once.

#### Auto recharge batteries in orbit
- If true, charges battery powered items when entering orbit.
</details>

### UI
<details>

*All options below have had compatibility tested with [LethalHUD](https://thunderstore.io/c/lethal-company/p/s1ckboy/LethalHUD/).*

#### Hide clock from HUD
- If enabled, hides the clock from the HUD.

#### Add clock to death screen
- If true, adds clock to death screen.

#### Hide weight from HUD
- If true, hides the weight from the HUD.

#### Hide chat from HUD
- If true, hides the chat from the HUD.
	- Remains hidden even if you type in it.

#### Set chat colon colour to blue
- If true, sets the colon in the chat to blue and prevents the colon from changing colours when using \<color> html attributes in chat messages.

#### Hide compass from HUD
- If true, hides the compass from the HUD.

#### Hands full text preset
- Preset for HandsFullText position/rotation/scale/opacity. DefaultNoChange does not modify the HUD.

<details>
<summary>Previews/Presets</summary>
<br />
<details>
<summary>Default/NoChange</summary>

![](https://i.imgur.com/V7m5eBW.png)
</details>

<details>
<summary>Below inventory</summary>

![](https://i.imgur.com/kBgCemU.png)
</details>

<details>
<summary>Above inventory</summary>

![](https://i.imgur.com/eOm2xXW.png)
</details>

<details>
<summary>Top of screen</summary>

![](https://i.imgur.com/fchz6eY.png)
</details>

<details>
<summary>Above vanilla stamina/health UI</summary>

![](https://i.imgur.com/ajdc74u.png)
</details>

<details>
<summary>Below chat</summary>

![](https://i.imgur.com/Eh01zv2.png)
</details>

<details>
<summary>Above tooltips</summary>

![](https://i.imgur.com/oZUOses.png)
</details>
</details>

#### Item lightning warning
- If true, warns the player which item is about to be struck by lightning with a visual indicator.

<details>
<summary><strong>Extra info</strong></summary>

- Compatibility tested with:
	- [LethalHUD](https://thunderstore.io/c/lethal-company/p/s1ckboy/LethalHUD/)
	- [LethalThing](https://thunderstore.io/c/lethal-company/p/Evaisa/LethalThings/)'s utility belt
	- [HotbarPlus](https://thunderstore.io/c/lethal-company/p/FlipMods/HotbarPlus/)
	- [ReservedItemSlots](https://thunderstore.io/c/lethal-company/p/FlipMods/ReservedItemSlotCore/)
- Should work out of the box with most item slot mods
- Uses an image component instead of a sprite renderer component, allowing the border to not be placed in front of everything on the screen
</details>

#### Remove item slot fade
- If true, removes the fade popout of the item slot frame when swapping item slots.

#### Hide HUD at terminal
- If true, hides the HUD whilst at the terminal.

#### Enable condensation on visor during flooded
- If true, shows helmet condensation during Flooded weather.
	- Flooded is missing a visor overlay called helmet condensation, which is present during rainy or stormy weather if you look up in the rain.

#### Fix quit game highlight colours
- If true, changes the green highlights and corners of the in-game quit menu to be highlighted orange like the rest of the game.

#### Change quit game confirmation text to orange
- If true, changes the light blue 'Would you like to leave the game?' text to be orange.

#### Hide join button
- If true, hides the join crew button in the main menu.

#### Hide invite friends button
- If true, hides the invite friends button in the quick menu.

#### Hide credits button
- If true, hides the Credits button in the main menu.

#### Fix utility slot item icon size
- If true, fits the item icon to the utility slot.

#### Change friends only text to private
- If true, changes the `Friends only` lobby option in lobby creation menu to say `Private`.

#### Hide control tips from HUD
- If true, hides the control tip labels (top right of HUD).

#### Customise control tip item name
- If true, enables replacing of item control tip text.
	- This was originally created to change the control tip text to match the scan node texts, but now you can just make it anything you want instead. Check the config for more info on how to use this.
	- This also toggles a fix for stun grenade and homemade flashbang control tips changing unexpectedly.

#### Scan node colour overrides
- Allows the change of scan node types for certain things, using GameObject or item names.

#### Hide warning display tips
- If true, hides all warning display tips (yellow display tips).

#### Hide low oxygen warning
- If true, hides the low oxygen warning.

#### Hide empty scan node subtext
- If true, hides scan node subtext when it is blank or has no value.
</details>

### Visuals
<details>

#### Disable film grain effect globally
- If true, attempts to globally disable film grain where it may be present.

#### Disable custom moon fog and colour adjustments
- If true, disables local fog and colour adjustments in matching moon level scenes.
	- Weather effects are left alone.
	- All players need to have this enabled.

#### Disable local player shadow
- If true, disables shadow casting for the local player only. Very useful for modded flashlights with very high intensities.
	- Compatibility added with [First Person View](https://old.thunderstore.io/c/lethal-company/p/seechela/First_Person_View/), [ModelReplacementAPI](https://old.thunderstore.io/c/lethal-company/p/BunyaPineTree/ModelReplacementAPI/), [LocalFlashlight](https://old.thunderstore.io/c/lethal-company/p/Command293/LocalFlashlight/) and [TooManyEmotes](https://old.thunderstore.io/c/lethal-company/p/FlipMods/TooManyEmotes/).

<details>
<summary><strong>Preview Images</strong></summary>

![](https://i.imgur.com/6i3PSPo.png)
![](https://i.imgur.com/usjnDqP.png)
</details>

#### Hide player arms
- If true, hides the player arms.

#### Enable texture fix for toy cube
- If true, changes the texture of Toy cube (rubix cube) scrap to a texture of a rubix cube that is actually solvable.

#### Enable LOD bias override
- If true, enables custom LOD distance.
	- This exists to prevent the visible pop-in to your liking. Increasing this will decrease performance.

</details>

### [DawnLib](https://thunderstore.io/c/lethal-company/p/TeamXiaolan/DawnLib/)
<details>

#### Hide and mute achievement popups
- If true, hides [DawnLib](https://thunderstore.io/c/lethal-company/p/TeamXiaolan/DawnLib/)'s achievement popups and sounds.
	- This shouldn't disturb earning achievements.

#### Replace hotloadUI player images
- If true, replaces DawnLib hotloading player Steam images with a vanilla image.
</details>

### [MoreBlood](https://thunderstore.io/c/lethal-company/p/FlipMods/MoreBlood/)
<details>

#### Fix footprint smearing
- If true, enables fix for [MoreBlood](https://thunderstore.io/c/lethal-company/p/FlipMods/MoreBlood/)'s footprint smearing.
</details>

### [MoreCompany](https://thunderstore.io/c/lethal-company/p/notnotnotswipez/MoreCompany/)
<details>

#### Hide main menu button
- If true, hides the MoreCompany cosmetic button in the main menu.
	- This does not disable cosmetics and the menu can still be accessed in-game via the pause menu.

#### Hide crew count in create lobby menu
- If true, hides the MoreCompany crew count in the create lobby menu.

#### Change cosmetic button icon to orange
- If true, changes the MoreCompany cosmetic button in the main menu and pause menu from green to orange.
</details>

### [LobbyImprovements](https://thunderstore.io/c/lethal-company/p/Dev1A3/LobbyImprovements/)
<details>

#### Change text
- If true, changes text on the create a lobby screen from `ImprovedLobby` -> `Lobby`.
</details>

### [LCBetterSaves](https://thunderstore.io/c/lethal-company/p/Pooble/LCBetterSaves/)
<details>

#### Change text
- If true, changes text on the create a lobby screen from `BetterSaves` -> `Save Files`.

#### Auto rename
- If true, automatically renames new saves to the lobby name.

#### Start credits fix
- If true, sets BetterSaves starting credits to 60 rather than 30.
</details>

### [InputUtils](https://thunderstore.io/c/lethal-company/p/Rune580/LethalCompany_InputUtils/)
<details>

#### Hide legacy control button inside control settings
- If true, hides the legacy control button inside control settings.

#### Flashlight toggle hotkey
- If true, adds a keybind to toggle flashlights at any time. Requires LethalCompany InputUtils to be installed.
	- Defaults to F and can be changed in the InputUtils keybind settings.
</details>

### [LethalConfig](https://thunderstore.io/c/lethal-company/p/AinaVT/LethalConfig/)
<details>

#### Hide main menu button
- If true, hides LethalConfig's button in the main menu.
	- This does not disable LethalConfig and the menu can still be accessed in-game via the pause menu.

#### Add space
- If true, renames `LethalConfig` to `Lethal Config` in the main menu and pause menu.
</details>

### [MZCoMagicShipping](https://thunderstore.io/c/lethal-company/p/XuXiaolan/MZCoMagicShipping/)
<details>

#### Crate never respawns
- If true, the magic crate does not respawn and is single use only.
</details>

### [ImmersiveVisor](https://thunderstore.io/c/lethal-company/p/Woecust/Immersive_Visor/)
<details>

#### Additional weather raindrops
- If true, Immersive Visor shows raindrops during the configured additional weathers. Requires ImmersiveVisor to be installed.

#### Additional raindrop weathers
- List of additional weather names that activate Immersive Visor raindrops.
	- Defaults to `Hurricane, Downpour`.
</details>

### [ShipWindows](https://thunderstore.io/c/lethal-company/p/TestAccount666/ShipWindows/)
<details>

#### Window shutters close on departure
- If true, ship window shutters close when the ship doors close on departure.
</details>

### [LethalNuke](https://thunderstore.io/c/lethal-company/p/bcs4313/Lethal_Nuke/)
<details>

#### Lethal nuke fix
- If true, prevents Lethal Nuke's particle effect from looping.
</details>

### [MirrorDecor](https://thunderstore.io/c/lethal-company/p/quackandcheese/MirrorDecor/)
<details>

#### Enable FPS cap
- If true, enables the FPS cap for MirrorDecor and prevents its camera from rendering when not on the ship.

#### FPS cap
- Sets the FPS cap for MirrorDecor's camera.
</details>

### [EnhancedMonsters](https://thunderstore.io/c/lethal-company/p/VELD/Enhanced_Monsters/)
<details>

#### Remove version number
- If true, removes EnhancedMonsters' version number from Lethal Company's version number text in the main menu.
</details>

### [LobbyControl](https://thunderstore.io/c/lethal-company/p/mattymatty/LobbyControl/)
<details>

#### Remove lobby command
- If true, removes the lobby command from the terminal's help/other screen.
	- This only hides the command.
</details>

### [GeneralImprovements](https://thunderstore.io/c/lethal-company/p/ShaosilGaming/GeneralImprovements/)
<details>

#### Player scan node red
- If true, sets the player scan node to be red for `Scan players`.

#### Add ShipInventory items to monitors
- If true, includes scrap stored in [ShipInventory](https://thunderstore.io/c/lethal-company/p/LethalCompanyModding/ShipInventoryUpdated/) on [GeneralImprovements](https://thunderstore.io/c/lethal-company/p/ShaosilGaming/GeneralImprovements/)' Ship Scrap monitor.

#### Change Players Alive to Crew Alive
- If true, changes GeneralImprovements' `Players Alive` monitor title to `Crew Alive`.
</details>

### [SolidLib](https://thunderstore.io/c/lethal-company/p/SolidStone/SolidLib/)
<details>

#### Fix outside music error
- If true, removes SolidLib's broken outside music patch and restores vanilla outside music.
</details>

### [LethalCasino](https://thunderstore.io/c/lethal-company/p/mrgrm7/LethalCasino/)
<details>

#### Remove ATM
- If true, disables LethalCasino's ATM at the Company.
</details>

### [LateGameUpgrades](https://thunderstore.io/c/lethal-company/p/malco/Lategame_Upgrades/)
<details>

#### Fix sample colliders
- If true, aligns enemy sample colliders with their meshes.
</details>

### [Oxygen](https://thunderstore.io/c/lethal-company/p/consequential/Oxygen/)
<details>

#### OopsAllFloodedFixed compatibility
- If true, gives Oxygen's `OxyBoost` store item OopsAllFloodedFixed's underwater stamina recovery.
	- Requires [OopsAllFloodedFixed](https://thunderstore.io/c/lethal-company/p/NotezyTeam/OopsAllFloodedFixed/) to be installed.
</details>

### [EladsHUD](https://thunderstore.io/c/lethal-company/p/EladNLG/EladsHUD/) (Soon to be discontinued in NicheTweaks)
<details>

#### V80 utility slot compatibility
- If true, allows the utility slot to be seen when using EladsHUD in Lethal Company V80.

#### Reorganise EladsHUD
- If true, moves InsanityDisplay's percentage down to be in line with Stamina and Oxygen. Requires [InsanityDisplay](https://thunderstore.io/c/lethal-company/p/Confusified/InsanityDisplay/) and [Oxygen](https://thunderstore.io/c/lethal-company/p/consequential/Oxygen/) to be installed and configured accordingly.

<details>
<summary><strong>Preview Images</strong></summary>

![](https://i.imgur.com/Kf9AZMg.png)
![](https://i.imgur.com/8HES8Fj.png)
</details>

#### Fix stamina bar 10% cap
- If true, fixes stamina bar being unable to deplete to 0% properly.

#### Disable stamina notch
- If true, hides the notch on the stamina bar that's present during stamina drain.

#### Hide weight
- If true, hides weight UI.

#### Trigger health bar popup on heal
- If true, will show health bar when health increases as well rather than when only decreasing.

#### Autohide stamina/oxygen/insanity bar
- If true, automatically hides [stamina](https://thunderstore.io/c/lethal-company/p/EladNLG/EladsHUD/)/[Oxygen](https://thunderstore.io/c/lethal-company/p/consequential/Oxygen/)/[Insanity](https://thunderstore.io/c/lethal-company/p/Confusified/InsanityDisplay/) bar when at configured value for a period of time.
- All bars have the following config options:
	- Configurable time until fade
	- Configurable number/percentage visibility
	- Configurable starting percentage before fading timer starts (not done for insanity bar)

#### Hide percentage dividers
- If true, hides the percentage divider UI elements. These are the small dots between each percent number. Requires [Oxygen](https://thunderstore.io/c/lethal-company/p/consequential/Oxygen/) to be installed.

</details>


# Future plans
- Screenshots for README
- Swap from imgur to catbox

# Credits
Some tweaks originate from [GeneralImprovements](https://old.thunderstore.io/c/lethal-company/p/ShaosilGaming/GeneralImprovements/)

[Sniper1.1](https://thunderstore.io/c/lethal-company/p/Sniper1_1/) for pointing me in the right direction in regards to flashlights and their shadows.

[Moroxide](https://thunderstore.io/c/lethal-company/p/Moroxide/) for being able to click fast enough during testing for the ghosting dropshit items (I can't)

[debbicar](https://thunderstore.io/c/lethal-company/p/debit_card_debit/) for their Toy cube (rubix cube) texture

[pacoito](https://thunderstore.io/c/lethal-company/p/pacoito/) for letting me use their code for `Fix zero scale items`

[zeeblo lite](https://www.youtube.com/watch?v=1c4Ut7nINkI)'s very useful modding tutorial

ChatGPT for answering so many questions about C# and Unity that it would drive any human insane
