class Theatre(object):
    def __init__(self, theatreName):
        self.__theatreName = theatreName

    def setTheatreName(self, TheatreName):
        self.__theatreName = TheatreName        

    def getTheatreName(self):
        return self.__theatreName 


class Movie(object):

    def __init__(self, movieName, show, theatre):        
        self.__movieName = movieName
        self.__show = show
        self.__theatre = theatre

    def setMovieName(self, moviename):
        self.__movieName = moviename   

    def getMovieName(self):            
        return self.__movieName       

    def setShow(self, Show):
        self.__show = Show         

    def getShow(self):
        return  self.__show  

    def getThreatre(self):
        return self.__theatre 

class Show(object):

    def __init__(self, show, seat, price):
        self.__show = show
        self.__seat = seat
        self.__price = price

    def setShowTime(self, Show):
        self.__show = Show
        
    def getShowTime(self):
        return self.__show

    def setSeat(self, Seat):
        self.__seat = Seat

    def getSeat(self):
        return self.__seat 

    def setPrice(self, Price):
        self.__price = Price
       
    def getPrice(self):
        return self.__price
                  
