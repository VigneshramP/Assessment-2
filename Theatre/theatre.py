import csv
import json

seatsReq = 0
movie = []
currentData = []
ticketPrice = 0
showTimeSeats = []

def checkForAns(ans):
	answer = ans.lower()
	if answer =="yes":
		return 1
	elif answer == "no":
		return 0
	else:
		print "\nEnter Yes or No\n"
		main()

def updateJson():
	defaultSeat = showTimeSeats["AvailableSeats"] - seatsReq
	showTimeSeats["AvailableSeats"] = defaultSeat 
	print showTimeSeats["AvailableSeats"]
	with open("current_movies.json","w") as f:
		json.dump(currentData,f)
	inFile = open("current_movies.json","r")
	outFile = open("Today.csv","w")
	writer = csv.writer(outFile)
	count = 0
	for row in json.loads(inFile.read()):
		if count == 0:
			header = row.keys()
			writer.writerow(header)
			count += 1
		writer.writerow(row.values())		

class Movie:
	
	def getJsonData(self,fileName):
		try:
			with open(fileName,'r') as f:
	  			json_currentData = f.read()
	  		obj = json.loads(json_currentData)
	  		return obj
	  	
	  	except IOError as err:
	  		print "File Open Error",err
	  		

	def getMovies(self):
		print "\n<===== MOVIES RUNNING NOW =====>\n"
		global currentData
		currentData = self.getJsonData('current_movies.json')
		for movieSerialNum, results in enumerate(currentData):
			print " {} {}\n".format(movieSerialNum + 1,results["name"])
		return movieSerialNum

newMovie = Movie()

class TicketBooking(Movie):

	def checkForSeats(self,noOfSeat):
		if seatsReq <= noOfSeat:
			self.checkOut()
		else:
			print "\n  Sorry no tickets available\n" 
			self.gotoStart()

	def gotoStart(self):
		ans = raw_input("\nWish to continue?\tYes or No\n\n")
		self.displayMovies() if (checkForAns(ans)) else  "\n<===== THANK YOU FOR USING TICKET NEW =====>"	
	
	def printTicket(self):
		print "\nHere is your ticket:"
		print "\nMovie Name: {}".format(movie['name'])
		print "\nShow Time: {}".format(json.dumps(showTimeSeats["AvailableSeats"]))
		print "\nNumber of seats booked: {}".format(seatsReq)
		print "\nTotal Amount: {} INR".format(ticketPrice)
		print "\n<===== SEATS ARE COFORMED =====>\n"
		updateJson()

	def conformBooking(self):
		ans = raw_input("\nAre you SURE?\tYes or No\n\n")
		self.printTicket() if (checkForAns(ans)) else self.gotoStart()

	def payForTicket(self):
		ans = raw_input("\nProceed to payment?\tYes or No\n\n")
		if (checkForAns(ans)):
			self.conformBooking()
		else:
			ans = raw_input("\nCancel the plan?\tYes or No\n\n")
			self.gotoStart() if (checkForAns(ans)) else self.checkOut()

	def checkOut(self):
		print"\nSelect Class:\n"
		print "\n1.First Class: {} INR".format(movie['first'])
		print "\n2.Second Class: {} INR".format(movie['second'])
		print "\n3.Third Class: {} INR".format(movie['third'])
		selectClass = int(input("\nWhich class?\n"))
		global ticketPrice
		if selectClass == 1:
			ticketPrice = movie['first'] * seatsReq
			print "Total Ticket Price ====> {} INR".format(ticketPrice)
		elif selectClass == 2:
			ticketPrice = movie['second'] * seatsReq
			print "Total Ticket Price ====> {} INR".format(ticketPrice)
		else:
			ticketPrice = movie['third'] * seatsReq
			print "\nTotal Ticket Price ====> {} INR".format(ticketPrice)
		self.payForTicket()

	def startBooking(self,ans):
		global seatsReq
		global showTimeSeats
		showTimeSeats = movie['showDetails'][ans]
		print "\nMovie Name: {}".format(movie['name'])
		print "\nShow Time: {}".format(json.dumps(showTimeSeats["ShowTime"]))
		print "\nAvailableSeats: {}".format(json.dumps(showTimeSeats["AvailableSeats"]))
		seatsReq = int(input("\nEnter the number of seats: \n"))
		noOfSeat = json.dumps(showTimeSeats["AvailableSeats"])
		self.checkForSeats(noOfSeat)

	def displayShowDetails(self):
		print "\nMovie Name: {}".format(movie['name'])
		print "\nDescription: {}".format(movie['description'])
		print "\nTheatre: {}".format(movie['Theatre'])
		for showNum in movie["showDetails"]:
			print "\n<===== {} =====>".format(json.dumps(showNum))	
		ans = int(input("\nEnter show\t0 or 1?\nIf Availbale show is Single Please Enter '0'\n"))
		self.startBooking(ans) if (ans <= 1) else self.gotoStart()				
	
	def initiateBooking(self,ans,movieSNum):
		if (checkForAns(ans)):
		 	movieNum = int(input("\nEnter the movie number: \n\n")-1)
		 	if movieNum > movieSNum:
		 		print "\nEnter correct movie number"
		 	else:
				global movie
				movie = currentData[movieNum]
				self.displayShowDetails()		

newTicket = TicketBooking()

def main():
	print "<====== WECOME TO TICKET NEW ======>\n"
	ans = raw_input("Do you want to book?\tYes or No\n\n")
	if (checkForAns(ans) == 1):
		movieSerialNum = newMovie.getMovies()
		newTicket.initiateBooking(ans,movieSerialNum)
	else :
		print " <======'THANKS FOR CHOOSING'======>\n"
		exit()	
	
if __name__ == '__main__':
	main()