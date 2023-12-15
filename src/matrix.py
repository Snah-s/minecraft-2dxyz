from colorama import Back, Style, init

init(autoreset=True)

void = Back.WHITE + "    " + Style.RESET_ALL
white = Back.WHITE + "    " + Style.RESET_ALL
black = Back.BLACK + "    " + Style.RESET_ALL
green = Back.GREEN + "    " + Style.RESET_ALL
yellow = Back.YELLOW + "    " + Style.RESET_ALL
red = Back.RED + "    " + Style.RESET_ALL
blue = Back.BLUE + "    " + Style.RESET_ALL
lightblack = Back.LIGHTBLACK_EX + "    " + Style.RESET_ALL
cyan = Back.CYAN + "    " + Style.RESET_ALL
magenta = Back.MAGENTA + "    " + Style.RESET_ALL

def create_matrix():
  matrix = [[void for j in range(42)] for i in range(21)]
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if j == 0:
        matrix[i][j] = str(i)
      if i == 0:
        matrix[i][j] = str(j)
  matrix[0][0] = '    '
  return matrix