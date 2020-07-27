import requests, json

class Robot:
	
	def __init__(self, name):
		self.name = name
		self.host = "http://" + self.name + "/api/v2.0.0/"
		self.header = {}
		
	def setHeader(self, auth):
		self.header["Content-Type"] = "application/json"
		self.header["Authorization"] = auth
		
	
	def getMissions(self):
		missionList = requests.get(self.host + "missions", headers = self.header)
		return missionList.json()
						
	def postMission(self, mission_id):
		mission = requests.post(self.host + "mission_queue/", json = mission_id, \
			headers = self.header)
		print(mission)
		
	def getStatus(self):
		status = requests.get(self.host + "status", headers = self.header)
		for key in status.json():
			print(key,status.json()[key])
			print("--"*20)
			
		return status.json()
			
	def putStatus(self, state):
		status = requests.put(self.host + "status", json = state, headers = self.header)
		print(status)
			
	def getMissionQueue(self):
		queue = requests.get(self.host + "mission_queue/", headers = self.header)
		return queue.json()
		
	def deleteMissionQueue(self):
		return requests.delete(self.host + "mission_queue/", headers = self.header)