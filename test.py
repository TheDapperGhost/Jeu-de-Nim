'''import pyaudio
import wave

filename = 'myfile.wav'

# Set chunk size of 1024 samples per data frame
chunk = 1024  

# Open the sound file 
wf = wave.open(filename, 'rb')

# Create an interface to PortAudio
p = pyaudio.PyAudio()

# Open a .Stream object to write the WAV file to
# 'output = True' indicates that the sound will be played rather than recorded
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

# Read data in chunks
data = wf.readframes(chunk)

# Play the sound by writing the audio data to the stream
while data != '':
    stream.write(data)
    data = wf.readframes(chunk)

# Close and terminate the stream
stream.close()
p.terminate()'''
import os

print(os.name)
'''


from term_image.image import from_file
image = from_file("allumette.ico")
print(image, image , sep="")  # Affiche l'image dans le terminal
image.draw()  # Affiche l'image dans le terminal
'''
#from image import DrawImage

#image = DrawImage.from_file("./allumette.ico")
#image.draw_image()

print("\ud83d\udd6f\ufe0f")