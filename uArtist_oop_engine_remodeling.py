import random

class Song:
#class Song, gets the name of the user as only argument
#has methods that randomly generates song key and tempo	
	def __init__(self, userName):
		self.userName = userName
	
	def song_key(self):
		
		diatonic = ['C', 'D', 'E', 'F','G', 'A', 'B']
		accidents = ['#', '']
		majorMinor = ['', 'm']
			
		diaKey = diatonic[random.randint(0, 6)]
		songAcc = accidents[random.randint(0, 1)] 
		majminState = majorMinor[random.randint(0, 1)]
			
		if diaKey == 'E':
			key = diaKey+majminState
		elif diaKey == 'B':	
			key = diaKey+majminState
		else:
			key = diaKey+songAcc+majminState
				  
		return key
	
	def song_bpm(self):

		bpms = [90, 95, 100, 105, 110, 115, 120, 125]
		
		bpmRoulette = bpms[random.randint(0, len(bpms)-1)]
		bpm = str(bpmRoulette)
		
		return bpm	

class Stems:

	def __init__(self, key, bpm):
		self.key = key
		self.bpm = bpm
	
userChoices = ['manuela', '12/12/2004', 0, 1, 1, 1,]

userSong = Song(userChoices[0])		
print('Song Key is: '+userSong.song_key())
print('Song bpm is: '+userSong.song_bpm())

userStems = Stems(userSong.song_key(), userSong.song_bpm())

print(userStems.key)
print(userStems.bpm)		
	
