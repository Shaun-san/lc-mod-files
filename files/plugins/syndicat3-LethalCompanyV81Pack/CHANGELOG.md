# Changelog

## 1.2.0 (2026-09-06)

- Loot: about 2x the vanilla number of scrap items on every moon, each worth 60 percent (WeatherRegistry
  amount 2.0 / value 0.6 on every weather, replacing the 1.3 amount multiplier of 1.1.2). A full clear is
  worth roughly 1.2x vanilla; the point is that everyone finds things.
- Quota: added seechela-Configurable_Quota with starting quota 160, base increase 120 and a mild
  per-player quota scale above 4 players. All of its other features are left off.
- Suits: 14 suit packs, 75 suits on the rack (about 50 MB): 17 plain colours and 11 glow colours for
  telling a big crew apart, 26 work and role suits (construction, maintenance, medic, quartermaster,
  SCP guard, hazmat, Company variants), a few iconic character suits (ODST, Vault Boy, Doomguy, the
  Scooby gang) and a few fun ones (Among Us crew, the 1000 quota stare). LethalFashion unlocks the six
  vanilla shop suits for free on new saves. More_Suits config ships with the marker-file trap disabled,
  two duplicate suits hidden, and headroom for 150 suits. With TooManySuits that is about 8 rack pages.

## 1.1.2 (2026-09-06)

Corrections to the 1.1.x tuning after a source-level review, plus a crew-size scrap multiplier.

- Fixed: the interior size caps shipped in 1.1.0/1.1.1 did nothing. LethalLevelLoader's "Restrict Dungeon
  Size Scaler" means 1 = use the cap (the key's own description reads the other way). Tower is now capped
  at 1.2x, Deepcore Mines and Liminal House at 1.25x, and the caps actually apply.
- Fixed: 1.1.1 had scaled the interior weights twice (the generator re-read its own output), leaving the
  custom interiors 4-9x rarer than intended. Weights are now absolute per moon: Storehouse 100 on
  Experimentation, Bunker 100 on March, Drains 100 on Vow, Tower 100 on Assurance and Retinue, Deepcore
  Mines 90 on Titan, Liminal House 80 on Offense and Rend, Tomb 150 on EGypt. Vanilla interiors are the
  majority again without any custom interior being effectively switched off.
- Crew-size loot: every weather now carries a scrap amount multiplier of 1.3 (WeatherRegistry, applied by
  the host on every moon). Vanilla never scales scrap with player count and no maintained mod does; this
  is the documented lever. 1.0 = vanilla for 4 players, 1.15 for 5-6, 1.3 for 7-8, 1.5 for 10-12. Heatwave,
  Snowfall and Blizzard no longer spawn fewer items than a clear day.
- Locker: the 1.1.0 weight cut never reached Offense and Assurance because the mod's per-moon list wins;
  that list is now 15/30/40 (was 25/75/100).
- Rolling Giant: pinned to its six vanilla moons (the profile had "spawn on any moon" switched on, which
  is not the mod default and was not written by the pack).
- Biodiversity Coil-crab: at most 2 per day and half as common on Offense. FacilityMeltdown: 3 extra
  monsters during a meltdown instead of 5.
- Loot on thin moons: Solace 15-18 items (was 12-14), Auralis 27-31 (was 23-26), Granductor 24-28 (was
  18-20, on a 2x interior).
- Reverted: SpawnCycleFixes is back at its default. Its schedule fix removes vanilla's double spawn wave at
  the start of the day, so it lowers early pressure rather than raising it.
- Safety net: if a host still has WeatherTweaks installed, its 21 combined weathers now have zero weight
  and its difficulty scaling and hidden forecasts are off. Uninstalling it is still the right fix.
- Note: the 1.1.0 "scrap value raised to Vow tier" edit for Retinue and Detritus only touched a value the
  game does not use for item counts; it was harmless and has been dropped from the notes.

## 1.1.1 (2026-09-06)

- WeatherRegistry: the per-moon "Level weights" that mods ship (for example Blizzard at 120 on every
  snow-tagged moon, Solar Flare at 200 on Embrion) bypassed the 1.1.0 default weights entirely. They are
  now overridden too, so snow moons get a light snow chance instead of a Blizzard most days.
- README: how to actually remove WeatherTweaks (mod managers keep mods a pack stopped listing) and a
  reminder that only the host's settings count for weather, interiors, scrap and enemies.

## 1.1.0 (2026-09-05)

Loot and pressure tuning after the first play sessions ("not enough loot inside, too hard").

- Removed WeatherTweaks (combined and progressing weathers, hidden forecasts, per-player difficulty scaling).
- WeatherRegistry: modded weather weights cut from 50-100 to 5-25, modded days roll back into vanilla odds
  the next day, first day of a new save is clear everywhere.
- LethalLevelLoader: Tower and Deepcore Mines size-capped and about three times rarer; Liminal House,
  Bunker, Drains and Storehouse about half as frequent. Retinue and Detritus scrap value raised to Vow tier
  and their outside enemy power lowered; Harbringer, EGypt and the Starlancer moons brought to vanilla
  enemy power for their price.
- SpawnCycleFixes: Consistent Spawn Times off (vanilla spawn pacing).
- Rolling Giant weights halved, max 2, Coilhead AI. Locker weight 30, max 2. LightBat weight 20.
  Observer max 2 chasers, anger threshold 10 scrap.
- All mods re-resolved to their newest Thunderstore release.

## 1.0.0 (2026-09-05)

- Initial release for Lethal Company v81.
- 135 curated mods plus 26 library dependencies, every one resolved to its newest Thunderstore release on
  2026-09-05 and checked for a v81-compatible build.
- Ships tuned configs for MoreCompany (16 players), GeneralImprovements (scannable tools), ButteryFixes
  (body collection handed to GeneralImprovements) and ArtificeBlizzard (random snow instead of permanent).
- Mirage uses the SyncedSkinwalkers preset so masked enemies spawn exactly as in vanilla.
