# Oblique Strategies V3.0

import random

OneOctave={"A":0,"A#/Bb":1,"B":2,"C":3,"C#/Db":4,"D":5,"D#/Eb":6,
            "E":7,"F":8,"F#/Gb":9,"G":10,"G#/Ab":11}

for key in OneOctave:
    transpose=OneOctave[key]
    
root,transpose=random.choice(list(OneOctave.items()))
pool=list(OneOctave.keys())+list(OneOctave.keys())

class Scale:
    def __init__(self,mode,notes,steps):
        self.mode=mode
        self.notes=notes
        self.steps=steps
        
modes=[]

# Diatonic Modes of Major Scale

for r in ["Ionian"]:
    Scale.mode=str(r)
    IonianSteps=[0,2,4,5,7,9,11]
    Ionian=[]
    for j in IonianSteps:
        note=pool[j+transpose]
        Ionian.append(note)
    Scale.notes=Ionian
    Scale.steps=7
    mode=Scale(str(r),Ionian,7)
    modes.append(mode)

for r in ["Dorian"]:
    Scale.mode=str(r)
    DorianSteps=[0,2,3,5,7,9,10]
    Dorian=[]
    for j in DorianSteps:
        note=pool[j+transpose]
        Dorian.append(note)
    Scale.notes=Dorian
    Scale.steps=7
    mode=Scale(str(r),Dorian,7)
    modes.append(mode)

for r in ["Phrygian"]:
    Scale.mode=str(r)
    PhrygianSteps=[0,1,3,5,7,8,10]
    Phrygian=[]
    for j in PhrygianSteps:
        note=pool[j+transpose]
        Phrygian.append(note)
    Scale.notes=Phrygian
    Scale.steps=7
    mode=Scale(str(r),Phrygian,7)
    modes.append(mode)

for r in ["Lydian"]:
    Scale.mode=str(r)
    LydianSteps=[0,2,4,6,7,9,11]
    Lydian=[]
    for j in LydianSteps:
        note=pool[j+transpose]
        Lydian.append(note)
    Scale.notes=Lydian
    Scale.steps=7
    mode=Scale(str(r),Lydian,7)
    modes.append(mode)

for r in ["Mixolydian"]:
    Scale.mode=str(r)
    MixolydianSteps=[0,2,4,5,7,9,10]
    Mixolydian=[]
    for j in MixolydianSteps:
        note=pool[j+transpose]
        Mixolydian.append(note)
    Scale.notes=Mixolydian
    Scale.steps=7
    mode=Scale(str(r),Mixolydian,7)
    modes.append(mode)

for r in ["Aeolian"]:
    Scale.mode=str(r)
    AeolianSteps=[0,2,3,5,7,8,10]
    Aeolian=[]
    for j in AeolianSteps:
        note=pool[j+transpose]
        Aeolian.append(note)
    Scale.notes=Aeolian
    Scale.steps=7
    mode=Scale(str(r),Aeolian,7)
    modes.append(mode)

for r in ["Locrian"]:
    Scale.mode=str(r)
    LocrianSteps=[0,1,3,5,6,8,10]
    Locrian=[]
    for j in LocrianSteps:
        note=pool[j+transpose]
        Locrian.append(note)
    Scale.notes=Locrian
    Scale.steps=7
    mode=Scale(str(r),Locrian,7)
    modes.append(mode)

# Diatonic Modes of Harmonic Major Scale

for r in ["Harmonic Major"]:
    Scale.mode=str(r)
    HarmonicMajorSteps=[0,2,4,5,7,8,11]
    HarmonicMajor=[]
    for j in HarmonicMajorSteps:
        note=pool[j+transpose]
        HarmonicMajor.append(note)
    Scale.notes=HarmonicMajor
    Scale.steps=7
    mode=Scale(str(r),HarmonicMajor,7)
    modes.append(mode)

for r in ["Dorian b5"]:
    Scale.mode=str(r)
    Dorianb5Steps=[0,2,3,5,6,9,10]
    Dorianb5=[]
    for j in Dorianb5Steps:
        note=pool[j+transpose]
        Dorianb5.append(note)
    Scale.notes=Dorianb5
    Scale.steps=7
    mode=Scale(str(r),Dorianb5,7)
    modes.append(mode)

for r in ["Phrygian b4"]:
    Scale.mode=str(r)
    Phrygianb4Steps=[0,1,3,4,7,8,10]
    Phrygianb4=[]
    for j in Phrygianb4Steps:
        note=pool[j+transpose]
        Phrygianb4.append(note)
    Scale.notes=Phrygianb4
    Scale.steps=7
    mode=Scale(str(r),Phrygianb4,7)
    modes.append(mode)

for r in ["Lydian b3"]:
    Scale.mode=str(r)
    Lydianb3Steps=[0,2,3,6,7,9,11]
    Lydianb3=[]
    for j in Lydianb3Steps:
        note=pool[j+transpose]
        Lydianb3.append(note)
    Scale.notes=Lydianb3
    Scale.steps=7
    mode=Scale(str(r),Lydianb3,7)
    modes.append(mode)

for r in ["Mixolydian b2"]:
    Scale.mode=str(r)
    Mixolydianb2Steps=[0,1,4,5,7,9,10]
    Mixolydianb2=[]
    for j in Mixolydianb2Steps:
        note=pool[j+transpose]
        Mixolydianb2.append(note)
    Scale.notes=Mixolydianb2
    Scale.steps=7
    mode=Scale(str(r),Mixolydianb2,7)
    modes.append(mode)

for r in ["Lydian Augmented #2"]:
    Scale.mode=str(r)
    LydianAug2Steps=[0,3,4,6,8,9,11]
    LydianAug2=[]
    for j in LydianAug2Steps:
        note=pool[j+transpose]
        LydianAug2.append(note)
    Scale.notes=LydianAug2
    Scale.steps=7
    mode=Scale(str(r),LydianAug2,7)
    modes.append(mode)

for r in ["Locrian bb7"]:
    Scale.mode=str(r)
    Locrianbb7Steps=[0,1,3,5,6,8,9]
    Locrianbb7=[]
    for j in Locrianbb7Steps:
        note=pool[j+transpose]
        Locrianbb7.append(note)
    Scale.notes=Locrianbb7
    Scale.steps=7
    mode=Scale(str(r),Locrianbb7,7)
    modes.append(mode)

# Diatonic Modes of Melodic Minor Scale

for r in ["Melodic Minor"]:
    Scale.mode=str(r)
    MelodicMinorSteps=[0,2,3,5,7,9,11]
    MelodicMinor=[]
    for j in MelodicMinorSteps:
        note=pool[j+transpose]
        MelodicMinor.append(note)
    Scale.notes=MelodicMinor
    Scale.steps=7
    mode=Scale(str(r),MelodicMinor,7)
    modes.append(mode)

for r in ["Dorian b2/Assyrian"]:
    Scale.mode=str(r)
    AssyrianSteps=[0,1,3,5,7,9,10]
    Assyrian=[]
    for j in AssyrianSteps:
        note=pool[j+transpose]
        Assyrian.append(note)
    Scale.notes=Assyrian
    Scale.steps=7
    mode=Scale(str(r),Assyrian,7)
    modes.append(mode)

for r in ["Lydian Augmented/Asgardian"]:
    Scale.mode=str(r)
    AsgardianSteps=[0,2,4,6,8,9,11]
    Asgardian=[]
    for j in AsgardianSteps:
        note=pool[j+transpose]
        Asgardian.append(note)
    Scale.notes=Asgardian
    Scale.steps=7
    mode=Scale(str(r),Asgardian,7)
    modes.append(mode)

for r in ["Lydian Dominant"]:
    Scale.mode=str(r)
    LydianDominantSteps=[0,2,4,6,7,9,10]
    LydianDominant=[]
    for j in LydianDominantSteps:
        note=pool[j+transpose]
        LydianDominant.append(note)
    Scale.notes=LydianDominant
    Scale.steps=7
    mode=Scale(str(r),LydianDominant,7)
    modes.append(mode)

for r in ["Aeolian Dominant/Mixolydian b6"]:
    Scale.mode=str(r)
    Mixolydianb6Steps=[0,2,4,5,7,8,10]
    Mixolydianb6=[]
    for j in Mixolydianb6Steps:
        note=pool[j+transpose]
        Mixolydianb6.append(note)
    Scale.notes=Mixolydianb6
    Scale.steps=7
    mode=Scale(str(r),Mixolydianb6,7)
    modes.append(mode)

for r in ["Half-Diminished/Sisyphean"]:
    Scale.mode=str(r)
    HalfDimSteps=[0,2,3,5,6,8,10]
    HalfDiminished=[]
    for j in HalfDimSteps:
        note=pool[j+transpose]
        HalfDiminished.append(note)
    Scale.notes=HalfDiminished
    Scale.steps=7
    mode=Scale(str(r),HalfDiminished,7)
    modes.append(mode)

for r in ["Altered Dominant/Palamidian"]:
    Scale.mode=str(r)
    AltDomSteps=[0,1,3,4,6,8,10]
    Altered=[]
    for j in AltDomSteps:
        note=pool[j+transpose]
        Altered.append(note)
    Scale.notes=Altered
    Scale.steps=7
    mode=Scale(str(r),Altered,7)
    modes.append(mode)

# Diatonic Modes of Harmonic Minor

for r in ["Harmonic Minor"]:
    Scale.mode=str(r)
    HarmonicMinorSteps=[0,2,3,5,7,8,11]
    HarmonicMinor=[]
    for j in HarmonicMinorSteps:
        note=pool[j+transpose]
        HarmonicMinor.append(note)
    Scale.notes=HarmonicMinor
    Scale.steps=7
    mode=Scale(str(r),HarmonicMinor,7)
    modes.append(mode)

for r in ["Locrian #6"]:
    Scale.mode=str(r)
    LocrianAug6Steps=[0,1,3,5,6,9,10]
    LocrianAug6=[]
    for j in LocrianAug6Steps:
        note=pool[j+transpose]
        LocrianAug6.append(note)
    Scale.notes=LocrianAug6
    Scale.steps=7
    mode=Scale(str(r),LocrianAug6,7)
    modes.append(mode)

for r in ["Ionian #5"]:
    Scale.mode=str(r)
    IonianAugSteps=[0,2,4,5,8,9,11]
    IonianAugmented=[]
    for j in IonianAugSteps:
        note=pool[j+transpose]
        IonianAugmented.append(note)
    Scale.notes=IonianAugmented
    Scale.steps=7
    mode=Scale(str(r),IonianAugmented,7)
    modes.append(mode)

for r in ["Ukrainian Dorian/Romanian Minor"]:
    Scale.mode=str(r)
    UkrainianDorianSteps=[0,2,3,6,7,9,10]
    UkrainianDorian=[]
    for j in UkrainianDorianSteps:
        note=pool[j+transpose]
        UkrainianDorian.append(note)
    Scale.notes=UkrainianDorian
    Scale.steps=7
    mode=Scale(str(r),UkrainianDorian,7)
    modes.append(mode)

for r in ["Phrygian Dominant"]:
    Scale.mode=str(r)
    PhrygianDominantSteps=[0,1,4,5,7,8,10]
    PhrygianDominant=[]
    for j in PhrygianDominantSteps:
        note=pool[j+transpose]
        PhrygianDominant.append(note)
    Scale.notes=PhrygianDominant
    Scale.steps=7
    mode=Scale(str(r),PhrygianDominant,7)
    modes.append(mode)

for r in ["Lydian #2/Maqam Mustar"]:
    Scale.mode=str(r)
    LydianPlus2Steps=[0,3,4,6,7,9,11]
    LydianPlus2=[]
    for j in LydianPlus2Steps:
        note=pool[j+transpose]
        LydianPlus2.append(note)
    Scale.notes=LydianPlus2
    Scale.steps=7
    mode=Scale(str(r),LydianPlus2,7)
    modes.append(mode)

for r in ["Altered Diminished"]:
    Scale.mode=str(r)
    AltDimSteps=[0,1,3,4,6,8,9]
    AlteredDiminished=[]
    for j in AltDimSteps:
        note=pool[j+transpose]
        AlteredDiminished.append(note)
    Scale.notes=AlteredDiminished
    Scale.steps=7
    mode=Scale(str(r),AlteredDiminished,7)
    modes.append(mode)

# Diatonic Modes of Double Harmonic Major

for r in ["Double Harmonic Major/Byzantine"]:
    Scale.mode=str(r)
    DoubleHarmonicMajorSteps=[0,1,4,5,7,8,11]
    DoubleHarmonicMajor=[]
    for j in DoubleHarmonicMajorSteps:
        note=pool[j+transpose]
        DoubleHarmonicMajor.append(note)
    Scale.notes=DoubleHarmonicMajor
    Scale.steps=7
    mode=Scale(str(r),DoubleHarmonicMajor,7)
    modes.append(mode)

for r in ["Lydian #2#6"]:
    Scale.mode=str(r)
    Lydian26Steps=[0,3,4,6,7,10,11]
    Lydian26=[]
    for j in Lydian26Steps:
        note=pool[j+transpose]
        Lydian26.append(note)
    Scale.notes=Lydian26
    Scale.steps=7
    mode=Scale(str(r),Lydian26,7)
    modes.append(mode)

for r in ["Ultraphrygian"]:
    Scale.mode=str(r)
    UltraphrygianSteps=[0,1,3,4,7,8,9]
    Ultraphrygian=[]
    for j in UltraphrygianSteps:
        note=pool[j+transpose]
        Ultraphrygian.append(note)
    Scale.notes=Ultraphrygian
    Scale.steps=7
    mode=Scale(str(r),Ultraphrygian,7)
    modes.append(mode)

for r in ["Hungarian Gypsy Minor"]:
    Scale.mode=str(r)
    HungarianGypsyMinorSteps=[0,2,3,6,7,8,11]
    HungarianGypsyMinor=[]
    for j in HungarianGypsyMinorSteps:
        note=pool[j+transpose]
        HungarianGypsyMinor.append(note)
    Scale.notes=HungarianGypsyMinor
    Scale.steps=7
    mode=Scale(str(r),HungarianGypsyMinor,7)
    modes.append(mode)

for r in ["Oriental"]:
    Scale.mode=str(r)
    OrientalSteps=[0,1,4,5,6,9,10]
    Oriental=[]
    for j in OrientalSteps:
        note=pool[j+transpose]
        Oriental.append(note)
    Scale.notes=Oriental
    Scale.steps=7
    mode=Scale(str(r),Oriental,7)
    modes.append(mode)

for r in ["Ionian #2#5"]:
    Scale.mode=str(r)
    IonianAug2Steps=[0,3,4,5,8,9,11]
    IonianAug2=[]
    for j in IonianAug2Steps:
        note=pool[j+transpose]
        IonianAug2.append(note)
    Scale.notes=IonianAug2
    Scale.steps=7
    mode=Scale(str(r),IonianAug2,7)
    modes.append(mode)

for r in ["Locrian bb3bb7"]:
    Scale.mode=str(r)
    Locrianbb3bb7Steps=[0,1,2,5,6,8,9]
    Locrianbb3bb7=[]
    for j in Locrianbb3bb7Steps:
        note=pool[j+transpose]
        Locrianbb3bb7.append(note)
    Scale.notes=Locrianbb3bb7
    Scale.steps=7
    mode=Scale(str(r),Locrianbb3bb7,7)
    modes.append(mode)

# Pentatonic Scales

for r in ["Pentatonic Minor/Celtic Amara"]:
    Scale.mode=str(r)
    AmaraSteps=[0,3,5,7,10]
    Amara=[]
    for j in AmaraSteps:
        note=pool[j+transpose]
        Amara.append(note)
    Scale.notes=Amara
    Scale.steps=5
    mode=Scale(str(r),Amara,5)
    modes.append(mode)

for r in ["Pentatonic Major/Yona Nuki Major"]:
    Scale.mode=str(r)
    PentatonicMajorSteps=[0,2,4,7,9]
    PentatonicMajor=[]
    for j in PentatonicMajorSteps:
        note=pool[j+transpose]
        PentatonicMajor.append(note)
    Scale.notes=PentatonicMajor
    Scale.steps=5
    mode=Scale(str(r),PentatonicMajor,5)
    modes.append(mode)

for r in ["Altered Pentatonic"]:
    Scale.mode=str(r)
    AltPentatonicSteps=[0,3,5,7,9]
    AlteredPentatonic=[]
    for j in AltPentatonicSteps:
        note=pool[j+transpose]
        AlteredPentatonic.append(note)
    Scale.notes=AlteredPentatonic
    Scale.steps=5
    mode=Scale(str(r),AlteredPentatonic,5)
    modes.append(mode)

for r in ["Yona Nuki Minor"]:
    Scale.mode=str(r)
    YonaNukiMinorSteps=[0,2,3,5,8]
    YonaNukiMinor=[]
    for j in YonaNukiMinorSteps:
        note=pool[j+transpose]
        YonaNukiMinor.append(note)
    Scale.notes=YonaNukiMinor
    Scale.steps=5
    mode=Scale(str(r),YonaNukiMinor,5)
    modes.append(mode)

for r in ["Hirajoshi"]:
    Scale.mode=str(r)
    HirajoshiSteps=[0,2,3,7,8]
    Hirajoshi=[]
    for j in HirajoshiSteps:
        note=pool[j+transpose]
        Hirajoshi.append(note)
    Scale.notes=Hirajoshi
    Scale.steps=5
    mode=Scale(str(r),Hirajoshi,5)
    modes.append(mode)

for r in ["Sakura"]:
    Scale.mode=str(r)
    SakuraSteps=[0,1,4,5,6]
    Sakura=[]
    for j in SakuraSteps:
        note=pool[j+transpose]
        Sakura.append(note)
    Scale.notes=Sakura
    Scale.steps=5
    mode=Scale(str(r),Sakura,5)
    modes.append(mode)

for r in ["Insen"]:
    Scale.mode=str(r)
    InsenSteps=[0,1,5,7,10]
    Insen=[]
    for j in InsenSteps:
        note=pool[j+transpose]
        Insen.append(note)
    Scale.notes=Insen
    Scale.steps=5
    mode=Scale(str(r),Insen,5)
    modes.append(mode)

for r in ["Iwato"]:
    Scale.mode=str(r)
    IwatoSteps=[0,1,5,6,10]
    Iwato=[]
    for j in IwatoSteps:
        note=pool[j+transpose]
        Iwato.append(note)
    Scale.notes=Iwato
    Scale.steps=5
    mode=Scale(str(r),Iwato,5)
    modes.append(mode)

for r in ["Yo"]:
    Scale.mode=str(r)
    YoSteps=[0,2,5,7,9]
    Yo=[]
    for j in YoSteps:
        note=pool[j+transpose]
        Yo.append(note)
    Scale.notes=Yo
    Scale.steps=5
    mode=Scale(str(r),Yo,5)
    modes.append(mode)

for r in ["Balinese Pelog"]:
    Scale.mode=str(r)
    BalineseSteps=[0,1,3,7,8]
    BalinesePelog=[]
    for j in BalineseSteps:
        note=pool[j+transpose]
        BalinesePelog.append(note)
    Scale.notes=BalinesePelog
    Scale.steps=5
    mode=Scale(str(r),BalinesePelog,5)
    modes.append(mode)

for r in ["Chinese"]:
    Scale.mode=str(r)
    ChineseSteps=[0,4,6,7,11]
    Chinese=[]
    for j in ChineseSteps:
        note=pool[j+transpose]
        Chinese.append(note)
    Scale.notes=Chinese
    Scale.steps=5
    mode=Scale(str(r),Chinese,5)
    modes.append(mode)

for r in ["Egyptian"]:
    Scale.mode=str(r)
    EgyptianSteps=[0,2,5,7,10]
    Egyptian=[]
    for j in EgyptianSteps:
        note=pool[j+transpose]
        Egyptian.append(note)
    Scale.notes=Egyptian
    Scale.steps=5
    mode=Scale(str(r),Egyptian,5)
    modes.append(mode)

for r in ["Akebono"]:
    Scale.mode=str(r)
    AkebonoSteps=[0,2,3,7,9]
    Akebono=[]
    for j in AkebonoSteps:
        note=pool[j+transpose]
        Akebono.append(note)
    Scale.notes=Akebono
    Scale.steps=5
    mode=Scale(str(r),Akebono,5)
    modes.append(mode)

# Bebop/Jazz/Blues/Gospel Scales

for r in ["Bebop Dominant"]:
    Scale.mode=str(r)
    BebopDominantSteps=[0,2,4,5,7,9,10,11]
    BebopDominant=[]
    for j in BebopDominantSteps:
        note=pool[j+transpose]
        BebopDominant.append(note)
    Scale.notes=BebopDominant
    Scale.steps=8
    mode=Scale(str(r),BebopDominant,8)
    modes.append(mode)

for r in ["Bebop Major"]:
    Scale.mode=str(r)
    BebopMajorSteps=[0,2,4,5,7,8,9,11]
    BebopMajor=[]
    for j in BebopMajorSteps:
        note=pool[j+transpose]
        BebopMajor.append(note)
    Scale.notes=BebopMajor
    Scale.steps=8
    mode=Scale(str(r),BebopMajor,8)
    modes.append(mode)

for r in ["Bebop Melodic Minor"]:
    Scale.mode=str(r)
    BebopMelodicMinorSteps=[0,2,3,5,7,8,9,11]
    BebopMelodicMinor=[]
    for j in BebopMelodicMinorSteps:
        note=pool[j+transpose]
        BebopMelodicMinor.append(note)
    Scale.notes=BebopMelodicMinor
    Scale.steps=8
    mode=Scale(str(r),BebopMelodicMinor,8)
    modes.append(mode)

for r in ["Dom7b5 Diminished"]:
    Scale.mode=str(r)
    Dom7b5DimSteps=[0,2,4,5,6,8,10,11]
    Dom7b5Diminished=[]
    for j in Dom7b5DimSteps:
        note=pool[j+transpose]
        Dom7b5Diminished.append(note)
    Scale.notes=Dom7b5Diminished
    Scale.steps=8
    mode=Scale(str(r),Dom7b5Diminished,8)
    modes.append(mode)

for r in ["Six-Note Blues Scale"]:
    Scale.mode=str(r)
    SixNoteBluesSteps=[0,3,5,6,9,10]
    SixNoteBlues=[]
    for j in SixNoteBluesSteps:
        note=pool[j+transpose]
        SixNoteBlues.append(note)
    Scale.notes=SixNoteBlues
    Scale.steps=6
    mode=Scale(str(r),SixNoteBlues,6)
    modes.append(mode)

for r in ["Nine-Note Blues Scale"]:
    Scale.mode=str(r)
    NineNoteBluesSteps=[0,2,3,4,5,7,9,10,11]
    NineNoteBlues=[]
    for j in NineNoteBluesSteps:
        note=pool[j+transpose]
        NineNoteBlues.append(note)
    Scale.notes=NineNoteBlues
    Scale.steps=9
    mode=Scale(str(r),NineNoteBlues,9)
    modes.append(mode)

for r in ["Gospel/Major Blues Scale"]:
    Scale.mode=str(r)
    GospelSteps=[0,2,3,4,7,9]
    Gospel=[]
    for j in GospelSteps:
        note=pool[j+transpose]
        Gospel.append(note)
    Scale.notes=Gospel
    Scale.steps=6
    mode=Scale(str(r),Gospel,6)
    modes.append(mode)

# Some More Hexatonic Scales/Modes

for r in ["Symmetrical Augmented"]:
    Scale.mode=str(r)
    SymmetricAugSteps=[0,3,4,7,8,10]
    SymmetricAugmented=[]
    for j in SymmetricAugSteps:
        note=pool[j+transpose]
        SymmetricAugmented.append(note)
    Scale.notes=SymmetricAugmented
    Scale.steps=6
    mode=Scale(str(r),SymmetricAugmented,6)
    modes.append(mode)

for r in ["Iberian Hexatonic"]:
    Scale.mode=str(r)
    IberianSteps=[0,1,4,5,7,10]
    IberianHexatonic=[]
    for j in IberianSteps:
        note=pool[j+transpose]
        IberianHexatonic.append(note)
    Scale.notes=IberianHexatonic
    Scale.steps=6
    mode=Scale(str(r),IberianHexatonic,6)
    modes.append(mode)

for r in ["Prometheus Scale"]:
    Scale.mode=str(r)
    PromethianSteps=[0,2,4,6,7,10]
    Prometheus=[]
    for j in PromethianSteps:
        note=pool[j+transpose]
        Prometheus.append(note)
    Scale.notes=Prometheus
    Scale.steps=6
    mode=Scale(str(r),Prometheus,6)
    modes.append(mode)

for r in ["Prometheus Neapolitan"]:
    Scale.mode=str(r)
    PromNeapolitanSteps=[0,1,4,6,9,10]
    PrometheusNeapolitan=[]
    for j in PromNeapolitanSteps:
        note=pool[j+transpose]
        PrometheusNeapolitan.append(note)
    Scale.notes=PrometheusNeapolitan
    Scale.steps=6
    mode=Scale(str(r),PrometheusNeapolitan,6)
    modes.append(mode)

for r in ["Prometheus Liszt"]:
    Scale.mode=str(r)
    PromLizSteps=[0,1,4,5,8,9]
    PrometheusLiszt=[]
    for j in PromLizSteps:
        note=pool[j+transpose]
        PrometheusLiszt.append(note)
    Scale.notes=PrometheusLiszt
    Scale.steps=6
    mode=Scale(str(r),PrometheusLiszt,6)
    modes.append(mode)

for r in ["Banshikicho"]:
    Scale.mode=str(r)
    BanshikichoSteps=[0,2,3,4,7,9]
    Banshikicho=[]
    for j in BanshikichoSteps:
        note=pool[j+transpose]
        Banshikicho.append(note)
    Scale.notes=Banshikicho
    Scale.steps=6
    mode=Scale(str(r),Banshikicho,6)
    modes.append(mode)

for r in ["Kurd/Annaziska Handpan Scale"]:
    Scale.mode=str(r)
    KurdishSteps=[0,2,3,5,7,8]
    Annaziska=[]
    for j in KurdishSteps:
        note=pool[j+transpose]
        Annaziska.append(note)
    Scale.notes=Annaziska
    Scale.steps=6
    mode=Scale(str(r),Annaziska,6)
    modes.append(mode)

# Ethnic & Symmetrical Scales

for r in ["Harmonic Minor Add b5"]:
    Scale.mode=str(r)
    HarmonicMinorb5Steps=[0,2,3,5,6,7,8,11]
    HarmonicMinorb5=[]
    for j in HarmonicMinorb5Steps:
        note=pool[j+transpose]
        HarmonicMinorb5.append(note)
    Scale.notes=HarmonicMinorb5
    Scale.steps=8
    mode=Scale(str(r),HarmonicMinorb5,8)
    modes.append(mode)

for r in ["Hungarian Major"]:
    Scale.mode=str(r)
    HungarianMajorSteps=[0,3,4,6,7,9,10]
    HungarianMajor=[]
    for j in HungarianMajorSteps:
        note=pool[j+transpose]
        HungarianMajor.append(note)
    Scale.notes=HungarianMajor
    Scale.steps=7
    mode=Scale(str(r),HungarianMajor,7)
    modes.append(mode)

for r in ["Diminished Octatonic"]:
    Scale.mode=str(r)
    DimOctatonicSteps=[0,2,3,5,6,8,9,11]
    DiminishedOctatonic=[]
    for j in DimOctatonicSteps:
        note=pool[j+transpose]
        DiminishedOctatonic.append(note)
    Scale.notes=DiminishedOctatonic
    Scale.steps=8
    mode=Scale(str(r),DiminishedOctatonic,8)
    modes.append(mode)

for r in ["Whole Tone"]:
    Scale.mode=str(r)
    WholeSteps=[0,2,4,6,8,10]
    WholeTone=[]
    for j in WholeSteps:
        note=pool[j+transpose]
        WholeTone.append(note)
    Scale.notes=WholeTone
    Scale.steps=6
    mode=Scale(str(r),WholeTone,6)
    modes.append(mode)

for r in ["Ultralocrian"]:
    Scale.mode=str(r)
    UltraLocrianSteps=[0,1,3,4,6,7,9]
    Ultralocrian=[]
    for j in UltraLocrianSteps:
        note=pool[j+transpose]
        Ultralocrian.append(note)
    Scale.notes=Ultralocrian
    Scale.steps=7
    mode=Scale(str(r),Ultralocrian,7)
    modes.append(mode)

for r in ["Japanese Nohkan Flute Scale"]:
    Scale.mode=str(r)
    NohkanSteps=[0,2,5,6,8,9,11]
    NohkanFlute=[]
    for j in NohkanSteps:
        note=pool[j+transpose]
        NohkanFlute.append(note)
    Scale.notes=NohkanFlute
    Scale.steps=7
    mode=Scale(str(r),NohkanFlute,7)
    modes.append(mode)

for r in ["Persian"]:
    Scale.mode=str(r)
    PersianSteps=[0,1,4,5,6,8,10]
    Persian=[]
    for j in PersianSteps:
        note=pool[j+transpose]
        Persian.append(note)
    Scale.notes=Persian
    Scale.steps=7
    mode=Scale(str(r),Persian,7)
    modes.append(mode)

for r in ["Arabic"]:
    Scale.mode=str(r)
    ArabianSteps=[0,2,4,5,6,8,10]
    Arabic=[]
    for j in ArabianSteps:
        note=pool[j+transpose]
        Arabic.append(note)
    Scale.notes=Arabic
    Scale.steps=7
    mode=Scale(str(r),Arabic,7)
    modes.append(mode)

for r in ["Neapolitan Minor"]:
    Scale.mode=str(r)
    NeapolitanMinorSteps=[0,1,3,5,7,8,11]
    NeapolitanMinor=[]
    for j in NeapolitanMinorSteps:
        note=pool[j+transpose]
        NeapolitanMinor.append(note)
    Scale.notes=NeapolitanMinor
    Scale.steps=7
    mode=Scale(str(r),NeapolitanMinor,7)
    modes.append(mode)

for r in ["Neapolitan Major"]:
    Scale.mode=str(r)
    NeapolitanMajorSteps=[0,1,3,5,7,9,11]
    NeapolitanMajor=[]
    for j in NeapolitanMajorSteps:
        note=pool[j+transpose]
        NeapolitanMajor.append(note)
    Scale.notes=NeapolitanMajor
    Scale.steps=7
    mode=Scale(str(r),NeapolitanMajor,7)
    modes.append(mode)

for r in ["Hijaz Kar Maqam"]:
    Scale.mode=str(r)
    HijazKarMaqamSteps=[0,1,4,5,7,8,11]
    HijazKarMaqam=[]
    for j in HijazKarMaqamSteps:
        note=pool[j+transpose]
        HijazKarMaqam.append(note)
    Scale.notes=HijazKarMaqam
    Scale.steps=7
    mode=Scale(str(r),HijazKarMaqam,7)
    modes.append(mode)

for r in ["Algerian Minor"]:
    Scale.mode=str(r)
    AlgerianSteps=[0,2,3,5,6,7,8,11]
    AlgerianMinor=[]
    for j in AlgerianSteps:
        note=pool[j+transpose]
        AlgerianMinor.append(note)
    Scale.notes=AlgerianMinor
    Scale.steps=8
    mode=Scale(str(r),AlgerianMinor,8)
    modes.append(mode)

for r in ["8-Note Spanish/Jewish"]:
    Scale.mode=str(r)
    Jewish8Steps=[0,1,3,4,5,6,8,10]
    Jewish8=[]
    for j in Jewish8Steps:
        note=pool[j+transpose]
        Jewish8.append(note)
    Scale.notes=Jewish8
    Scale.steps=8
    mode=Scale(str(r),Jewish8,8)
    modes.append(mode)

for r in ["Scala Enigmatica (Ascending)"]:
    Scale.mode=str(r)
    EnigmaticUpSteps=[0,1,4,6,8,10,11]
    EnigmaticASC=[]
    for j in EnigmaticUpSteps:
        note=pool[j+transpose]
        EnigmaticASC.append(note)
    Scale.notes=EnigmaticASC
    Scale.steps=7
    mode=Scale(str(r),EnigmaticASC,7)
    modes.append(mode)

for r in ["Scala Enigmatica (Descending)"]:
    Scale.mode=str(r)
    EnigmaticDownSteps=[0,11,10,8,5,4,1]
    EnigmaticDESC=[]
    for j in EnigmaticDownSteps:
        note=pool[j+transpose]
        EnigmaticDESC.append(note)
    Scale.notes=EnigmaticDESC
    Scale.steps=7
    mode=Scale(str(r),EnigmaticDESC,7)
    modes.append(mode)

for r in ["Raga Asavari"]:
    Scale.mode=str(r)
    AsavariSteps=[0,1,5,7,8,0,10,8,7,5,3,1,0]
    RagaAsavari=[]
    for j in AsavariSteps:
        note=pool[j+transpose]
        RagaAsavari.append(note)
    Scale.notes=RagaAsavari
    Scale.steps=13
    mode=Scale(str(r),RagaAsavari,13)
    modes.append(mode)

for r in ["Enigmatic Minor"]:
    Scale.mode=str(r)
    EnigminorSteps=[0,1,3,6,7,10,11]
    EnigmaticMinor=[]
    for j in EnigminorSteps:
        note=pool[j+transpose]
        EnigmaticMinor.append(note)
    Scale.notes=EnigmaticMinor
    Scale.steps=7
    mode=Scale(str(r),EnigmaticMinor,7)
    modes.append(mode)

# Select Mode @ Random

y=random.randint(0,78)
choice=modes[y]
print("Choice of Mode:")
print(choice.mode,"in",root)
print("Notes Spelled Out:")
print(choice.notes)






