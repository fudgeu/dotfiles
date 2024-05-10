if [[ $1 == "up" ]]; then
	wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%+ -l 1.0
	echo $((($(wpctl get-volume @DEFAULT_AUDIO_SINK@ | cut -c 9-) * 100) | 0)) >> /tmp/wobpipe
elif [[ $1 == "down" ]]; then
	wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%- -l 0.0
	echo $((($(wpctl get-volume @DEFAULT_AUDIO_SINK@ | cut -c 9-) * 100) | 0)) >> /tmp/wobpipe
else
	echo "Unknown argument: $1. Valid options are: up, down"
fi
