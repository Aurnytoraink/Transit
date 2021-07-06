# ⚠️ THIS IS A STILL AT ALPHA STAGE ⚠️

<h1 align="center">
  <img src="data/icons/logo/com.github.Aurnytoraink.Transit.svg" alt="Transit" width="192" height="192"/><br>
  <p style="font-size: small;">(I need a icon)</p>
  Transit
</h1>

<p align="center"><strong>Get schedules for trains, buses, subways, etc.</strong></p>

<br>


## 🧪 Features

**TODO**

## 🏗️ Building from source

### GNOME Builder
GNOME Builder is the environment used for developing this application. 
It can use Flatpak manifests to create a consistent building and running 
environment cross-distro. Thus, it is highly recommended you use it.

1. Download [GNOME Builder](https://flathub.org/apps/details/org.gnome.Builder).
2. In Builder, click the "Clone Repository" button at the bottom, using `https://github.com/Aurnytoraink/Transit.git` as the URL.
3. Click the build button at the top once the project is loaded.

### Meson
```
git clone https://github.com/Aurnytoraink/Transit.git
cd Transit
meson builddir --prefix=/usr/local
ninja -C builddir install
```
