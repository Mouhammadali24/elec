[app]
title = CircleCalc
package.name = elec
package.domain = org.mouhammadali24
version = 1.0.0

source.dir = .
source.include_exts = py,kv,png,jpg,ttf
requirements = python3,kivy==2.3.0,kivymd

orientation = portrait
fullscreen = 0

android.api = 33
android.ndk = 25b
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
android.build_tools_version = 33.0.2

icon.filename = icon.png
presplash.filename = splash.png
presplash.keep_ratio = 1
presplash_color = white

[buildozer]
log_level = 2
warn_on_root = 1
