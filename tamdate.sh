#!/bin/bash

# tamdate.sh - echoes the date in the Tamrielic calendar
# Calendar information from http://www.uesp.net/wiki/Lore:Calendar

usage() {
        echo Usage: tamdate.sh [options]
        echo Options:
        echo   -m = include Tamrielic month
        echo   -d = include Tamrielic weekday
        echo   -h = include Tamrielic holiday, if applicable
        echo   -D \<date\> = use \<date\>, syntax: %u %m %d \(see strftime\(3\)\)
        echo   -? = display help
        echo Default is to include everything and use today\'s date.
}

while getopts mdhD:? opt; do
        case $opt in
                m)
                        INCTAMMONTH=yes
                        OPTSGIVEN=yes
                        ;;
                d)
                        INCTAMWEEKDAY=yes
                        OPTSGIVEN=yes
                        ;;
                h)
                        INCHOLIDAY=yes
                        OPTSGIVEN=yes
                        ;;
                D)
                        DATESTR=$OPTARG
                        ;;
                ?)
                        usage
                        exit
                        ;;
        esac
done
# defaults
if [[ -z $OPTSGIVEN ]]; then
        INCTAMMONTH=yes
        INCTAMWEEKDAY=yes
        INCHOLIDAY=yes
fi

if [[ -z $DATESTR ]]; then
        DATESTR=$(date +"%u %m %d")
fi
WEEKDAY=$(echo $DATESTR | cut -f 1 -d " ")
MONTH=$(echo $DATESTR | cut -f 2 -d " ")
DAY=$(echo $DATESTR | cut -f 3 -d " ")
DAY=${DAY#0} # chop off any leading zero

# Convert weekday
if [[ -n $INCTAMWEEKDAY ]]; then
        TW=( Sundas Morndas Tirdas Middas Turdas Fredas Loredas )
        if [[ $WEEKDAY == "7" ]]; then
                WEEKDAY=0
        fi
        TAMWEEKDAY=${TW[$WEEKDAY]}
fi

# Convert month
if [[ -n $INCTAMMONTH ]]; then
        TM=( "Morning Star" "Sun's Dawn" "First Seed" "Rain's Hand"
                "Second Seed" Midyear "Sun's Height" "Last Seed"
                Hearthfire Frostfall "Sun's Dusk" "Evening Star" )
        MONTH=$(($MONTH - 1));
        TAMMONTH=${TM[$MONTH]}
fi

if [[ -n $INCTAMWEEKDAY ]]; then
        echo -n $TAMWEEKDAY
        if [[ -n $INCTAMMONTH ]]; then
                echo -n " "
        fi
fi
if [[ -n $INCTAMMONTH ]]; then
        echo -n $TAMMONTH
fi
echo " $DAY"

if [[ -z $INCHOLIDAY ]]; then
        exit 0
fi

# Look for a holiday
declare -a HS
case $MONTH in
0)  # January
        HS[1]="New Life Festival; Clavicus Vile's Summoning Day"
        HS[2]="Scour Day"
        HS[12]="Ovank'a"
        HS[13]="Meridia's Summoning Day"
        HS[15]="South Winds Prayer"
        HS[16]="Day of Lights"
        HS[18]="Waking Day"
        ;;
1)
        HS[2]="Mad Pelagius; Sheogorath's Summoning Day"
        HS[5]="Othroktide"
        HS[8]="Day of Release"
        HS[13]="Feast of the Dead"
        HS[16]="Heart's Day; Sanguine's Summoning Day"
        HS[27]="Perserverance Day"
        HS[28]="Aduros Nau"
        ;;
2)
        HS[5]="Hermaeus Mora's Summoning Day"
        HS[7]="First Planting"
        HS[9]="Day of Waiting"
        HS[21]="Hogithum; Azura's Summoning Day"
        HS[25]="Flower Day"
        HS[26]="Festival of Blades"
        ;;
3)
        HS[1]=Gardtide
        HS[9]="Peryite's Summoning Day"
        HS[13]="Day of the Dead"
        HS[20]="Day of Shame"
        HS[28]="Jester's Day"
        ;;
4)
        HS[7]="Second Planting"
        HS[9]="Marukh's Day; Namira's Summoning Day"
        HS[20]="Fire Festival"
        HS[30]="Fishing Day"
        ;;
5)
        HS[1]="Drigh R'Zimb"
        HS[5]="Hircine's Summoning Day"
        HS[16]="Mid Year Celebration"
        HS[23]="Dancing Day"
        HS[24]=Tibedetha
        ;;
6)
        HS[10]="Merchants Festival; Vaernima's Summoning Day"
        HS[12]="Divad Etep't"
        HS[20]="Sun's Rest"
        HS[29]="Fiery Night"
        ;;
7)
        HS[2]="Maiden Katrica"
        HS[11]="Koomu Alezer'i"
        HS[14]="Feast of the Tiger"
        HS[21]="Appreciation Day"
        HS[27]="Harvest's End"
        ;;
8)
        HS[3]="Tales and Tallows"
        HS[6]=Khurat
        HS[8]="Nocturnal's Summoning Day"
        HS[12]=Riglametha
        HS[19]="Children's Day"
        ;;
9)
        HS[5]="Dirij Tereur"
        HS[8]="Malacath's Summoning Day"
        HS[13]="Witches Festival; Mephala's Summoning Day"
        HS[23]="Broken Diamonds"
        HS[30]="Emperor's Day"
        ;;
10)
        HS[2]="Gauntlet; Boethiah's Summoning Day"
        HS[3]="Serpent's Dance"
        HS[8]="Moon Festival"
        HS[18]="Hel Anseilak"
        HS[20]="Warriors Festival; Mehrunes Dagon's Summoning Day"
        ;;
11)
        HS[15]="North Winds Prayer"
        HS[18]="Baranth Do"
        HS[20]="Chil'a; Molag Bal's Summoning Day"
        HS[25]=Saturalia
        HS[31]="Old Life Festival"
        ;;
esac
HOLIDAY=${HS[$DAY]}

if [[ -n $HOLIDAY ]]; then
        echo $HOLIDAY
fi
