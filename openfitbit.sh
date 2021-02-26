#!/bin/sh
while true
do
  am start --user 0 -n com.fitbit.FitbitMobile/com.fitbit.FirstActivity
  am start --user 0 -n com.fitbit.FitbitMobile/com.fitbit.MainActivity
  sleep 30
done
