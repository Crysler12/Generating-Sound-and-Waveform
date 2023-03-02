import pygame
import numpy
import math
import time


pygame.init()


bits = 16       #Change this to 13, para tolerable sa max volume
sample_rate = 44100
pygame.mixer.pre_init(sample_rate, bits)


def sine_x(amp, freq, time):
    return int(round(amp * math.sin(2 * math.pi * freq * time)))


class Tone:
    def sine(freq, duration=1, speaker=None):


        num_samples =  int(round(duration * sample_rate))


        sound_buffer = numpy.zeros((num_samples, 2), dtype = numpy.int16)
        amplitude = 2 ** (bits - 1) - 1


        for sample_num in range(num_samples):
            timeF = float(sample_num) / sample_rate


            sine = sine_x(amplitude, freq, timeF)


            if speaker == 'r':
                sound_buffer[sample_num][1] = sine
            if speaker == 'l':
                sound_buffer[sample_num][0] = sine


            else:
                sound_buffer[sample_num][1] = sine
                sound_buffer[sample_num][0] = sine


        sound = pygame.sndarray.make_sound(sound_buffer)
        sound.play(loops=1, maxtime=int(duration * 1000))
        time.sleep(duration)




#Frequency_Codes [Tone.Sine(freq,duration)]  #Lyrics             #Piano_Notes    
Tone.sine(293.66, duration=0.3)              #I                  #D4          
Tone.sine(329.63, duration=0.3)              #Found              #E4  
Tone.sine(392.00, duration=0.3)              #The                #G4
Tone.sine(392.00, duration=1.2)              #Love               #G4
time.sleep(0.5)


Tone.sine(493.88, duration=0.4)              #Fo                 #B4
Tone.sine(440.00, duration=0.2)              #o                  #A4
Tone.sine(392.00, duration=0.4)              #or                 #G4
Tone.sine(493.88, duration=1.25)             #Me                 #B4
time.sleep(0.5)


Tone.sine(440.00, duration=0.3)              #Dar                #A4
Tone.sine(493.88, duration=0.3)              #ling               #B4
Tone.sine(493.88, duration=0.3)              #just               #B4
Tone.sine(440.00, duration=0.35)             #di                 #A4
Tone.sine(392.00, duration=0.3)              #ive right          #G4
Tone.sine(392.00, duration=1.00)             #in                 #G4
time.sleep(0.5)


Tone.sine(392.00, duration=0.3)              #And                #G4
Tone.sine(392.00, duration=0.3)              #Fol                #G4
Tone.sine(440.00, duration=0.3)              #low                #A4
Tone.sine(493.88, duration=0.3)              #my                 #B4
Tone.sine(440.00, duration=1.3)              #Lead               #A4
time.sleep(0.5)


Tone.sine(392.00, duration=0.3)              #Well               #G4
Tone.sine(493.88, duration=0.3)              #I                  #B4
Tone.sine(440.00, duration=0.3)              #Found              #A4
Tone.sine(392.00, duration=0.3)              #The                #G4
Tone.sine(493.88, duration=1.2)              #Girl               #B4
time.sleep(0.5)


Tone.sine(587.33, duration=0.6)              #Beau               #D5
Tone.sine(493.88, duration=0.3)              #ti                 #B4
Tone.sine(392.00, duration=0.5)              #ful                #G4
Tone.sine(392.00, duration=0.3)              #And                #G4
Tone.sine(392.00, duration=0.6)              #Sweet              #G4
time.sleep(0.5)


Tone.sine(392.00, duration=0.3)              #Oh,                #G4
Tone.sine(392.00, duration=0.3)              #I                  #G4
Tone.sine(440.00, duration=0.3)              #Ne                 #A4
Tone.sine(493.88, duration=0.3)              #ver                #B4
Tone.sine(523.25, duration=0.7)              #Knew               #C5
Tone.sine(523.25, duration=0.3)              #you                #C5
Tone.sine(493.88, duration=0.7)              #Were               #B4
Tone.sine(440.00, duration=0.3)              #The                #A4
Tone.sine(440.00, duration=0.3)              #Some               #A4
Tone.sine(392.00, duration=0.6)              #One                #G4
Tone.sine(392.00, duration=0.3)              #Wait               #G4
Tone.sine(440.00, duration=0.3)              #ting               #A4
Tone.sine(493.88, duration=0.3)              #for                #B4
Tone.sine(440.00, duration=1.2)              #me                 #A4
time.sleep(0.1)


Tone.sine(392.00, duration=0.3)              #Cause              #G4
Tone.sine(587.33, duration=0.3)              #We                 #D4
Tone.sine(587.33, duration=0.3)              #were               #D4
Tone.sine(587.33, duration=0.3)              #Just               #D4
Tone.sine(659.25, duration=0.3)              #Kids               #E4
Tone.sine(493.88, duration=0.3)              #when               #B4
Tone.sine(440.00, duration=0.3)              #We                 #A4
Tone.sine(493.88, duration=0.85)             #Fell               #B4
Tone.sine(493.88, duration=0.85)             #In                 #B4                
Tone.sine(493.88, duration=0.85)             #Love               #B4
time.sleep(0.1)


Tone.sine(493.88, duration=0.3)              #Not                #B4
Tone.sine(440.00, duration=0.3)              #Know               #A4
Tone.sine(392.00, duration=0.3)              #wing               #G4
Tone.sine(493.88, duration=0.85)             #What               #B4
Tone.sine(493.88, duration=0.85)             #It                 #B4
Tone.sine(493.88, duration=0.85)             #was                #B4
time.sleep(0.1)


Tone.sine(493.88, duration=0.3)              #I                  #B4
Tone.sine(440.00, duration=0.3)              #will               #A4
Tone.sine(392.00, duration=0.3)              #not                #G4
Tone.sine(523.25, duration=1.0)              #Give               #C5
Tone.sine(493.88, duration=1.0)              #You                #B4
Tone.sine(392.00, duration=1.0)              #Up                 #G4
Tone.sine(293.66, duration=1.0)              #this               #D4
Tone.sine(493.88, duration=1.2)              #Ti                 #B4
Tone.sine(523.25, duration=0.3)              #I                  #C5
Tone.sine(493.88, duration=0.3)              #I                  #B4
Tone.sine(440.00, duration=1.0)              #ime                #A4
time.sleep(0.1)


Tone.sine(493.88, duration=0.3)              #Dar                #B4
Tone.sine(440.00, duration=0.3)              #ling               #A4
Tone.sine(392.00, duration=0.3)              #just               #G4
Tone.sine(493.88, duration=1.0)              #Kiss               #B4
Tone.sine(493.88, duration=1.0)              #Me                 #B4
Tone.sine(493.88, duration=1.0)              #Slow               #B4


Tone.sine(493.88, duration=0.3)              #Your               #B4
Tone.sine(440.00, duration=0.3)              #Heart              #A4
Tone.sine(392.00, duration=0.3)              #is                 #G4
Tone.sine(493.88, duration=1.0)              #All                #B4
Tone.sine(493.88, duration=1.0)              #I                  #B4
Tone.sine(493.88, duration=1.0)              #Own                #B4


Tone.sine(493.88, duration=0.3)              #And                #B4
Tone.sine(440.00, duration=0.3)              #In                 #A4
Tone.sine(392.00, duration=0.3)              #Your               #G4
Tone.sine(523.25, duration=1.0)              #Eyes               #C5
Tone.sine(493.88, duration=1.0)              #Your               #B4
Tone.sine(392.00, duration=1.0)              #Hold               #G4
Tone.sine(293.66, duration=0.6)              #ding               #D4
Tone.sine(440.00, duration=1.5)              #Mine               #A4
time.sleep(0.4)  


Tone.sine(587.33, duration=1.0)              #Ba                 #D5
Tone.sine(493.88, duration=0.3)              #By                 #B4
Tone.sine(440.00, duration=0.3)              #y                  #A4
Tone.sine(392.00, duration=0.3)              #y                  #G4
Tone.sine(392.00, duration=1.5)              #I                  #G4
time.sleep(0.4)  
                                               
Tone.sine(783.99, duration=0.7)              #Dan                #G5
Tone.sine(739.99, duration=0.3)              #Cing               #f#5
Tone.sine(659.25, duration=0.7)              #In                 #E5
Tone.sine(587.33, duration=0.3)              #The                #D5
Tone.sine(493.88, duration=1.4)              #Dark               #B4
time.sleep(0.4)


Tone.sine(392.00, duration=0.3)              #With               #G4
Tone.sine(587.33, duration=0.7)              #You                #D5
Tone.sine(523.25, duration=0.3)              #Bet                #C5
Tone.sine(493.88, duration=0.7)              #Ween               #B4
Tone.sine(440.00, duration=0.3)              #my                 #A4
Tone.sine(392.00, duration=1.2)              #arms               #G4
time.sleep(0.4)  


Tone.sine(783.99, duration=0.7)              #Bare               #G5
Tone.sine(739.99, duration=0.3)              #foot               #f#5
Tone.sine(659.25, duration=0.7)              #on                 #E5
Tone.sine(392.00, duration=0.3)              #the                #G4
Tone.sine(493.88, duration=1.5)              #Grass              #B4
time.sleep(0.4)


Tone.sine(587.33, duration=0.3)              #Lis                #D5
Tone.sine(587.33, duration=0.3)              #ten                #D5
Tone.sine(587.33, duration=0.3)              #ning               #D5
Tone.sine(587.33, duration=0.7)              #to                 #D5
Tone.sine(659.25, duration=0.3)              #our                #E5
Tone.sine(493.88, duration=0.3)              #fav(o)             #B4
Tone.sine(440.00, duration=0.3)              #(o)rite            #A4
Tone.sine(392.00, duration=0.3)              #song               #G4
time.sleep(0.4)


Tone.sine(493.88, duration=0.3)              #When               #B4
Tone.sine(587.33, duration=0.3)              #you                #D5
Tone.sine(783.99, duration=0.7)              #said               #G5
Tone.sine(739.99, duration=0.3)              #you                #f#5
Tone.sine(659.25, duration=0.7)              #look               #E5
Tone.sine(739.99, duration=0.3)              #a                  #f#5
Tone.sine(493.88, duration=1.0)              #mess               #B4


Tone.sine(392.00, duration=0.32)             #I                  #G4
Tone.sine(440.00, duration=0.32)             #whis               #A4
Tone.sine(493.88, duration=0.32)             #pered              #B4
Tone.sine(587.33, duration=0.7)              #un                 #D5
Tone.sine(523.25, duration=0.3)              #der                #C5
Tone.sine(493.88, duration=0.7)              #neath              #B4
Tone.sine(523.25, duration=0.3)              #my                 #C5
Tone.sine(493.88, duration=0.8)              #breath             #B4


Tone.sine(392.00, duration=0.3)              #But                #G4
Tone.sine(440.00, duration=0.9)              #you                #A4
Tone.sine(523.25, duration=1.1)              #heard              #C5
Tone.sine(493.88, duration=0.3)              #it                 #B4


Tone.sine(392.00, duration=0.3)              #Dar                #G4
Tone.sine(440.00, duration=0.3)              #ling               #A4
Tone.sine(493.88, duration=1.0)              #you                #B4
Tone.sine(440.00, duration=1.0)              #look               #A4
time.sleep(0.1)


Tone.sine(440.00, duration=1.0)              #per                #A4
Tone.sine(392.00, duration=0.7)              #fect               #G4
Tone.sine(392.00, duration=0.3)              #to                 #G4
Tone.sine(392.00, duration=0.6)              #night              #G4
time.sleep(0.1)


Tone.sine(246.94, duration=0.3)              #outro              #B3
Tone.sine(293.66, duration=0.3)                                  #D4
Tone.sine(440.00, duration=0.3)                                  #A4
Tone.sine(293.66, duration=0.3)                                  #D4
Tone.sine(440.00, duration=0.3)                                  #A4
Tone.sine(392.00, duration=0.3)                                  #G4
Tone.sine(246.94, duration=0.3)                                  #B4
Tone.sine(392.00, duration=0.3)                                  #G4
Tone.sine(369.99, duration=0.3)                                  #F#4
Tone.sine(220.00, duration=0.3)                                  #A3
Tone.sine(369.99, duration=0.3)                                  #F#4
Tone.sine(329.63, duration=0.9)                                  #E4
Tone.sine(329.63, duration=0.3)                                  #E4
Tone.sine(369.99, duration=0.3)                                  #F#4
Tone.sine(392.00, duration=0.3)                                  #G4
Tone.sine(392.00, duration=0.9)                                  #G4
Tone.sine(369.99, duration=0.9)                                  #F#4
Tone.sine(392.00, duration=1.2)                                  #G4
