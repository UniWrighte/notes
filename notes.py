import random

notes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# Notes are: C, C#/D♭, D, D#/E♭, E, F, F#/G♭, G, G#/A♭, A, A#/B♭, B

def randomSong(size):
	song = []
	for i in range(size):
		index = random.randint(0, len(notes) - 1)
		song.append(notes[index])
	return song

song = randomSong(30)
print(song)