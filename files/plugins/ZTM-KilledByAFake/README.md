# KilledByAFake

You heard your friend calling for help. You followed the voice. It wasn't them.

With [Coroner](https://thunderstore.io/c/lethal-company/p/EliteMasterEric/Coroner/), the
performance report tells you a Masked got you. With **KilledByAFake**, it tells you
*which friend it was pretending to be*:

```
Notes:
* Was killed by a fake Bob.
```

## What it does

When a Masked enemy kills a player, this mod checks who that Masked was imitating —
voice via [Mirage](https://thunderstore.io/c/lethal-company/p/qwbarch/Mirage/), suit and
appearance via Mirage's visual copying or the vanilla mask-conversion — and rewrites
Coroner's cause of death on the performance report with the impostor's identity.

- Works for naturally spawned Masked (Mirage picks who they imitate).
- Works for Masked created by the Comedy/Tragedy mask: victims see
  *"Was killed by a fake \<whoever put the mask on\>."*
- If the Masked wasn't imitating anyone, Coroner's normal messages are left untouched.
- Respects Coroner's config: if cause-of-death display is disabled, nothing is shown.

## Requirements

- [Coroner](https://thunderstore.io/c/lethal-company/p/EliteMasterEric/Coroner/) (hard requirement)
- [Mirage](https://thunderstore.io/c/lethal-company/p/qwbarch/Mirage/) (this is where the fun comes from)

Install on all clients — everyone should run the same mods anyway.

## How it works (for the curious)

Two small Harmony patches: one on `MaskedPlayerEnemy.FinishKillAnimation` records which
player the Masked was mimicking at the moment of the kill (read from Mirage's synced
`MimicPlayer` component via reflection, falling back to the vanilla `mimickingPlayer`
field), and one on `HUDManager.FillEndGameStats` runs after Coroner writes the report
and replaces its Masked death line with the personalized one. No extra netcode — the
kill animation is already synced, so every client records the name locally.

## Credits

- [EliteMasterEric](https://thunderstore.io/c/lethal-company/p/EliteMasterEric/) for Coroner and its modding API.
- [qwbarch](https://thunderstore.io/c/lethal-company/p/qwbarch/) for Mirage.
- Built by **Zacca** (ZTM).
