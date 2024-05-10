#!/bin/zsh

echo Killing current desktop portal instances...
sleep 1
killall -e xdg-desktop-portal-hyprland
killall xdg-desktop-portal
/usr/lib/xdg-desktop-portal-hyprland &
sleep 2
/usr/lib/xdg-desktop-portal &
echo Desktop portals restarted
