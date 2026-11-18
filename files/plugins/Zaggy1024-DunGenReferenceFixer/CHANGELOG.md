## Version 0.0.2
Use TypeForwardedTo instead of a MonoMod native hook to redirect to the new DunGen assembly. This method allows MonoMod to fix other mods' scripting assemblies, as well as the assets previously fixed by the native hook.

The engine calling the native hook from multiple threads at once could also cause crashes, which this avoids.

## Version 0.0.1
Initial version.
