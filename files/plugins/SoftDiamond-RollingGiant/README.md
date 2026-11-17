# Rolling Giant

> Note: This is a build created for v81. Reach outs have been made to both modders for the original project and the v73 project. I am happy to deprecate my project/continue the project as/if needed.

> Made by Andrew Burke

Adds the Rolling Giant as a new enemy type into Lethal Company. Sounds are included.

Features:

- Adds the Rolling Giant as a new enemy
- Adds a custom scrap poster for the Rolling Giant
- Rolling Giants can be scanned to read their own unique bestiary entry
- Multiple AI behaviours to choose from
- Can change the scale of the Rolling Giant between two values
- Can change the Rolling Giant's movement speed, wait durations, move durations, and more
- Rolling Giants have the option to rotate to face the player if they have been still for some time
- Can change the AI type of all Rolling Giants on the fly:
  - A hot key to reload the entire config file
  - Hotkeys to cycle between AI types

![There should be the picture... Something went wrong.](https://github.com/nomnomab/lc-rolling-giant/blob/b7ec500fe67ce588190dbb03c3a2a0baad42bfda/Images/promo.png?raw=true)

## Installation

Put the `/BepInEx/` folder inside your `/steamapps/common/Lethal Company/` folder after installing all the dependencies.

## Config

Generated after launching the game for the first time.

### General

- `GiantScaleInsideMin` - The minimum scale of the Rolling Giant's model inside
  - This changes how small the Giant can be
- `GiantScaleInsideMax` - The maximum scale of the Rolling Giant's model inside
  - This changes how big the Giant can be
- `GiantScaleOutsideMin` - The minimum scale of the Rolling Giant's model outside
  - This changes how small the Giant can be
- `GiantScaleOutsideMax` - The maximum scale of the Rolling Giant's model outside
  - This changes how big the Giant can be

### Spawn Conditions

These do not update when reloading the config in-game!

- `SpawnIn` - Levels that the Rolling Giant can spawn in, separated by their chances of spawning
  - Vanilla caps at 100, but you can go farther.
  - This chance is also a weight, not a percentage
  - Higher chance = higher chance to get picked
  - The names are what you see in the terminal
  - `Vow:45,March:45,Rend:54,Dine:65,Offense:45,Titan:65`
- `SpawnInOutsideChance` - The chance for the Rolling Giant to spawn outside in the levels from `SpawnIn`
- `SpawnInAny` - If the Rolling Giant can spawn on any level
- `SpawnInAnyChance` - The chance for the Rolling Giant to spawn in any level
- `SpawnInAnyOutsideChance` - The chance for the Rolling Giant to spawn outside in any level
- `CanSpawnInside` - If the Rolling Giant should spawn inside the dungeon
- `CanSpawnOutside` - If the Rolling Giant should spawn outside
- `DisableOutsideAtNight` - If the Rolling Giant will turn off if it is outside at night.
- `MaxPerLevel` - The maximum amount of Rolling Giant's that can spawn in a level
- `SpawnPosterIn` - Where the Rolling Giant poster scrap can spawn, separated by their chances of spawning
  - Vanilla caps at 100, but you can go farther.
  - This chance is also a weight, not a percentage
  - Higher chance = higher chance to get picked
  - The names are what you see in the terminal
  - `Vow:12,March:12,Rend:12,Dine:12,Offense:12,Titan:12`

### AI

- `AiType` - Type of AI the Rolling Giant uses
  - Putting multiple will randomly choose between them each time you land on a moon 
  - Coilhead - Move when the player is not looking at it
  - InverseCoilhead - Move when the player is looking at it
  - RandomlyMoveWhileLooking - Randomly move while the player is looking at it
    - `WaitTimeMin` - The minimum duration in seconds that the Rolling Giant waits before moving again
    - `WaitTimeMax` - The maximum duration in seconds that the Rolling Giant waits before moving again
    - `RandomMoveTimeMin` - The minimum duration in seconds that the Rolling Giant moves toward the player
    - `RandomMoveTimeMax` - The maximum duration in seconds that the Rolling Giant moves toward the player
  - LookingTooLongKeepsAgro - If the player looks at it for too long it doesn't stop chasing
    - `LookTimeBeforeAgro` - How long the player can look at the Rolling Giant before it starts chasing.
  - FollowOnceAgro - Once the player is noticed, the Rolling Giant will follow the player constantly
  - OnceSeenAgroAfterTimer - Once the player sees the Rolling Giant, it will agro after a timer
    - `WaitTimeMin` - The minimum duration in seconds that the Rolling Giant waits before chasing the player
    - `WaitTimeMax` - The minimum duration in seconds that the Rolling Giant waits before chasing the player
  - All - Will select all of the ai types
- `AiTypeChangeOnHourInterval` - If the AI type should change every X hours. Set to 0 to disable
- `MoveSpeed` - Speed of the Rolling Giant's movement in m/s²
- `MoveAcceleration` - How long it takes the Rolling Giant to get to its movement speed in seconds
- `MoveDeceleration` - How long it takes the Rolling Giant to stop moving in seconds
- `RotateToLookAtPlayer` - If the Rolling Giant should rotate to face the player if it has been still for some time
- `DelayBeforeLookingAtPlayer` - The delay before the Rolling Giant looks at the player
- `LookAtPlayerDuration` - The duration the Rolling Giant takes to look at the player

### Host

These do not update when reloading the config in-game!

- `GotoPreviousAiTypeKey` - The key to go to the previous AI type
  - This uses Unity's New Input System's key-bind names
  - Defaults to `Keypad 7`
- `GotoNextAiTypeKey` - The key to go to the next AI type
  - This uses Unity's New Input System's key-bind names
  - Defaults to `Keypad 8`
- `ReloadConfigKey` - The key to reload the config. Does not update spawn conditions
  - This uses Unity's New Input System's key-bind names
  - Defaults to `Keypad 9`

### Building the project

#### Removing the local plugin package step

Remove the `PreBuild` step in the csproj, and replace the `PostBuild` step with

```cs
<Target Name="PostBuild" AfterTargets="PostBuildEvent">
  <Exec Command="cd $(NetcodePatcherDir)&#xA;NetcodePatcher.dll $(TargetDir) deps/&#xA;xcopy /y /d &quot;$(TargetDir)$(TargetName).dll&quot; &quot;$(GameDir)\BepInEx\plugins\RollingGiant\&quot;&#xA;" />
</Target>
```

Also remove:

```cs
<ItemGroup>
  <Folder Include="plugin\BepInEx\plugins\RollingGiant\" />
</ItemGroup>
```

#### Initial steps

1. Open the .csproj
2. Change `<GameDir>` to where your game is installed
3. Change `<NetcodePatcherDir>` to where you have the [Unity Netcode Patcher](https://github.com/EvaisaDev/UnityNetcodePatcher) extracted

> Can also remove the enter netcode patcher step if you want to use the nuget version instead, but I haven't updated to that yet, so I haven't looked into it

4. Build

When built, it will patch the dll and then copy the dll to the game's plugin folder.

If you don't want the auto-copying to the game directory, then remove this from the `PostBuild` step:

```cs
xcopy /y /d &quot;$(TargetDir)$(TargetName).dll&quot; &quot;$(GameDir)\BepInEx\plugins\RollingGiant\&quot;&#xA;
```
## Acknowledgments

- `Ayyobee` for a bunch of online testing and suggestions.
- `Krampus` for the help with the new Rolling Giant model.
- `@Headcraps` for the [original Rolling Giant model](https://rigmodels.com/model.php?view=The_Rolling_Giant_[Tov3_Accurate]_3d_model__50038756bcfa4e3082bee7211dbd22a0)!

<br/>

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/B0B6R2Z9U)
