import unittest
from theatre import checkForAns
from theatre import newTicket
from theatre import newMovie

class theatreTest(unittest.Testcase):
	
	def testCheckForAns(self):
		result = checkForAns("YES")
		self.assertEqual(result,1)

	def test_checkForAns(self):
		result = checkForAns("yes")
		self.assertEqual (result,1)

	def test_CheckForAns(self):
		result = checkForAns("no")
		self.assertEqual(result,0)

	def test_Check_ForAns(self):
		result = checkForAns("no")
		self.assertNotEqual(result,1)
	
	def testcheckforAns(self):
		result = checkForAns("yes")
		self.assertTrue(result,1)

	def testcheck_for_Ans(self):
		result = checkForAns("no")
		self.assertFalse(result,1)

	def testNewMovie(self):
		result = newMovie.getMovie("yes")
		assertEqual(result,("yes",3))

	def test_new_Movie(self):
		result = newMovie.getMovie()
		assertTrue(result,3)

	def test_New_Movie(self):
		result = newMovie.getMovie()
		assertNotEqual(result,2)

	def testnewmovie(self):
		result = newMovie.getMovie()
		assertFalse(result,2)

	def testJsonData(self):
		result = newMovie.getJsonData('/home/linuxuser/Desktop/test.json')
		excepted = """[{"showDetails": [{"ShowTime": "10:00am", "AvailableSeats": 48}, {"ShowTime": "18:00pm", "AvailableSeats": 47}]"""
		self.assertEqual(result,excepted)


	def test_Json_data(self):
		result = newMovie.getJsonData('/home/linuxuser/Desktop/test.json')
		excepted = """[{"showDetails": [{"ShowTime": "10:00am", "AvailableSeats": 48}, {"ShowTime": "18:00pm", "AvailableSeats": 47}]"""
		self.assertNotEqual(result,excepted)

	def test_Json_Data(self):
		result = newMovie.getJsonData('/home/linuxuser/Desktop/test.json')
		excepted = """[{"showDetails": [{"ShowTime": "10:00am", "AvailableSeats": 48}, {"ShowTime": "18:00pm", "AvailableSeats": 47}]"""
		self.assertTrue(result,excepted)

	def testJson_Data(self):
		result = newMovie.getJsonData('/home/linuxuser/Desktop/test.json')
		excepted = """[{"showDetails": [{"ShowTime": "10:00am", "AvailableSeats": 48}, {"ShowTime": "18:00pm", "AvailableSeats": 47}]"""
		self.assertFalse(result,excepted)	

		
if __name__ == '__main__':
	unittest.main()
