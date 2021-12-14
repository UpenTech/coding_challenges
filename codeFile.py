from colorama import Fore

class Database:

	def __init__(self, loc):
		self.loc = loc

	def startupWindow(self):

		print("\n" * 8)
		print("\t" *4, end = "")
		print("<    " + Fore.YELLOW + "CENTRAL DATABASE OF XYZ CAMPUS" + Fore.RESET + "    >")
		print("\n" *2)
		print("\t" * 5, end = "")
		print("Secret Code: ", end = "\n" * 8)

Data = Database("A")
Data.startupWindow()
