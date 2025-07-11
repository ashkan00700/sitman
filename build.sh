#!/usr/bin/env bash
# نصب وابستگی‌ها
pip install -r requirements.txt

# اجرای migrate برای دیتابیس
python manage.py migrate

# جمع‌آوری static files برای سرویس‌دهی در production
python manage.py collectstatic --noinput
