from classes import Theatre,Movie,Show

# List to store all the theatres 
theatres = []
# List to store all the movies 
movies = []

def createTheatres():
  athreatre = Theatre('Sathyam')
  bthreatre = Theatre('Luxe - Mini')
  theatres.append(athreatre)
  theatres.append(bthreatre)
  return athreatre,bthreatre

def createShows():
  showMrg = Show("10.00 AM", 50, 300)
  showAft = Show("14.00 PM", 50, 400)
  showEven = Show("18.00 PM", 50, 500)
  show = [showMrg,showAft,showEven]

  newshowMrg = Show("10.00 AM", 25, 300)
  newshowAft = Show("15.00 PM", 25, 400)
  newshowEven = Show("18.30 AM", 25, 500)
  newshow = [newshowMrg,newshowAft,newshowEven]    
  return show, newshow

def createMovies(athreatre,bthreatre,show,newshow):
  movie = Movie("Avengers - Endgame", show, athreatre)
  newMovie = Movie("STAR WARS - THE RISE IF SKYWALKER", newshow, bthreatre) 
  movies.append(movie)
  movies.append(newMovie) 

         
def listTheatres():
  print"<===== Theatre List =====>\n"
  for theatre_idx,theatre_val in enumerate(theatres):
    print"{}{}{}".format(theatre_idx+1, '.', theatre_val.getTheatreName(),)

def bookTickets(movie):
  show = int(input("Please Select show : "))       
  if show <= len(movie.getShow()):   
    ticket = int(input("\nHow Many Seats are Required\n"))
    show = movie.getShow()[show-1]
    movieSeat = int(show.getSeat())-ticket
    if movieSeat >= 0:
      show.setSeat(movieSeat) 
      print "Total Ticket Value\n",int(show.getPrice()) * ticket
      threatreName = movie.getThreatre()
      print(threatreName.getTheatreName() + " " + "- Threatre")
      print(movie.getMovieName() + " " + "Movie")
      print"{} ".format(ticket) ,"Seats Are Booked !!!"

    elif movieSeat == 0:
      print("Seats are not available")      
    else:
      print("Seats are not available") 
  else:
    print("Please Check Your Input")    

def listShows():
  theatre = int(input("Select threatre: "))
  movie = movies[theatre-1]  
  print(movie.getMovieName())
  for show in movie.getShow():
    print(show.getShowTime() + " - Show " + str(show.getSeat()) + " - Seats " + str(show.getPrice()) + " - Price ")     
  bookTickets(movie) 
    
def listMovies():
    print('\n<===== Movies List =====>\n')
    for movie_idx,movie_val in enumerate(movies):
        print("{}{}{}".format(movie_idx + 1, '.', movie_val.getMovieName(), ))

def getChoice():
    choice =int (input("\nSelect Your Choice\n1. Theatres List \n2. Book Tickets\n3. Movies List\n"))
    return choice
 
def main():
  print "\n<===== WELCOME =====>\n" 
  athreatre,bthreatre = createTheatres()
  show, newshow = createShows()
  createMovies(athreatre,bthreatre,show,newshow)
  while True:
    try:
      userChoice = getChoice()          
      if userChoice == 1:
          listTheatres()
      elif userChoice == 2:
          listTheatres()
          listShows()
      elif userChoice == 3:
          listMovies()
      else:
          print('Please Check!!!')
    
    except (SyntaxError, ValueError):   
      print("You ! Are Not Given Input!!!") 

if __name__ == "__main__":
    main()