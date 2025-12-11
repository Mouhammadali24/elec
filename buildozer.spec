[app]
# اسم التطبيق الذي يظهر على الهاتف
title = Wire Diameter Calculator

# اسم الحزمة (package name)
package.name = wirecalc
package.domain = org.mohammad

# ملف البداية
source.dir = .
source.main = main.py

# أيقونة التطبيق (اختياري – ضع icon.png بجانب main.py)
icon.filename = icon.png

# المكتبات المطلوبة
requirements = python3,kivy,kivymd

# نسخة التطبيق
version = 0.1

# اتجاه الشاشة
orientation = portrait

# السماح باستخدام الإنترنت (اختياري)
android.permissions = INTERNET

# إعدادات أندرويد
android.api = 33
android.minapi = 21
android.ndk_path = /home/mou/.buildozer/android/platform/android-ndk-r25b
# لا تضع android.sdk = 33، اتركه فارغ أو ضع المسار إذا عندك SDK يدويًا

# اسم الحزمة النهائي
package = org.mohammad.wirecalc

# لغة واجهة المستخدم
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1