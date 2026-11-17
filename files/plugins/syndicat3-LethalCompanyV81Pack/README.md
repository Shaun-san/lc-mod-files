# Lethal Company v81 Friends Pack

A vanilla-plus modpack for **Lethal Company v81**, built for a group of friends who want the
game to feel like Lethal Company, only smoother, bigger and with more to discover.

**What you get**

- Bigger lobbies (up to 16 players) and proximity-friendly quality of life.
- Bug fixes and performance mods so v81 runs cleanly for everyone.
- A curated slice of new moons, interiors, monsters and scrap that fit the vanilla tone.
- Emotes, suits and cosmetics for fun, plus richer weather and ambience.
- No difficulty overhauls. Everything is configurable and the defaults are tuned for a casual-to-medium crew.

Every mod in this pack was checked against Thunderstore on 5 September 2026 for a v81-compatible
release. If an update to the game lands, check the CHANGELOG or re-run the build script (see below).

## Installing

1. Install a mod manager: [Thunderstore Mod Manager](https://www.overwolf.com/app/Thunderstore-Thunderstore_Mod_Manager)
   or [r2modman](https://thunderstore.io/c/lethal-company/p/ebkr/r2modman/) (lighter, no Overwolf).
2. Select **Lethal Company**, create a profile, open **Online**, search for this pack and hit **Download**.
   All dependencies install automatically.
3. Press **Start modded**. The host and every friend must be on the same pack version.

Everyone should install the same version of the pack. Client-only mods (cosmetics, HUD, sound) are safe to
toggle per person, but keep the server-side mods identical to the host or you will desync.

## Mod list

<!-- MODLIST:START -->
### Core, libraries, fixes and performance

| Mod | Version | Tier | What it does |
|---|---|---|---|
| [AdditionalNetworking](https://thunderstore.io/c/lethal-company/p/mattymatty/AdditionalNetworking/) by mattymatty | 2.4.1 | essential | Explicit networking for held slot, inventory, shotgun ammo/safety, boombox state and crouch (fixes Old Bird/Giant ignoring crouched players) |
| [AutoHookGenPatcher](https://thunderstore.io/c/lethal-company/p/Hamunii/AutoHookGenPatcher/) by Hamunii | 1.1.1 | essential | Generates MMHOOK assemblies on demand (multithreaded, cached) for every mod that uses MonoMod hooks |
| [BepInExPack](https://thunderstore.io/c/lethal-company/p/BepInEx/BepInExPack/) by BepInEx | 5.4.2305 | essential | The mod loader itself |
| [ButteryFixes](https://thunderstore.io/c/lethal-company/p/ButteryStancakes/ButteryFixes/) by ButteryStancakes | 1.17.19 | essential | The largest vanilla-compatible bug-fix collection (dropship, Cruiser, nutcracker clock, conductive items, v70 manor breaker rooms, grading errors) |
| [CullFactory](https://thunderstore.io/c/lethal-company/p/fumiko/CullFactory/) by fumiko | 2.0.11 | essential | Portal occlusion culling of interior tiles/items/lights with zero visual change by default |
| [DetourContext_Dispose_Fix](https://thunderstore.io/c/lethal-company/p/Hamunii/DetourContext_Dispose_Fix/) by Hamunii | 1.0.9 | essential | Preloader patcher that fixes MonoMod DetourContext.Dispose so hook priorities apply correctly |
| [EnemySoundFixes](https://thunderstore.io/c/lethal-company/p/ButteryStancakes/EnemySoundFixes/) by ButteryStancakes | 1.9.15 | essential | Restores missing/incorrect enemy SFX (bracken stun, snare flea loops, hurt sounds) and mutes Cruiser audio in orbit |
| [FixPluginTypesSerialization](https://thunderstore.io/c/lethal-company/p/Evaisa/FixPluginTypesSerialization/) by Evaisa | 1.1.4 | essential | Native preloader patcher that lets Unity deserialize Serializable types from plugin assemblies |
| [HarmonyXTranspilerFix](https://thunderstore.io/c/lethal-company/p/DiFFoZ/HarmonyXTranspilerFix/) by DiFFoZ | 1.1.0 | essential | Backports HarmonyX upstream fixes (transpiler misbehaviour, TargetMethods double-call) |
| [LCMaxSoundsFix](https://thunderstore.io/c/lethal-company/p/Hardy/LCMaxSoundsFix/) by Hardy | 1.2.0 | essential | Raises Unity's simultaneous-voice cap so footsteps/enemy audio stop dropping out in modded lobbies |
| [LethalFixes](https://thunderstore.io/c/lethal-company/p/Dev1A3/LethalFixes/) by Dev1A3 | 1.3.3 | essential | Bundles many host/client fixes (stormy weather, rank sync, kick message, Cruiser seat/steering desync, old-bird desync, terminal scan) plus the Dissonance/RPC log-level lag fixes |
| [LethalPerformance](https://thunderstore.io/c/lethal-company/p/DiFFoZ/LethalPerformance/) by DiFFoZ | 1.3.0 | essential | Caches FindObjectOfType-style lookups, reduces allocations, save hitching and HDRP memory |
| [MaskFixes](https://thunderstore.io/c/lethal-company/p/ButteryStancakes/MaskFixes/) by ButteryStancakes | 1.6.2 | essential | Fixes Masked lag spike on spawn, stuck roaming loops, proximity warning not working for clients, and mimic suit/radar desync - all relevant with 4-8 players |
| [MonkeyInjectionLibrary](https://thunderstore.io/c/lethal-company/p/mattymatty/MonkeyInjectionLibrary/) by mattymatty | 1.0.2 | essential | Preloader library that injects interfaces into base-game classes |
| [MonoDetour](https://thunderstore.io/c/lethal-company/p/MonoDetour/MonoDetour/) by MonoDetour | 0.7.15 | essential | Detouring library required by MonoDetour_BepInEx_5, TypeLoadExceptionFixer and LethalLib |
| [MonoDetour_BepInEx_5](https://thunderstore.io/c/lethal-company/p/MonoDetour/MonoDetour_BepInEx_5/) by MonoDetour | 0.7.15 | essential | BepInEx 5 logger + HarmonyX interop for MonoDetour |
| [PathfindingLagFix](https://thunderstore.io/c/lethal-company/p/Zaggy1024/PathfindingLagFix/) by Zaggy1024 | 2.4.2 | essential | Threads vanilla enemy pathfinding off the main thread - the main host-side frametime fix |
| [PathfindingLib](https://thunderstore.io/c/lethal-company/p/Zaggy1024/PathfindingLib/) by Zaggy1024 | 2.4.1 | essential | Native-hooked async pathfinding library required by PathfindingLagFix, DawnLib and SmartEnemyPathfinding |
| [StarlancerAIFix](https://thunderstore.io/c/lethal-company/p/AudioKnight/StarlancerAIFix/) by AudioKnight | 3.13.2 | essential | Assigns correct indoor/outdoor AI when an enemy ends up on the wrong side of the door, fixing stuck/teleporting enemies |
| [TypeLoadExceptionFixer](https://thunderstore.io/c/lethal-company/p/Hamunii/TypeLoadExceptionFixer/) by Hamunii | 1.0.4 | essential | Preloader patcher that stops Assembly.GetTypes and Unity Input System init from exploding when a stale/unloadable mod type exists - the classic 'one broken mod kills the whole... |
| [AsyncLoggers](https://thunderstore.io/c/lethal-company/p/mattymatty/AsyncLoggers/) by mattymatty | 2.2.3 | recommended | Moves BepInEx/Unity logging to its own thread and adds per-source log-level filtering |
| [BarberFixes](https://thunderstore.io/c/lethal-company/p/ButteryStancakes/BarberFixes/) by ButteryStancakes | 1.3.1 | recommended | Makes Barbers actually work when more than one spawns and fixes freezes/errors after a non-host kill |
| [BepInEx_Faster_Load_AssetBundles_Patcher](https://thunderstore.io/c/lethal-company/p/DiFFoZ/BepInEx_Faster_Load_AssetBundles_Patcher/) by DiFFoZ | 1.1.0 | recommended | Decompresses asset bundles once to a cache |
| [ChuxiaFixes](https://thunderstore.io/c/lethal-company/p/chuxiaaaa/ChuxiaFixes/) by chuxiaaaa | 1.0.7 | recommended | Fixes late-join gift box, spectator death-box names/avatars, 'unknown' player names, NetworkObject parent refs and disables the perf-hurting network analyzer - very useful for... |
| [DestroyItemInSlotFix](https://thunderstore.io/c/lethal-company/p/JacobG5/DestroyItemInSlotFix/) by JacobG5 | 1.0.0 | recommended | Patches the one line Zeekerss missed when v80 added the utility slot, so any mod calling DestroyItemInSlotAndSync stops throwing |
| [DunGenReferenceFixer](https://thunderstore.io/c/lethal-company/p/Zaggy1024/DunGenReferenceFixer/) by Zaggy1024 | 0.0.1 | recommended | Repairs interior asset references for custom interiors that were not rebuilt for v80+ |
| [EntranceTeleportOptimizations](https://thunderstore.io/c/lethal-company/p/mattymatty/EntranceTeleportOptimizations/) by mattymatty | 1.0.0 | recommended | Caches EntranceTeleport instances to remove expensive GetObjectsByType calls during teleports and dungeon generation |
| [JetpackFixes](https://thunderstore.io/c/lethal-company/p/ButteryStancakes/JetpackFixes/) by ButteryStancakes | 1.6.3 | recommended | Removes the bogus 'overheat' explosions caused by collider detection (belt bags, tulip snakes) and fixes the proximity beep |
| [LethalConfig](https://thunderstore.io/c/lethal-company/p/AinaVT/LethalConfig/) by AinaVT | 1.4.6 | recommended | In-game config menu so friends can flip settings without editing cfg files |
| [LethalError](https://thunderstore.io/c/lethal-company/p/chuxiaaaa/LethalError/) by chuxiaaaa | 1.0.6 | recommended | Removes the vanilla 'An error occurred!' popup spam and shows useful detail instead |
| [LethalLib](https://thunderstore.io/c/lethal-company/p/Evaisa/LethalLib/) by Evaisa | 1.2.0 | recommended | Content library that most custom items, enemies and shop entries are registered through |
| [LethalSponge](https://thunderstore.io/c/lethal-company/p/Scoops/LethalSponge/) by Scoops | 1.4.3 | recommended | Client-side FPS suite: input-system rework (fixes growing input lag), ship camera frame limiting, item LODs, optional asset de-duping |
| [LoadingInfo](https://thunderstore.io/c/lethal-company/p/chuxiaaaa/LoadingInfo/) by chuxiaaaa | 1.1.4 | recommended | Shows which players have not finished loading on the seed screen - removes the 'who are we waiting for' problem in 8-player lobbies |
| [LostEnemyFix](https://thunderstore.io/c/lethal-company/p/JacobG5/LostEnemyFix/) by JacobG5 | 1.1.1 | recommended | Kills enemies that lose the NavMesh instead of letting them spam errors every frame (v80 only partially fixed this in vanilla) |
| [MaskedInvisFix](https://thunderstore.io/c/lethal-company/p/VirusTLNR/MaskedInvisFix/) by VirusTLNR | 0.0.3 | recommended | Fixes Masked going invisible after a player dies (SetVisibilityOfMasked bug) - a common v81 complaint |
| [Matty_Fixes](https://thunderstore.io/c/lethal-company/p/mattymatty/Matty_Fixes/) by mattymatty | 1.1.41 | recommended | 100% vanilla-compatible fixes: cabinet items falling on load, item clipping into ground, orphaned radar icons, items spawning inside furniture, conductive-mesh warnings |
| [MeleeFixes](https://thunderstore.io/c/lethal-company/p/ButteryStancakes/MeleeFixes/) by ButteryStancakes | 1.5.1 | recommended | Fixes shovel becoming unusable after a mid-swing death, knife wasting hits on corpses, shotgun multi-target damage and a lag-causing search on every hit sound |
| [NestFix](https://thunderstore.io/c/lethal-company/p/PureFPSZac/NestFix/) by PureFPSZac | 1.3.0 | recommended | Stops Baboon Hawk nests spawning inside walls or overhanging ledges |
| [RevisitStingers](https://thunderstore.io/c/lethal-company/p/ButteryStancakes/RevisitStingers/) by ButteryStancakes | 1.3.1 | recommended | Lets the once-per-save interior stinger tracks replay under configurable conditions |
| [ReviveDesyncPatch](https://thunderstore.io/c/lethal-company/p/DaanSmoki/ReviveDesyncPatch/) by DaanSmoki | 1.0.0 | recommended | Adds a timeout to the end-of-round revive check that can softlock the lever at '[Wait for ship to land]' with MoreCompany-sized lobbies - directly relevant to the bigger-lobby... |
| [SpawnCycleFixes](https://thunderstore.io/c/lethal-company/p/ButteryStancakes/SpawnCycleFixes/) by ButteryStancakes | 1.2.2 | recommended | Fixes double spawns at day start and other spawn-cycle inconsistencies so enemy pressure is fair and predictable |
| [SpiderPositionFix](https://thunderstore.io/c/lethal-company/p/Fandovec03/SpiderPositionFix/) by Fandovec03 | 1.6.5 | recommended | Stops bunker spider mesh/agent desync and failed wall climbs |
| [VertexLibrary](https://thunderstore.io/c/lethal-company/p/LethalCompanyModding/VertexLibrary/) by LethalCompanyModding | 1.1.0 | recommended | OBB helper library required by Matty_Fixes (and CruiserImproved-era mods) |
| [WeedKillerFixes](https://thunderstore.io/c/lethal-company/p/ButteryStancakes/WeedKillerFixes/) by ButteryStancakes | 1.2.0 | recommended | Fixes weed-killer cooldown wasting sprays on the Cruiser and the severe lag spike when spraying with no Cadavers present |
| [Chameleon](https://thunderstore.io/c/lethal-company/p/ButteryStancakes/Chameleon/) by ButteryStancakes | 2.4.3 | optional | Cohesive visual polish (planet preview on ship camera, door/window fixes, fog quality, moon-appropriate entrance doors) |
| [HookGenPatcher](https://thunderstore.io/c/lethal-company/p/Evaisa/HookGenPatcher/) by Evaisa | 0.0.5 | optional | Legacy MMHOOK generator |
| [ReXuvination](https://thunderstore.io/c/lethal-company/p/XuXiaolan/ReXuvination/) by XuXiaolan | 1.1.0 | optional | Preloader that trims collision-layer work (EnemyAICollisionDetect, physics regions, traps) |
| [SmartEnemyPathfinding](https://thunderstore.io/c/lethal-company/p/Zaggy1024/SmartEnemyPathfinding/) by Zaggy1024 | 0.0.4 | optional | Lets Masked use custom-moon elevators and roam via fire exits through PathfindingLib's smart API |

### Quality of life

| Mod | Version | Tier | What it does |
|---|---|---|---|
| [Coroner](https://thunderstore.io/c/lethal-company/p/EliteMasterEric/Coroner/) by EliteMasterEric | 2.4.1 | essential | Cause-of-death on the end-of-round report with easter eggs |
| [CruiserImproved](https://thunderstore.io/c/lethal-company/p/DiggC/CruiserImproved/) by DiggC | 1.6.4 | essential | Fixes Cruiser desyncs (steering, radio, wheel torque, floating items on reload) and adds lean-to-look-back, scan while seated, sane collision damage |
| [GeneralImprovements](https://thunderstore.io/c/lethal-company/p/ShaosilGaming/GeneralImprovements/) by ShaosilGaming | 1.5.5 | essential | The single best vanilla-plus QoL bundle: hotbar ordering, number-key slot switching, flashlight/walkie shortcuts, faster scrolling/terminal, 14 configurable ship monitors, suit +... |
| [GoodItemScan](https://thunderstore.io/c/lethal-company/p/TestAccount666/GoodItemScan/) by TestAccount666 | 2.1.0 | essential | Replaces the flaky vanilla scanner with a reliable, performant one (up to 666 nodes, no missed items, configurable node colors/fade) |
| [ScienceBird_Tweaks](https://thunderstore.io/c/lethal-company/p/ScienceBird/ScienceBird_Tweaks/) by ScienceBird | 4.7.5 | essential | Ship-collider fixes (teleport button, suit rack, catwalk), hover-tip fixes, head-cam tweaks, shotgun QoL and dozens of small vanilla-feel fixes |
| [AutoScroll](https://thunderstore.io/c/lethal-company/p/mrov/AutoScroll/) by mrov | 0.0.1 | recommended | Ship monitor text auto-scrolls so long moon/weather descriptions are readable |
| [BetterEXP](https://thunderstore.io/c/lethal-company/p/Swaggies/BetterEXP/) by Swaggies | 3.0.1 | recommended | Makes the XP/rank system reward scrap collection and teamwork with fun end-of-day notes |
| [BetterPaycheck](https://thunderstore.io/c/lethal-company/p/Swaggies/BetterPaycheck/) by Swaggies | 0.9.2 | recommended | Readable itemised 'Paycheck!' screen when selling |
| [CoronerIntegrations](https://thunderstore.io/c/lethal-company/p/Turkeysteaks/CoronerIntegrations/) by Turkeysteaks | 0.7.0 | recommended | Adds Coroner death messages for common modded monsters (Locker, Rolling Giant, SirenHead, Biodiversity, LegendWeathers, etc.) |
| [LCBetterSaves](https://thunderstore.io/c/lethal-company/p/Pooble/LCBetterSaves/) by Pooble | 1.7.3 | recommended | Unlimited, renamable save slots so the host can keep separate files per friend group |
| [LobbyImprovements](https://thunderstore.io/c/lethal-company/p/Dev1A3/LobbyImprovements/) by Dev1A3 | 1.1.4 | recommended | Lobby passwords, invite-only toggle, copyable lobby IDs, recently-played-with integration and better ban prompts |
| [NameplateTweaks](https://thunderstore.io/c/lethal-company/p/taffyko/NameplateTweaks/) by taffyko | 1.0.7 | recommended | Bigger nameplates, speaking indicator above heads, nameplates follow crouching, distance limit |
| [NicheTweaks](https://thunderstore.io/c/lethal-company/p/mr_hat/NicheTweaks/) by mr_hat | 0.5.1 | recommended | Grab-bag of small fixes and QoL: global voice volume slider + per-player volume saving (great for 8 friends), FPS uncap, audio warmups to kill first-play lag spikes, hoarder-bug... |
| [RuntimeIcons](https://thunderstore.io/c/lethal-company/p/LethalCompanyModding/RuntimeIcons/) by LethalCompanyModding | 0.3.3 | recommended | Renders real item icons in the hotbar instead of the generic vanilla silhouettes |
| [RuntimeIcons_BetterRotations](https://thunderstore.io/c/lethal-company/p/debit_card_debit/RuntimeIcons_BetterRotations/) by debit_card_debit | 1.2.17 | recommended | Hand-tuned icon angles for RuntimeIcons so items are recognisable at a glance |
| [ScannableCodes](https://thunderstore.io/c/lethal-company/p/Dev1A3/ScannableCodes/) by Dev1A3 | 1.0.9 | recommended | Scanning a turret/landmine/big door shows its terminal code |
| [SellMyScrap](https://thunderstore.io/c/lethal-company/p/Zehs/SellMyScrap/) by Zehs | 1.15.3 | recommended | 'sell quota' / 'sell <amount>' / 'sell all' terminal commands with confirmation and overtime preview |
| [ShipWindows](https://thunderstore.io/c/lethal-company/p/TestAccount666/ShipWindows/) by TestAccount666 | 2.11.1 | recommended | Five purchasable ship windows (type 'windows' in terminal) with shutters and a space skybox |
| [SpectateEnemies](https://thunderstore.io/c/lethal-company/p/AllToasters/SpectateEnemies/) by AllToasters | 2.9.1 | recommended | Dead players can spectate monsters (with flashlight and zoom) instead of only teammates |
| [TerminalFormatter](https://thunderstore.io/c/lethal-company/p/mrov/TerminalFormatter/) by mrov | 0.3.7 | recommended | Cleanly reformats Store/Moons/Buy/Route/Bestiary/Storage terminal pages with tables, weather and prices |
| [TerminalUtils](https://thunderstore.io/c/lethal-company/p/mrov/TerminalUtils/) by mrov | 0.0.16 | recommended | Required library for TerminalFormatter 0.3+ (moon/store catalogue logic that works with both LLL and DawnLib) |
| [ToggleMute](https://thunderstore.io/c/lethal-company/p/quackandcheese/ToggleMute/) by quackandcheese | 1.3.1 | recommended | Rebindable mute hotkey (default M) with on-screen muted indicator |
| [TwoRadarMaps](https://thunderstore.io/c/lethal-company/p/Zaggy1024/TwoRadarMaps/) by Zaggy1024 | 1.6.5 | recommended | Terminal radar and front-monitor radar become independent so one friend on the terminal and another watching the map do not fight over 'switch' |
| [Universal_Radar](https://thunderstore.io/c/lethal-company/p/ScienceBird/Universal_Radar/) by ScienceBird | 1.2.4 | recommended | Auto-generates contour maps and radar meshes for modded moons and restores old radar in interiors without sprites |
| [AccurateStaminaDisplay](https://thunderstore.io/c/lethal-company/p/ButteryStancakes/AccurateStaminaDisplay/) by ButteryStancakes | 2.2.1 | optional | Stamina bar reflects real stamina (vanilla lies at both ends) with a red 'can't sprint' segment |
| [CoronerMimics](https://thunderstore.io/c/lethal-company/p/EliteMasterEric/CoronerMimics/) by EliteMasterEric | 1.0.2 | optional | Coroner death messages for x753-Mimics |
| [DiFFoZTweaks](https://thunderstore.io/c/lethal-company/p/DiFFoZ/DiFFoZTweaks/) by DiFFoZ | 1.6.1 | optional | Soft-mask fix, cap on rendered MoreCompany cosmetics (default 15, helps 8-player lobbies), plugin blacklist, taskbar flash when loaded |
| [FinallyCorrectKeys](https://thunderstore.io/c/lethal-company/p/Rminin/FinallyCorrectKeys/) by Rminin | 1.6.1 | optional | Control tips and hover prompts show your actual rebound keys |
| [KilledByAFake](https://thunderstore.io/c/lethal-company/p/ZTM/KilledByAFake/) by ZTM | 1.0.1 | optional | Coroner + Mirage integration: the end-of-round report says 'Was killed by a fake Bob' naming the friend the masked was imitating - cheap fun for a Mirage pack that already ships... |
| [OpenBodyCams](https://thunderstore.io/c/lethal-company/p/Zaggy1024/OpenBodyCams/) by Zaggy1024 | 3.0.12 | optional | High-quality first-person body cam on the ship monitor with cosmetics support and terminal PiP |

### Multiplayer, emotes and cosmetics

| Mod | Version | Tier | What it does |
|---|---|---|---|
| [LobbyControl](https://thunderstore.io/c/lethal-company/p/mattymatty/LobbyControl/) by mattymatty | 2.5.12 | essential | Late-join while in orbit (terminal 'lobby open'), join-queue that fixes player-in-wall/no-voice on join, save hot-load, and removal of item/scrap sync limits |
| [Mirage](https://thunderstore.io/c/lethal-company/p/qwbarch/Mirage/) by qwbarch | 1.29.1 | essential | Synced voice mimicking (everyone hears the same clip) with masked enemies copying the mimicked player's suit and cosmetics |
| [MirageCore](https://thunderstore.io/c/lethal-company/p/qwbarch/MirageCore/) by qwbarch | 1.0.4 | essential | Hard dependency bundle for Mirage (pulls NAudio, OpusDotNet, Concentus, LethalSettings, AutoHookGenPatcher) |
| [MoreCompany](https://thunderstore.io/c/lethal-company/p/notnotnotswipez/MoreCompany/) by notnotnotswipez | 1.14.0 | essential | The de-facto stable lobby-size expansion (up to 8+ players) with built-in cosmetics |
| [FashionableCompany](https://thunderstore.io/c/lethal-company/p/Smxrez/FashionableCompany/) by Smxrez | 1.2.1 | recommended | 20 clothing/accessory cosmetics (scarf, beret, bowler, tie, crown...) from the same author |
| [Generic_Cosmetics](https://thunderstore.io/c/lethal-company/p/Generic_GMD/Generic_Cosmetics/) by Generic_GMD | 1.1.0 | recommended | 20 'underpaid disposable worker' cosmetics (antenna, technician hat, wrench, holstered tools) plus a Storehouse suit when More_Suits is present |
| [More_Suits](https://thunderstore.io/c/lethal-company/p/x753/More_Suits/) by x753 | 1.5.4 | recommended | Adds 9 clean suits and is the loader library for every PNG suit pack |
| [SimpleCompany](https://thunderstore.io/c/lethal-company/p/Smxrez/SimpleCompany/) by Smxrez | 2.0.4 | recommended | 21 vanilla-esque equipment cosmetics (hardhat, headset, toolbelt, medkit, O2 cage...) for MoreCompany |
| [SyncedSkinwalkers](https://thunderstore.io/c/lethal-company/p/Enchanted_Games/SyncedSkinwalkers/) by Enchanted_Games | 2.1.1 | recommended | Config preset for Mirage that keeps masked enemies fully vanilla (vanilla spawning, mask on, arms-out, no held items) while letting most other monsters occasionally mimic voices -... |
| [TooManyEmotes](https://thunderstore.io/c/lethal-company/p/FlipMods/TooManyEmotes/) by FlipMods | 2.3.17 | recommended | 300+ emotes with a radial wheel, sync-with-teammate prompts, third-person emote camera, optional emote store progression, and masked enemies emoting (pairs with Mirage) |
| [TooManySuits](https://thunderstore.io/c/lethal-company/p/Verity/TooManySuits/) by Verity | 2.0.4 | recommended | Adds in-world page buttons to the suit rack so multiple suit packs stay usable instead of overflowing the rack |
| [ClassicSuitRestoration](https://thunderstore.io/c/lethal-company/p/ButteryStancakes/ClassicSuitRestoration/) by ButteryStancakes | 2.1.3 | optional | Adds the brown teaser/anniversary suit as a vanilla-faithful extra |
| [MoreCompanyCosmeticSorter](https://thunderstore.io/c/lethal-company/p/POTATOH/MoreCompanyCosmeticSorter/) by POTATOH | 1.3.1 | optional | Sorts the MoreCompany cosmetic list by body slot with filters and a Clear All button - worth it once 3-4 cosmetic packs are installed |
| [Thighs_Cosmetics](https://thunderstore.io/c/lethal-company/p/Thighs/Thighs_Cosmetics/) by Thighs | 1.2.6 | optional | A well-made grab bag of hats, glasses, goggles and a few jokes (jester hat, ushanka, cat ears, night-vision goggles) - taste-dependent but actively maintained |

### Items, shop and scrap

| Mod | Version | Tier | What it does |
|---|---|---|---|
| [TerrasScrap](https://thunderstore.io/c/lethal-company/p/Terraformer9x/TerrasScrap/) by Terraformer9x | 81.4.2 | essential | The canonical 'Zeekerss-styled' vanilla-plus scrap pack (lava lamp, toaster, fan, coffee pot, stapler, trophies, etc.) - looks and sounds like it shipped with the game |
| [Casino_v81_Patch](https://thunderstore.io/c/lethal-company/p/lethal_coder/Casino_v81_Patch/) by lethal_coder | 1.0.0 | recommended | Tiny patch that makes LethalCasino load on v81 |
| [FacilityMeltdown](https://thunderstore.io/c/lethal-company/p/loaforc/FacilityMeltdown/) by loaforc | 2.7.5 | recommended | Pulling the apparatus starts a 2-minute reactor meltdown escape sequence |
| [Lategame_Upgrades](https://thunderstore.io/c/lethal-company/p/malco/Lategame_Upgrades/) by malco | 3.14.1 | recommended | The standard 'something to spend credits on' mod: 30+ terminal-purchased upgrades (stamina, speed, health, night vision, lightning rod, etc.) |
| [LethalCasino](https://thunderstore.io/c/lethal-company/p/mrgrm7/LethalCasino/) by mrgrm7 | 1.1.3 | recommended | A casino at the Company building (slots, roulette, blackjack, wheel, bar, jukebox, ATM) where you gamble scrap |
| [NeedyCats](https://thunderstore.io/c/lethal-company/p/Jordo/NeedyCats/) by Jordo | 1.2.5 | recommended | Cats roam facilities, meow loudly unless petted, and can be brought home |
| [SigurdsScrap](https://thunderstore.io/c/lethal-company/p/cookiecaker/SigurdsScrap/) by cookiecaker | 1.0.3 | recommended | Six lore-friendly scrap items that Sigurd's logs mention but vanilla never shipped (frying pan, big nail, scissors, box of stamps, bundle of cords, metal grinder) |
| [UsualScrap](https://thunderstore.io/c/lethal-company/p/etherealemil/UsualScrap/) by etherealemil | 2.0.7 | recommended | Big, polished pack of new scrap (fuel cylinder, capsules, crowbar, sledgehammer, padlock, candy dispenser, mansion/other scrap packs) plus purchasable equipment (handlamp,... |
| [Beanies_Furniture](https://thunderstore.io/c/lethal-company/p/Beaniebe/Beanies_Furniture/) by Beaniebe | 1.0.4 | optional | 'Vanilla plus furniture' store items (oak chair, stool, beanbag, tables, carpets, shelf, lamp, cabinet, fridge/freezer) - cheap ship decor that matches the vanilla catalogue |
| [Company_Globes](https://thunderstore.io/c/lethal-company/p/DeviousEquine/Company_Globes/) by DeviousEquine | 1.1.1 | optional | Antique globe scrap depicting the moons - pure vanilla-plus flavour scrap |
| [PizzaProbability](https://thunderstore.io/c/lethal-company/p/TrippyTree/PizzaProbability/) by TrippyTree | 1.2.4 | optional | Makes FacilityMeltdown a 50% (configurable, per-moon) chance instead of guaranteed, and scales apparatus value by risk - keeps apparatus runs closer to vanilla while retaining the... |
| [UpturnedVariety](https://thunderstore.io/c/lethal-company/p/ButteryStancakes/UpturnedVariety/) by ButteryStancakes | 2.3.0 | optional | Alternate skins for vanilla scrap plus one boombox and one record-player track, all built from Zeekerss's own Upturned assets |

### Monsters

| Mod | Version | Tier | What it does |
|---|---|---|---|
| [Biodiversity](https://thunderstore.io/c/lethal-company/p/super_fucking_cool_and_badass_team/Biodiversity/) by super_fucking_cool_and_badass_team | 0.2.9 | recommended | Adds variants of vanilla creatures (Aloe/Bracken, Ogopogo/Leviathan, Boom birds & Coil-crabs, Prototax, Leaf boys) plus a Scrap Radar |
| [Locker](https://thunderstore.io/c/lethal-company/p/zealsprince/Locker/) by zealsprince | 1.6.3 | recommended | Coil-head-like situational threat that reacts to flashlights and scanning |
| [Mimics](https://thunderstore.io/c/lethal-company/p/x753/Mimics/) by x753 | 2.7.4 | recommended | The classic fire-exit mimic: subtle, vanilla-looking, teaches observation |
| [Observer](https://thunderstore.io/c/lethal-company/p/Reiko88/Observer/) by Reiko88 | 2.0.1 | recommended | High-quality ghostly spectre that marks greedy scrap hoarders and resurrects a weapon-wielding chaser |
| [Peepers](https://thunderstore.io/c/lethal-company/p/x753/Peepers/) by x753 | 1.0.5 | recommended | Cute non-lethal outdoor critters that cling to you and add weight |
| [RollingGiant](https://thunderstore.io/c/lethal-company/p/SoftDiamond/RollingGiant/) by SoftDiamond | 2.6.3 | recommended | The iconic Rolling Giant with multiple AI modes |
| [CoilHeadStare](https://thunderstore.io/c/lethal-company/p/TwinDimensionalProductions/CoilHeadStare/) by TwinDimensionalProductions | 1.1.0 | optional | Purely cosmetic client-side patch: Coil Head slowly turns to face you and its spring bounces when hit |
| [FairAI](https://thunderstore.io/c/lethal-company/p/TheFluff/FairAI/) by TheFluff | 1.6.1 | optional | Makes landmines and turrets affect enemies too, which feels like a fairness fix rather than a difficulty change |
| [LightBat](https://thunderstore.io/c/lethal-company/p/Necessitas/LightBat/) by Necessitas | 1.0.8 | optional | Non-hostile light-feeding fauna (like locusts) that drain your flashlight |

### Moons and interiors

| Mod | Version | Tier | What it does |
|---|---|---|---|
| [LethalLevelLoader](https://thunderstore.io/c/lethal-company/p/IAmBatby/LethalLevelLoader/) by IAmBatby | 1.7.12 | essential | The loader every custom moon and interior in this list depends on |
| [33Granductor](https://thunderstore.io/c/lethal-company/p/MrSaltedBeef/33Granductor/) by MrSaltedBeef | 1.5.2 | recommended | Single high-quality 450-credit stormy mountain moon with lightning-rod gimmick |
| [57_Harbringer](https://thunderstore.io/c/lethal-company/p/WaterGun/57_Harbringer/) by WaterGun | 2.6.1 | recommended | Author-described "1 new vanilla moon": a frozen ocean moon with a bridge and motorboat fire-exit route |
| [Atlas](https://thunderstore.io/c/lethal-company/p/dopadream/Atlas/) by dopadream | 1.0.7 | recommended | Client-side HDRI skyboxes chosen by LLL content tags |
| [Deepcore_Mines](https://thunderstore.io/c/lethal-company/p/Beaniebe/Deepcore_Mines/) by Beaniebe | 1.0.9 | recommended | 5-floor mine interior acting as a Mineshaft variant with tag-based cave themes |
| [DistinctMoonVariety](https://thunderstore.io/c/lethal-company/p/DistinctBlaze/DistinctMoonVariety/) by DistinctBlaze | 3.0.5 | recommended | Four moons explicitly designed to "fit into the vanilla moon roster" (C free, B free, A 550, S 250) |
| [E_Gypt_Moon](https://thunderstore.io/c/lethal-company/p/KayNetsua/E_Gypt_Moon/) by KayNetsua | 2.0.27 | recommended | Classic intermediate pyramid moon (10-EGypt), one of the most downloaded moons ever, still actively maintained |
| [Generic_Interiors](https://thunderstore.io/c/lethal-company/p/Generic_GMD/Generic_Interiors/) by Generic_GMD | 5.2.0 | recommended | The most widely shipped interior pack: 6 vanilla-friendly interiors (Storehouse, Bunker, Drains, Substation, Tower, Liminal Facility) with separate asset bundles so unwanted ones... |
| [Liminal_House](https://thunderstore.io/c/lethal-company/p/Beaniebe/Liminal_House/) by Beaniebe | 1.1.6 | recommended | Vanilla-themed modern-house interior built as a Manor counterpart |
| [StarlancerMoons](https://thunderstore.io/c/lethal-company/p/AudioKnight/StarlancerMoons/) by AudioKnight | 4.0.1 | recommended | Four polished, vanilla-feeling moons covering every tier: Solace (free, B), Triskelion (350, B+), Auralis (850, SS) and a hidden moon |
| [Tomb](https://thunderstore.io/c/lethal-company/p/Tolian/Tomb/) by Tolian | 0.3.5 | optional | Egyptian tomb interior by KayNetsua/Tolian that thematically completes E_Gypt |

### Weather, ambience and audio

| Mod | Version | Tier | What it does |
|---|---|---|---|
| [loaforcsSoundAPI](https://thunderstore.io/c/lethal-company/p/loaforc/loaforcsSoundAPI/) by loaforc | 2.0.13 | essential | The sound-replacement framework used by every modern sound pack (UniqueItemSounds, LETHALRESONANCE, Ardie, NoSqueak) |
| [loaforcsSoundAPI_LethalCompany](https://thunderstore.io/c/lethal-company/p/loaforc/loaforcsSoundAPI_LethalCompany/) by loaforc | 1.0.2 | essential | Lethal Company condition bindings (moon name, dungeon, time of day, player location) for SoundAPI |
| [WeatherRegistry](https://thunderstore.io/c/lethal-company/p/mrov/WeatherRegistry/) by mrov | 0.8.8 | essential | The weather framework every modded weather depends on |
| [Kenjis_Weathers](https://thunderstore.io/c/lethal-company/p/rectorado/Kenjis_Weathers/) by rectorado | 1.1.0 | recommended | Three simple, well-scoped weathers (Gusty, Infested, Acid Rain) explicitly designed to feel like vanilla and to combine with other weathers |
| [LegendWeathers](https://thunderstore.io/c/lethal-company/p/Zigzag/LegendWeathers/) by Zigzag | 2.2.2 | recommended | Two rare, high-production-value event weathers (Blood Moon, Majora Moon) with low default weights - a memorable 'curated slice' of content rather than a constant difficulty change |
| [LethalElementsForky](https://thunderstore.io/c/lethal-company/p/seechela/LethalElementsForky/) by seechela | 1.4.2 | recommended | The maintained v81 fork of Lethal Elements: Heatwave, Solar Flare, Snowfall, Blizzard, Toxic Smog with proper snow accumulation and auroras |
| [LightsOut](https://thunderstore.io/c/lethal-company/p/mrov/LightsOut/) by mrov | 0.2.1 | recommended | Disables the ship's decorative lamps/apparatice light sources to gain FPS |
| [UniqueItemSounds](https://thunderstore.io/c/lethal-company/p/debit_card_debit/UniqueItemSounds/) by debit_card_debit | 0.2.3 | recommended | Hand-recorded grab/drop sounds for ~20 vanilla scrap items plus a few modded ones |
| [ArtificeBlizzard](https://thunderstore.io/c/lethal-company/p/ButteryStancakes/ArtificeBlizzard/) by ButteryStancakes | 1.2.0 | optional | Restores Zeekerss's original snowy Artifice as a pseudo-weather |

### Light balance and progression

| Mod | Version | Tier | What it does |
|---|---|---|---|
| [Configurable_Quota](https://thunderstore.io/c/lethal-company/p/seechela/Configurable_Quota/) by seechela | 1.6.0 | recommended | Quota tuned for the 2x-loot economy: higher starting quota and increase, and a mild per-player quota scale above 4 players |
| [Fairer_Fire_Exits](https://thunderstore.io/c/lethal-company/p/MikuOreo/Fairer_Fire_Exits/) by MikuOreo | 2.0.2 | recommended | Places fire exits in the tile furthest from every other exit and guarantees they spawn, ending 'fire exit is 5 m from main' days |

### Libraries pulled in as dependencies

| Mod | Version | Tier | What it does |
|---|---|---|---|
| [Auralis](https://thunderstore.io/c/lethal-company/p/AudioKnight/Auralis/) by AudioKnight | 4.0.1 | essential | Library required by AudioKnight-StarlancerMoons |
| [Beanie_Lib](https://thunderstore.io/c/lethal-company/p/Beaniebe/Beanie_Lib/) by Beaniebe | 1.0.9 | essential | Library required by Beaniebe-Deepcore_Mines, Generic_GMD-Generic_Interiors |
| [Concentus](https://thunderstore.io/c/lethal-company/p/qwbarch/Concentus/) by qwbarch | 2.3.0 | essential | Library required by Enchanted_Games-SyncedSkinwalkers, qwbarch-MirageCore |
| [CSync](https://thunderstore.io/c/lethal-company/p/Sigurd/CSync/) by Sigurd | 5.0.1 | essential | Library required by etherealemil-UsualScrap, malco-Lategame_Upgrades |
| [DawnLib](https://thunderstore.io/c/lethal-company/p/TeamXiaolan/DawnLib/) by TeamXiaolan | 0.9.25 | essential | Library required by AudioKnight-StarlancerMoons, DeviousEquine-Company_Globes, Reiko88-Observer, Terraformer9x-TerrasScrap, TestAccount666-ShipWindows, cookiecaker-SigurdsScrap, etherealemil-UsualScrap, loaforc-FacilityMeltdown |
| [Generic_Doorscript](https://thunderstore.io/c/lethal-company/p/Generic_GMD/Generic_Doorscript/) by Generic_GMD | 1.0.2 | essential | Library required by Generic_GMD-Generic_Interiors |
| [Interactive_Terminal_API](https://thunderstore.io/c/lethal-company/p/WhiteSpike/Interactive_Terminal_API/) by WhiteSpike | 1.3.3 | essential | Library required by TestAccount666-ShipWindows, malco-Lategame_Upgrades |
| [itolib](https://thunderstore.io/c/lethal-company/p/pacoito/itolib/) by pacoito | 0.9.3 | essential | Library required by Beaniebe-Deepcore_Mines, MrSaltedBeef-33Granductor |
| [JKConfig](https://thunderstore.io/c/lethal-company/p/rectorado/JKConfig/) by rectorado | 1.0.1 | essential | Library required by Generic_GMD-Generic_Interiors |
| [JLL](https://thunderstore.io/c/lethal-company/p/JacobG5/JLL/) by JacobG5 | 1.10.1 | essential | Library required by Beaniebe-Beanies_Furniture, Beaniebe-Deepcore_Mines, Beaniebe-Liminal_House, DistinctBlaze-DistinctMoonVariety, Generic_GMD-Generic_Interiors, KayNetsua-E_Gypt_Moon, MrSaltedBeef-33Granductor, Tolian-Tomb, rectorado-Kenjis_Weathers |
| [KenjiLib](https://thunderstore.io/c/lethal-company/p/rectorado/KenjiLib/) by rectorado | 0.7.1 | essential | Library required by Generic_GMD-Generic_Interiors, MrSaltedBeef-33Granductor, rectorado-Kenjis_Weathers |
| [LethalCompany_InputUtils](https://thunderstore.io/c/lethal-company/p/Rune580/LethalCompany_InputUtils/) by Rune580 | 0.7.13 | essential | Library required by AllToasters-SpectateEnemies, FlipMods-TooManyEmotes, Rminin-FinallyCorrectKeys, malco-Lategame_Upgrades, quackandcheese-ToggleMute |
| [LethalNetworkAPI](https://thunderstore.io/c/lethal-company/p/xilophor/LethalNetworkAPI/) by xilophor | 3.4.2 | essential | Library required by seechela-Configurable_Quota |
| [LethalSettings](https://thunderstore.io/c/lethal-company/p/willis81808/LethalSettings/) by willis81808 | 1.4.1 | essential | Library required by Enchanted_Games-SyncedSkinwalkers, qwbarch-MirageCore |
| [ManuLib](https://thunderstore.io/c/lethal-company/p/Generic_GMD/ManuLib/) by Generic_GMD | 1.1.1 | essential | Library required by Generic_GMD-Generic_Interiors, rectorado-Kenjis_Weathers |
| [MrovLib](https://thunderstore.io/c/lethal-company/p/mrov/MrovLib/) by mrov | 0.4.15 | essential | Library required by mrov-TerminalUtils, mrov-WeatherRegistry |
| [NAudio](https://thunderstore.io/c/lethal-company/p/Bobbie/NAudio/) by Bobbie | 2.2.2 | essential | Library required by Enchanted_Games-SyncedSkinwalkers, qwbarch-MirageCore |
| [NAudioLame](https://thunderstore.io/c/lethal-company/p/qwbarch/NAudioLame/) by qwbarch | 2.1.1 | essential | Library required by Enchanted_Games-SyncedSkinwalkers |
| [OdinSerializer](https://thunderstore.io/c/lethal-company/p/Lordfirespeed/OdinSerializer/) by Lordfirespeed | 2024.2.2700 | essential | Library required by xilophor-LethalNetworkAPI, xilophor-StaticNetcodeLib |
| [OpusDotNet](https://thunderstore.io/c/lethal-company/p/qwbarch/OpusDotNet/) by qwbarch | 1.0.30 | essential | Library required by Enchanted_Games-SyncedSkinwalkers, qwbarch-MirageCore |
| [Solace](https://thunderstore.io/c/lethal-company/p/AudioKnight/Solace/) by AudioKnight | 4.0.1 | essential | Library required by AudioKnight-StarlancerMoons |
| [StarlancerZero](https://thunderstore.io/c/lethal-company/p/AudioKnight/StarlancerZero/) by AudioKnight | 4.0.1 | essential | Library required by AudioKnight-StarlancerMoons |
| [StaticNetcodeLib](https://thunderstore.io/c/lethal-company/p/xilophor/StaticNetcodeLib/) by xilophor | 1.2.0 | essential | Library required by EliteMasterEric-Coroner |
| [TerraMesh](https://thunderstore.io/c/lethal-company/p/v0xx/TerraMesh/) by v0xx | 1.2.0 | essential | Library required by ScienceBird-Universal_Radar, seechela-LethalElementsForky |
| [TestAccountCore](https://thunderstore.io/c/lethal-company/p/TestAccount666/TestAccountCore/) by TestAccount666 | 1.18.0 | essential | Library required by TestAccount666-GoodItemScan, TestAccount666-ShipWindows |
| [Triskelion](https://thunderstore.io/c/lethal-company/p/AudioKnight/Triskelion/) by AudioKnight | 4.0.1 | essential | Library required by AudioKnight-StarlancerMoons |

### Suits and player models

| Mod | Version | Tier | What it does |
|---|---|---|---|
| [1000_Quota_Stare](https://thunderstore.io/c/lethal-company/p/ManiaBania/1000_Quota_Stare/) by ManiaBania | 1.0.0 | recommended | The Lethal Company '1000 quota stare' meme suit |
| [AmongUsSuits](https://thunderstore.io/c/lethal-company/p/ViViKo/AmongUsSuits/) by ViViKo | 1.0.2 | recommended | Red, Blue, Green and Orange crewmate suits with glowing visors |
| [ClassicDoomguy](https://thunderstore.io/c/lethal-company/p/Regretti/ClassicDoomguy/) by Regretti | 1.0.0 | recommended | Doomguy Praetor armour with normal map |
| [CudisRealisticSuits](https://thunderstore.io/c/lethal-company/p/kidcudilovers/CudisRealisticSuits/) by kidcudilovers | 1.0.0 | recommended | Vanilla-tone work suits: Construction, Maintenance, Custodian, Relay, Squad I (orange), Squad II (blue) |
| [Fashion_Company](https://thunderstore.io/c/lethal-company/p/Dwarggo/Fashion_Company/) by Dwarggo | 1.3.1 | recommended | Company-issued variants: Arctic, Dog, Elite, Highclass, Hightech, Speedster, Used, Workout (two with emissive trim) |
| [GlowStickSuits](https://thunderstore.io/c/lethal-company/p/Norman/GlowStickSuits/) by Norman | 1.0.4 | recommended | 11 glow-in-the-dark colour suits (Red through White, numbered in rainbow order) for finding each other on dark moons |
| [LethalFashion](https://thunderstore.io/c/lethal-company/p/BatTeam/LethalFashion/) by BatTeam | 1.0.8 | recommended | Host-only: unlocks the six vanilla store suits (Green, Hazard, Pajama, Purple, Bee, Bunny) free from day one; clients do not need it |
| [ODST_Suit](https://thunderstore.io/c/lethal-company/p/TeamClark/ODST_Suit/) by TeamClark | 1.0.0 | recommended | Halo ODST armour |
| [RustHazmatSuit](https://thunderstore.io/c/lethal-company/p/TeamClark/RustHazmatSuit/) by TeamClark | 1.0.0 | recommended | Yellow hazmat suit from Rust |
| [Scooby_Doo_Crew_Suits](https://thunderstore.io/c/lethal-company/p/CoNcept_Temple_Modding/Scooby_Doo_Crew_Suits/) by CoNcept_Temple_Modding | 1.0.4 | recommended | Fred, Daphne ('Daphane' in-game), Velma, Shaggy and Scooby - a five-piece set for a whole squad |
| [SCP_Foundation_Suit](https://thunderstore.io/c/lethal-company/p/TeamClark/SCP_Foundation_Suit/) by TeamClark | 1.1.0 | recommended | SCP Facility Guard tactical security uniform |
| [SuitsPlus](https://thunderstore.io/c/lethal-company/p/FREAKS/SuitsPlus/) by FREAKS | 3.0.0 | recommended | 17 plain colour suits (prefixed '(Color)') so a big crew can tell each other apart, plus 10 '(Custom)' cartoon/fun suits; 2 customs disabled in config as duplicates of Fashion_Comp |
| [True_Team_Company](https://thunderstore.io/c/lethal-company/p/TrueCompany/True_Team_Company/) by TrueCompany | 1.1.0 | recommended | Role-labelled crew suits: Civilian, Commander, Corpsman, Grunt, Mechanic, Medic, Quartermaster, Scientist, Sergeant, Technician |
| [Vault_Boy_Suit](https://thunderstore.io/c/lethal-company/p/TeamClark/Vault_Boy_Suit/) by TeamClark | 1.0.0 | recommended | Fallout Vault Boy blue/yellow jumpsuit (author cleared it for modpacks) |

<!-- MODLIST:END -->

## Config notes

Configs shipped in this pack (found in `config/` and applied automatically by the mod manager):

- **MoreCompany**: player count set to 16. The game UI and most HUD mods are only really tested up to 8,
  so expect small layout quirks above that. Lower it in the mod manager's Config Editor if you prefer.
- **Mirage** (masked enemies mimic player voices): the SyncedSkinwalkers preset is included, which keeps
  masked spawning fully vanilla and lets most monsters mimic voices. Its config files are the Mirage config;
  do not add a second copy. Voice recording can be turned off per player in the Mirage settings menu.
- **GeneralImprovements**: tools are scannable (`ScannableTools = All`). Everything else is GI's default,
  which is mostly off; browse its LethalConfig page, there is a lot of good stuff in there.
- **ButteryFixes**: `BodiesCollectSelf` is off because GeneralImprovements owns body collection.
- **ArtificeBlizzard**: snow on Artifice is a 25% roll on clear days instead of permanent.

### Loot and pressure tuning (1.1.x)

Version 1.0.0 played harder and stingier than vanilla. The causes were measured from real session logs
and the mods' generated configs, and fixed with config rather than by removing content:

- **Weather** (WeatherRegistry): modded weathers shipped with weights of 50 to 100 each plus per-moon
  overrides like Blizzard 120 on every snow moon, so most weather rolls were modded and a Blood Moon could
  land on the free starter moon on day one. Modded weights are now 5 to 25 with small per-moon values,
  a modded day rolls back into vanilla odds the next day, and the first day of a new save is clear
  everywhere like vanilla. WeatherTweaks was removed from the pack (see the host checklist: it stays
  installed until you uninstall it).
- **More loot on the floor** (1.2.0): every weather in `mrov.WeatherRegistry.cfg` carries a scrap amount
  multiplier of **2.0** and a scrap value multiplier of **0.6**, applied by the host on every moon. So a
  moon that spawns 12 items in vanilla spawns about 24, each worth 60 percent, and a full clear is worth
  about 1.2x vanilla. Weathers keep their own character on top (a Heatwave still spawns fewer, richer
  items). To change the feel, edit the two keys in every weather section; the ratio is what matters.
- **Quota to match** (Configurable Quota): starting quota 160 instead of 130 and base increase 120 instead
  of 100, the same 20 percent as the loot. Above 4 players the quota increase also scales by 8 percent per
  extra player (8 players = 1.32x). Every other feature of that mod (death penalties, scrap loss on wipe,
  buy-rate randomness, dynamic scaling) is off. Tune it in `com.seeya.configurablequota.cfg`.

- **Interiors** (LethalLevelLoader): the custom interiors were injected at the same weight as the vanilla
  Facility on the thinnest moons (Storehouse on Experimentation, Tower on Assurance, Drains on Vow,
  Bunker on March, Liminal House on Offense and Rend, Deepcore Mines on Titan), and Tower multiplies the
  dungeon by 1.5 on top. Scrap count is a per-moon number, so a bigger interior only spreads the same
  items thinner. Weights are now about a third of the vanilla interior's, and Tower (1.2x), Deepcore
  Mines and Liminal House (1.25x) are size-capped. Nothing is disabled. Liminal House keeps a lot of its
  scrap inside drawers and cabinets, so open them.
- **Moons**: Retinue and Detritus had Titan-tier outside enemy power on free-tier moons; Harbringer and
  EGypt ran well above the vanilla moon at their price; the Starlancer moons had high inside power for
  their tier. All brought in line. Solace, Auralis and Granductor had too few items for their interior
  size and got Offense, Titan and Titan-tier counts respectively.
- **Suits** (1.2.0): 14 packs, about 75 suits on the rack, all plain PNG suits loaded by More_Suits, so
  nothing else changes. The shipped `x753.More_Suits.cfg` turns on `Ignore !less-suits.txt` (four of the
  packs ship a marker file that would otherwise silently delete More_Suits' own nine suits), hides two
  duplicate suits, unlocks the store-priced modded suits, and raises the suit cap to 150. Trim the rack by
  adding file names to `Disabled Suit List`; the pack pages are alphabetical by mod author, so the plain
  colour suits sit under F (SuitsPlus) and the glow suits under N. LethalFashion makes the six vanilla shop
  suits free, but only on a save started after it was installed.
- **Monsters**: Rolling Giant weights halved on its six vanilla moons, max 2, classic Coil-Head
  behaviour. Locker 15/30/40 on Experimentation/Assurance/Offense (was 25/75/100), max 2. LightBat
  weight 20 (was 45). Observer at most 2 chasers (was 6), angered by 10 hoarded scrap (was 6). Coil-crab
  at most 2 per day and half as common on Offense. Meltdowns spawn 3 extra monsters instead of 5.

Every one of these is a plain config value, so the host can nudge any of them in the mod manager's
Config Editor or the in-game LethalConfig menu. Delete a shipped file to return that mod to its defaults.

### Things the host should do once, after the first launch

**Only the host's settings count.** Weather, which interior generates, how much scrap spawns and how many
enemies appear are all decided by whoever hosts the lobby. If the host is on an old version or still has
WeatherTweaks installed, everyone gets the old experience no matter what the clients run.

1. **If you updated from 1.0.0 or 1.1.0, uninstall WeatherTweaks.** The mod manager updates the pack's
   mods and copies the new config files, but it does **not** uninstall mods the new version stopped
   listing. In the profile's **Installed** tab find **WeatherTweaks** and click **Uninstall**, or start a
   fresh profile from the pack. If the tuning still does not seem to apply, delete the shipped files from
   `BepInEx/config` (they start with "Shipped by the Lethal Company v81 Friends Pack") and let the manager
   re-copy them.
2. **Check it took**, as host, after one launch: in the terminal type `simulate vow`, `simulate titan` and
   `simulate offense` (LethalLevelLoader prints interior odds; the vanilla interior should be around 70 to
   80 percent) and `weather forecast artifice` (WeatherRegistry prints weather odds; clear should be around
   a third and there should be no combined entries with `+` or `>`).
3. **Lategame Upgrades**: it is the biggest departure from vanilla in this pack. For a vanilla-plus feel,
   turn off Contracts, Interns (UsualScrap's Defibrillator is the revive item), Midas Touch, Scavenger
   Instincts, Item Duplicator, Scrap Keeper, Life Insurance and Deeper Pockets. Keep the stat upgrades.
4. **UsualScrap**: set `Disable Item Icons` to true so RuntimeIcons draws the hotbar icons, and turn off the
   Traffic Cone (TerrasScrap has one too). If your group prefers safe scrap, also disable the Fuel Cylinder,
   Radioactive Cell and Sacrificial Capsule.
5. **PizzaProbability / FacilityMeltdown**: if a modded moon turns red during a meltdown, disable meltdown
   for that moon in PizzaProbability's per-moon list.
6. **OpenBodyCams**: with LethalLib installed the body cam is a 200-credit antenna upgrade in the store.
   Everyone has the pack, so that is fine; set `Enabled = false` under Ship Upgrade if you want it free.
7. **Optional, Mimics**: fire-exit mimics only spawn in the interiors on their whitelist, which is the
   vanilla ones plus a few popular custom interiors. Adding more is possible in the Mimics config but the
   mod warns not every interior works with it, so the pack leaves it alone.

Everything not listed ships with the mod author's defaults.

## Known caveats

- LethalCasino is a v73 build kept alive by the Casino v81 Patch. Chip bags despawn from the ship on reload.
- AsyncLoggers writes an extra SQLite log database and fetches the SQLite library on first run. Harmless,
  and it can be disabled in its config folder if you do not want it.
- Generic Interiors includes a "Liminal Facility" backrooms-style interior. It has no weight on any moon
  in this pack, so it will not generate unless you add it. Do not blacklist its bundle: Storehouse lives
  in the same file.

## Building or updating this pack yourself

The pack is generated from `modlist.json` with `build_modpack.py`. The script asks Thunderstore for the
newest release of every mod, refuses to build if anything is deprecated or a dependency is missing,
rewrites the mod table above, and produces the upload-ready zip.

```bash
python build_modpack.py --check   # dry run: resolve versions and report problems
python build_modpack.py           # write manifest.json, README table and the zip
```

Bump `version_number` in `modlist.json` before each upload.

## Credits

All credit goes to the mod authors linked in the table. This pack only assembles their work.
