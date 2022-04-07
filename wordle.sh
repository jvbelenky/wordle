#!/bin/bash

# read the green letters and their positions
echo Enter the green letters, separated by spaces. If you have none, press enter.
read green_read
if [[ $green_read != "" ]] ; 
   then
      echo Enter the green letters\' positions separated by spaces, with the first position in the word being 1
      read green_pos_read
      green_pos=$green_pos_read
   else
      green_pos=""
fi
green=$(echo "$green_read" | tr '[:lower:]' '[:upper:]')

# read the yellow letters and their positions
echo Enter the yellow letters, separated by spaces. If you have none, press enter.
read yellow_read
if [[ $yellow_read != "" ]] ; 
   then
      IFS=" " read -a yellow_letters <<< $yellow_read
      for i in "${yellow_letters[@]}"
          do echo Enter the possible positions of $i separated by spaces, with the first position in the word being 1
          read pos
          yellow_write=$(echo "${yellow_write[@]} -yp $pos") 
          yellow_show=$(echo "${yellow_show[@]} $pos ;") 
	  done
      yellow_show=${yellow_show%?}
   else
      yellow_show=" "
      yellow_write=" "
fi

yellow=$(echo "$yellow_read" | tr '[:lower:]' '[:upper:]')


# read the unguessed letters
echo Enter all the letters you haven\'t guessed yet.
read white
#sort alphabetically; convert to uppercase; remove duplicates
white=$(echo "$white" | grep -o . | sort |tr -d "\n" | tr '[:lower:]' '[:upper:]' | tr -s 'A-Z' | sed "s/[^A-Z]*//g")" "

echo Known green letters: $green\; known positions: $green_pos 
echo Known yellow letters: $yellow\; possible positions: $yellow_show #${yellow_pos[@]}
echo Unguessed: $white
echo Is this correct? y/n

read confirmation

if [[ $confirmation = "y" ]] ;
  then
    #launch python script here
    python main.py --green $green --green-position $green_pos --yellow $yellow $yellow_write --unguessed $white
elif [[ $confirmation = "n" || $confirmation = "" ]] ;
  then
    echo "Aborting" 
else
    echo Is this correct? y/n
    read confirmation
fi