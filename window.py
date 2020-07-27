import tkinter as tk
from robot import Robot

class Window:
	def __init__(self):
		
		ip, auth = self.readFILE()
		ip = ip.rstrip('\n')
		
		self.master = tk.Tk()
		self.master.title("MiR Controller")
		self.master.geometry("500x500")
		self.master.config(background = "white")
		
		self.tb1 = tk.Text(self.master, bd = 0)
		self.tb1.insert(tk.END,"-"*23 + "Connect to Robot" + "-"*23)
		self.tb1.config(state = tk.DISABLED)
		self.tb1.place(x = 0, y = 0)
		
		self.connect = tk.Button(self.master, text = "connect", command = self.connect)
		self.connect.place(x = 400, y = 35)
		
		self.host = tk.Entry(self.master, bd = 2)
		self.host.insert(0,ip)
		self.host.place(x = 160, y = 30)
		
		self.auth = tk.Entry(self.master, width = 40, bd = 2)
		self.auth.insert(0,auth)
		self.auth.place(x = 100, y = 55)
			
		self.runButton = None
		self.missionList = None
		self.playButton = None
		self.pauseButton = None
	
	def readFILE(self):
		FILE = open("address.txt", 'r+')
		codes = FILE.readlines()
		FILE.close()
		return codes
	
	def writeFILE(self, name, auth):
		FILE = open("address.txt", 'w+')
		FILE.writelines([name, "\n", auth])
		FILE.close()
		
	
	def connect(self):
		name = self.host.get()
		auth = self.auth.get()
		self.writeFILE(name, auth)
		self.robot = Robot(name)
		self.robot.setHeader(auth)
		#self.missionQueue = self.robot.getMissionQueue()
		#self.last = len(self.missionQueue)
		#print(self.missionQueue[self.last])

		print("Connecting to Robot at " + name)
		self.update()
		
	def start(self):
		tk.mainloop()
		
	def missions(self):
		#self.getMissions = self.robot.getMissions()
		self.getMissions = ["One", "Two", "Three"]
		self.missionList = tk.Listbox(self.master,selectmode = tk.SINGLE, \
		yscrollcommand = True, height = 5, width = 40)
		self.missionList.place(x = 10, y = 115)
		
		self.dic = {}
		
		for i in range(len(self.getMissions)):
			item = self.getMissions[i]
			#self.dic[item['name']] = i
			self.missionList.insert(tk.END, item)

	def status(self):
		#status = self.robot.getStatus()
		#missionQueue = self.robot.getMissionQueue()
		missionQueue = [10,11,12]
		self.last = 1
		
		#self.statusText.config(state = tk.NORMAL)
		#self.statusText.insert(tk.END, "Battery Percentage: " + status["battery_percentage"])
		#self.statusText.config(state = tk.DISABLED)
		
		newMissions = missionQueue[self.last:]
		var = tk.StringVar()
		newMissionQueue = tk.Label(self.master, textvariable = var, width = 30, height = 10, anchor = tk.N)
		message = "Mission Queue:\n"
		for item in newMissions:
			message += str(item) + "\n"
			
		
		newMissionQueue.place(x = 248, y = 260)
		var.set(message)
		
		
		
	def run(self):
		self.selected = self.missionList.get(self.missionList.curselection())
		missionID = {"mission_id" : self.getMissions[self.dic[self.selected]]['guid']}
		self.robot.postMission(missionID)
		
	def pause(self):
		self.pauseButton.config(state = tk.DISABLED)
		self.playButton.config(state = tk.NORMAL)
		self.robot.putStatus({"state_id": 4})
		print("Pause")
		
	def play(self):
		self.playButton.config(state = tk.DISABLED)
		self.pauseButton.config(state = tk.NORMAL)
		self.robot.putStatus({"state_id": 3})
		print("Play")
		
	def delete(self):
		self.robot.deleteMissionQueue()
		
		
	def update(self):
		if self.runButton == None:
			self.vline = tk.Text(self.master, width = 1, bd = 0)
			self.vline.insert(tk.END,"|"*20)
			self.vline.config(state = tk.DISABLED)
			
			self.hline = tk.Text(self.master, bd = 0, height = 1)
			self.hline.insert(tk.END, "-"*23+ "Mission Control" + "-"* 24)
			self.hline.config(state = tk.DISABLED)
			self.hline.place(x = 0, y = 80)
			
			self.hline2 = tk.Text(self.master, bd =0, height = 1)
			self.hline2.insert(tk.END, "-"*25 + "Robot Status" + "-"*25)
			self.hline2.config(state = tk.DISABLED)
			self.hline2.place(x = 0, y = 220)
			
			self.hline3 = tk.Text(self.master, bd =0, height = 1)
			self.hline3.insert(tk.END, "-"*11 + "Battery" + "-"*11)
			self.hline3.config(state = tk.DISABLED)
			self.hline3.place(x = 0, y = 320)
			
			self.playButton = tk.Button(self.master, text = "Play", command = self.play)
			self.playButton.place(x = 430, y = 140)
			
			self.pauseButton = tk.Button(self.master, text = "Pause", command = self.pause)
			self.pauseButton.place(x = 385, y = 140)
			
			self.runButton = tk.Button(self.master, text = "Send Mission", command = self.run)
			self.runButton.place(x = 300, y = 140)
			
			self.deleteButton = tk.Button(self.master, text = "Delete Queue", command = self.delete)
			
			self.deleteButton.place(x = 120, y = 270)
			
			self.statusButton = tk.Button(self.master, text = "Update Status", command = self.status)
			self.statusButton.place(x = 20, y = 270)
			
			self.statusText = tk.Text(self.master, bd = 0)
			self.statusText.config(state = tk.DISABLED)
		if self.missionList == None:
			self.missions()
		
		