#!/bin/sh

if [ ! -s /usr/share/games/fheroes2/data/HEROES2.AGG ]; then
	echo "You need to copy files from data and maps directories from original game"
	echo "into your /usr/share/games/fheroes2/{maps,data} directories respectively"
	exit 1;
fi


if [ ! -d "$HOME/.fheroes2" ]; then
	mkdir -p $HOME/.fheroes2/files/save

	ln -s /usr/share/games/fheroes2/data $HOME/.fheroes2/data
	ln -s /usr/share/games/fheroes2/maps $HOME/.fheroes2/maps
	
	for i in fonts images lang music sounds stats; do
		ln -s /usr/share/games/fheroes2/files/$i $HOME/.fheroes2/files/$i
	done

	cp /usr/share/games/fheroes2/fheroes2.cfg $HOME/.fheroes2/
fi

export FHEROES2_DATA=$HOME/.fheroes2
/usr/games/fheroes2.bin

