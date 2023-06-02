# Oblique Strategies Version 5.0

import random
from midiutil import MIDIFile

# ROOT

Octave={"A":0,"A#/Bb":1,"B":2,"C":3,"C#/Db":4,"D":5,"D#/Eb":6,
        "E":7,"F":8,"F#/Gb":9,"G":10,"G#/Ab":11}

for key in Octave:
    transpose=Octave[key]

root,transpose=random.choice(list(Octave.items()))
notepool=list(Octave.keys())+list(Octave.keys())

# SCALE OBJECT

class Scale:
    def __init__(self,mode,notes,steps,probmatrix):
        self.mode=mode
        self.notes=notes
        self.steps=steps
        self.probmatrix=probmatrix

modes=[]

# DIATONIC MODES OF MAJOR SCALE

for r in ["Ionian"]:
    Scale.mode=str(r)
    IonianSteps=[0,2,4,5,7,9,11]
    IonianProbs=[10,15,25,10,5,15,20]
    Ionian=[]
    for j in IonianSteps:
        note=notepool[j+transpose]
        Ionian.append(note)
    Scale.notes=Ionian
    Scale.steps=7
    Scale.probmatrix=IonianProbs
    mode=Scale(str(r),Ionian,7,IonianProbs)
    modes.append(mode)

for r in ["Dorian"]:
    Scale.mode=str(r)
    DorianSteps=[0,2,3,5,7,9,10]
    DorianProbs=[10,15,20,10,5,25,15]
    Dorian=[]
    for j in DorianSteps:
        note=notepool[j+transpose]
        Dorian.append(note)
    Scale.notes=Dorian
    Scale.steps=7
    Scale.probmatrix=DorianProbs
    mode=Scale(str(r),Dorian,7,DorianProbs)
    modes.append(mode)

for r in ["Phrygian"]:
    Scale.mode=str(r)
    PhrygianSteps=[0,1,3,5,7,8,10]
    PhrygianProbs=[10,25,20,5,10,15,15]
    Phrygian=[]
    for j in PhrygianSteps:
        note=notepool[j+transpose]
        Phrygian.append(note)
    Scale.notes=Phrygian
    Scale.steps=7
    Scale.probmatrix=PhrygianProbs
    mode=Scale(str(r),Phrygian,7,PhrygianProbs)
    modes.append(mode)

for r in ["Lydian"]:
    Scale.mode=str(r)
    LydianSteps=[0,2,4,6,7,9,11]
    LydianProbs=[10,10,15,30,5,10,20]
    Lydian=[]
    for j in LydianSteps:
        note=notepool[j+transpose]
        Lydian.append(note)
    Scale.notes=Lydian
    Scale.steps=7
    Scale.probmatrix=LydianProbs
    mode=Scale(str(r),Lydian,7,LydianProbs)
    modes.append(mode)

for r in ["Mixolydian"]:
    Scale.mode=str(r)
    MixolydianSteps=[0,2,4,5,7,9,10]
    MixolydianProbs=[10,10,25,10,5,15,25]
    Mixolydian=[]
    for j in MixolydianSteps:
        note=notepool[j+transpose]
        Mixolydian.append(note)
    Scale.notes=Mixolydian
    Scale.steps=7
    Scale.probmatrix=MixolydianProbs
    mode=Scale(str(r),Mixolydian,7,MixolydianProbs)
    modes.append(mode)

for r in ["Aeolian"]:
    Scale.mode=str(r)
    AeolianSteps=[0,2,3,5,7,8,10]
    AeolianProbs=[10,15,20,10,5,25,15]
    Aeolian=[]
    for j in AeolianSteps:
        note=notepool[j+transpose]
        Aeolian.append(note)
    Scale.notes=Aeolian
    Scale.steps=7
    Scale.probmatrix=AeolianProbs
    mode=Scale(str(r),Aeolian,7,AeolianProbs)
    modes.append(mode)

for r in ["Locrian"]:
    Scale.mode=str(r)
    LocrianSteps=[0,1,3,5,6,8,10]
    LocrianProbs=[10,20,20,5,25,10,10]
    Locrian=[]
    for j in LocrianSteps:
        note=notepool[j+transpose]
        Locrian.append(note)
    Scale.notes=Locrian
    Scale.steps=7
    Scale.probmatrix=LocrianProbs
    mode=Scale(str(r),Locrian,7,LocrianProbs)
    modes.append(mode)

# DIATONIC MODES OF HARMONIC MAJOR SCALE

for r in ["Harmonic Major"]:
    Scale.mode=str(r)
    HarmonicMajorSteps=[0,2,4,5,7,8,11]
    HarmonicMajorProbs=[10,10,25,5,5,25,20]
    HarmonicMajor=[]
    for j in HarmonicMajorSteps:
        note=notepool[j+transpose]
        HarmonicMajor.append(note)
    Scale.notes=HarmonicMajor
    Scale.steps=7
    Scale.probmatrix=HarmonicMajorProbs
    mode=Scale(str(r),HarmonicMajor,7,HarmonicMajorProbs)
    modes.append(mode)

for r in ["Dorian b5"]:
    Scale.mode=str(r)
    Dorianb5Steps=[0,2,3,5,6,9,10]
    Dorianb5Probs=[10,10,25,5,20,20,10]
    Dorianb5=[]
    for j in Dorianb5Steps:
        note=notepool[j+transpose]
        Dorianb5.append(note)
    Scale.notes=Dorianb5
    Scale.steps=7
    Scale.probmatrix=Dorianb5Probs
    mode=Scale(str(r),Dorianb5,7,Dorianb5Probs)
    modes.append(mode)

for r in ["Phrygian b4"]:
    Scale.mode=str(r)
    Phrygianb4Steps=[0,1,3,4,7,8,10]
    Phrygianb4Probs=[10,25,15,15,5,15,15]
    Phrygianb4=[]
    for j in Phrygianb4Steps:
        note=notepool[j+transpose]
        Phrygianb4.append(note)
    Scale.notes=Phrygianb4
    Scale.steps=7
    Scale.probmatrix=Phrygianb4Probs
    mode=Scale(str(r),Phrygianb4,7,Phrygianb4Probs)
    modes.append(mode)

for r in ["Lydian b3"]:
    Scale.mode=str(r)
    Lydianb3Steps=[0,2,3,6,7,9,11]
    Lydianb3Probs=[10,10,25,25,5,10,15]
    Lydianb3=[]
    for j in Lydianb3Steps:
        note=notepool[j+transpose]
        Lydianb3.append(note)
    Scale.notes=Lydianb3
    Scale.steps=7
    Scale.probmatrix=Lydianb3Probs
    mode=Scale(str(r),Lydianb3,7,Lydianb3Probs)
    modes.append(mode)

for r in ["Mixolydian b2"]:
    Scale.mode=str(r)
    Mixolydianb2Steps=[0,1,4,5,7,9,10]
    Mixolydianb2Probs=[10,25,20,10,5,15,20]
    Mixolydianb2=[]
    for j in Mixolydianb2Steps:
        note=notepool[j+transpose]
        Mixolydianb2.append(note)
    Scale.notes=Mixolydianb2
    Scale.steps=7
    Scale.probmatrix=Mixolydianb2Probs
    mode=Scale(str(r),Mixolydianb2,7,Mixolydianb2Probs)
    modes.append(mode)

for r in ["Lydian Augmented #2"]:
    Scale.mode=str(r)
    LydianAug2Steps=[0,3,4,6,8,9,11]
    LydianAug2Probs=[10,20,15,20,20,5,10]
    LydianAug2=[]
    for j in LydianAug2Steps:
        note=notepool[j+transpose]
        LydianAug2.append(note)
    Scale.notes=LydianAug2
    Scale.steps=7
    Scale.probmatrix=LydianAug2Probs
    mode=Scale(str(r),LydianAug2,7,LydianAug2Probs)
    modes.append(mode)

for r in ["Locrian bb7"]:
    Scale.mode=str(r)
    Locrianbb7Steps=[0,1,3,5,6,8,9]
    Locrianbb7Probs=[10,20,15,5,20,10,20]
    Locrianbb7=[]
    for j in Locrianbb7Steps:
        note=notepool[j+transpose]
        Locrianbb7.append(note)
    Scale.notes=Locrianbb7
    Scale.steps=7
    Scale.probmatrix=Locrianbb7Probs
    mode=Scale(str(r),Locrianbb7,7,Locrianbb7Probs)
    modes.append(mode)

# DIATONIC MODES OF MELODIC MINOR SCALE

for r in ["Melodic Minor"]:
    Scale.mode=str(r)
    MelodicMinorSteps=[0,2,3,5,7,9,11]
    MelodicMinorProbs=[15,10,25,5,5,20,20]
    MelodicMinor=[]
    for j in MelodicMinorSteps:
        note=notepool[j+transpose]
        MelodicMinor.append(note)
    Scale.notes=MelodicMinor
    Scale.steps=7
    Scale.probmatrix=MelodicMinorProbs
    mode=Scale(str(r),MelodicMinor,7,MelodicMinorProbs)
    modes.append(mode)

for r in ["Dorian b2 / Assyrian"]:
    Scale.mode=str(r)
    AssyrianSteps=[0,1,3,5,7,9,10]
    AssyrianProbs=[10,25,20,5,5,20,15]
    Assyrian=[]
    for j in AssyrianSteps:
        note=notepool[j+transpose]
        Assyrian.append(note)
    Scale.notes=Assyrian
    Scale.steps=7
    Scale.probmatrix=AssyrianProbs
    mode=Scale(str(r),Assyrian,7,AssyrianProbs)
    modes.append(mode)

for r in ["Lydian Augmented / Asgardian"]:
    Scale.mode=str(r)
    LydianAugSteps=[0,2,4,6,8,9,11]
    LydianAugProbs=[10,10,20,25,15,10,10]
    LydianAugmented=[]
    for j in LydianAugSteps:
        note=notepool[j+transpose]
        LydianAugmented.append(note)
    Scale.notes=LydianAugmented
    Scale.steps=7
    Scale.probmatrix=LydianAugProbs
    mode=Scale(str(r),LydianAugmented,7,LydianAugProbs)
    modes.append(mode)

for r in ["Lydian Dominant"]:
    Scale.mode=str(r)
    LydianDominantSteps=[0,2,4,6,7,9,10]
    LydianDominantProbs=[10,10,15,25,5,15,20]
    LydianDominant=[]
    for j in LydianDominantSteps:
        note=notepool[j+transpose]
        LydianDominant.append(note)
    Scale.notes=LydianDominant
    Scale.steps=7
    Scale.probmatrix=LydianDominantProbs
    mode=Scale(str(r),LydianDominant,7,LydianDominantProbs)
    modes.append(mode)

for r in ["Aeolian Dominant / Mixolydian b6"]:
    Scale.mode=str(r)
    Mixolydianb6Steps=[0,2,4,5,7,8,10]
    Mixolydianb6Probs=[10,10,25,5,10,25,15]
    Mixolydianb6=[]
    for j in Mixolydianb6Steps:
        note=notepool[j+transpose]
        Mixolydianb6.append(note)
    Scale.notes=Mixolydianb6
    Scale.steps=7
    Scale.probmatrix=Mixolydianb6Probs
    mode=Scale(str(r),Mixolydianb6,7,Mixolydianb6Probs)
    modes.append(mode)

for r in ["Half-Diminished / Sisyphean"]:
    Scale.mode=str(r)
    SisypheanSteps=[0,2,3,5,6,8,10]
    SisypheanProbs=[10,10,25,5,25,10,15]
    Sisyphean=[]
    for j in SisypheanSteps:
        note=notepool[j+transpose]
        Sisyphean.append(note)
    Scale.notes=Sisyphean
    Scale.steps=7
    Scale.probmatrix=SisypheanProbs
    mode=Scale(str(r),Sisyphean,7,SisypheanProbs)
    modes.append(mode)

for r in ["Altered Dominant / Palamidian"]:
    Scale.mode=str(r)
    AlteredSteps=[0,1,3,4,6,8,10]
    AlteredProbs=[10,15,15,15,15,15,15]
    Altered=[]
    for j in AlteredSteps:
        note=notepool[j+transpose]
        Altered.append(note)
    Scale.notes=Altered
    Scale.steps=7
    Scale.probmatrix=AlteredProbs
    mode=Scale(str(r),Altered,7,AlteredProbs)
    modes.append(mode)

# DIATONIC MODES OF HARMONIC MINOR SCALE

for r in ["Harmonic Minor"]:
    Scale.mode=str(r)
    HarmonicMinorSteps=[0,2,3,5,7,8,11]
    HarmonicMinorProbs=[10,10,25,5,10,25,25]
    HarmonicMinor=[]
    for j in HarmonicMinorSteps:
        note=notepool[j+transpose]
        HarmonicMinor.append(note)
    Scale.notes=HarmonicMinor
    Scale.steps=7
    Scale.probmatrix=HarmonicMinorProbs
    mode=Scale(str(r),HarmonicMinor,7,HarmonicMinorProbs)
    modes.append(mode)

for r in ["Locrian #6"]:
    Scale.mode=str(r)
    Locrian6SharpSteps=[0,1,3,5,6,9,10]
    Locrian6SharpProbs=[10,15,15,5,25,25,5]
    Locrian6Sharp=[]
    for j in Locrian6SharpSteps:
        note=notepool[j+transpose]
        Locrian6Sharp.append(note)
    Scale.notes=Locrian6Sharp
    Scale.steps=7
    Scale.probmatrix=Locrian6SharpProbs
    mode=Scale(str(r),Locrian6Sharp,7,Locrian6SharpProbs)
    modes.append(mode)

for r in ["Ionian #5"]:
    Scale.mode=str(r)
    IonianAugSteps=[0,2,4,5,8,9,11]
    IonianAugProbs=[10,10,25,5,25,10,15]
    IonianAug=[]
    for j in IonianAugSteps:
        note=notepool[j+transpose]
        IonianAug.append(note)
    Scale.notes=IonianAug
    Scale.steps=7
    Scale.probmatrix=IonianAugProbs
    mode=Scale(str(r),IonianAug,7,IonianAugProbs)
    modes.append(mode)

for r in ["Ukrainian Dorian / Romanian Minor"]:
    Scale.mode=str(r)
    UkraDorianSteps=[0,2,3,6,7,9,10]
    UkraDorianProbs=[10,10,20,25,10,15,10]
    UkraDorian=[]
    for j in UkraDorianSteps:
        note=notepool[j+transpose]
        UkraDorian.append(note)
    Scale.notes=UkraDorian
    Scale.steps=7
    Scale.probmatrix=UkraDorianProbs
    mode=Scale(str(r),UkraDorian,7,UkraDorianProbs)
    modes.append(mode)

for r in ["Phrygian Dominant / Spanish Gypsy"]:
    Scale.mode=str(r)
    SpanishGypsySteps=[0,1,4,5,7,8,10]
    SpanishGypsyProbs=[10,25,25,5,5,15,15]
    SpanishGypsy=[]
    for j in SpanishGypsySteps:
        note=notepool[j+transpose]
        SpanishGypsy.append(note)
    Scale.notes=SpanishGypsy
    Scale.steps=7
    Scale.probmatrix=SpanishGypsyProbs
    mode=Scale(str(r),SpanishGypsy,7,SpanishGypsyProbs)
    modes.append(mode)

for r in ["Lydian #2 / Maqam Mustar"]:
    Scale.mode=str(r)
    MaqamMustarSteps=[0,3,4,6,7,9,11]
    MaqamMustarProbs=[10,15,20,25,10,10,10]
    MaqamMustar=[]
    for j in MaqamMustarSteps:
        note=notepool[j+transpose]
        MaqamMustar.append(note)
    Scale.notes=MaqamMustar
    Scale.steps=7
    Scale.probmatrix=MaqamMustarProbs
    mode=Scale(str(r),MaqamMustar,7,MaqamMustarProbs)
    modes.append(mode)

for r in ["Altered Diminished"]:
    Scale.mode=str(r)
    AltDimSteps=[0,1,3,4,6,8,9]
    AltDimProbs=[10,15,15,10,25,10,15]
    AltDim=[]
    for j in AltDimSteps:
        note=notepool[j+transpose]
        AltDim.append(note)
    Scale.notes=AltDim
    Scale.steps=7
    Scale.probmatrix=AltDimProbs
    mode=Scale(str(r),AltDim,7,AltDimProbs)
    modes.append(mode)

# DIATONIC MODES OF DOUBLE HARMONIC MAJOR SCALE

for r in ["Double Harmonic Major / Byzantine"]:
    Scale.mode=str(r)
    DoubleHarmMajorSteps=[0,1,4,5,7,8,11]
    DoubleHarmMajorProbs=[10,20,20,5,5,20,20]
    DoubleHarmMajor=[]
    for j in DoubleHarmMajorSteps:
        note=notepool[j+transpose]
        DoubleHarmMajor.append(note)
    Scale.notes=DoubleHarmMajor
    Scale.steps=7
    Scale.probmatrix=DoubleHarmMajorProbs
    mode=Scale(str(r),DoubleHarmMajor,7,DoubleHarmMajorProbs)
    modes.append(mode)

for r in ["Lydian #2#6"]:
    Scale.mode=str(r)
    LydianAug26Steps=[0,3,4,6,7,10,11]
    LydianAug26Probs=[10,20,15,25,5,15,10]
    LydianAug26=[]
    for j in LydianAug26Steps:
        note=notepool[j+transpose]
        LydianAug26.append(note)
    Scale.notes=LydianAug26
    Scale.steps=7
    Scale.probmatrix=LydianAug26Probs
    mode=Scale(str(r),LydianAug26,7,LydianAug26Probs)
    modes.append(mode)

for r in ["Ultra-Phrygian"]:
    Scale.mode=str(r)
    UltraphrygianSteps=[0,1,3,4,7,8,9]
    UltraphrygianProbs=[10,25,15,10,5,15,20]
    Ultraphrygian=[]
    for j in UltraphrygianSteps:
        note=notepool[j+transpose]
        Ultraphrygian.append(note)
    Scale.notes=Ultraphrygian
    Scale.steps=7
    Scale.probmatrix=UltraphrygianProbs
    mode=Scale(str(r),Ultraphrygian,7,UltraphrygianProbs)
    modes.append(mode)

for r in ["Hungarian Gypsy Minor"]:
    Scale.mode=str(r)
    HungarianGypsyMinorSteps=[0,2,3,6,7,8,11]
    HungarianGypsyMinorProbs=[10,10,25,20,5,15,15]
    HungarianGypsyMinor=[]
    for j in HungarianGypsyMinorSteps:
        note=notepool[j+transpose]
        HungarianGypsyMinor.append(note)
    Scale.notes=HungarianGypsyMinor
    Scale.steps=7
    Scale.probmatrix=HungarianGypsyMinorProbs
    mode=Scale(str(r),HungarianGypsyMinor,7,HungarianGypsyMinorProbs)
    modes.append(mode)

for r in ["Oriental"]:
    Scale.mode=str(r)
    OrientalSteps=[0,1,4,5,6,9,10]
    OrientalProbs=[10,20,20,5,15,15,15]
    Oriental=[]
    for j in OrientalSteps:
        note=notepool[j+transpose]
        Oriental.append(note)
    Scale.notes=Oriental
    Scale.steps=7
    Scale.probmatrix=OrientalProbs
    mode=Scale(str(r),Oriental,7,OrientalProbs)
    modes.append(mode)

for r in ["Ionian #2#5"]:
    Scale.mode=str(r)
    IonianAug2Steps=[0,3,4,5,8,9,11]
    IonianAug2Probs=[10,20,20,5,15,15,15]
    IonianAug2=[]
    for j in IonianAug2Steps:
        note=notepool[j+transpose]
        IonianAug2.append(note)
    Scale.notes=IonianAug2
    Scale.steps=7
    Scale.probmatrix=IonianAug2Probs
    mode=Scale(str(r),IonianAug2,7,IonianAug2Probs)
    modes.append(mode)

for r in ["Locrian bb3bb7"]:
    Scale.mode=str(r)
    Locrianbb3bb7Steps=[0,1,2,5,6,8,9]
    Locrianbb3bb7Probs=[10,20,25,5,20,10,10]
    Locrianbb3bb7=[]
    for j in Locrianbb3bb7Steps:
        note=notepool[j+transpose]
        Locrianbb3bb7.append(note)
    Scale.notes=Locrianbb3bb7
    Scale.steps=7
    Scale.probmatrix=Locrianbb3bb7Probs
    mode=Scale(str(r),Locrianbb3bb7,7,Locrianbb3bb7Probs)
    modes.append(mode)

# PENTATONIC SCALES

for r in ["Pentatonic Minor / Celtic Amara"]:
    Scale.mode=str(r)
    AmaraSteps=[0,3,5,7,10]
    AmaraProbs=[25,30,10,10,25]
    Amara=[]
    for j in AmaraSteps:
        note=notepool[j+transpose]
        Amara.append(note)
    Scale.notes=Amara
    Scale.steps=5
    Scale.probmatrix=AmaraProbs
    mode=Scale(str(r),Amara,5,AmaraProbs)
    modes.append(mode)

for r in ["Pentatonic Major / Yona Nuki Major"]:
    Scale.mode=str(r)
    YonaNukiMajorSteps=[0,2,4,7,9]
    YonaNukiMajorProbs=[25,20,25,15,15]
    YonaNukiMajor=[]
    for j in YonaNukiMajorSteps:
        note=notepool[j+transpose]
        YonaNukiMajor.append(note)
    Scale.notes=YonaNukiMajor
    Scale.steps=5
    Scale.probmatrix=YonaNukiMajorProbs
    mode=Scale(str(r),YonaNukiMajor,5,YonaNukiMajorProbs)
    modes.append(mode)

for r in ["Altered Pentatonic"]:
    Scale.mode=str(r)
    AltPentatonicSteps=[0,3,5,7,9]
    AltPentatonicProbs=[20,25,15,15,25]
    AltPentatonic=[]
    for j in AltPentatonicSteps:
        note=notepool[j+transpose]
        AltPentatonic.append(note)
    Scale.notes=AltPentatonic
    Scale.steps=5
    Scale.probmatrix=AltPentatonicProbs
    mode=Scale(str(r),AltPentatonic,5,AltPentatonicProbs)
    modes.append(mode)

for r in ["Yona Nuki Minor"]:
    Scale.mode=str(r)
    YonaNukiMinorSteps=[0,2,3,5,8]
    YonaNukiMinorProbs=[20,20,25,10,25]
    YonaNukiMinor=[]
    for j in YonaNukiMinorSteps:
        note=notepool[j+transpose]
        YonaNukiMinor.append(note)
    Scale.notes=YonaNukiMinor
    Scale.steps=5
    Scale.probmatrix=YonaNukiMinorProbs
    mode=Scale(str(r),YonaNukiMinor,5,YonaNukiMinorProbs)
    modes.append(mode)

for r in ["Hirajoshi"]:
    Scale.mode=str(r)
    HirajoshiSteps=[0,2,3,7,8]
    HirajoshiProbs=[25,20,25,15,15]
    Hirajoshi=[]
    for j in HirajoshiSteps:
        note=notepool[j+transpose]
        Hirajoshi.append(note)
    Scale.notes=Hirajoshi
    Scale.steps=5
    Scale.probmatrix=HirajoshiProbs
    mode=Scale(str(r),Hirajoshi,5,HirajoshiProbs)
    modes.append(mode)

for r in ["Sakura"]:
    Scale.mode=str(r)
    SakuraSteps=[0,1,4,5,6]
    SakuraProbs=[20,25,25,10,20]
    Sakura=[]
    for j in SakuraSteps:
        note=notepool[j+transpose]
        Sakura.append(note)
    Scale.notes=Sakura
    Scale.steps=5
    Scale.probmatrix=SakuraProbs
    mode=Scale(str(r),Sakura,5,SakuraProbs)
    modes.append(mode)

for r in ["Insen"]:
    Scale.mode=str(r)
    InsenSteps=[0,1,5,7,10]
    InsenProbs=[20,25,15,15,25]
    Insen=[]
    for j in InsenSteps:
        note=notepool[j+transpose]
        Insen.append(note)
    Scale.notes=Insen
    Scale.steps=5
    Scale.probmatrix=InsenProbs
    mode=Scale(str(r),Insen,5,InsenProbs)
    modes.append(mode)

for r in ["Iwato"]:
    Scale.mode=str(r)
    IwatoSteps=[0,1,5,6,10]
    IwatoProbs=[20,25,15,20,20]
    Iwato=[]
    for j in IwatoSteps:
        note=notepool[j+transpose]
        Iwato.append(note)
    Scale.notes=Iwato
    Scale.steps=5
    Scale.probmatrix=IwatoProbs
    mode=Scale(str(r),Iwato,5,IwatoProbs)
    modes.append(mode)

for r in ["Yo"]:
    Scale.mode=str(r)
    YoSteps=[0,2,5,7,9]
    YoProbs=[20,25,15,15,25]
    Yo=[]
    for j in YoSteps:
        note=notepool[j+transpose]
        Yo.append(note)
    Scale.notes=Yo
    Scale.steps=5
    Scale.probmatrix=YoProbs
    mode=Scale(str(r),Yo,5,YoProbs)
    modes.append(mode)

for r in ["Balinese Pelog"]:
    Scale.mode=str(r)
    BalineseSteps=[0,1,3,7,8]
    BalineseProbs=[20,25,25,10,20]
    BalinesePelog=[]
    for j in BalineseSteps:
        note=notepool[j+transpose]
        BalinesePelog.append(note)
    Scale.notes=BalinesePelog
    Scale.steps=5
    Scale.probmatrix=BalineseProbs
    mode=Scale(str(r),BalinesePelog,5,BalineseProbs)
    modes.append(mode)

for r in ["Chinese Pentatonic"]:
    Scale.mode=str(r)
    ChineseSteps=[0,4,6,7,11]
    ChineseProbs=[20,20,25,15,20]
    Chinese=[]
    for j in ChineseSteps:
        note=notepool[j+transpose]
        Chinese.append(note)
    Scale.notes=Chinese
    Scale.steps=5
    Scale.probmatrix=ChineseProbs
    mode=Scale(str(r),Chinese,5,ChineseProbs)
    modes.append(mode)

for r in ["Egyptian"]:
    Scale.mode=str(r)
    EgyptianSteps=[0,2,5,7,10]
    EgyptianProbs=[20,25,15,15,25]
    Egyptian=[]
    for j in EgyptianSteps:
        note=notepool[j+transpose]
        Egyptian.append(note)
    Scale.notes=Egyptian
    Scale.steps=5
    Scale.probmatrix=EgyptianProbs
    mode=Scale(str(r),Egyptian,5,EgyptianProbs)
    modes.append(mode)

for r in ["Japanese Akebono"]:
    Scale.mode=str(r)
    AkebonoSteps=[0,2,3,7,9]
    AkebonoProbs=[20,25,25,10,20]
    Akebono=[]
    for j in AkebonoSteps:
        note=notepool[j+transpose]
        Akebono.append(note)
    Scale.notes=Akebono
    Scale.steps=5
    Scale.probmatrix=AkebonoProbs
    mode=Scale(str(r),Akebono,5,AkebonoProbs)
    modes.append(mode)

# BEBOP/JAZZ/BLUES/GOSPEL SCALES

for r in ["Bebop Dominant"]:
    Scale.mode=str(r)
    BebopDomSteps=[0,2,4,5,7,9,10,11]
    BebopDomProbs=[10,10,20,10,10,20,10,10]
    BebopDominant=[]
    for j in BebopDomSteps:
        note=notepool[j+transpose]
        BebopDominant.append(note)
    Scale.notes=BebopDominant
    Scale.steps=8
    Scale.probmatrix=BebopDomProbs
    mode=Scale(str(r),BebopDominant,8,BebopDomProbs)
    modes.append(mode)

for r in ["Bebop Major"]:
    Scale.mode=str(r)
    BebopMajorSteps=[0,2,4,5,7,8,9,11]
    BebopMajorProbs=[10,10,20,10,10,20,10,10]
    BebopMajor=[]
    for j in BebopMajorSteps:
        note=notepool[j+transpose]
        BebopMajor.append(note)
    Scale.notes=BebopMajor
    Scale.steps=8
    Scale.probmatrix=BebopMajorProbs
    mode=Scale(str(r),BebopMajor,8,BebopMajorProbs)
    modes.append(mode)

for r in ["Bebop Melodic Minor"]:
    Scale.mode=str(r)
    BebopMelodicMinorSteps=[0,2,3,5,7,8,9,11]
    BebopMelodicMinorProbs=[10,10,20,10,10,20,10,10]
    BebopMelodicMinor=[]
    for j in BebopMelodicMinorSteps:
        note=notepool[j+transpose]
        BebopMelodicMinor.append(note)
    Scale.notes=BebopMelodicMinor
    Scale.steps=8
    Scale.probmatrix=BebopMelodicMinorProbs
    mode=Scale(str(r),BebopMelodicMinor,8,BebopMelodicMinorProbs)
    modes.append(mode)

for r in ["Dom7b5 Diminished"]:
    Scale.mode=str(r)
    Dom7b5DimSteps=[0,2,4,5,6,8,10,11]
    Dom7b5DimProbs=[10,10,20,10,20,10,10,10]
    Dom7b5Diminished=[]
    for j in Dom7b5DimSteps:
        note=notepool[j+transpose]
        Dom7b5Diminished.append(note)
    Scale.notes=Dom7b5Diminished
    Scale.steps=8
    Scale.probmatrix=Dom7b5DimProbs
    mode=Scale(str(r),Dom7b5Diminished,8,Dom7b5DimProbs)
    modes.append(mode)

for r in ["Six-Note Blues Scale"]:
    Scale.mode=str(r)
    SixNoteBluesSteps=[0,3,5,6,9,10]
    SixNoteBluesProbs=[15,20,15,15,15,20]
    SixNoteBlues=[]
    for j in SixNoteBluesSteps:
        note=notepool[j+transpose]
        SixNoteBlues.append(note)
    Scale.notes=SixNoteBlues
    Scale.steps=6
    Scale.probmatrix=SixNoteBluesProbs
    mode=Scale(str(r),SixNoteBlues,6,SixNoteBluesProbs)
    modes.append(mode)

for r in ["Nine-Note Blues Scale"]:
    Scale.mode=str(r)
    NineNoteBluesSteps=[0,2,3,4,5,7,9,10,11]
    NineNoteBluesProbs=[10,10,15,15,10,5,15,10,10]
    NineNoteBlues=[]
    for j in NineNoteBluesSteps:
        note=notepool[j+transpose]
        NineNoteBlues.append(note)
    Scale.notes=NineNoteBlues
    Scale.steps=9
    Scale.probmatrix=NineNoteBluesProbs
    mode=Scale(str(r),NineNoteBlues,9,NineNoteBluesProbs)
    modes.append(mode)

for r in ["Gospel / Major Blues Scale"]:
    Scale.mode=str(r)
    GospelSteps=[0,2,3,4,7,9]
    GospelProbs=[10,15,15,20,20,20]
    Gospel=[]
    for j in GospelSteps:
        note=notepool[j+transpose]
        Gospel.append(note)
    Scale.notes=Gospel
    Scale.steps=6
    Scale.probmatrix=GospelProbs
    mode=Scale(str(r),Gospel,6,GospelProbs)
    modes.append(mode)

# HEXATONIC SCALES

for r in ["Symmetrical Augmented"]:
    Scale.mode=str(r)
    SymmetricalAugSteps=[0,3,4,7,8,10]
    SymmetricalAugProbs=[10,20,20,10,20,20]
    SymmetricalAugmented=[]
    for j in SymmetricalAugSteps:
        note=notepool[j+transpose]
        SymmetricalAugmented.append(note)
    Scale.notes=SymmetricalAugmented
    Scale.steps=6
    Scale.probmatrix=SymmetricalAugProbs
    mode=Scale(str(r),SymmetricalAugmented,6,SymmetricalAugProbs)
    modes.append(mode)

for r in ["Iberian Hexatonic"]:
    Scale.mode=str(r)
    IberianSteps=[0,1,4,5,7,10]
    IberianProbs=[10,20,20,10,20,20]
    IberianHexatonic=[]
    for j in IberianSteps:
        note=notepool[j+transpose]
        IberianHexatonic.append(note)
    Scale.notes=IberianHexatonic
    Scale.steps=6
    Scale.probmatrix=IberianProbs
    mode=Scale(str(r),IberianHexatonic,6,IberianProbs)
    modes.append(mode)

for r in ["Prometheus Scale"]:
    Scale.mode=str(r)
    PromethianSteps=[0,2,4,6,7,10]
    PromethianProbs=[10,20,20,25,10,15]
    Prometheus=[]
    for j in PromethianSteps:
        note=notepool[j+transpose]
        Prometheus.append(note)
    Scale.notes=Prometheus
    Scale.steps=6
    Scale.probmatrix=PromethianProbs
    mode=Scale(str(r),Prometheus,6,PromethianProbs)
    modes.append(mode)

for r in ["Prometheus Neapolitan"]:
    Scale.mode=str(r)
    PromNeapolitanSteps=[0,1,4,6,9,10]
    PromNeapolitanProbs=[10,20,20,20,15,15]
    PrometheusNeapolitan=[]
    for j in PromNeapolitanSteps:
        note=notepool[j+transpose]
        PrometheusNeapolitan.append(note)
    Scale.notes=PrometheusNeapolitan
    Scale.steps=6
    Scale.probmatrix=PromNeapolitanProbs
    mode=Scale(str(r),PrometheusNeapolitan,6,PromNeapolitanProbs)
    modes.append(mode)

for r in ["Prometheus Liszt"]:
    Scale.mode=str(r)
    PromLizSteps=[0,1,4,5,8,9]
    PromLizProbs=[10,20,20,10,20,20]
    PrometheusLiszt=[]
    for j in PromLizSteps:
        note=notepool[j+transpose]
        PrometheusLiszt.append(note)
    Scale.notes=PrometheusLiszt
    Scale.steps=6
    Scale.probmatrix=PromLizProbs
    mode=Scale(str(r),PrometheusLiszt,6,PromLizProbs)
    modes.append(mode)

for r in ["Banshikicho"]:
    Scale.mode=str(r)
    BanshikichoSteps=[0,2,3,4,7,9]
    BanshikichoProbs=[10,20,20,20,10,20]
    Banshikicho=[]
    for j in BanshikichoSteps:
        note=notepool[j+transpose]
        Banshikicho.append(note)
    Scale.notes=Banshikicho
    Scale.steps=6
    Scale.probmatrix=BanshikichoProbs
    mode=Scale(str(r),Banshikicho,6,BanshikichoProbs)
    modes.append(mode)

for r in ["Kurd / Annaziska Handpan Scale"]:
    Scale.mode=str(r)
    KurdishSteps=[0,2,3,5,7,8]
    KurdishProbs=[10,20,20,10,20,20]
    Annaziska=[]
    for j in KurdishSteps:
        note=notepool[j+transpose]
        Annaziska.append(note)
    Scale.notes=Annaziska
    Scale.steps=6
    Scale.probmatrix=KurdishProbs
    mode=Scale(str(r),Annaziska,6,KurdishProbs)
    modes.append(mode)

# ETHNIC & SYMMETRICAL SCALES

for r in ["Harmonic Minor b5"]:
    Scale.mode=str(r)
    HarmMinorb5Steps=[0,2,3,5,6,8,11]
    HarmMinorb5Probs=[10,10,20,10,25,15,10]
    HarmonicMinorb5=[]
    for j in HarmMinorb5Steps:
        note=notepool[j+transpose]
        HarmonicMinorb5.append(note)
    Scale.notes=HarmonicMinorb5
    Scale.steps=7
    Scale.probmatrix=HarmMinorb5Probs
    mode=Scale(str(r),HarmonicMinorb5,7,HarmMinorb5Probs)
    modes.append(mode)

for r in ["Hungarian Major"]:
    Scale.mode=str(r)
    HungarianMajorSteps=[0,3,4,6,7,9,10]
    HungarianMajorProbs=[10,15,20,15,10,15,15]
    HungarianMajor=[]
    for j in HungarianMajorSteps:
        note=notepool[j+transpose]
        HungarianMajor.append(note)
    Scale.notes=HungarianMajor
    Scale.steps=7
    Scale.probmatrix=HungarianMajorProbs
    mode=Scale(str(r),HungarianMajor,7,HungarianMajorProbs)
    modes.append(mode)

for r in ["Diminished Octatonic"]:
    Scale.mode=str(r)
    DimOctatonicSteps=[0,2,3,5,6,8,9,11]
    DimOctatonicProbs=[10,10,20,10,15,15,10,10]
    DiminishedOctatonic=[]
    for j in DimOctatonicSteps:
        note=notepool[j+transpose]
        DiminishedOctatonic.append(note)
    Scale.notes=DiminishedOctatonic
    Scale.steps=8
    Scale.probmatrix=DimOctatonicProbs
    mode=Scale(str(r),DiminishedOctatonic,8,DimOctatonicProbs)
    modes.append(mode)

for r in ["Whole-Tone Scale"]:
    Scale.mode=str(r)
    WholeToneSteps=[0,2,4,6,8,10]
    WholeToneProbs=[10,10,20,25,25,10]
    WholeTone=[]
    for j in WholeToneSteps:
        note=notepool[j+transpose]
        WholeTone.append(note)
    Scale.notes=WholeTone
    Scale.steps=6
    Scale.probmatrix=WholeToneProbs
    mode=Scale(str(r),WholeTone,6,WholeToneProbs)
    modes.append(mode)

for r in ["Ultra-Locrian"]:
    Scale.mode=str(r)
    UltralocrianSteps=[0,1,3,4,6,7,9]
    UltralocrianProbs=[10,20,20,10,15,5,20]
    Ultralocrian=[]
    for j in UltralocrianSteps:
        note=notepool[j+transpose]
        Ultralocrian.append(note)
    Scale.notes=Ultralocrian
    Scale.steps=7
    Scale.probmatrix=UltralocrianProbs
    mode=Scale(str(r),Ultralocrian,7,UltralocrianProbs)
    modes.append(mode)

for r in ["Japanese Nohkan Flute Scale"]:
    Scale.mode=str(r)
    NohkanSteps=[0,2,5,6,8,9,11]
    NohkanProbs=[10,15,10,20,15,15,15]
    NohkanFlute=[]
    for j in NohkanSteps:
        note=notepool[j+transpose]
        NohkanFlute.append(note)
    Scale.notes=NohkanFlute
    Scale.steps=7
    Scale.probmatrix=NohkanProbs
    mode=Scale(str(r),NohkanFlute,7,NohkanProbs)
    modes.append(mode)

for r in ["Persian"]:
    Scale.mode=str(r)
    PersianSteps=[0,1,4,5,6,8,10]
    PersianProbs=[10,25,15,10,15,15,10]
    Persian=[]
    for j in PersianSteps:
        note=notepool[j+transpose]
        Persian.append(note)
    Scale.notes=Persian
    Scale.steps=7
    Scale.probmatrix=PersianProbs
    mode=Scale(str(r),Persian,7,PersianProbs)
    modes.append(mode)

for r in ["Arabic Scale"]:
    Scale.mode=str(r)
    ArabicSteps=[0,2,4,5,6,8,10]
    ArabicProbs=[10,15,20,10,20,15,10]
    Arabic=[]
    for j in ArabicSteps:
        note=notepool[j+transpose]
        Arabic.append(note)
    Scale.notes=Arabic
    Scale.steps=7
    Scale.probmatrix=ArabicProbs
    mode=Scale(str(r),Arabic,7,ArabicProbs)
    modes.append(mode)

for r in ["Neapolitan Minor"]:
    Scale.mode=str(r)
    NeapolitanMinorSteps=[0,1,3,5,7,8,11]
    NeapolitanMinorProbs=[10,20,20,10,10,15,15]
    NeapolitanMinor=[]
    for j in NeapolitanMinorSteps:
        note=notepool[j+transpose]
        NeapolitanMinor.append(note)
    Scale.notes=NeapolitanMinor
    Scale.steps=7
    Scale.probmatrix=NeapolitanMinorProbs
    mode=Scale(str(r),NeapolitanMinor,7,NeapolitanMinorProbs)
    modes.append(mode)

for r in ["Neapolitan Major"]:
    Scale.mode=str(r)
    NeapolitanMajorSteps=[0,1,3,5,7,9,11]
    NeapolitanMajorProbs=[10,20,20,10,10,15,15]
    NeapolitanMajor=[]
    for j in NeapolitanMajorSteps:
        note=notepool[j+transpose]
        NeapolitanMajor.append(note)
    Scale.notes=NeapolitanMajor
    Scale.steps=7
    Scale.probmatrix=NeapolitanMajorProbs
    mode=Scale(str(r),NeapolitanMajor,7,NeapolitanMajorProbs)
    modes.append(mode)

for r in ["Hijaz Kar Maqam"]:
    Scale.mode=str(r)
    HijazKarMaqamSteps=[0,1,4,5,7,8,11]
    HijazKarMaqamProbs=[10,20,20,10,10,15,15]
    HijazKarMaqam=[]
    for j in HijazKarMaqamSteps:
        note=notepool[j+transpose]
        HijazKarMaqam.append(note)
    Scale.notes=HijazKarMaqam
    Scale.steps=7
    Scale.probmatrix=HijazKarMaqamProbs
    mode=Scale(str(r),HijazKarMaqam,7,HijazKarMaqamProbs)
    modes.append(mode)

for r in ["Algerian Minor"]:
    Scale.mode=str(r)
    AlgerianSteps=[0,2,3,5,6,7,8,11]
    AlgerianProbs=[10,10,20,10,15,10,15,10]
    AlgerianMinor=[]
    for j in AlgerianSteps:
        note=notepool[j+transpose]
        AlgerianMinor.append(note)
    Scale.notes=AlgerianMinor
    Scale.steps=8
    Scale.probmatrix=AlgerianProbs
    mode=Scale(str(r),AlgerianMinor,8,AlgerianProbs)
    modes.append(mode)

for r in ["8-Note Spanish/Jewish"]:
    Scale.mode=str(r)
    JewishSteps=[0,1,3,4,5,6,8,10]
    JewishProbs=[10,20,15,15,10,10,10,10]
    Jewish8=[]
    for j in JewishSteps:
        note=notepool[j+transpose]
        Jewish8.append(note)
    Scale.notes=Jewish8
    Scale.steps=8
    Scale.probmatrix=JewishProbs
    mode=Scale(str(r),Jewish8,8,JewishProbs)
    modes.append(mode)

for r in ["Scala Enigmatica (ascending)"]:
    Scale.mode=str(r)
    EnigmaticASteps=[0,1,4,6,8,10,11]
    EnigmaticAProbs=[10,20,15,15,20,10,10]
    EnigmaticA=[]
    for j in EnigmaticASteps:
        note=notepool[j+transpose]
        EnigmaticA.append(note)
    Scale.notes=EnigmaticA
    Scale.steps=7
    Scale.probmatrix=EnigmaticAProbs
    mode=Scale(str(r),EnigmaticA,7,EnigmaticAProbs)
    modes.append(mode)

for r in ["Scala Enigmatica (descending)"]:
    Scale.mode=str(r)
    EnigmaticDSteps=[0,11,10,8,5,4,1]
    EnigmaticDProbs=[10,10,20,15,15,20,10]
    EnigmaticD=[]
    for j in EnigmaticDSteps:
        note=notepool[j+transpose]
        EnigmaticD.append(note)
    Scale.notes=EnigmaticD
    Scale.steps=7
    Scale.probmatrix=EnigmaticDProbs
    mode=Scale(str(r),EnigmaticD,7,EnigmaticDProbs)
    modes.append(mode)

for r in ["Raga Asavari"]:
    Scale.mode=str(r)
    AsavariSteps=[0,1,5,7,8,0,10,8,7,5,3,1,0]
    AsavariProbs=[5,15,5,5,10,5,10,10,5,5,15,5,5]
    Asavari=[]
    for j in AsavariSteps:
        note=notepool[j+transpose]
        Asavari.append(note)
    Scale.notes=Asavari
    Scale.steps=13
    Scale.probmatrix=AsavariProbs
    mode=Scale(str(r),Asavari,13,AsavariProbs)
    modes.append(mode)

for r in ["Enigmatic Minor"]:
    Scale.mode=str(r)
    EnigmaticMinorSteps=[0,1,3,6,7,10,11]
    EnigmaticMinorProbs=[10,20,20,15,15,10,10]
    EnigmaticMinor=[]
    for j in EnigmaticMinorSteps:
        note=notepool[j+transpose]
        EnigmaticMinor.append(note)
    Scale.notes=EnigmaticMinor
    Scale.steps=7
    Scale.probmatrix=EnigmaticMinorProbs
    mode=Scale(str(r),EnigmaticMinor,7,EnigmaticMinorProbs)
    modes.append(mode)
    
# Select Mode

whim=random.randint(0,len(modes)-1)
choice=modes[whim]
moodi=choice.notes
print("Mode:",choice.mode,"in",root)
print("Notes spelled out:")
print(moodi)

# RHYTHM SEQUENCING

class Rhythm:
    def __init__(self,meter,style,sequence):
        self.meter=meter
        self.style=style
        self.sequence=sequence

# Rhythm Blocks

Short=[[1],[0.5,0.5],[0.75,0.25],[0.25,0.75]]
Long=[[1,0.5],[0.5,1],[0.5,0.5,0.5],[1.5],[0.75,0.75]]

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

    for s in ["Bumble-Bee Interlude"]:
        Rhythm.style=str(s)

        pattern24=[0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25]
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

for time in ["21/8"]:
    Rhythm.meter=str(time)

    for s in ["Charles Ives Rip-Off"]:
        Rhythm.style=str(s)

        for i in Long:                           
            pattern218=7*i
            Rhythm.sequence=pattern218
            pattern=Rhythm(str(time),str(s),pattern218)
            patterns.append(pattern)

# SELECT METER & PATTERN

xopowo=random.randint(0,len(patterns)-1)
ChoosePattern=patterns[xopowo]
print("")
print("Meter:",ChoosePattern.meter)
print("Style:",ChoosePattern.style)
print("Sequence in Beats:")
print(ChoosePattern.sequence)

boogie=ChoosePattern.sequence

# Create a Random Motif (moodi=mode/boogie=rhythm)

class RndPattern:
    def __init__(self,pitch,duration):
        self.pitch=pitch
        self.duration=duration

RandomMotif=[]

for rstep in boogie:
    choosepitch=random.choices(moodi,weights=(choice.probmatrix),k=1)[0]
    RndPattern.duration=rstep
    NOTE=RndPattern(choosepitch,rstep)
    RandomMotif.append(NOTE)

# Modulated Launderings

modulations={
    "Ionian":[HarmonicMajor,Mixolydian,MelodicMinor],
    "Dorian":[Aeolian,Assyrian,Dorianb5],
    "Phrygian":[SpanishGypsy,Locrian,Aeolian],
    "Lydian":[Lydianb3,LydianDominant,LydianAugmented],
    "Mixolydian":[Mixolydianb2,Mixolydianb6,Ionian],
    "Aeolian":[Phrygian,Mixolydianb6,HarmonicMinor],
    "Locrian":[Locrian6Sharp,Locrianbb7,Ultralocrian],
    "Harmonic Major":[HarmonicMinor,Mixolydianb6,Ionian],
    "Dorian b5":[Dorian,Locrian,Oriental],
    "Phrygian b4":[SpanishGypsy,Phrygian,Ultraphrygian],
    "Lydian b3":[Lydian,MelodicMinor,UkraDorian],
    "Mixolydian b2":[Mixolydian,Phrygian,SpanishGypsy],
    "Lydian Augmented #2":[LydianAugmented,LydianAug26,HungarianGypsyMinor],
    "Locrian bb7":[Locrianbb3bb7,Locrian,DiminishedOctatonic],
    "Melodic Minor":[Dorian,Ionian,Lydianb3],
    "Dorian b2 / Assyrian":[Dorian,Phrygian,Mixolydianb2],
    "Lydian Augmented / Asgardian":[Lydian,LydianAug2,IonianAug],
    "Lydian Dominant":[Mixolydian,Lydian,MaqamMustar],
    "Aeolian Dominant / Mixolydian b6":[Mixolydian,Altered,Aeolian],
    "Half-Diminished / Sisyphean":[Locrian,Aeolian,Altered],
    "Altered Dominant / Palamidian":[Mixolydian,Locrian,Locrian6Sharp],
    "Harmonic Minor":[Dorian,Aeolian,HarmonicMajor],
    "Locrian #6":[Locrian,Dorianb5,Dom7b5Diminished],
    "Ionian #5":[Ionian,LydianAugmented,IonianAug2],
    "Ukrainian Dorian / Romanian Minor":[HungarianGypsyMinor,MaqamMustar,EnigmaticMinor],
    "Phrygian Dominant / Spanish Gypsy":[Phrygian,Altered,DoubleHarmMajor],
    "Lydian #2 / Maqam Mustar":[LydianAug26,Lydian,IonianAug2],
    "Altered Diminished":[Altered,Ultraphrygian,Ultralocrian],
    "Double Harmonic Major / Byzantine":[SpanishGypsy,HarmonicMajor,Phrygian],
    "Lydian #2#6":[MaqamMustar,PrometheusNeapolitan,HungarianMajor],
    "Ultra-Phrygian":[Phrygianb4,Phrygian,SpanishGypsy],
    "Hungarian Gypsy Minor":[DiminishedOctatonic,Ultralocrian,HarmonicMinorb5],
    "Oriental":[Mixolydianb2,Locrian,IberianHexatonic],
    "Ionian #2#5":[MaqamMustar,IonianAug,LydianAugmented],
    "Locrian bb3bb7":[Locrian6Sharp,Locrian,Ultralocrian],
    "Pentatonic Minor / Celtic Amara":[AltPentatonic,YonaNukiMinor,Hirajoshi],
    "Pentatonic Major / Yona Nuki Major":[Yo,Chinese,Egyptian],
    "Altered Pentatonic":[Akebono,Hirajoshi,BalinesePelog],
    "Yona Nuki Minor":[Hirajoshi,Amara,Akebono],
    "Hirajoshi":[YonaNukiMinor,Akebono,Sakura],
    "Sakura":[Hirajoshi,YonaNukiMajor,Yo],
    "Insen":[Hirajoshi,Sakura,Iwato],
    "Iwato":[Insen,Hirajoshi,Sakura],
    "Yo":[Egyptian,YonaNukiMinor,Hirajoshi],
    "Balinese Pelog":[Sakura,YonaNukiMinor,Akebono],
    "Chinese Pentatonic":[YonaNukiMajor,Egyptian,Akebono],
    "Egyptian":[Amara,Hirajoshi,Yo],
    "Japanese Akebono":[YonaNukiMajor,Hirajoshi,Egyptian],
    "Bebop Dominant":[Mixolydian,Ionian,Mixolydianb2],
    "Bebop Major":[Ionian,Mixolydianb6,LydianAugmented],
    "Bebop Melodic Minor":[Aeolian,IonianAug,MelodicMinor],
    "Dom7b5 Diminished":[Mixolydianb6,HarmonicMajor,Sisyphean],
    "Six-Note Blues Scale":[IberianHexatonic,Gospel,Banshikicho],
    "Nine-Note Blues Scale":[LydianDominant,Mixolydian,Mixolydianb2],
    "Gospel / Major Blues Scale":[SixNoteBlues,Dorian,MelodicMinor],
    "Symmetrical Augmented":[MaqamMustar,HarmonicMajor,IonianAug2],
    "Iberian Hexatonic":[Mixolydianb2,PrometheusNeapolitan,PrometheusLiszt],
    "Prometheus Scale":[LydianDominant,PrometheusNeapolitan,PrometheusLiszt],
    "Prometheus Neapolitan":[Prometheus,PrometheusLiszt,UkraDorian],
    "Prometheus Liszt":[SpanishGypsy,Phrygian,Ultraphrygian],
    "Banshikicho":[Gospel,Annaziska,IberianHexatonic],
    "Kurd / Annaziska Handpan Scale":[BalinesePelog,YonaNukiMinor,Aeolian],
    "Harmonic Minor b5":[HarmonicMinor,AlgerianMinor,DiminishedOctatonic],
    "Hungarian Major":[MaqamMustar,LydianAug26,LydianDominant],
    "Diminished Octatonic":[HarmonicMinorb5,HarmonicMinor,Locrianbb7],
    "Whole-Tone Scale":[LydianAugmented,IonianAug,NohkanFlute],
    "Ultra-Locrian":[Locrianbb7,DiminishedOctatonic,Locrian6Sharp],
    "Japanese Nohkan Flute Scale":[LydianAugmented,IonianAug,MaqamMustar],
    "Persian":[AlgerianMinor,SpanishGypsy,Phrygian],
    "Arabic Scale":[Mixolydianb6,Locrian,Aeolian],
    "Neapolitan Minor":[Phrygian,Aeolian,HarmonicMinor],
    "Neapolitan Major":[Phrygian,MelodicMinor,Dorian],
    "Hijaz Kar Maqam":[SpanishGypsy,HarmonicMajor,NeapolitanMajor],
    "Algerian Minor":[HarmonicMinor,HarmonicMinorb5,Locrian],
    "8-Note Spanish/Jewish":[Phrygian,Aeolian,Mixolydianb6],
    "Scala Enigmatica (ascending)":[UkraDorian,PrometheusNeapolitan,MaqamMustar],
    "Scala Enigmatica (descending)":[LydianAug26,Ultralocrian,EnigmaticMinor],
    "Raga Asavari":[Persian,Phrygian,SpanishGypsy],
    "Enigmatic Minor":[UkraDorian,Ultraphrygian,HungarianGypsyMinor]    
    }

# checking:    
# for key,val in modulations.items():
# print(f"{key}-->{val}")

modulaatio=random.choice(modulations[choice.mode])

# Create Modulated Sequence

class ModulatedSeq:
    def __init__(self,pitch,duration):
        self.pitch=pitch
        self.duration=duration
        
modulated=[]

for rstep in boogie:
    choosepitch=random.choice(modulaatio)
    ModulatedSeq.duration=rstep
    NOTE=ModulatedSeq(choosepitch,rstep)
    modulated.append(NOTE)

ModMotif=RandomMotif+modulated

# Convert to MIDI Values in Keyboard Ranges

class MIDIPattern:
    def __init__(self,region,midinotes):
        self.region=region
        self.midinotes=midinotes

for reg in ["Subsonic"]:
    MIDIPattern.region=str(reg)

    Subsonic=[]

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

    for item in ModMotif:
        sound=item.pitch
        Subsonic.append(midinotes[sound])
    MIDIPattern.midinotes=Subsonic

for reg in ["Basso Ostinato C1 to B1"]:
    MIDIPattern.region=str(reg)

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

    for item in ModMotif:
        sound=item.pitch
        BassoOstinato.append(midinotes[sound])
    MIDIPattern.midinotes=BassoOstinato

for reg in ["Double Bass Range C2 to B2"]:
    MIDIPattern.region=str(reg)

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

    for item in ModMotif:
        sound=item.pitch
        DoubleBass.append(midinotes[sound])
    MIDIPattern.midinotes=DoubleBass

for reg in ["Viola/Cello Range C3 to B3"]:
    MIDIPattern.region=str(reg)

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

    for item in ModMotif:
        sound=item.pitch
        ViolaCello.append(midinotes[sound])
    MIDIPattern.midinotes=ViolaCello

for reg in ["Middle-C Range from C4 to B4"]:
    MIDIPattern.region=str(reg)

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

    for item in ModMotif:
        sound=item.pitch
        MiddleC.append(midinotes[sound])
    MIDIPattern.midinotes=MiddleC

for reg in ["Melody Range from C5 to B5"]:
    MIDIPattern.region=str(reg)

    HighReg=[]

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

    for item in ModMotif:
        sound=item.pitch
        HighReg.append(midinotes[sound])
    MIDIPattern.midinotes=HighReg

for reg in ["Overtones C6 to B6"]:
    MIDIPattern.region=str(reg)

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

    for item in ModMotif:
        sound=item.pitch
        Overtones.append(midinotes[sound])
    MIDIPattern.midinotes=Overtones

for reg in ["Canine Boogie from C7 to B7"]:
    MIDIPattern.region=str(reg)

    CanineBoogie=[]

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

    for item in ModMotif:
        sound=item.pitch
        CanineBoogie.append(midinotes[sound])
    MIDIPattern.midinotes=CanineBoogie

# Composite MIDI-Keyboard Ranges

for reg in ["Low Quarter"]:
    MIDIPattern.region=str(reg)
    LowQ=Subsonic+BassoOstinato
    MIDIPattern.midinotes=LowQ

for reg in ["Low to Midland"]:
    MIDIPattern.region=str(reg)
    LowMid=DoubleBass+ViolaCello
    MIDIPattern.midinotes=LowMid

for reg in ["From Mid to High"]:
    MIDIPattern.region=str(reg)
    MidHigh=MiddleC+HighReg
    MIDIPattern.midinotes=MidHigh

for reg in ["Canine Overtones"]:
    MIDIPattern.region=str(reg)
    CanineOD=Overtones+CanineBoogie
    MIDIPattern.midinotes=CanineOD

# Select Keyboard Range

regions=[Subsonic,BassoOstinato,DoubleBass,ViolaCello,MiddleC,HighReg,
         Overtones,CanineBoogie,LowQ,LowMid,MidHigh,CanineOD]

selection=random.randint(0,len(regions)-1)
KBRange=regions[selection]

# Define Tempo

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

# CREATE A MIDI FILE

mf=MIDIFile(1)
track=0
time=0
channel=0
volume=100
nn=0

name=ChoosePattern.meter+" Riff in "+root+" "+choice.mode
mf.addTrackName(track,time,name)
newname=name.replace("/","_")

mf.addTempo(track,time,tracktempo)

for beat in boogie*2:
    pitch=KBRange[nn]
    duration=beat
    mf.addNote(track,channel,pitch,time,duration,volume)
    time=time+duration
    nn=nn+1

with open(newname+".mid","wb") as outf:
    mf.writeFile(outf)







        

    







    

    

    
    


    

