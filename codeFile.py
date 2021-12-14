from colorama import Fore

class Database:

	def __init__(self, loc):
		self.loc = loc

	def startupWindow(self):

		print("\n" * 8)
		print("\t" *4, end = "")
		print("<    " + Fore.YELLOW + "CENTRAL DATABASE OF XYZ CAMPUS" + Fore.RESET + "    >")


Data = Database("A")
Data.startupWindow()
