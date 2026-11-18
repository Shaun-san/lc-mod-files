# Changelog

## 1.7.2
- Added optional verbose logging of every RPC being sent.

## 1.7.0
- TZP voice pitch effect is now working with more than 4 players by using LethalPerformance API.
- A patch to MelaniesVoice to use voice group audio mixer, so TZP effect would apply to TTS.

## 1.6.0
- Added logging for RPCs sent on unspawned NetworkBehaviours and for deferred messages purged by Netcode.
- Added extra logging when a spawned NetworkObject is destroyed on a non-host client.
- Removed NoNagle override for Facepunch transport send types.

## 1.5.1
- README update (thanks Shaydelity)

## 1.5.0
- Add fix of softmask for mods that are using soft dependency resolving.

## 1.4.0
- Added ignore plugin loading list option.
- Added logging of SteamNetworkingSockets errors due to unable to send message.
- Added NoNagle to some RPC delivery flags.

## 1.3.0
- Added log and exception handler of null AudioSource in AudioReverbTrigger.

## 1.2.2
- Removed hotfix of JLL.

## 1.2.0
- Added hotfix for JLL item shop that prevented clients to buy items.
