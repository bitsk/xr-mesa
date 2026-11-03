# Independent XR Mesa adaptation

The default source commit contains the A081 render/display ownership patch on its recorded upstream base. Optional workarounds in optional-patches are preserved separately and are not enabled by packaging.

`dpkg-buildpackage -us -uc -b` builds only the MSM Turnip Vulkan driver. Libraries and ICD manifests are installed in a private multiarch xr-mesa directory. A session selects the manifest with VK_DRIVER_FILES for an ordinary user process; the default system ICD directories remain unchanged.

This packaging requires an adequate target-distribution Mesa build environment. Source availability, package build, ABI closure, display enumeration and actual presentation are separate validation stages. Prepared source retains genuine upstream ancestry; this repository versions the maintained patch series and packaging.
