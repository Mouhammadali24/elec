[app]
title = cablecalc
package.name = cablecalc
package.domain = org.mouhammad
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.2.1,kivymd
orientation = portrait
fullscreen = 0

# لو التطبيق يحتاج صلاحيات (مثال: إنترنت)
android.permissions = INTERNET

# لو عندك مجلدات إضافية للصور أو البيانات
# source.include_patterns = assets/*,images/*

[buildozer]
log_level = 2
warn_on_root = 1

# تحديد نسخة SDK و NDK لتفادي مشاكل التوافق
android.api = 33
android.ndk = 25b
android.arch = arm64-v8a