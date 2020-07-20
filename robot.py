import requests, json

class Robot:
	
	def __init__(self):
		self.name = input("What is the ip of the Robot")
		self.host = "http://" + self.name + "/api/v2.0.0/"
		self.header = {}
		
	def setHeader(self):
		header["Content-Type"] = "application/json"
		header["Authorization"] = input("Enter Authorization code.")
	
	def getMissions(self):
		self.missionList = requests.get(self.host + "missions", headers = self.header)
			
	def printMissions(self):
		for line in self.missionList.json():
			print(line)