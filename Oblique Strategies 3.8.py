# Oblique Strategies Version 3.8

import random
from itertools import permutations
from midiutil import MIDIFile

# Define Root

OneOctave={"A":0,"A#/Bb":1,"B":2,"C":3,"C#/Db":4,"D":5,"D#/Eb":6,
            "E":7,"F":8,"F#/Gb":9,"G":10,"G#/Ab":11}

for key in OneOctave:
    transpose=OneOctave[key]
    
root,transpose=random.choice(list(OneOctave.items()))
pool=list(OneOctave.keys())+list(OneOctave.keys())

# Define Scale Object

class Scale:
    def __init__(self,mode,notes,steps,color):
        self.mode=mode
        self.notes=notes
        self.steps=steps
        self.color=color
        
modes=[]

# DIATONIC MODES OF MAJOR SCALE

for r in ["Ionian"]:
    Scale.mode=str(r)
    IonianSteps=[0,2,4,5,7,9,11]
    Ionian=[]
    for j in IonianSteps:
        note=pool[j+transpose]
        Ionian.append(note)
    Scale.notes=Ionian
    c1=Ionian[2];c2=Ionian[6];c3=Ionian[5]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),Ionian,7,color)
    modes.append(mode)

for r in ["Dorian"]:
    Scale.mode=str(r)
    DorianSteps=[0,2,3,5,7,9,10]
    Dorian=[]
    for j in DorianSteps:
        note=pool[j+transpose]
        Dorian.append(note)
    Scale.notes=Dorian
    c1=Dorian[5];c2=Dorian[2];c3=Dorian[6]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),Dorian,7,color)
    modes.append(mode)

for r in ["Phrygian"]:
    Scale.mode=str(r)
    PhrygianSteps=[0,1,3,5,7,8,10]
    Phrygian=[]
    for j in PhrygianSteps:
        note=pool[j+transpose]
        Phrygian.append(note)
    Scale.notes=Phrygian
    c1=Phrygian[1];c2=Phrygian[2];c3=Phrygian[6]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),Phrygian,7,color)
    modes.append(mode)

for r in ["Lydian"]:
    Scale.mode=str(r)
    LydianSteps=[0,2,4,6,7,9,11]
    Lydian=[]
    for j in LydianSteps:
        note=pool[j+transpose]
        Lydian.append(note)
    Scale.notes=Lydian
    c1=Lydian[3];c2=Lydian[2];c3=Lydian[6]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),Lydian,7,color)
    modes.append(mode)

for r in ["Mixolydian"]:
    Scale.mode=str(r)
    MixolydianSteps=[0,2,4,5,7,9,10]
    Mixolydian=[]
    for j in MixolydianSteps:
        note=pool[j+transpose]
        Mixolydian.append(note)
    Scale.notes=Mixolydian
    c1=Mixolydian[6];c2=Mixolydian[2];c3=Mixolydian[5]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),Mixolydian,7,color)
    modes.append(mode)

for r in ["Aeolian"]:
    Scale.mode=str(r)
    AeolianSteps=[0,2,3,5,7,8,10]
    Aeolian=[]
    for j in AeolianSteps:
        note=pool[j+transpose]
        Aeolian.append(note)
    Scale.notes=Aeolian
    c1=Aeolian[5];c2=Aeolian[2];c3=Aeolian[6]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),Aeolian,7,color)
    modes.append(mode)

for r in ["Locrian"]:
    Scale.mode=str(r)
    LocrianSteps=[0,1,3,5,6,8,10]
    Locrian=[]
    for j in LocrianSteps:
        note=pool[j+transpose]
        Locrian.append(note)
    Scale.notes=Locrian
    c1=Locrian[1];c2=Locrian[4];c3=Locrian[2]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),Locrian,7,color)
    modes.append(mode)

# DIATONIC MODES OF HARMONIC MAJOR

for r in ["Harmonic Major"]:
    Scale.mode=str(r)
    HarmonicMajorSteps=[0,2,4,5,7,8,11]
    HarmonicMajor=[]
    for j in HarmonicMajorSteps:
        note=pool[j+transpose]
        HarmonicMajor.append(note)
    Scale.notes=HarmonicMajor
    c1=HarmonicMajor[5];c2=HarmonicMajor[6];c3=HarmonicMajor[2]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),HarmonicMajor,7,color)
    modes.append(mode)

for r in ["Dorian b5"]:
    Scale.mode=str(r)
    Dorianb5Steps=[0,2,3,5,6,9,10]
    Dorianb5=[]
    for j in Dorianb5Steps:
        note=pool[j+transpose]
        Dorianb5.append(note)
    Scale.notes=Dorianb5
    c1=Dorianb5[5];c2=Dorianb5[4];c3=Dorianb5[2]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),Dorianb5,7,color)
    modes.append(mode)

for r in ["Phrygian b4"]:
    Scale.mode=str(r)
    Phrygianb4Steps=[0,1,3,4,7,8,10]
    Phrygianb4=[]
    for j in Phrygianb4Steps:
        note=pool[j+transpose]
        Phrygianb4.append(note)
    Scale.notes=Phrygianb4
    c1=Phrygianb4[1];c2=Phrygianb4[3];c3=Phrygianb4[2]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),Phrygianb4,7,color)
    modes.append(mode)

for r in ["Lydian b3"]:
    Scale.mode=str(r)
    Lydianb3Steps=[0,2,3,6,7,9,11]
    Lydianb3=[]
    for j in Lydianb3Steps:
        note=pool[j+transpose]
        Lydianb3.append(note)
    Scale.notes=Lydianb3
    c1=Lydianb3[3];c2=Lydianb3[2];c3=Lydianb3[6]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),Lydianb3,7,color)
    modes.append(mode)

for r in ["Mixolydian b2"]:
    Scale.mode=str(r)
    Mixolydianb2Steps=[0,1,4,5,7,9,10]
    Mixolydianb2=[]
    for j in Mixolydianb2Steps:
        note=pool[j+transpose]
        Mixolydianb2.append(note)
    Scale.notes=Mixolydianb2
    c1=Mixolydianb2[6];c2=Mixolydian[1];c3=Mixolydian[2]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),Mixolydianb2,7,color)
    modes.append(mode)

for r in ["Lydian Augmented #2"]:
    Scale.mode=str(r)
    LydianAug2Steps=[0,3,4,6,8,9,11]
    LydianAug2=[]
    for j in LydianAug2Steps:
        note=pool[j+transpose]
        LydianAug2.append(note)
    Scale.notes=LydianAug2
    c1=LydianAug2[3];c2=LydianAug2[1];c3=LydianAug2[2]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),LydianAug2,7,color)
    modes.append(mode)

for r in ["Locrian bb7"]:
    Scale.mode=str(r)
    Locrianbb7Steps=[0,1,3,5,6,8,9]
    Locrianbb7=[]
    for j in Locrianbb7Steps:
        note=pool[j+transpose]
        Locrianbb7.append(note)
    Scale.notes=Locrianbb7
    c1=Locrianbb7[1];c2=Locrianbb7[6];c3=Locrianbb7[4]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),Locrianbb7,7,color)
    modes.append(mode)

# DIATONIC MODES OF MELODIC MINOR SCALE

for r in ["Melodic Minor"]:
    Scale.mode=str(r)
    MelodicMinorSteps=[0,2,3,5,7,9,11]
    MelodicMinor=[]
    for j in MelodicMinorSteps:
        note=pool[j+transpose]
        MelodicMinor.append(note)
    Scale.notes=MelodicMinor
    c1=MelodicMinor[2];c2=MelodicMinor[6];c3=MelodicMinor[5]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),MelodicMinor,7,color)
    modes.append(mode)

for r in ["Dorian b2/Assyrian"]:
    Scale.mode=str(r)
    AssyrianSteps=[0,1,3,5,7,9,10]
    Assyrian=[]
    for j in AssyrianSteps:
        note=pool[j+transpose]
        Assyrian.append(note)
    Scale.notes=Assyrian
    c1=Assyrian[5];c2=Assyrian[1];c3=Assyrian[2]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),Assyrian,7,color)
    modes.append(mode)

for r in ["Lydian Augmented/Asgardian"]:
    Scale.mode=str(r)
    AsgardianSteps=[0,2,4,6,8,9,11]
    Asgardian=[]
    for j in AsgardianSteps:
        note=pool[j+transpose]
        Asgardian.append(note)
    Scale.notes=Asgardian
    c1=Asgardian[3];c2=Asgardian[4];c3=Asgardian[2]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),Asgardian,7,color)
    modes.append(mode)

for r in ["Lydian Dominant"]:
    Scale.mode=str(r)
    LydianDominantSteps=[0,2,4,6,7,9,10]
    LydianDominant=[]
    for j in LydianDominantSteps:
        note=pool[j+transpose]
        LydianDominant.append(note)
    Scale.notes=LydianDominant
    c1=LydianDominant[3];c2=LydianDominant[6];c3=LydianDominant[2]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),LydianDominant,7,color)
    modes.append(mode)

for r in ["Aeolian Dominant/Mixolydian b6"]:
    Scale.mode=str(r)
    Mixolydianb6Steps=[0,2,4,5,7,8,10]
    Mixolydianb6=[]
    for j in Mixolydianb6Steps:
        note=pool[j+transpose]
        Mixolydianb6.append(note)
    Scale.notes=Mixolydianb6
    c1=Mixolydianb6[6];c2=Mixolydianb6[5];c3=Mixolydianb6[2]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),Mixolydianb6,7,color)
    modes.append(mode)

for r in ["Half-Diminished/Sisyphean"]:
    Scale.mode=str(r)
    HalfDimSteps=[0,2,3,5,6,8,10]
    HalfDiminished=[]
    for j in HalfDimSteps:
        note=pool[j+transpose]
        HalfDiminished.append(note)
    Scale.notes=HalfDiminished
    c1=HalfDiminished[4];c2=HalfDiminished[2];c3=HalfDiminished[6]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),HalfDiminished,7,color)
    modes.append(mode)

for r in ["Altered Dominant/Palamidian"]:
    Scale.mode=str(r)
    AltDomSteps=[0,1,3,4,6,8,10]
    Altered=[]
    for j in AltDomSteps:
        note=pool[j+transpose]
        Altered.append(note)
    Scale.notes=Altered
    c1=Altered[6];c2=Altered[2];c3=Altered[3]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),Altered,7,color)
    modes.append(mode)

# DIATONIC MODES OF HARMONIC MINOR

for r in ["Harmonic Minor"]:
    Scale.mode=str(r)
    HarmonicMinorSteps=[0,2,3,5,7,8,11]
    HarmonicMinor=[]
    for j in HarmonicMinorSteps:
        note=pool[j+transpose]
        HarmonicMinor.append(note)
    Scale.notes=HarmonicMinor
    c1=HarmonicMinor[5];c2=HarmonicMinor[6];c3=HarmonicMinor[2]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),HarmonicMinor,7,color)
    modes.append(mode)

for r in ["Locrian #6"]:
    Scale.mode=str(r)
    LocrianAug6Steps=[0,1,3,5,6,9,10]
    LocrianAug6=[]
    for j in LocrianAug6Steps:
        note=pool[j+transpose]
        LocrianAug6.append(note)
    Scale.notes=LocrianAug6
    c1=LocrianAug6[5];c2=LocrianAug6[1];c3=LocrianAug6[4]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),LocrianAug6,7,color)
    modes.append(mode)

for r in ["Ionian #5"]:
    Scale.mode=str(r)
    IonianAugSteps=[0,2,4,5,8,9,11]
    IonianAugmented=[]
    for j in IonianAugSteps:
        note=pool[j+transpose]
        IonianAugmented.append(note)
    Scale.notes=IonianAugmented
    c1=IonianAugmented[4];c2=IonianAugmented[2];c3=IonianAugmented[6]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),IonianAugmented,7,color)
    modes.append(mode)

for r in ["Ukrainian Dorian/Romanian Minor"]:
    Scale.mode=str(r)
    UkrainianDorianSteps=[0,2,3,6,7,9,10]
    UkrainianDorian=[]
    for j in UkrainianDorianSteps:
        note=pool[j+transpose]
        UkrainianDorian.append(note)
    Scale.notes=UkrainianDorian
    c1=UkrainianDorian[5];c2=UkrainianDorian[3];c3=UkrainianDorian[6]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),UkrainianDorian,7,color)
    modes.append(mode)

for r in ["Phrygian Dominant"]:
    Scale.mode=str(r)
    PhrygianDominantSteps=[0,1,4,5,7,8,10]
    PhrygianDominant=[]
    for j in PhrygianDominantSteps:
        note=pool[j+transpose]
        PhrygianDominant.append(note)
    Scale.notes=PhrygianDominant
    c1=PhrygianDominant[1];c2=PhrygianDominant[2];c3=PhrygianDominant[6]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),PhrygianDominant,7,color)
    modes.append(mode)

for r in ["Lydian #2/Maqam Mustar"]:
    Scale.mode=str(r)
    LydianPlus2Steps=[0,3,4,6,7,9,11]
    LydianPlus2=[]
    for j in LydianPlus2Steps:
        note=pool[j+transpose]
        LydianPlus2.append(note)
    Scale.notes=LydianPlus2
    c1=LydianPlus2[3];c2=LydianPlus2[1];c3=LydianPlus2[6]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),LydianPlus2,7,color)
    modes.append(mode)

for r in ["Altered Diminished"]:
    Scale.mode=str(r)
    AltDimSteps=[0,1,3,4,6,8,9]
    AlteredDiminished=[]
    for j in AltDimSteps:
        note=pool[j+transpose]
        AlteredDiminished.append(note)
    Scale.notes=AlteredDiminished
    c1=AlteredDiminished[6];c2=AlteredDiminished[2]
    c3=AlteredDiminished[3]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),AlteredDiminished,7,color)
    modes.append(mode)

# DIATONIC MODES OF DOUBLE HARMONIC MAJOR

for r in ["Double Harmonic Major/Byzantine"]:
    Scale.mode=str(r)
    DoubleHarmonicMajorSteps=[0,1,4,5,7,8,11]
    DoubleHarmonicMajor=[]
    for j in DoubleHarmonicMajorSteps:
        note=pool[j+transpose]
        DoubleHarmonicMajor.append(note)
    Scale.notes=DoubleHarmonicMajor
    c1=DoubleHarmonicMajor[1];c2=DoubleHarmonicMajor[2]
    c3=DoubleHarmonicMajor[6]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),DoubleHarmonicMajor,7,color)
    modes.append(mode)

for r in ["Lydian #2#6"]:
    Scale.mode=str(r)
    Lydian26Steps=[0,3,4,6,7,10,11]
    Lydian26=[]
    for j in Lydian26Steps:
        note=pool[j+transpose]
        Lydian26.append(note)
    Scale.notes=Lydian26
    c1=Lydian26[3];c2=Lydian26[5];c3=Lydian26[1]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),Lydian26,7,color)
    modes.append(mode)

for r in ["Ultraphrygian"]:
    Scale.mode=str(r)
    UltraphrygianSteps=[0,1,3,4,7,8,9]
    Ultraphrygian=[]
    for j in UltraphrygianSteps:
        note=pool[j+transpose]
        Ultraphrygian.append(note)
    Scale.notes=Ultraphrygian
    c1=Ultraphrygian[1];c2=Ultraphrygian[6];c3=Ultraphrygian[2]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),Ultraphrygian,7,color)
    modes.append(mode)

for r in ["Hungarian Gypsy Minor"]:
    Scale.mode=str(r)
    HungarianGypsyMinorSteps=[0,2,3,6,7,8,11]
    HungarianGypsyMinor=[]
    for j in HungarianGypsyMinorSteps:
        note=pool[j+transpose]
        HungarianGypsyMinor.append(note)
    Scale.notes=HungarianGypsyMinor
    c1=HungarianGypsyMinor[2];c2=HungarianGypsyMinor[6]
    c3=HungarianGypsyMinor[3]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),HungarianGypsyMinor,7,color)
    modes.append(mode)

for r in ["Oriental"]:
    Scale.mode=str(r)
    OrientalSteps=[0,1,4,5,6,9,10]
    Oriental=[]
    for j in OrientalSteps:
        note=pool[j+transpose]
        Oriental.append(note)
    Scale.notes=Oriental
    c1=Oriental[1];c2=Oriental[2];c3=Oriental[3]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),Oriental,7,color)
    modes.append(mode)

for r in ["Ionian #2#5"]:
    Scale.mode=str(r)
    IonianAug2Steps=[0,3,4,5,8,9,11]
    IonianAug2=[]
    for j in IonianAug2Steps:
        note=pool[j+transpose]
        IonianAug2.append(note)
    Scale.notes=IonianAug2
    c1=IonianAug2[4];c2=IonianAug2[1];c3=IonianAug2[2]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),IonianAug2,7,color)
    modes.append(mode)

for r in ["Locrian bb3bb7"]:
    Scale.mode=str(r)
    Locrianbb3bb7Steps=[0,1,2,5,6,8,9]
    Locrianbb3bb7=[]
    for j in Locrianbb3bb7Steps:
        note=pool[j+transpose]
        Locrianbb3bb7.append(note)
    Scale.notes=Locrianbb3bb7
    c1=Locrianbb3bb7[2];c2=Locrianbb3bb7[6]
    c3=Locrianbb3bb7[1]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),Locrianbb3bb7,7,color)
    modes.append(mode)

# PENTATONIC SCALES

for r in ["Pentatonic Minor/Celtic Amara"]:
    Scale.mode=str(r)
    AmaraSteps=[0,3,5,7,10]
    Amara=[]
    for j in AmaraSteps:
        note=pool[j+transpose]
        Amara.append(note)
    Scale.notes=Amara
    c1=Amara[1];c2=Amara[4];c3=Amara[3]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=5
    mode=Scale(str(r),Amara,5,color)
    modes.append(mode)

for r in ["Pentatonic Major/Yona Nuki Major"]:
    Scale.mode=str(r)
    PentatonicMajorSteps=[0,2,4,7,9]
    PentatonicMajor=[]
    for j in PentatonicMajorSteps:
        note=pool[j+transpose]
        PentatonicMajor.append(note)
    Scale.notes=PentatonicMajor
    c1=PentatonicMajor[2];c2=PentatonicMajor[4]
    c3=PentatonicMajor[3]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=5
    mode=Scale(str(r),PentatonicMajor,5,color)
    modes.append(mode)

for r in ["Altered Pentatonic"]:
    Scale.mode=str(r)
    AltPentatonicSteps=[0,3,5,7,9]
    AlteredPentatonic=[]
    for j in AltPentatonicSteps:
        note=pool[j+transpose]
        AlteredPentatonic.append(note)
    Scale.notes=AlteredPentatonic
    c1=AlteredPentatonic[2];c2=AlteredPentatonic[4]
    c3=AlteredPentatonic[3]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=5
    mode=Scale(str(r),AlteredPentatonic,5,color)
    modes.append(mode)

for r in ["Yona Nuki Minor"]:
    Scale.mode=str(r)
    YonaNukiMinorSteps=[0,2,3,5,8]
    YonaNukiMinor=[]
    for j in YonaNukiMinorSteps:
        note=pool[j+transpose]
        YonaNukiMinor.append(note)
    Scale.notes=YonaNukiMinor
    c1=YonaNukiMinor[2];c2=YonaNukiMinor[4]
    c3=YonaNukiMinor[1]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=5
    mode=Scale(str(r),YonaNukiMinor,5,color)
    modes.append(mode)

for r in ["Hirajoshi"]:
    Scale.mode=str(r)
    HirajoshiSteps=[0,2,3,7,8]
    Hirajoshi=[]
    for j in HirajoshiSteps:
        note=pool[j+transpose]
        Hirajoshi.append(note)
    Scale.notes=Hirajoshi
    c1=Hirajoshi[2];c2=Hirajoshi[4];c3=Hirajoshi[1]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=5
    mode=Scale(str(r),Hirajoshi,5,color)
    modes.append(mode)

for r in ["Sakura"]:
    Scale.mode=str(r)
    SakuraSteps=[0,1,4,5,6]
    Sakura=[]
    for j in SakuraSteps:
        note=pool[j+transpose]
        Sakura.append(note)
    Scale.notes=Sakura
    c1=Sakura[1];c2=Sakura[2];c3=Sakura[4]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=5
    mode=Scale(str(r),Sakura,5,color)
    modes.append(mode)

for r in ["Insen"]:
    Scale.mode=str(r)
    InsenSteps=[0,1,5,7,10]
    Insen=[]
    for j in InsenSteps:
        note=pool[j+transpose]
        Insen.append(note)
    Scale.notes=Insen
    c1=Insen[1];c2=Insen[2];c3=Insen[4]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=5
    mode=Scale(str(r),Insen,5,color)
    modes.append(mode)

for r in ["Iwato"]:
    Scale.mode=str(r)
    IwatoSteps=[0,1,5,6,10]
    Iwato=[]
    for j in IwatoSteps:
        note=pool[j+transpose]
        Iwato.append(note)
    Scale.notes=Iwato
    c1=Iwato[1];c2=Iwato[4];c3=Iwato[3]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=5
    mode=Scale(str(r),Iwato,5,color)
    modes.append(mode)

for r in ["Yo"]:
    Scale.mode=str(r)
    YoSteps=[0,2,5,7,9]
    Yo=[]
    for j in YoSteps:
        note=pool[j+transpose]
        Yo.append(note)
    Scale.notes=Yo
    c1=Yo[2];c2=Yo[1];c3=Yo[4]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=5
    mode=Scale(str(r),Yo,5,color)
    modes.append(mode)

for r in ["Balinese Pelog"]:
    Scale.mode=str(r)
    BalineseSteps=[0,1,3,7,8]
    BalinesePelog=[]
    for j in BalineseSteps:
        note=pool[j+transpose]
        BalinesePelog.append(note)
    Scale.notes=BalinesePelog
    c1=BalinesePelog[1];c2=BalinesePelog[4]
    c3=BalinesePelog[2]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=5
    mode=Scale(str(r),BalinesePelog,5,color)
    modes.append(mode)

for r in ["Chinese"]:
    Scale.mode=str(r)
    ChineseSteps=[0,4,6,7,11]
    Chinese=[]
    for j in ChineseSteps:
        note=pool[j+transpose]
        Chinese.append(note)
    Scale.notes=Chinese
    c1=Chinese[1];c2=Chinese[2];c3=Chinese[4]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=5
    mode=Scale(str(r),Chinese,5,color)
    modes.append(mode)

for r in ["Egyptian"]:
    Scale.mode=str(r)
    EgyptianSteps=[0,2,5,7,10]
    Egyptian=[]
    for j in EgyptianSteps:
        note=pool[j+transpose]
        Egyptian.append(note)
    Scale.notes=Egyptian
    c1=Egyptian[4];c2=Egyptian[2];c3=Egyptian[1]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=5
    mode=Scale(str(r),Egyptian,5,color)
    modes.append(mode)

for r in ["Akebono"]:
    Scale.mode=str(r)
    AkebonoSteps=[0,2,3,7,9]
    Akebono=[]
    for j in AkebonoSteps:
        note=pool[j+transpose]
        Akebono.append(note)
    Scale.notes=Akebono
    c1=Akebono[2];c2=Akebono[4];c3=Akebono[1]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=5
    mode=Scale(str(r),Akebono,5,color)
    modes.append(mode)

# BEBOP/JAZZ/BLUES/GOSPEL SCALES

for r in ["Bebop Dominant"]:
    Scale.mode=str(r)
    BebopDominantSteps=[0,2,4,5,7,9,10,11]
    BebopDominant=[]
    for j in BebopDominantSteps:
        note=pool[j+transpose]
        BebopDominant.append(note)
    Scale.notes=BebopDominant
    c1=BebopDominant[2];c2=BebopDominant[7]
    c3=BebopDominant[6]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=8
    mode=Scale(str(r),BebopDominant,8,color)
    modes.append(mode)

for r in ["Bebop Major"]:
    Scale.mode=str(r)
    BebopMajorSteps=[0,2,4,5,7,8,9,11]
    BebopMajor=[]
    for j in BebopMajorSteps:
        note=pool[j+transpose]
        BebopMajor.append(note)
    Scale.notes=BebopMajor
    c1=BebopMajor[2];c2=BebopMajor[5];c3=BebopMajor[6]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=8
    mode=Scale(str(r),BebopMajor,8,color)
    modes.append(mode)

for r in ["Bebop Melodic Minor"]:
    Scale.mode=str(r)
    BebopMelodicMinorSteps=[0,2,3,5,7,8,9,11]
    BebopMelodicMinor=[]
    for j in BebopMelodicMinorSteps:
        note=pool[j+transpose]
        BebopMelodicMinor.append(note)
    Scale.notes=BebopMelodicMinor
    c1=BebopMelodicMinor[2];c2=BebopMelodicMinor[5]
    c3=BebopMelodicMinor[6]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=8
    mode=Scale(str(r),BebopMelodicMinor,8,color)
    modes.append(mode)

for r in ["Dom7b5 Diminished"]:
    Scale.mode=str(r)
    Dom7b5DimSteps=[0,2,4,5,6,8,10,11]
    Dom7b5Diminished=[]
    for j in Dom7b5DimSteps:
        note=pool[j+transpose]
        Dom7b5Diminished.append(note)
    Scale.notes=Dom7b5Diminished
    c1=Dom7b5Diminished[4];c2=Dom7b5Diminished[6]
    c3=Dom7b5Diminished[2]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=8
    mode=Scale(str(r),Dom7b5Diminished,8,color)
    modes.append(mode)

for r in ["Six-Note Blues Scale"]:
    Scale.mode=str(r)
    SixNoteBluesSteps=[0,3,5,6,9,10]
    SixNoteBlues=[]
    for j in SixNoteBluesSteps:
        note=pool[j+transpose]
        SixNoteBlues.append(note)
    Scale.notes=SixNoteBlues
    c1=SixNoteBlues[1];c2=SixNoteBlues[4]
    c3=SixNoteBlues[5]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=6
    mode=Scale(str(r),SixNoteBlues,6,color)
    modes.append(mode)

for r in ["Nine-Note Blues Scale"]:
    Scale.mode=str(r)
    NineNoteBluesSteps=[0,2,3,4,5,7,9,10,11]
    NineNoteBlues=[]
    for j in NineNoteBluesSteps:
        note=pool[j+transpose]
        NineNoteBlues.append(note)
    Scale.notes=NineNoteBlues
    c1=NineNoteBlues[2];c2=NineNoteBlues[6]
    c3=NineNoteBlues[7]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=9
    mode=Scale(str(r),SixNoteBlues,9,color)
    modes.append(mode)

for r in ["Gospel/Major Blues Scale"]:
    Scale.mode=str(r)
    GospelSteps=[0,2,3,4,7,9]
    Gospel=[]
    for j in GospelSteps:
        note=pool[j+transpose]
        Gospel.append(note)
    Scale.notes=Gospel
    c1=Gospel[2];c2=Gospel[3];c3=Gospel[5]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=6
    mode=Scale(str(r),Gospel,6,color)
    modes.append(mode)

# HEXATONIC SCALES

for r in ["Symmetrical Augmented"]:
    Scale.mode=str(r)
    SymmetricAugSteps=[0,3,4,7,8,10]
    SymmetricAugmented=[]
    for j in SymmetricAugSteps:
        note=pool[j+transpose]
        SymmetricAugmented.append(note)
    Scale.notes=SymmetricAugmented
    c1=SymmetricAugmented[1];c2=SymmetricAugmented[5]
    c3=SymmetricAugmented[4]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=6
    mode=Scale(str(r),SymmetricAugmented,6,color)
    modes.append(mode)

for r in ["Iberian Hexatonic"]:
    Scale.mode=str(r)
    IberianSteps=[0,1,4,5,7,10]
    IberianHexatonic=[]
    for j in IberianSteps:
        note=pool[j+transpose]
        IberianHexatonic.append(note)
    Scale.notes=IberianHexatonic
    c1=IberianHexatonic[1];c2=IberianHexatonic[2]
    c3=IberianHexatonic[5]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=6
    mode=Scale(str(r),IberianHexatonic,6,color)
    modes.append(mode)

for r in ["Prometheus Scale"]:
    Scale.mode=str(r)
    PromethianSteps=[0,2,4,6,7,10]
    Prometheus=[]
    for j in PromethianSteps:
        note=pool[j+transpose]
        Prometheus.append(note)
    Scale.notes=Prometheus
    c1=Prometheus[2];c2=Prometheus[3];c3=Prometheus[5]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=6
    mode=Scale(str(r),Prometheus,6,color)
    modes.append(mode)

for r in ["Prometheus Neapolitan"]:
    Scale.mode=str(r)
    PromNeapolitanSteps=[0,1,4,6,9,10]
    PrometheusNeapolitan=[]
    for j in PromNeapolitanSteps:
        note=pool[j+transpose]
        PrometheusNeapolitan.append(note)
    Scale.notes=PrometheusNeapolitan
    c1=PrometheusNeapolitan[1];c2=PrometheusNeapolitan[3]
    c3=PrometheusNeapolitan[4]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=6
    mode=Scale(str(r),PrometheusNeapolitan,6,color)
    modes.append(mode)

for r in ["Prometheus Liszt"]:
    Scale.mode=str(r)
    PromLizSteps=[0,1,4,5,8,9]
    PrometheusLiszt=[]
    for j in PromLizSteps:
        note=pool[j+transpose]
        PrometheusLiszt.append(note)
    Scale.notes=PrometheusLiszt
    c1=PrometheusLiszt[1];c2=PrometheusLiszt[3]
    c3=PrometheusLiszt[4]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=6
    mode=Scale(str(r),PrometheusLiszt,6,color)
    modes.append(mode)

for r in ["Banshikicho"]:
    Scale.mode=str(r)
    BanshikichoSteps=[0,2,3,4,7,9]
    Banshikicho=[]
    for j in BanshikichoSteps:
        note=pool[j+transpose]
        Banshikicho.append(note)
    Scale.notes=Banshikicho
    c1=Banshikicho[2];c2=Banshikicho[5];c3=Banshikicho[1]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=6
    mode=Scale(str(r),Banshikicho,6,color)
    modes.append(mode)

for r in ["Kurd/Annaziska Handpan Scale"]:
    Scale.mode=str(r)
    KurdishSteps=[0,2,3,5,7,8]
    Annaziska=[]
    for j in KurdishSteps:
        note=pool[j+transpose]
        Annaziska.append(note)
    Scale.notes=Annaziska
    c1=Annaziska[2];c2=Annaziska[5];c3=Annaziska[1]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=6
    mode=Scale(str(r),Annaziska,6,color)
    modes.append(mode)

# ETHNIC & SYMMETRICAL SCALES

for r in ["Harmonic Minor Add b5"]:
    Scale.mode=str(r)
    HarmonicMinorb5Steps=[0,2,3,5,6,7,8,11]
    HarmonicMinorb5=[]
    for j in HarmonicMinorb5Steps:
        note=pool[j+transpose]
        HarmonicMinorb5.append(note)
    Scale.notes=HarmonicMinorb5
    c1=HarmonicMinorb5[2];c2=HarmonicMinorb5[4]
    c3=HarmonicMinorb5[7]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=8
    mode=Scale(str(r),HarmonicMinorb5,8,color)
    modes.append(mode)

for r in ["Hungarian Major"]:
    Scale.mode=str(r)
    HungarianMajorSteps=[0,3,4,6,7,9,10]
    HungarianMajor=[]
    for j in HungarianMajorSteps:
        note=pool[j+transpose]
        HungarianMajor.append(note)
    Scale.notes=HungarianMajor
    c1=HungarianMajor[2];c2=HungarianMajor[3]
    c3=HungarianMajor[5]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),HungarianMajor,7,color)
    modes.append(mode)

for r in ["Diminished Octatonic"]:
    Scale.mode=str(r)
    DimOctatonicSteps=[0,2,3,5,6,8,9,11]
    DiminishedOctatonic=[]
    for j in DimOctatonicSteps:
        note=pool[j+transpose]
        DiminishedOctatonic.append(note)
    Scale.notes=DiminishedOctatonic
    c1=DiminishedOctatonic[2];c2=DiminishedOctatonic[4]
    c3=DiminishedOctatonic[6]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=8
    mode=Scale(str(r),DiminishedOctatonic,8,color)
    modes.append(mode)

for r in ["Whole Tone"]:
    Scale.mode=str(r)
    WholeSteps=[0,2,4,6,8,10]
    WholeTone=[]
    for j in WholeSteps:
        note=pool[j+transpose]
        WholeTone.append(note)
    Scale.notes=WholeTone
    c1=WholeTone[2];c2=WholeTone[3];c3=WholeTone[4]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=6
    mode=Scale(str(r),WholeTone,6,color)
    modes.append(mode)

for r in ["Ultralocrian"]:
    Scale.mode=str(r)
    UltraLocrianSteps=[0,1,3,4,6,7,9]
    Ultralocrian=[]
    for j in UltraLocrianSteps:
        note=pool[j+transpose]
        Ultralocrian.append(note)
    Scale.notes=Ultralocrian
    c1=Ultralocrian[1];c2=Ultralocrian[6];c3=Ultralocrian[4]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),Ultralocrian,7,color)
    modes.append(mode)

for r in ["Japanese Nohkan Flute Scale"]:
    Scale.mode=str(r)
    NohkanSteps=[0,2,5,6,8,9,11]
    NohkanFlute=[]
    for j in NohkanSteps:
        note=pool[j+transpose]
        NohkanFlute.append(note)
    Scale.notes=NohkanFlute
    c1=NohkanFlute[3];c2=NohkanFlute[2];c3=NohkanFlute[6]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),NohkanFlute,7,color)
    modes.append(mode)

for r in ["Persian"]:
    Scale.mode=str(r)
    PersianSteps=[0,1,4,5,6,8,10]
    Persian=[]
    for j in PersianSteps:
        note=pool[j+transpose]
        Persian.append(note)
    Scale.notes=Persian
    c1=Persian[1];c2=Persian[4];c3=Persian[5]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),Persian,7,color)
    modes.append(mode)

for r in ["Arabic"]:
    Scale.mode=str(r)
    ArabianSteps=[0,2,4,5,6,8,10]
    Arabic=[]
    for j in ArabianSteps:
        note=pool[j+transpose]
        Arabic.append(note)
    Scale.notes=Arabic
    c1=Arabic[2];c2=Arabic[4];c3=Arabic[5]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),Arabic,7,color)
    modes.append(mode)

for r in ["Neapolitan Minor"]:
    Scale.mode=str(r)
    NeapolitanMinorSteps=[0,1,3,5,7,8,11]
    NeapolitanMinor=[]
    for j in NeapolitanMinorSteps:
        note=pool[j+transpose]
        NeapolitanMinor.append(note)
    Scale.notes=NeapolitanMinor
    c1=NeapolitanMinor[1];c2=NeapolitanMinor[2]
    c3=NeapolitanMinor[5]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),NeapolitanMinor,7,color)
    modes.append(mode)

for r in ["Neapolitan Major"]:
    Scale.mode=str(r)
    NeapolitanMajorSteps=[0,1,3,5,7,9,11]
    NeapolitanMajor=[]
    for j in NeapolitanMajorSteps:
        note=pool[j+transpose]
        NeapolitanMajor.append(note)
    Scale.notes=NeapolitanMajor
    c1=NeapolitanMajor[1];c2=NeapolitanMajor[2]
    c3=NeapolitanMajor[5]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),NeapolitanMajor,7,color)
    modes.append(mode)

for r in ["Hijaz Kar Maqam"]:
    Scale.mode=str(r)
    HijazKarMaqamSteps=[0,1,4,5,7,8,11]
    HijazKarMaqam=[]
    for j in HijazKarMaqamSteps:
        note=pool[j+transpose]
        HijazKarMaqam.append(note)
    Scale.notes=HijazKarMaqam
    c1=HijazKarMaqam[1];c2=HijazKarMaqam[2]
    c3=HijazKarMaqam[6]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),HijazKarMaqam,7,color)
    modes.append(mode)

for r in ["Algerian Minor"]:
    Scale.mode=str(r)
    AlgerianSteps=[0,2,3,5,6,7,8,11]
    AlgerianMinor=[]
    for j in AlgerianSteps:
        note=pool[j+transpose]
        AlgerianMinor.append(note)
    Scale.notes=AlgerianMinor
    c1=AlgerianMinor[2];c2=AlgerianMinor[4]
    c3=AlgerianMinor[6]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=8
    mode=Scale(str(r),AlgerianMinor,8,color)
    modes.append(mode)

for r in ["8-Note Spanish/Jewish"]:
    Scale.mode=str(r)
    Jewish8Steps=[0,1,3,4,5,6,8,10]
    Jewish8=[]
    for j in Jewish8Steps:
        note=pool[j+transpose]
        Jewish8.append(note)
    Scale.notes=Jewish8
    c1=Jewish8[1];c2=Jewish8[2];c3=Jewish8[5]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=8
    mode=Scale(str(r),Jewish8,8,color)
    modes.append(mode)

for r in ["Scala Enigmatica (Ascending)"]:
    Scale.mode=str(r)
    EnigmaticUpSteps=[0,1,4,6,8,10,11]
    EnigmaticASC=[]
    for j in EnigmaticUpSteps:
        note=pool[j+transpose]
        EnigmaticASC.append(note)
    Scale.notes=EnigmaticASC
    c1=EnigmaticASC[1];c2=EnigmaticASC[3];c3=EnigmaticASC[4]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),EnigmaticASC,7,color)
    modes.append(mode)

for r in ["Scala Enigmatica (Descending)"]:
    Scale.mode=str(r)
    EnigmaticDownSteps=[0,11,10,8,5,4,1]
    EnigmaticDESC=[]
    for j in EnigmaticDownSteps:
        note=pool[j+transpose]
        EnigmaticDESC.append(note)
    Scale.notes=EnigmaticDESC
    c1=EnigmaticDESC[1];c2=EnigmaticDESC[4];c3=EnigmaticDESC[5]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),EnigmaticDESC,7,color)
    modes.append(mode)

for r in ["Raga Asavari"]:
    Scale.mode=str(r)
    AsavariSteps=[0,1,5,7,8,0,10,8,7,5,3,1,0]
    RagaAsavari=[]
    for j in AsavariSteps:
        note=pool[j+transpose]
        RagaAsavari.append(note)
    Scale.notes=RagaAsavari
    c1=RagaAsavari[1];c2=RagaAsavari[4];c3=RagaAsavari[6]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=13
    mode=Scale(str(r),RagaAsavari,13,color)
    modes.append(mode)

for r in ["Enigmatic Minor"]:
    Scale.mode=str(r)
    EnigminorSteps=[0,1,3,6,7,10,11]
    EnigmaticMinor=[]
    for j in EnigminorSteps:
        note=pool[j+transpose]
        EnigmaticMinor.append(note)
    Scale.notes=EnigmaticMinor
    c1=EnigmaticMinor[1];c2=EnigmaticMinor[2];c3=EnigmaticMinor[3]
    color=[c1,c2,c3];Scale.color=color
    Scale.steps=7
    mode=Scale(str(r),EnigmaticMinor,7,color)
    modes.append(mode)

# Select Mode/Scale

y=random.randint(0,78)
choice=modes[y]
print("Mode:",choice.mode,"in",root)
print("Notes spelled out:")
print(choice.notes);print("")
print("Color Notes:",choice.color)
moodi=choice.notes
colors=choice.color
print("")

# Convert into MIDI values

class MIDIPattern:
    def __init__(self,region,midinotes):
        self.trackname=trackname
        self.midinotes=midinotes

ColorInMidi=[]

for r in ["Subsonic Bass in Range C0-B0"]:
    MIDIPattern.region=str(r)

    SubsonicBass=[]
    midinotes={
            "C":12,
            "C#/Db":13,
            "D":14,
            "D#/Eb":15,
            "E":16,
            "F":17,
            "F#/Gb":18,
            "G":19,
            "G#/Ab":20,
            "A":21,
            "A#/Bb":22,
            "B":23
            }

    for i in moodi:
        SubsonicBass.append(midinotes[i])
    MIDIPattern.midinotes=SubsonicBass
    for c in colors:
        ColorInMidi.append(midinotes[c])
    print("MIDI Values for Subsonic Range:")
    print(SubsonicBass)

for r in ["Basso Ostinato C1 to B1"]:
    MIDIPattern.region=str(r)

    BassoOstinato=[]
    midinotes={
            "C":24,
            "C#/Db":25,
            "D":26,
            "D#/Eb":27,
            "E":28,
            "F":29,
            "F#/Gb":30,
            "G":31,
            "G#/Ab":32,
            "A":33,
            "A#/Bb":34,
            "B":35
            }

    for i in moodi:
        BassoOstinato.append(midinotes[i])
    MIDIPattern.midinotes=BassoOstinato
    for c in colors:
        ColorInMidi.append(midinotes[c])
    print("MIDI Values for Basso Ostinato Range:")
    print(BassoOstinato)

for r in ["Double Bass & Cello Range C2 to B2"]:
    MIDIPattern.region=str(r)

    DoubleBass=[]
    midinotes={
            "C":36,
            "C#/Db":37,
            "D":38,
            "D#/Eb":39,
            "E":40,
            "F":41,
            "F#/Gb":42,
            "G":43,
            "G#/Ab":44,
            "A":45,
            "A#/Bb":46,
            "B":47
            }

    for i in moodi:
        DoubleBass.append(midinotes[i])
    MIDIPattern.midinotes=DoubleBass
    for c in colors:
        ColorInMidi.append(midinotes[c])
    print("MIDI Values for Double Bass Range:")
    print(DoubleBass)
        
for r in ["Cello/Viola Range C3 to B3"]:
    MIDIPattern.region=str(r)

    ViolaCello=[]
    midinotes={
            "C":48,
            "C#/Db":49,
            "D":50,
            "D#/Eb":51,
            "E":52,
            "F":53,
            "F#/Gb":54,
            "G":55,
            "G#/Ab":56,
            "A":57,
            "A#/Bb":58,
            "B":59
            }

    for i in moodi:
        ViolaCello.append(midinotes[i])
    MIDIPattern.midinotes=ViolaCello
    for c in colors:
        ColorInMidi.append(midinotes[c])
    print("MIDI Values for Cello/Viola Range:")
    print(ViolaCello)

for r in ["Melody Range from C4 to B4"]:
    MIDIPattern.region=str(r)

    MiddleC=[]
    midinotes={
            "C":60,
            "C#/Db":61,
            "D":62,
            "D#/Eb":63,
            "E":64,
            "F":65,
            "F#/Gb":66,
            "G":67,
            "G#/Ab":68,
            "A":69,
            "A#/Bb":70,
            "B":71
            }

    for i in moodi:
        MiddleC.append(midinotes[i])
    MIDIPattern.midinotes=MiddleC
    for c in colors:
        ColorInMidi.append(midinotes[c])
    print("MIDI Values for Middle-C Range:")
    print(MiddleC)

for r in ["Melody Range from C5 to B5"]:
    MIDIPattern.region=str(r)

    HighRegister=[]
    midinotes={
            "C":72,
            "C#/Db":73,
            "D":74,
            "D#/Eb":75,
            "E":76,
            "F":77,
            "F#/Gb":78,
            "G":79,
            "G#/Ab":80,
            "A":81,
            "A#/Bb":82,
            "B":83
            }

    for i in moodi:
        HighRegister.append(midinotes[i])
    MIDIPattern.midinotes=HighRegister
    for c in colors:
        ColorInMidi.append(midinotes[c])
    print("MIDI Values for High Register:")
    print(HighRegister)

for r in ["Overtones C6 to B6"]:
    MIDIPattern.region=str(r)

    Overtones=[]
    midinotes={
            "C":84,
            "C#/Db":85,
            "D":86,
            "D#/Eb":87,
            "E":88,
            "F":89,
            "F#/Gb":90,
            "G":91,
            "G#/Ab":92,
            "A":93,
            "A#/Bb":94,
            "B":95
            }

    for i in moodi:
        Overtones.append(midinotes[i])
    MIDIPattern.midinotes=Overtones
    for c in colors:
        ColorInMidi.append(midinotes[c])
    print("MIDI Values for Synthetic Overtones:")
    print(Overtones)

for r in ["Canine Sci-Fi Range C7 to B7"]:
    MIDIPattern.region=str(r)

    Canine=[]
    midinotes={
            "C":96,
            "C#/Db":97,
            "D":98,
            "D#/Eb":99,
            "E":100,
            "F":101,
            "F#/Gb":102,
            "G":103,
            "G#/Ab":104,
            "A":105,
            "A#/Bb":106,
            "B":107
            }

    for i in moodi:
        Canine.append(midinotes[i])
    MIDIPattern.midinotes=Canine
    for c in colors:
        ColorInMidi.append(midinotes[c])
    print("MIDI Values for Canine Register:")
    print(Canine)


# Composite Keyboard Ranges

for r in ["Low End"]:
    MIDIPattern.region=str(r)
    LowEnd=SubsonicBass+BassoOstinato
    MIDIPattern.midinotes=LowEnd

for r in ["LowMid"]:
    MIDIPattern.region=str(r)
    LowMid=DoubleBass+ViolaCello
    MIDIPattern.midinotes=LowMid

for r in ["MidHigh"]:
    MIDIPattern.region=str(r)
    MidHigh=MiddleC+HighRegister
    MIDIPattern.midinotes=MidHigh

for r in ["MIDI Overtones"]:
    MIDIPattern.region=str(r)
    MidiOvertones=Overtones+Canine
    MIDIPattern.midinotes=MidiOvertones

for r in ["Full MIDI Range"]:
    MIDIPattern.region=str(r)
    FullRange=LowEnd+LowMid+MidHigh+MidiOvertones
    MIDIPattern.midinotes=FullRange

# RHYTHM SEQUENCING

class Rhythm:
    def __init__(self,meter,style,sequence):
        self.meter=meter
        self.style=style
        self.sequence=sequence

# Rhythm Blocks & An Empty List For Meters

Short=[[1],[0.5,0.5]]
Long=[[1,0.5],[0.5,1],[0.5,0.5,0.5]]

patterns=[]

# CROTCHET-BASED METERS & PATTERNS

for time in ["2/4"]:
    Rhythm.meter=str(time)

    for s in ["Pasodoble"]:
        Rhythm.style=str(s)

        pattern24=[1,1/3,1/3,1/3,0.5,0.5,0.5,0.5,0.25,0.25,0.5]
        Rhythm.sequence=pattern24
        pattern=Rhythm(str(time),str(s),pattern24)
        patterns.append(pattern)

    for s in ["Marcha Mora"]:
        Rhythm.style=str(s)

        pattern24=[0.75,0.25,0.5,0.5,0.5,0.5,0.25,0.25,0.25,0.25]
        Rhythm.sequence=pattern24
        pattern=Rhythm(str(time),str(s),pattern24)
        patterns.append(pattern)

    for s in ["Chastushka"]:
        Rhythm.style=str(s)

        pattern24=[1,0.5,0.5,1,0.5,0.5,1,0.5,0.5,2]
        Rhythm.sequence=pattern24
        pattern=Rhythm(str(time),str(s),pattern24)
        patterns.append(pattern)

    for s in ["Punk Polka"]:
        Rhythm.style=str(s)

        pattern24=[0.5,0.5,0.25,0.25,0.25,0.25]
        Rhythm.sequence=pattern24
        pattern=Rhythm(str(time),str(s),pattern24)
        patterns.append(pattern)

    for s in ["Bohemian Oompah"]:
        Rhythm.style=str(s)

        pattern24=[0.25,0.25,0.5,0.25,0.25,0.5,0.5,0.5,1]
        Rhythm.sequence=pattern24
        pattern=Rhythm(str(time),str(s),pattern24)
        patterns.append(pattern)

    for s in ["Habanera"]:
        Rhythm.style=str(s)

        pattern24=[0.75,0.25,0.5,0.5]
        Rhythm.sequence=pattern24
        pattern=Rhythm(str(time),str(s),pattern24)
        patterns.append(pattern)

    for s in ["Random"]:
        Rhythm.style=str(s)

        for i in Short:
            for k in Short:
                pattern24=i+k
                Rhythm.sequence=pattern24
                pattern=Rhythm(str(time),str(s),pattern24)
                patterns.append(pattern)

for time in ["3/4"]:
    Rhythm.meter=str(time)

    for s in ["Waltz"]:
        Rhythm.style=str(s)

        pattern34=[1,1.5,0.5,2,1,1,0.5,0.5,0.5,0.5,3]
        Rhythm.sequence=pattern34
        pattern=Rhythm(str(time),str(s),pattern34)
        patterns.append(pattern)

    for s in ["Mazurka"]:
        Rhythm.style=str(s)

        pattern34=[0.5,0.25,0.25,0.5,0.5,0.5,0.5,0.5,0.25,0.25,2]
        Rhythm.sequence=pattern34
        pattern=Rhythm(str(time),str(s),pattern34)
        patterns.append(pattern)

    for s in ["Polonaise"]:
        Rhythm.style=str(s)

        pattern34=[1,0.5,0.5,0.5,0.5,0.5,0.5,1,1]
        Rhythm.sequence=pattern34
        pattern=Rhythm(str(time),str(s),pattern34)
        patterns.append(pattern)

    for s in ["Random"]:
        Rhythm.style=str(s)

        for i in Short:
            for k in Short:
                for j in Short:
                    pattern34=i+k+j
                    Rhythm.sequence=pattern34
                    pattern=Rhythm(str(time),str(s),pattern34)
                    patterns.append(pattern)

for time in ["4/4"]:
    Rhythm.meter=str(time)

    for s in ["Random"]:
        Rhythm.style=str(s)

        for i in Short:
            for k in Short:
                for j in Short:
                    for l in Short:
                        pattern44=i+k+j+l
                        Rhythm.sequence=pattern44
                        pattern=Rhythm(str(time),str(s),pattern44)
                        patterns.append(pattern)

for time in ["5/4"]:
    Rhythm.meter=str(time)

    for s in ["Cretic Quintuple"]:
        Rhythm.style=str(s)

        pattern54=[2,2,1]
        Rhythm.sequence=pattern54
        pattern=Rhythm(str(time),str(s),pattern54)
        patterns.append(pattern)

    for s in ["Kalevala Runometric"]:
        Rhythm.style=str(s)

        pattern54=[2,1,2]
        Rhythm.sequence=pattern54
        pattern=Rhythm(str(time),str(s),pattern54)
        patterns.append(pattern)

    for s in ["Bacchic Quintuple"]:
        Rhythm.style=str(s)

        pattern54=[1,2,2]
        Rhythm.sequence=pattern54
        pattern=Rhythm(str(time),str(s),pattern54)
        patterns.append(pattern)

    for s in ["Seven Days"]:
        Rhythm.style=str(s)

        pattern54=[3,2]
        Rhythm.sequence=pattern54
        pattern=Rhythm(str(time),str(s),pattern54)
        patterns.append(pattern)

    for s in ["Random"]:
        Rhythm.style=str(s)

        for i in Short:
            for k in Short:
                for j in Short:
                    for l in Short:
                        for m in Short:
                            pattern54=i+k+j+l+m
                            Rhythm.sequence=pattern54
                            pattern=Rhythm(str(time),str(s),pattern54)
                            patterns.append(pattern)

for time in ["6/4"]:
    Rhythm.meter=str(time)

    for s in ["Rare Compound Triple Meter"]:
        Rhythm.style=str(s)

        for i in Short:
            for k in Short:
                for j in Short:
                    for l in Short:
                        for m in Short:
                            for n in Short:
                                pattern64=i+k+j+l+m+n
                                Rhythm.sequence=pattern64
                                pattern=Rhythm(str(time),str(s),pattern64)
                                patterns.append(pattern)

for time in ["7/4"]:
    Rhythm.meter=str(m)

    for s in ["Bulgarian Rachenitsa"]:
        Rhythm.style=str(s)

        pattern74=[2,2,3]
        Rhythm.sequence=pattern74
        pattern=Rhythm(str(time),str(s),pattern74)
        patterns.append(pattern)

    for s in ["Indian Rupak"]:
        Rhythm.style=str(s)

        pattern74=[3,3,2]
        Rhythm.sequence=pattern74
        pattern=Rhythm(str(time),str(s),pattern74)
        patterns.append(pattern)

    for s in ["Random"]:
        Rhythm.style=str(s)

        for i in Short:
            for k in Short:
                for j in Short:
                    for l in Short:
                        for m in Short:
                            for n in Short:
                                for p in Short:
                                    pattern74=i+k+j+l+m+n+p
                                    Rhythm.sequence=pattern74
                                    pattern=Rhythm(str(time),str(s),pattern74)
                                    patterns.append(pattern)

for time in ["9/4"]:
    Rhythm.meter=str(time)

    for s in ["Agon Syncopation (Stravinsky)"]:
        Rhythm.style=str(s)

        pattern94=[3,2,2,2]
        Rhythm.sequence=pattern94
        pattern=Rhythm(str(time),str(s),pattern94)
        patterns.append(pattern)

    for s in ["Trad. Korean Semachi Jangdan"]:
        Rhythm.style=str(s)

        pattern94=[3,2,1,1,2]
        Rhythm.sequence=pattern94
        pattern=Rhythm(str(time),str(s),pattern94)
        patterns.append(pattern)

for time in ["10/4"]:
    Rhythm.meter=str(time)

    for s in ["Mudawwar Shami"]:
        Rhythm.style=str(s)

        pattern104=[2,2,2,1,1,2]
        Rhythm.sequence=pattern104
        pattern=Rhythm(str(time),str(s),pattern104)
        patterns.append(pattern)

    for s in ["Everything In Its Right Place"]:
        Rhythm.style=str(s)

        pattern104=[1,0.5,1,1,1,1,1,1,0.5,0.25,0.25,0.25,0.25]
        Rhythm.sequence=pattern104
        pattern=Rhythm(str(time),str(s),pattern104)
        patterns.append(pattern)

for time in ["12/4"]:
    Rhythm.meter=str(time)

    for s in ["Mudawwar Masri"]:
        Rhythm.style=str(s)

        pattern124=[2,2,2,1,1,2,2]
        Rhythm.sequence=pattern124
        pattern=Rhythm(str(time),str(s),pattern124)
        patterns.append(pattern)

    for s in ["Trad. Korean Jungmori Jangdan"]:
        Rhythm.style=str(s)

        pattern124=[3,3,3,3]
        Rhythm.sequence=pattern124
        pattern=Rhythm(str(time),str(s),pattern124)
        patterns.append(pattern)

for time in ["13/4"]:
    Rhythm.meter=str(time)

    for s in ["Iqa' Murabba"]:
        Rhythm.style=str(s)

        pattern134=[1,1,1,2,2,2,1,1,2]
        Rhythm.sequence=pattern134
        pattern=Rhythm(str(time),str(s),pattern134)
        patterns.append(pattern)

for time in ["14/4"]:
    Rhythm.meter=str(time)

    for s in ["Iqa' Muhajjar"]:
        Rhythm.style=str(s)

        pattern144=[1,1,2,2,2,2,2,1,1]
        Rhythm.sequence=pattern144
        pattern=Rhythm(str(time),str(s),pattern144)
        patterns.append(pattern)

for time in ["16/4"]:
    Rhythm.meter=str(time)

    for s in ["Iqa' Mukhammas"]:
        Rhythm.style=str(s)

        pattern164=[2,2,2,2,2,1,1,2,1,1]
        Rhythm.sequence=pattern164
        pattern=Rhythm(str(time),str(s),pattern164)
        patterns.append(pattern)

for time in ["19/4"]:
    Rhythm.meter=str(time)

    for s in ["Iqa' Awfar Masri"]:
        Rhythm.style=str(s)

        pattern194=[2,4,2,2,2,1,2,4]
        Rhythm.sequence=pattern194
        pattern=Rhythm(str(time),str(s),pattern194)
        patterns.append(pattern)

for time in ["20/4"]:
    Rhythm.style=str(time)

    for s in ["Iqa' Fakhit"]:
        Rhythm.style=str(s)

        pattern204=[1,1,1,0.5,0.5,2,2,1,1,2,1,1,2,2,1,1]
        Rhythm.sequence=pattern204
        pattern=Rhythm(str(time),str(s),pattern204)
        patterns.append(pattern)

# QUAVER-BASED METERS & PATTERNS

for time in ["5/8"]:
    Rhythm.meter=str(time)

    for s in ["Random"]:
        Rhythm.style=str(s)

        for i in Short:
            for k in Long:
                
                pattern58=i+k
                Rhythm.sequence=pattern58
                pattern=Rhythm(str(time),str(s),pattern58)
                patterns.append(pattern)

                pattern58=k+i
                Rhythm.sequence=pattern58
                pattern=Rhythm(str(time),str(s),pattern58)
                patterns.append(pattern)

for time in ["6/8"]:
    Rhythm.meter=str(time)

    for s in ["Random"]:
        Rhythm.style=str(s)

        for i in Long:
            for k in Long:
                pattern68=i+k
                Rhythm.sequence=pattern68
                pattern=Rhythm(str(time),str(s),pattern68)
                patterns.append(pattern)

for time in ["7/8"]:
    Rhythm.meter=str(time)

    for s in ["Macedonian Ruchenitsa"]:
        Rhythm.style=str(s)

        pattern78=[1,1,1.5]
        Rhythm.sequence=pattern78
        pattern=Rhythm(str(time),str(s),pattern78)
        patterns.append(pattern)

    for s in ["Iqa' Dawr Hindi"]:
        Rhythm.style=str(s)

        pattern78=[0.5,0.5,0.5,1,1]
        Rhythm.sequence=pattern78
        pattern=Rhythm(str(time),str(s),pattern78)
        patterns.append(pattern)

    for s in ["Random"]:
        Rhythm.style=str(s)

        for i in Short:
            for k in Short:
                for j in Long:
                    
                    pattern78=i+k+j
                    Rhythm.sequence=pattern78
                    pattern=Rhythm(str(time),str(s),pattern78)
                    patterns.append(pattern)

                    pattern78=i+j+k
                    Rhythm.sequence=pattern78
                    pattern=Rhythm(str(time),str(s),pattern78)
                    patterns.append(pattern)

                    pattern78=j+i+k
                    Rhythm.sequence=pattern78
                    pattern=Rhythm(str(time),str(s),pattern78)
                    patterns.append(pattern)

for time in ["9/8"]:
    Rhythm.meter=str(time)

    for s in ["Turkish Karsilama"]:
        Rhythm.style=str(s)

        pattern98=[1,1,1.5,1]
        Rhythm.sequence=pattern98
        pattern=Rhythm(str(time),str(s),pattern98)
        patterns.append(pattern)

    for s in ["Irish Hot Jig"]:
        Rhythm.style=str(s)

        pattern98=[1.5,1.5,1.5]
        Rhythm.sequence=pattern98
        pattern=Rhythm(str(time),str(s),pattern98)
        patterns.append(pattern)

    for s in ["Bulgarian Daichovo"]:
        Rhythm.style=str(s)

        pattern98=[1,1,1,1.5]
        Rhythm.sequence=pattern98
        pattern=Rhythm(str(time),str(s),pattern98)
        patterns.append(pattern)

    for s in ["Iqa' Aqsaq"]:
        Rhythm.style=str(s)

        pattern98=[1,1,1,1,0.5]
        Rhythm.sequence=pattern98
        pattern=Rhythm(str(time),str(s),pattern98)
        patterns.append(pattern)

    for s in ["Random"]:
        Rhythm.style=str(s)

        for i in Long:
            for k in Long:
                for j in Long:
                    pattern98=i+k+j
                    Rhythm.sequence=pattern98
                    pattern=Rhythm(str(time),str(s),pattern98)
                    patterns.append(pattern)

for time in ["10/8"]:
    Rhythm.meter=str(time)

    for s in ["Random"]:
        Rhythm.style=str(s)

        for i in Short:
            for k in Long:
                for j in Short:
                    for l in Long:
                        
                        pattern108=i+k+j+l
                        Rhythm.sequence=pattern108
                        pattern=Rhythm(str(time),str(s),pattern108)
                        patterns.append(pattern)

                        pattern108=k+i+l+j
                        Rhythm.sequence=pattern108
                        pattern=Rhythm(str(time),str(s),pattern108)
                        patterns.append(pattern)

for time in ["11/8"]:
    Rhythm.meter=str(m)

    for s in ["Bulgarian Kopanitsa"]:
        Rhythm.style=str(s)

        pattern118=[2,1.5,2]
        Rhythm.sequence=pattern118
        pattern=Rhythm(str(time),str(s),pattern118)
        patterns.append(pattern)

    for s in ["Macedonian Acano Mlada Nevesto"]:
        Rhythm.style=str(s)

        pattern118=[1.5,2,1,1]
        Rhythm.sequence=pattern118
        pattern=Rhythm(str(time),str(s),pattern118)
        patterns.append(pattern)

    for s in ["Random"]:
        Rhythm.style=str(s)

        for i in Long:
            for k in Long:
                for j in Long:
                    for m in Short:

                        pattern118=i+k+j+m
                        Rhythm.sequence=pattern118
                        pattern=Rhythm(str(time),str(s),pattern118)
                        patterns.append(pattern)

                        pattern118=i+m+k+j
                        Rhythm.sequence=pattern118
                        pattern=Rhythm(str(time),str(s),pattern118)
                        patterns.append(pattern)

                        pattern118=i+k+m+j
                        Rhythm.sequence=pattern118
                        pattern=Rhythm(str(time),str(s),pattern118)
                        patterns.append(pattern)

for time in ["12/8"]:
    Rhythm.meter=str(m)

    for s in ["Trad. Korean Jajinmori Jangdan"]:
        Rhythm.style=str(s)

        pattern128=[1,0.5,0.5,1,1,0.5,0.5,1]
        Rhythm.sequence=pattern128
        pattern=Rhythm(str(time),str(s),pattern128)
        patterns.append(pattern)

    for s in ["Random"]:
        Rhythm.style=str(s)

        for i in Long:
            for k in Long:
                for j in Long:
                    for m in Long:
                        pattern128=i+k+j+m
                        Rhythm.sequence=pattern128
                        pattern=Rhythm(str(time),str(s),pattern128)
                        patterns.append(pattern)

for time in ["13/8"]:
    Rhythm.meter=str(time)

    for s in ["Iqa' Dharafat"]:
        Rhythm.style=str(s)

        pattern138=[1.5,1.5,1,0.5,0.5,1.5]
        Rhythm.sequence=pattern138
        pattern=Rhythm(str(time),str(s),pattern138)
        patterns.append(pattern)

    for s in ["Random"]:
        Rhythm.style=str(s)

        for i in Long:
            for k in Long:
                for j in Long:
                    for m in Short:
                        for n in Short:
                            
                            pattern138=i+k+j+m+n
                            Rhythm.sequence=pattern138
                            pattern=Rhythm(str(time),str(s),pattern138)
                            patterns.append(pattern)

for time in ["15/8"]:
    Rhythm.meter=str(time)

    for s in ["Random"]:
        Rhythm.style=str(s)

        for i in Long:
            for k in Long:
                for j in Long:
                    for m in Short:
                        for n in Short:
                            for p in Short:
                                pattern158=i+k+j+m+n+p
                                Rhythm.sequence=pattern158
                                pattern=Rhythm(str(time),str(s),pattern158)
                                patterns.append(pattern)

for time in ["17/8"]:
    Rhythm.meter=str(time)

    for s in ["Iqa' Khosh Rang"]:
        Rhythm.style=str(s)

        pattern178=[1,0.5,1,0.5,0.5,1,0.5,1,0.5,0.5,1,0.5]
        Rhythm.sequence=pattern178
        pattern=Rhythm(str(time),str(s),pattern178)
        patterns.append(pattern)

# SELECT METER & PATTERN

xo=random.randint(0,len(patterns)-1)
ChoosePattern=patterns[xo]
print("")
print("Meter:",ChoosePattern.meter)
print("Style:",ChoosePattern.style)
print("Sequence in Beats:")
print(ChoosePattern.sequence)
boogie=ChoosePattern.sequence

# SELECT KEYBOARD RANGE

KeyboardRange=[SubsonicBass,BassoOstinato,DoubleBass,ViolaCello,
               MiddleC,HighRegister,Overtones,Canine,LowEnd,LowMid,
               MidHigh,MidiOvertones,FullRange]
pick=random.randint(0,len(KeyboardRange)-1)
Register=KeyboardRange[pick]

# Create a Random Motif

class NOTE:
    def __init__(self,pitch,duration):
        self.pitch=pitch
        self.duration=duration

RandomMotif=[]

for a in boogie:
    w=random.randint(0,choice.steps-1)
    NOTE.pitch=Register[w]
    NOTE.duration=a
    noteofchoice=NOTE(Register[w],a)
    RandomMotif.append(noteofchoice)


# CREATE A MIDI FILE

mf=MIDIFile(1)
track=0
time=0
channel=0
volume=100

name=ChoosePattern.meter+" Riff in "+root+" "+choice.mode
mf.addTrackName(track,time,name)
newname=name.replace("/","_")

# DEFINE TEMPO

class Tempo:
    def __init__(self,BPM,classical):
        self.BPM=BPM
        self.classical=classical
        
tempos=[]

for label in ["Grave"]:
    
    Tempo.classical=str(label)
    bpm=random.randint(20,40)
    TMP=Tempo(bpm,str(label))
    tempos.append(TMP)

for label in ["Lento"]:

    Tempo.classical=str(label)
    bpm=random.randint(40,60)
    TMP=Tempo(bpm,str(label))
    tempos.append(TMP)

for label in ["Larghetto"]:

    Tempo.classical=str(label)
    bpm=random.randint(60,66)
    TMP=Tempo(bpm,str(label))
    tempos.append(TMP)

for label in ["Adagio"]:

    Tempo.classical=str(label)
    bpm=random.randint(66,76)
    TMP=Tempo(bpm,str(label))
    tempos.append(TMP)

for label in ["Andante"]:
    Tempo.classical=str(label)
    bpm=random.randint(76,108)
    TMP=Tempo(bpm,str(label))
    tempos.append(TMP)

for label in ["Moderato"]:
    Tempo.classical=str(label)
    bpm=random.randint(108,120)
    TMP=Tempo(bpm,str(label))
    tempos.append(TMP)

for label in ["Allegro"]:
    Tempo.classical=str(label)
    bpm=random.randint(120,156)
    TMP=Tempo(bpm,str(label))
    tempos.append(TMP)

for label in ["Vivace"]:
    Tempo.classical=str(label)
    bpm=random.randint(156,168)
    TMP=Tempo(bpm,str(label))
    tempos.append(TMP)

for label in ["Presto"]:
    Tempo.classical=str(label)
    bpm=random.randint(168,200)
    TMP=Tempo(bpm,str(label))
    tempos.append(TMP)

for label in ["Prestissimo"]:
    Tempo.classical=str(label)
    bpm=random.randint(200,208)
    TMP=Tempo(bpm,str(label))
    tempos.append(TMP)

dice=random.randint(0,9)
ChooseTempo=tempos[dice]
tracktempo=ChooseTempo.BPM
print("Tracktempo:",ChooseTempo.BPM,"BPM")
print("Or, to put it more classy:",ChooseTempo.classical)
                  
mf.addTempo(track,time,tracktempo)

for item in RandomMotif:
    pitch=item.pitch
    duration=item.duration
    mf.addNote(track,channel,pitch,time,duration,volume)
    time=time+duration

with open(newname+".mid","wb") as outf:
    mf.writeFile(outf)






        
        

                        



    

                    





                

    

        

    






        

    

    
        

        



        
        

        

    




    


    

    







    
    
