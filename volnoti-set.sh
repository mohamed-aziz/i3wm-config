#!/bin/bash
mute=`amixer -c 0 get Master | grep Mono | cut -d " " -f8`
vol=`amixer -c 0 get Master | grep Mono | cut -d " " -f6 | tr -d '[]' | tr -d '\n'`
if [ $mute == "[on]" ]
then
    volnoti-show $vol
else
    volnoti-show -m
fi
