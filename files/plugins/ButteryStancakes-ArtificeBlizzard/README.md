> Artifice was an ice/snow blizzard moon just like Rend and Dine, up until two days before Version 50 went into public beta. I made the change last-minute because thought its more complex design benefited from you actually being able to see and hear.

– Zeekerss, [The Version 50 Post](https://www.patreon.com/posts/version-50-post-101884472)

# Artifice Blizzard
This mod is meant to address the "what-if" scenario of Artifice remaining a snowy map in the full release of v50. It should fall mostly in line with the aesthetics of the vanilla snowy maps (Rend, Dine, and Titan)

By default, using this mod will make Artifice always snowy, as well as disable daytime spawns (bees and tulip snakes) in your own hosted games. However there are a multitude of config settings you can tweak, to get the snowy Artifice experience you desire best.

All settings are client-side and only affect your game, with the exception of the "Spawning" settings which only work in games you host. (They will not cause desync when joining other games, however.) Random chance is seeded and thus multiple players using the same config settings should get the same collective experience.

## Configuration
- Spawning
  - `DaytimeSpawns`: Whether daytime enemies (manticoils, circuit bees, tulip snakes) are allowed to spawn. (Defaults to `false`)
  - `BaboonWeight`: Spawn weight for baboon hawks. `0` disables spawns entirely. (Defaults to `7`, the vanilla value. Must be between 0 and 100)
    - Percent chance calculation: `BaboonWeight / (BaboonWeight + 93) * 100%`
  - `AlwaysOverrideSpawns`: Whether to apply the above settings all the time or only when Artifice is snowy. (Defaults to `false`, meaning default spawn settings are used if Artifice is not snowy. SEE `SnowMode`)
- Visuals
  - `FogDistance`: Controls visibility in the snowstorm. Lower values mean denser fog. (Defaults to `8.0`. Must be between 2.4 and 25.0)
    - Rend uses `3.7`, Titan uses `5.0`, and Dine uses `10.0`.
	- Artifice uses `25.0` in vanilla.
  - `FogColor`: Controls the color of the snowstorm.  (Defaults to `Neutral`)
    - `Neutral` matches Rend.
	- `BrightBlue` matches the appearance of earlier versions of this mod.
	- `Bluish` is somewhere in between (same brightness as Rend, but with a tint of blue hue)
- Random
  - `SnowMode`: Controls when the blizzard will be active. `Always` means always snowy. `RandomWhenClear` has a random chance to make it snowy during mild weather, as a sort of pseudo-weather effect. `RandomAnyWeather` will always randomize snow and allows it to stack with other weather types. (Default to `Always`)
  - `RandomChance`: When using either of the random options, this is the exact chance value. (Defaults to `0.25`, or 25% chance. Must be between `0.0` and `1.0`, which are "never" and "guaranteed" respectively.)