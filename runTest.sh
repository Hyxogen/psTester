# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    runTest.sh                                         :+:    :+:             #
#                                                      +:+                     #
#    By: dmeijer <dmeijer@student.codam.nl>           +#+                      #
#                                                    +#+                       #
#    Created: 2021/12/15 16:00:32 by dmeijer       #+#    #+#                  #
#    Updated: 2021/12/15 16:00:33 by dmeijer       ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

#!/bin/bash
clear

#Colors
BLACK="\033[0;30m"
RED="\033[0;31m"
GREEN="\033[0;32m"
ORANGE="\033[0;33m"
BLUE="\033[0;34m"
PURPLE="\033[0;35m"
CYAN="\033[0;36m"
LIGHT_GRAY="\033[0;37m"

DARK_GRAY="\033[1;30m"
LIGHT_RED="\033[1;31m"
LIGHT_GREEN="\033[1;32m"
YELLOW="\033[1;33m"
LIGHT_BLUE="\033[1;34m"
LIGHT_PURPLE="\033[1;35m"
LIGHT_CYAN="\033[1;36m"
WHITE="\033[1;37m"
RESET="\033[0m"

PUSH_SWAP_DIR="../"
OUT_FILE="deepthought"

BANNER="██████╗ ██╗   ██╗███████╗██╗  ██╗    ███████╗██╗    ██╗ █████╗ ██████╗ 
██╔══██╗██║   ██║██╔════╝██║  ██║    ██╔════╝██║    ██║██╔══██╗██╔══██╗
██████╔╝██║   ██║███████╗███████║    ███████╗██║ █╗ ██║███████║██████╔╝
██╔═══╝ ██║   ██║╚════██║██╔══██║    ╚════██║██║███╗██║██╔══██║██╔═══╝ 
██║     ╚██████╔╝███████║██║  ██║    ███████║╚███╔███╔╝██║  ██║██║     
╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝     
                                                                       
████████╗███████╗███████╗████████╗███████╗██████╗                      
╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗                     
   ██║   █████╗  ███████╗   ██║   █████╗  ██████╔╝                     
   ██║   ██╔══╝  ╚════██║   ██║   ██╔══╝  ██╔══██╗                     
   ██║   ███████╗███████║   ██║   ███████╗██║  ██║                     
   ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝                     
                                                                       "

FT_PRINTF_DIR="../"
FT_PRINTF_INCLUDE_DIR="${FT_PRINTF_DIR}/include"

WAIT="0"

echo -n > "$OUT_FILE"

SetColor() {
	printf "$1"
}

SetColor "$LIGHT_BLUE"
printf "$BANNER"
printf "by dmeijer"
sleep "$WAIT"
printf "\n"
SetColor "$LIGHT_GREEN"
printf "Building push_swap...	"
make -C "$PUSH_SWAP_DIR" fclean >> "$OUT_FILE"
make -C "$PUSH_SWAP_DIR" all >> "$OUT_FILE"
make -C "$PUSH_SWAP_DIR" bonus >> "$OUT_FILE"
SetColor "$GREEN"
printf "Done!\n"
SetColor "$RESET"