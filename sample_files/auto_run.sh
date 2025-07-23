#!/bin/bash

# runs mlb_graphical_standings and uses a different prompt depending on the day of the week.
# expects prompt_Mon.txt, prompt_Tue.txt, ... etcs to be in ~/.config/mlb-graphical-standings

# Get the current day of the week (e.g., Mon, Tue, Wed...)
day_of_week=$(date +%a)

/usr/bin/python3 -m mlb_graphical_standings.graphical_standings \
    -p ~/.config/mlb-graphical-standings/prompt_${day_of_week}.txt
