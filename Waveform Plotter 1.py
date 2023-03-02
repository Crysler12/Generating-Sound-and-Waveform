import math
import numpy
import time
import pygame
import matplotlib.pyplot as plt

pygame.init()
bits = 16
sample_rate = 44100
pygame.mixer.pre_init(sample_rate, bits)


def sine_x(amp, freq, time):
    return int(round(amp * math.sin(2 * math.pi * freq * time)))


class Tone:
    def sine(frequency, duration=1, speaker=None):
        
        num_samples = int(round(duration * sample_rate))

        
        buf = numpy.zeros((num_samples, 2), dtype=numpy.int16)
        amplitude = 2 ** (bits - 1) - 1

        for s in range(num_samples):
            t = float(s) / sample_rate    # time in seconds

            sine = sine_x(amplitude, frequency, t)

            
            if speaker == 'r':
                buf[s][1] = sine  # right
            elif speaker == 'l':
                buf[s][0] = sine  # left

            else:
                buf[s][0] = sine  # left
                buf[s][1] = sine  # right

        sound = pygame.sndarray.make_sound(buf)
        one_sec = 1000  # Milliseconds
        sound.play(loops=1, maxtime=int(duration * one_sec))
        time.sleep(duration)

    def plot(note_name, frequency, duration):
       
        num_samples = int(round(duration * sample_rate))
        buf = numpy.zeros((num_samples, 2), dtype=numpy.int16)
        amplitude = 2 ** (bits - 1) - 1
        t = numpy.arange(num_samples) / sample_rate

     
        waveform = amplitude * numpy.sin(2 * numpy.pi * frequency * t)

       
        plt.plot(t, waveform)
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.title(f'{note_name} ({frequency} Hz)')
        plt.show()

#Plotting the waveform of the chosen lyrics to show Frequncy Shift Keying
Tone.plot("G4", 392.00, 0.3)              #Well               #G4
Tone.plot("B4", 493.88, 0.3)              #I                  #B4
Tone.plot("A4", 440.00, 0.3)              #Found              #A4
Tone.plot("G4", 392.00, 0.3)              #The                #G4
Tone.plot("B4", 493.88, 1.2)              #Girl               #B4

Tone.plot("D5", 587.33, 0.6)              #Beau               #D5
Tone.plot("B4", 493.88, 0.3)              #ti                 #B4
Tone.plot("G4", 392.00, 0.5)              #ful                #G4
Tone.plot("G4", 392.00, 0.3)              #And                #G4               
Tone.plot("G4", 392.00, 0.6)              #Sweet              #G4  

Tone.plot("B4", 493.88, 0.3)              #Not                #B4
Tone.plot("A4", 440.00, 0.3)              #Know               #A4
Tone.plot("G4", 392.00, 0.3)              #wing               #G4
Tone.plot("B4", 493.88, 0.85)             #What               #B4
Tone.plot("B4", 493.88, 0.85)             #It                 #B4
Tone.plot("B4", 493.88, 0.85)             #was                #B4

Tone.plot("B4", 493.88, 0.3)              #Dar                #B4
Tone.plot("A4", 440.00, 0.3)              #ling               #A4
Tone.plot("G4", 392.00, 0.3)              #just               #G4
Tone.plot("B4", 493.88, 1.0)              #Kiss               #B4
Tone.plot("B4", 493.88, 1.0)              #Me                 #B4
Tone.plot("B4", 493.88, 1.0)              #Slow               #B4

Tone.plot("G4", 392.00, 0.3)              #With               #G4
Tone.plot("D5", 587.33, 0.7)              #You                #D5
Tone.plot("B5", 523.25, 0.3)              #Bet                #C5
Tone.plot("B4", 493.88, 0.7)              #Ween               #B4
Tone.plot("A4", 440.00, 0.3)              #my                 #A4
Tone.plot("G4", 392.00, 1.2)              #arms               #G4