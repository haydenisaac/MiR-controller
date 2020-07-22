import tkinter as tk
from robot import Robot

class Window:
	def __init__(self):
		self.master = tk.Tk()
		
		self.master.title("MiR Controller")
		self.master.geometry("500x500")
		self.connect = tk.Button(self.master, text = "connect", command = self.connect)
		self.connect.pack()
		self.host = tk.Entry(self.master)
		self.host.insert(0,"Enter your IP")
		self.host.pack()
			
		self.runButton = None
		self.missionList = None
		
	def connect(self):
		self.name = self.host.get()
		if self.name == "Enter your IP":
			print("Put in a valid IP address")
		else:
			self.robot = Robot(self.name)
			self.robot.setHeader()
			print("Connecting to Robot at " + self.name)
			self.update()
		
	def start(self):
		tk.mainloop()
		
	def missions(self):
		self.getMissions = self.robot.getMissions()
		self.missionList = tk.Listbox(self.master,selectmode = tk.SINGLE, \
		yscrollcommand = True, height = 5, width = 40)
		self.missionList.pack()
		
		self.dic = {}
		
		for i in range(len(self.getMissions)):
			item = self.getMissions[i]
			self.dic[item['name']] = i
			self.missionList.insert(tk.END, item['name'])

	def status(self):
		self.robot.getStatus()
		
	def run(self):
		self.selected = self.missionList.get(self.missionList.curselection())
		missionID = {"mission_id" : self.getMissions[self.dic[self.selected]]['guid']}
		self.robot.postMission(missionID)
		
	def update(self):
		if self.runButton == None:
			self.runButton = tk.Button(self.master, text = "Run", command = self.run)
			self.runButton.pack()
			self.statusButton = tk.Button(self.master, text = "Status", command = self.status)
			self.statusButton.pack()
		if self.missionList == None:
			self.missions()
		
		