from colors import bcolors
class hands:
    rock=f"""{bcolors.RED}


   _________
  |   |  |  \__
  /¨¨¨¨===  |  |
 /    ___/__|__|
|    /         |
 \____ROCK_____/ {bcolors.DEFAULT}"""

    paper=f"""{bcolors.YELLOW}
    __ __ __
   |  |  |  |__
   |¨¨|¨¨|¨¨|  |
__ |¨¨|¨¨|¨¨|¨¨|
\ \|  |  |  |¨¨|
|  \__         |
|              |
 \____PAPER____/{bcolors.DEFAULT}"""

    scissor=f"""{bcolors.CYAN}
 __       __
 \  \   /  /
  \  \ /  /
   \  V  /__ __
  /¨¨¨¨===  |  |
 /    ___/__|__|
|    /         |
 \__SCISSORS___/{bcolors.DEFAULT}"""

class start:
   splash=f"""
                    Welcome to{bcolors.RED}
          ___           ___           ___     
         /\  \         /\  \         /\  \    
        /::\  \       /::\  \       /::\  \   
       /:/\:\  \     /:/\:\  \     /:/\ \  \  
      /::\~\:\  \   /::\~\:\  \   _\:\ ~\ \  \ 
     /:/\:\ \:\__\ /:/\:\ \:\__\ /\ \:\ \ \__\.
     \/_|::\/:/  / \/__\:\/:/  / \:\ \:\ \/__/
        |:|::/  /       \::/  /   \:\ \:\__\  
        |:|\/__/         \/__/     \:\/:/  /  
        |:|  |                      \::/  /   
         \|__|                       \/__/    
{bcolors.GREEN}To begin playing, press either (R)ock, (P)aper or (S)cissors{bcolors.DEFAULT}
                To quit press Q"""