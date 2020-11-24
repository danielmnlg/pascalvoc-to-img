import glob
import os
import xmltodict
import json
import pprint
import cv2
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
#dirs = os.listdir('../../Data Asli/FIX/Mobil/') #list directory in Land Use Images folder
label = 0
im_arr = []
mobil = 0
motor = 0
pohon = 0
pkl = 0
pejalan_kaki = 0
truk = 0
bus = 0
rambu = 0
rumah = 0
sepeda = 0
becak = 0
sedan = 0
halte = 0
PA = 0
GI = 0
I = 0
JI = 0
MI = 0
N = 0
JA = 0
K = 0
PE = 0
DO = 0
M = 0
GHA = 0
SA = 0
NE = 0
BE = 0
TO = 0
H = 0
NI = 0
HAN = 0
GE = 0
GO = 0
BI = 0
A = 0
NYA = 0
HA = 0
GA = 0
T = 0
WA = 0
GHU = 0
NG = 0
NGE = 0
LI = 0
KA = 0
KAN = 0
NU = 0
MAN = 0
PI = 0
KAH = 0
KU = 0
TI = 0
TU = 0
KI = 0
LA = 0
PAH = 0
GAN = 0
TA = 0
GH = 0
SE = 0
YU = 0
LAH = 0
GU = 0
S = 0
MU = 0
L = 0
YAN = 0
YAU = 0
SAI = 0
PAN = 0
DAI = 0
HE = 0
LAU = 0
GHI = 0
RA = 0
MA = 0
DI = 0
LO = 0
LU = 0
RU = 0
NGAN = 0
JE = 0
MO = 0
NGI = 0
CA = 0
SU = 0
SANG = 0
BU = 0
JU = 0
RAI = 0
NAN = 0
SI = 0
NA = 0
DU = 0
WAI = 0
E = 0
NYE = 0
BA = 0
KAR = 0
KANG = 0
BO = 0
LAN = 0
TE = 0
PO = 0
YA = 0
CU = 0
WAH = 0
U = 0
GHAU = 0
NGAH = 0
WANG = 0
NANG = 0
LANG = 0
ME = 0
NAI = 0
NYU = 0
WO = 0
BAI = 0
BAH = 0
YANG = 0
KE = 0
BAN = 0
YAI = 0
DE = 0
TAI = 0
LAI = 0
JAR = 0
JANG = 0
CE = 0
NYAI = 0
NO = 0
YAR = 0
LE = 0
BAR = 0
PU = 0
RANG = 0
JAN = 0
DA = 0
NAU = 0
JAU = 0
KO = 0
SAN = 0
DAH = 0
HAR = 0
RAH = 0
RI = 0
AH = 0
TANG = 0
KAI = 0
NGA = 0
WAR = 0
NAR = 0
BANG = 0
PAI = 0
RAU = 0
GHAN = 0
B = 0
GHANG = 0
SO = 0
HI = 0
NAH = 0
TAN = 0
KAU = 0
CAN = 0
WAN = 0
CO = 0
R = 0
BAU = 0
DAN = 0
CAR = 0
HANG = 0
ANG = 0
PAU = 0
SAR = 0
SAU = 0
TAU = 0
AN = 0
GAR = 0
SAH = 0
TAR = 0
WI = 0
GHAH = 0
GHE = 0
GHO = 0
GHAI = 0
TAH = 0
PANG = 0
WE = 0
PAR = 0
RAR = 0
CANG = 0
LAR = 0
NGAR = 0
DANG = 0
NGAI = 0
NYI = 0
GANG = 0
HAI = 0
AU = 0
AI = 0
AR = 0
O = 0
MAI = 0
NGO = 0
NGU = 0
DAR = 0
NYAN = 0
NYO = 0
NYAR = 0
NYAH = 0
JAI = 0
DAU = 0
HO = 0
MAU = 0
MANG = 0
HU = 0
HAH = 0
WU = 0
D = 0
HAU = 0
CAU = 0
WAU = 0
RE = 0
RO = 0
MAR = 0
GAI = 0
JO = 0
NGAU = 0
NGANG = 0
NYANG = 0
YAH = 0
MAH = 0
CAH = 0
CAI = 0
GAU = 0
GAH = 0
YE = 0
YI = 0
NYAU = 0
GHAR = 0
CI = 0
YO = 0
RAN = 0
JAH = 0

def read_content(xml_file: str):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    #print ("Works!")
    list_with_all_boxes = []
    for boxes in root.iter('object'):
        filename = root.find('filename').text
        class_name = boxes.find('name').text
        ymin, xmin, ymax, xmax = None, None, None, None
        for box in boxes.findall("bndbox"):
            ymin = int(box.find("ymin").text)
            xmin = int(box.find("xmin").text)
            ymax = int(box.find("ymax").text)
            xmax = int(box.find("xmax").text)
        list_with_single_boxes = [xmin, ymin, xmax, ymax, class_name]
        list_with_all_boxes.append(list_with_single_boxes)
    return filename, list_with_all_boxes
def process(PA,GI,I,JI,MI,N,JA,K,PE,DO,M,GHA,SA,NE,BE,TO,H,NI,HAN,GE,GO,BI,A,NYA,HA,GA,T,WA,GHU,NG,NGE,LI,KA,KAN,NU,MAN,PI,KAH,KU,TI,TU,KI,LA,PAH,GAN,TA,GH,SE,YU,LAH,GU,S,MU,L,YAN,YAU,SAI,PAN,DAI,HE,LAU,GHI,RA,MA,DI,LO,LU,RU,NGAN,JE,MO,NGI,CA,SU,SANG,BU,JU,RAI,NAN,SI,NA,DU,WAI,E,NYE,BA,KAR,KANG,BO,LAN,TE,PO,YA,CU,WAH,U,GHAU,NGAH,WANG,NANG,LANG,ME,NAI,NYU,WO,BAI,BAH,YANG,KE,BAN,YAI,DE,TAI,LAI,JAR,JANG,CE,NYAI,NO,YAR,LE,BAR,PU,RANG,JAN,DA,NAU,JAU,KO,SAN,DAH,HAR,RAH,RI,AH,TANG,KAI,NGA,WAR,NAR,BANG,PAI,RAU,GHAN,B,GHANG,SO,HI,NAH,TAN,KAU,CAN,WAN,CO,R,BAU,DAN,CAR,HANG,ANG,PAU,SAR,SAU,TAU,AN,GAR,SAH,TAR,WI,GHAH,GHE,GHO,GHAI,TAH,PANG,WE,PAR,RAR,CANG,LAR,NGAR,DANG,NGAI,NYI,GANG,HAI,AU,AI,AR,O,MAI,NGO,NGU,DAR,NYAN,NYO,NYAR,NYAH,JAI,DAU,HO,MAU,MANG,HU,HAH,WU,D,HAU,CAU,WAU,RE,RO,MAR,GAI,JO,NGAU,NGANG,NYANG,YAH,MAH,CAH,CAI,GAU,GAH,YE,YI,NYAU,GHAR,CI,YO,RAN,JAH):
        for pic in glob.glob('input/*.xml'):
            try:
                    #print(pic)
                    fname = "data/Null/Null.jpg"
                    name, boxes = read_content(pic)
                    #print(name)
                    print(boxes)
                    im = cv2.imread("images/"+name)
                    #open image
                    #print("FOTO ORIGINAL")
                    #plt.imshow(im)
                    #plt.show()
                    #save_dir = "D:/google-images-deep-learning/PascalVOC-to-Images-master/data/"+name
                    #try:
                    #    os.mkdir(save_dir)
                    #except:
                    #    pass
                    for x in boxes:
                        nop = 1

                        if str(x[4]) == "PA":
                            PA = PA + 1
                            fname = "data/"+x[4]+"/"+str(PA)+".jpg"

                        elif str(x[4]) == "GI":
                            GI = GI + 1
                            fname = "data/"+x[4]+"/"+str(GI)+".jpg"

                        elif str(x[4]) == "I":
                            I = I + 1
                            fname = "data/"+x[4]+"/"+str(I)+".jpg"

                        elif str(x[4]) == "JI":
                            JI = JI + 1
                            fname = "data/"+x[4]+"/"+str(JI)+".jpg"

                        elif str(x[4]) == "MI":
                            MI = MI + 1
                            fname = "data/"+x[4]+"/"+str(MI)+".jpg"

                        elif str(x[4]) == "N":
                            N = N + 1
                            fname = "data/"+x[4]+"/"+str(N)+".jpg"

                        elif str(x[4]) == "JA":
                            JA = JA + 1
                            fname = "data/"+x[4]+"/"+str(JA)+".jpg"

                        elif str(x[4]) == "K":
                            K = K + 1
                            fname = "data/"+x[4]+"/"+str(K)+".jpg"

                        elif str(x[4]) == "PE":
                            PE = PE + 1
                            fname = "data/"+x[4]+"/"+str(PE)+".jpg"

                        elif str(x[4]) == "DO":
                            DO = DO + 1
                            fname = "data/"+x[4]+"/"+str(DO)+".jpg"

                        elif str(x[4]) == "M":
                            M = M + 1
                            fname = "data/"+x[4]+"/"+str(M)+".jpg"

                        elif str(x[4]) == "GHA":
                            GHA = GHA + 1
                            fname = "data/"+x[4]+"/"+str(GHA)+".jpg"

                        elif str(x[4]) == "SA":
                            SA = SA + 1
                            fname = "data/"+x[4]+"/"+str(SA)+".jpg"

                        elif str(x[4]) == "NE":
                            NE = NE + 1
                            fname = "data/"+x[4]+"/"+str(NE)+".jpg"

                        elif str(x[4]) == "BE":
                            BE = BE + 1
                            fname = "data/"+x[4]+"/"+str(BE)+".jpg"

                        elif str(x[4]) == "TO":
                            TO = TO + 1
                            fname = "data/"+x[4]+"/"+str(TO)+".jpg"

                        elif str(x[4]) == "H":
                            H = H + 1
                            fname = "data/"+x[4]+"/"+str(H)+".jpg"

                        elif str(x[4]) == "NI":
                            NI = NI + 1
                            fname = "data/"+x[4]+"/"+str(NI)+".jpg"

                        elif str(x[4]) == "HAN":
                            HAN = HAN + 1
                            fname = "data/"+x[4]+"/"+str(HAN)+".jpg"

                        elif str(x[4]) == "GE":
                            GE = GE + 1
                            fname = "data/"+x[4]+"/"+str(GE)+".jpg"

                        elif str(x[4]) == "GO":
                            GO = GO + 1
                            fname = "data/"+x[4]+"/"+str(GO)+".jpg"

                        elif str(x[4]) == "BI":
                            BI = BI + 1
                            fname = "data/"+x[4]+"/"+str(BI)+".jpg"

                        elif str(x[4]) == "A":
                            A = A + 1
                            fname = "data/"+x[4]+"/"+str(A)+".jpg"

                        elif str(x[4]) == "NYA":
                            NYA = NYA + 1
                            fname = "data/"+x[4]+"/"+str(NYA)+".jpg"

                        elif str(x[4]) == "HA":
                            HA = HA + 1
                            fname = "data/"+x[4]+"/"+str(HA)+".jpg"

                        elif str(x[4]) == "GA":
                            GA = GA + 1
                            fname = "data/"+x[4]+"/"+str(GA)+".jpg"

                        elif str(x[4]) == "T":
                            T = T + 1
                            fname = "data/"+x[4]+"/"+str(T)+".jpg"

                        elif str(x[4]) == "WA":
                            WA = WA + 1
                            fname = "data/"+x[4]+"/"+str(WA)+".jpg"

                        elif str(x[4]) == "GHU":
                            GHU = GHU + 1
                            fname = "data/"+x[4]+"/"+str(GHU)+".jpg"

                        elif str(x[4]) == "NG":
                            NG = NG + 1
                            fname = "data/"+x[4]+"/"+str(NG)+".jpg"

                        elif str(x[4]) == "NGE":
                            NGE = NGE + 1
                            fname = "data/"+x[4]+"/"+str(NGE)+".jpg"

                        elif str(x[4]) == "LI":
                            LI = LI + 1
                            fname = "data/"+x[4]+"/"+str(LI)+".jpg"

                        elif str(x[4]) == "KA":
                            KA = KA + 1
                            fname = "data/"+x[4]+"/"+str(KA)+".jpg"

                        elif str(x[4]) == "KAN":
                            KAN = KAN + 1
                            fname = "data/"+x[4]+"/"+str(KAN)+".jpg"

                        elif str(x[4]) == "NU":
                            NU = NU + 1
                            fname = "data/"+x[4]+"/"+str(NU)+".jpg"

                        elif str(x[4]) == "MAN":
                            MAN = MAN + 1
                            fname = "data/"+x[4]+"/"+str(MAN)+".jpg"

                        elif str(x[4]) == "PI":
                            PI = PI + 1
                            fname = "data/"+x[4]+"/"+str(PI)+".jpg"

                        elif str(x[4]) == "KAH":
                            KAH = KAH + 1
                            fname = "data/"+x[4]+"/"+str(KAH)+".jpg"

                        elif str(x[4]) == "KU":
                            KU = KU + 1
                            fname = "data/"+x[4]+"/"+str(KU)+".jpg"

                        elif str(x[4]) == "TI":
                            TI = TI + 1
                            fname = "data/"+x[4]+"/"+str(TI)+".jpg"

                        elif str(x[4]) == "TU":
                            TU = TU + 1
                            fname = "data/"+x[4]+"/"+str(TU)+".jpg"

                        elif str(x[4]) == "KI":
                            KI = KI + 1
                            fname = "data/"+x[4]+"/"+str(KI)+".jpg"

                        elif str(x[4]) == "LA":
                            LA = LA + 1
                            fname = "data/"+x[4]+"/"+str(LA)+".jpg"

                        elif str(x[4]) == "PAH":
                            PAH = PAH + 1
                            fname = "data/"+x[4]+"/"+str(PAH)+".jpg"

                        elif str(x[4]) == "GAN":
                            GAN = GAN + 1
                            fname = "data/"+x[4]+"/"+str(GAN)+".jpg"

                        elif str(x[4]) == "TA":
                            TA = TA + 1
                            fname = "data/"+x[4]+"/"+str(TA)+".jpg"

                        elif str(x[4]) == "GH":
                            GH = GH + 1
                            fname = "data/"+x[4]+"/"+str(GH)+".jpg"

                        elif str(x[4]) == "SE":
                            SE = SE + 1
                            fname = "data/"+x[4]+"/"+str(SE)+".jpg"

                        elif str(x[4]) == "YU":
                            YU = YU + 1
                            fname = "data/"+x[4]+"/"+str(YU)+".jpg"

                        elif str(x[4]) == "LAH":
                            LAH = LAH + 1
                            fname = "data/"+x[4]+"/"+str(LAH)+".jpg"

                        elif str(x[4]) == "GU":
                            GU = GU + 1
                            fname = "data/"+x[4]+"/"+str(GU)+".jpg"

                        elif str(x[4]) == "S":
                            S = S + 1
                            fname = "data/"+x[4]+"/"+str(S)+".jpg"

                        elif str(x[4]) == "MU":
                            MU = MU + 1
                            fname = "data/"+x[4]+"/"+str(MU)+".jpg"

                        elif str(x[4]) == "L":
                            L = L + 1
                            fname = "data/"+x[4]+"/"+str(L)+".jpg"

                        elif str(x[4]) == "YAN":
                            YAN = YAN + 1
                            fname = "data/"+x[4]+"/"+str(YAN)+".jpg"

                        elif str(x[4]) == "YAU":
                            YAU = YAU + 1
                            fname = "data/"+x[4]+"/"+str(YAU)+".jpg"

                        elif str(x[4]) == "SAI":
                            SAI = SAI + 1
                            fname = "data/"+x[4]+"/"+str(SAI)+".jpg"

                        elif str(x[4]) == "PAN":
                            PAN = PAN + 1
                            fname = "data/"+x[4]+"/"+str(PAN)+".jpg"

                        elif str(x[4]) == "DAI":
                            DAI = DAI + 1
                            fname = "data/"+x[4]+"/"+str(DAI)+".jpg"

                        elif str(x[4]) == "HE":
                            HE = HE + 1
                            fname = "data/"+x[4]+"/"+str(HE)+".jpg"

                        elif str(x[4]) == "LAU":
                            LAU = LAU + 1
                            fname = "data/"+x[4]+"/"+str(LAU)+".jpg"

                        elif str(x[4]) == "GHI":
                            GHI = GHI + 1
                            fname = "data/"+x[4]+"/"+str(GHI)+".jpg"

                        elif str(x[4]) == "RA":
                            RA = RA + 1
                            fname = "data/"+x[4]+"/"+str(RA)+".jpg"

                        elif str(x[4]) == "MA":
                            MA = MA + 1
                            fname = "data/"+x[4]+"/"+str(MA)+".jpg"

                        elif str(x[4]) == "DI":
                            DI = DI + 1
                            fname = "data/"+x[4]+"/"+str(DI)+".jpg"

                        elif str(x[4]) == "LO":
                            LO = LO + 1
                            fname = "data/"+x[4]+"/"+str(LO)+".jpg"

                        elif str(x[4]) == "LU":
                            LU = LU + 1
                            fname = "data/"+x[4]+"/"+str(LU)+".jpg"

                        elif str(x[4]) == "RU":
                            RU = RU + 1
                            fname = "data/"+x[4]+"/"+str(RU)+".jpg"

                        elif str(x[4]) == "NGAN":
                            NGAN = NGAN + 1
                            fname = "data/"+x[4]+"/"+str(NGAN)+".jpg"

                        elif str(x[4]) == "JE":
                            JE = JE + 1
                            fname = "data/"+x[4]+"/"+str(JE)+".jpg"

                        elif str(x[4]) == "MO":
                            MO = MO + 1
                            fname = "data/"+x[4]+"/"+str(MO)+".jpg"

                        elif str(x[4]) == "NGI":
                            NGI = NGI + 1
                            fname = "data/"+x[4]+"/"+str(NGI)+".jpg"

                        elif str(x[4]) == "CA":
                            CA = CA + 1
                            fname = "data/"+x[4]+"/"+str(CA)+".jpg"

                        elif str(x[4]) == "SU":
                            SU = SU + 1
                            fname = "data/"+x[4]+"/"+str(SU)+".jpg"

                        elif str(x[4]) == "SANG":
                            SANG = SANG + 1
                            fname = "data/"+x[4]+"/"+str(SANG)+".jpg"

                        elif str(x[4]) == "BU":
                            BU = BU + 1
                            fname = "data/"+x[4]+"/"+str(BU)+".jpg"

                        elif str(x[4]) == "JU":
                            JU = JU + 1
                            fname = "data/"+x[4]+"/"+str(JU)+".jpg"

                        elif str(x[4]) == "RAI":
                            RAI = RAI + 1
                            fname = "data/"+x[4]+"/"+str(RAI)+".jpg"

                        elif str(x[4]) == "NAN":
                            NAN = NAN + 1
                            fname = "data/"+x[4]+"/"+str(NAN)+".jpg"

                        elif str(x[4]) == "SI":
                            SI = SI + 1
                            fname = "data/"+x[4]+"/"+str(SI)+".jpg"

                        elif str(x[4]) == "NA":
                            NA = NA + 1
                            fname = "data/"+x[4]+"/"+str(NA)+".jpg"

                        elif str(x[4]) == "DU":
                            DU = DU + 1
                            fname = "data/"+x[4]+"/"+str(DU)+".jpg"

                        elif str(x[4]) == "WAI":
                            WAI = WAI + 1
                            fname = "data/"+x[4]+"/"+str(WAI)+".jpg"

                        elif str(x[4]) == "E":
                            E = E + 1
                            fname = "data/"+x[4]+"/"+str(E)+".jpg"

                        elif str(x[4]) == "NYE":
                            NYE = NYE + 1
                            fname = "data/"+x[4]+"/"+str(NYE)+".jpg"

                        elif str(x[4]) == "BA":
                            BA = BA + 1
                            fname = "data/"+x[4]+"/"+str(BA)+".jpg"

                        elif str(x[4]) == "KAR":
                            KAR = KAR + 1
                            fname = "data/"+x[4]+"/"+str(KAR)+".jpg"

                        elif str(x[4]) == "KANG":
                            KANG = KANG + 1
                            fname = "data/"+x[4]+"/"+str(KANG)+".jpg"

                        elif str(x[4]) == "BO":
                            BO = BO + 1
                            fname = "data/"+x[4]+"/"+str(BO)+".jpg"

                        elif str(x[4]) == "LAN":
                            LAN = LAN + 1
                            fname = "data/"+x[4]+"/"+str(LAN)+".jpg"

                        elif str(x[4]) == "TE":
                            TE = TE + 1
                            fname = "data/"+x[4]+"/"+str(TE)+".jpg"

                        elif str(x[4]) == "PO":
                            PO = PO + 1
                            fname = "data/"+x[4]+"/"+str(PO)+".jpg"

                        elif str(x[4]) == "YA":
                            YA = YA + 1
                            fname = "data/"+x[4]+"/"+str(YA)+".jpg"

                        elif str(x[4]) == "CU":
                            CU = CU + 1
                            fname = "data/"+x[4]+"/"+str(CU)+".jpg"

                        elif str(x[4]) == "WAH":
                            WAH = WAH + 1
                            fname = "data/"+x[4]+"/"+str(WAH)+".jpg"

                        elif str(x[4]) == "U":
                            U = U + 1
                            fname = "data/"+x[4]+"/"+str(U)+".jpg"

                        elif str(x[4]) == "GHAU":
                            GHAU = GHAU + 1
                            fname = "data/"+x[4]+"/"+str(GHAU)+".jpg"

                        elif str(x[4]) == "NGAH":
                            NGAH = NGAH + 1
                            fname = "data/"+x[4]+"/"+str(NGAH)+".jpg"

                        elif str(x[4]) == "WANG":
                            WANG = WANG + 1
                            fname = "data/"+x[4]+"/"+str(WANG)+".jpg"

                        elif str(x[4]) == "NANG":
                            NANG = NANG + 1
                            fname = "data/"+x[4]+"/"+str(NANG)+".jpg"

                        elif str(x[4]) == "LANG":
                            LANG = LANG + 1
                            fname = "data/"+x[4]+"/"+str(LANG)+".jpg"

                        elif str(x[4]) == "ME":
                            ME = ME + 1
                            fname = "data/"+x[4]+"/"+str(ME)+".jpg"

                        elif str(x[4]) == "NAI":
                            NAI = NAI + 1
                            fname = "data/"+x[4]+"/"+str(NAI)+".jpg"

                        elif str(x[4]) == "NYU":
                            NYU = NYU + 1
                            fname = "data/"+x[4]+"/"+str(NYU)+".jpg"

                        elif str(x[4]) == "WO":
                            WO = WO + 1
                            fname = "data/"+x[4]+"/"+str(WO)+".jpg"

                        elif str(x[4]) == "BAI":
                            BAI = BAI + 1
                            fname = "data/"+x[4]+"/"+str(BAI)+".jpg"

                        elif str(x[4]) == "BAH":
                            BAH = BAH + 1
                            fname = "data/"+x[4]+"/"+str(BAH)+".jpg"

                        elif str(x[4]) == "YANG":
                            YANG = YANG + 1
                            fname = "data/"+x[4]+"/"+str(YANG)+".jpg"

                        elif str(x[4]) == "KE":
                            KE = KE + 1
                            fname = "data/"+x[4]+"/"+str(KE)+".jpg"

                        elif str(x[4]) == "BAN":
                            BAN = BAN + 1
                            fname = "data/"+x[4]+"/"+str(BAN)+".jpg"

                        elif str(x[4]) == "YAI":
                            YAI = YAI + 1
                            fname = "data/"+x[4]+"/"+str(YAI)+".jpg"

                        elif str(x[4]) == "DE":
                            DE = DE + 1
                            fname = "data/"+x[4]+"/"+str(DE)+".jpg"

                        elif str(x[4]) == "TAI":
                            TAI = TAI + 1
                            fname = "data/"+x[4]+"/"+str(TAI)+".jpg"

                        elif str(x[4]) == "LAI":
                            LAI = LAI + 1
                            fname = "data/"+x[4]+"/"+str(LAI)+".jpg"

                        elif str(x[4]) == "JAR":
                            JAR = JAR + 1
                            fname = "data/"+x[4]+"/"+str(JAR)+".jpg"

                        elif str(x[4]) == "JANG":
                            JANG = JANG + 1
                            fname = "data/"+x[4]+"/"+str(JANG)+".jpg"

                        elif str(x[4]) == "CE":
                            CE = CE + 1
                            fname = "data/"+x[4]+"/"+str(CE)+".jpg"

                        elif str(x[4]) == "NYAI":
                            NYAI = NYAI + 1
                            fname = "data/"+x[4]+"/"+str(NYAI)+".jpg"

                        elif str(x[4]) == "NO":
                            NO = NO + 1
                            fname = "data/"+x[4]+"/"+str(NO)+".jpg"

                        elif str(x[4]) == "YAR":
                            YAR = YAR + 1
                            fname = "data/"+x[4]+"/"+str(YAR)+".jpg"

                        elif str(x[4]) == "LE":
                            LE = LE + 1
                            fname = "data/"+x[4]+"/"+str(LE)+".jpg"

                        elif str(x[4]) == "BAR":
                            BAR = BAR + 1
                            fname = "data/"+x[4]+"/"+str(BAR)+".jpg"

                        elif str(x[4]) == "PU":
                            PU = PU + 1
                            fname = "data/"+x[4]+"/"+str(PU)+".jpg"

                        elif str(x[4]) == "RANG":
                            RANG = RANG + 1
                            fname = "data/"+x[4]+"/"+str(RANG)+".jpg"

                        elif str(x[4]) == "JAN":
                            JAN = JAN + 1
                            fname = "data/"+x[4]+"/"+str(JAN)+".jpg"

                        elif str(x[4]) == "DA":
                            DA = DA + 1
                            fname = "data/"+x[4]+"/"+str(DA)+".jpg"

                        elif str(x[4]) == "NAU":
                            NAU = NAU + 1
                            fname = "data/"+x[4]+"/"+str(NAU)+".jpg"

                        elif str(x[4]) == "JAU":
                            JAU = JAU + 1
                            fname = "data/"+x[4]+"/"+str(JAU)+".jpg"

                        elif str(x[4]) == "KO":
                            KO = KO + 1
                            fname = "data/"+x[4]+"/"+str(KO)+".jpg"

                        elif str(x[4]) == "SAN":
                            SAN = SAN + 1
                            fname = "data/"+x[4]+"/"+str(SAN)+".jpg"

                        elif str(x[4]) == "DAH":
                            DAH = DAH + 1
                            fname = "data/"+x[4]+"/"+str(DAH)+".jpg"

                        elif str(x[4]) == "HAR":
                            HAR = HAR + 1
                            fname = "data/"+x[4]+"/"+str(HAR)+".jpg"

                        elif str(x[4]) == "RAH":
                            RAH = RAH + 1
                            fname = "data/"+x[4]+"/"+str(RAH)+".jpg"

                        elif str(x[4]) == "RI":
                            RI = RI + 1
                            fname = "data/"+x[4]+"/"+str(RI)+".jpg"

                        elif str(x[4]) == "AH":
                            AH = AH + 1
                            fname = "data/"+x[4]+"/"+str(AH)+".jpg"

                        elif str(x[4]) == "TANG":
                            TANG = TANG + 1
                            fname = "data/"+x[4]+"/"+str(TANG)+".jpg"

                        elif str(x[4]) == "KAI":
                            KAI = KAI + 1
                            fname = "data/"+x[4]+"/"+str(KAI)+".jpg"

                        elif str(x[4]) == "NGA":
                            NGA = NGA + 1
                            fname = "data/"+x[4]+"/"+str(NGA)+".jpg"

                        elif str(x[4]) == "WAR":
                            WAR = WAR + 1
                            fname = "data/"+x[4]+"/"+str(WAR)+".jpg"

                        elif str(x[4]) == "NAR":
                            NAR = NAR + 1
                            fname = "data/"+x[4]+"/"+str(NAR)+".jpg"

                        elif str(x[4]) == "BANG":
                            BANG = BANG + 1
                            fname = "data/"+x[4]+"/"+str(BANG)+".jpg"

                        elif str(x[4]) == "PAI":
                            PAI = PAI + 1
                            fname = "data/"+x[4]+"/"+str(PAI)+".jpg"

                        elif str(x[4]) == "RAU":
                            RAU = RAU + 1
                            fname = "data/"+x[4]+"/"+str(RAU)+".jpg"

                        elif str(x[4]) == "GHAN":
                            GHAN = GHAN + 1
                            fname = "data/"+x[4]+"/"+str(GHAN)+".jpg"

                        elif str(x[4]) == "B":
                            B = B + 1
                            fname = "data/"+x[4]+"/"+str(B)+".jpg"

                        elif str(x[4]) == "GHANG":
                            GHANG = GHANG + 1
                            fname = "data/"+x[4]+"/"+str(GHANG)+".jpg"

                        elif str(x[4]) == "SO":
                            SO = SO + 1
                            fname = "data/"+x[4]+"/"+str(SO)+".jpg"

                        elif str(x[4]) == "HI":
                            HI = HI + 1
                            fname = "data/"+x[4]+"/"+str(HI)+".jpg"

                        elif str(x[4]) == "NAH":
                            NAH = NAH + 1
                            fname = "data/"+x[4]+"/"+str(NAH)+".jpg"

                        elif str(x[4]) == "TAN":
                            TAN = TAN + 1
                            fname = "data/"+x[4]+"/"+str(TAN)+".jpg"

                        elif str(x[4]) == "KAU":
                            KAU = KAU + 1
                            fname = "data/"+x[4]+"/"+str(KAU)+".jpg"

                        elif str(x[4]) == "CAN":
                            CAN = CAN + 1
                            fname = "data/"+x[4]+"/"+str(CAN)+".jpg"

                        elif str(x[4]) == "WAN":
                            WAN = WAN + 1
                            fname = "data/"+x[4]+"/"+str(WAN)+".jpg"

                        elif str(x[4]) == "CO":
                            CO = CO + 1
                            fname = "data/"+x[4]+"/"+str(CO)+".jpg"

                        elif str(x[4]) == "R":
                            R = R + 1
                            fname = "data/"+x[4]+"/"+str(R)+".jpg"

                        elif str(x[4]) == "BAU":
                            BAU = BAU + 1
                            fname = "data/"+x[4]+"/"+str(BAU)+".jpg"

                        elif str(x[4]) == "DAN":
                            DAN = DAN + 1
                            fname = "data/"+x[4]+"/"+str(DAN)+".jpg"

                        elif str(x[4]) == "CAR":
                            CAR = CAR + 1
                            fname = "data/"+x[4]+"/"+str(CAR)+".jpg"

                        elif str(x[4]) == "HANG":
                            HANG = HANG + 1
                            fname = "data/"+x[4]+"/"+str(HANG)+".jpg"

                        elif str(x[4]) == "ANG":
                            ANG = ANG + 1
                            fname = "data/"+x[4]+"/"+str(ANG)+".jpg"

                        elif str(x[4]) == "PAU":
                            PAU = PAU + 1
                            fname = "data/"+x[4]+"/"+str(PAU)+".jpg"

                        elif str(x[4]) == "SAR":
                            SAR = SAR + 1
                            fname = "data/"+x[4]+"/"+str(SAR)+".jpg"

                        elif str(x[4]) == "SAU":
                            SAU = SAU + 1
                            fname = "data/"+x[4]+"/"+str(SAU)+".jpg"

                        elif str(x[4]) == "TAU":
                            TAU = TAU + 1
                            fname = "data/"+x[4]+"/"+str(TAU)+".jpg"

                        elif str(x[4]) == "AN":
                            AN = AN + 1
                            fname = "data/"+x[4]+"/"+str(AN)+".jpg"

                        elif str(x[4]) == "GAR":
                            GAR = GAR + 1
                            fname = "data/"+x[4]+"/"+str(GAR)+".jpg"

                        elif str(x[4]) == "SAH":
                            SAH = SAH + 1
                            fname = "data/"+x[4]+"/"+str(SAH)+".jpg"

                        elif str(x[4]) == "TAR":
                            TAR = TAR + 1
                            fname = "data/"+x[4]+"/"+str(TAR)+".jpg"

                        elif str(x[4]) == "WI":
                            WI = WI + 1
                            fname = "data/"+x[4]+"/"+str(WI)+".jpg"

                        elif str(x[4]) == "GHAH":
                            GHAH = GHAH + 1
                            fname = "data/"+x[4]+"/"+str(GHAH)+".jpg"

                        elif str(x[4]) == "GHE":
                            GHE = GHE + 1
                            fname = "data/"+x[4]+"/"+str(GHE)+".jpg"

                        elif str(x[4]) == "GHO":
                            GHO = GHO + 1
                            fname = "data/"+x[4]+"/"+str(GHO)+".jpg"

                        elif str(x[4]) == "GHAI":
                            GHAI = GHAI + 1
                            fname = "data/"+x[4]+"/"+str(GHAI)+".jpg"

                        elif str(x[4]) == "TAH":
                            TAH = TAH + 1
                            fname = "data/"+x[4]+"/"+str(TAH)+".jpg"

                        elif str(x[4]) == "PANG":
                            PANG = PANG + 1
                            fname = "data/"+x[4]+"/"+str(PANG)+".jpg"

                        elif str(x[4]) == "WE":
                            WE = WE + 1
                            fname = "data/"+x[4]+"/"+str(WE)+".jpg"

                        elif str(x[4]) == "PAR":
                            PAR = PAR + 1
                            fname = "data/"+x[4]+"/"+str(PAR)+".jpg"

                        elif str(x[4]) == "RAR":
                            RAR = RAR + 1
                            fname = "data/"+x[4]+"/"+str(RAR)+".jpg"

                        elif str(x[4]) == "CANG":
                            CANG = CANG + 1
                            fname = "data/"+x[4]+"/"+str(CANG)+".jpg"

                        elif str(x[4]) == "LAR":
                            LAR = LAR + 1
                            fname = "data/"+x[4]+"/"+str(LAR)+".jpg"

                        elif str(x[4]) == "NGAR":
                            NGAR = NGAR + 1
                            fname = "data/"+x[4]+"/"+str(NGAR)+".jpg"

                        elif str(x[4]) == "DANG":
                            DANG = DANG + 1
                            fname = "data/"+x[4]+"/"+str(DANG)+".jpg"

                        elif str(x[4]) == "NGAI":
                            NGAI = NGAI + 1
                            fname = "data/"+x[4]+"/"+str(NGAI)+".jpg"

                        elif str(x[4]) == "NYI":
                            NYI = NYI + 1
                            fname = "data/"+x[4]+"/"+str(NYI)+".jpg"

                        elif str(x[4]) == "GANG":
                            GANG = GANG + 1
                            fname = "data/"+x[4]+"/"+str(GANG)+".jpg"

                        elif str(x[4]) == "HAI":
                            HAI = HAI + 1
                            fname = "data/"+x[4]+"/"+str(HAI)+".jpg"

                        elif str(x[4]) == "AU":
                            AU = AU + 1
                            fname = "data/"+x[4]+"/"+str(AU)+".jpg"

                        elif str(x[4]) == "AI":
                            AI = AI + 1
                            fname = "data/"+x[4]+"/"+str(AI)+".jpg"

                        elif str(x[4]) == "AR":
                            AR = AR + 1
                            fname = "data/"+x[4]+"/"+str(AR)+".jpg"

                        elif str(x[4]) == "O":
                            O = O + 1
                            fname = "data/"+x[4]+"/"+str(O)+".jpg"

                        elif str(x[4]) == "MAI":
                            MAI = MAI + 1
                            fname = "data/"+x[4]+"/"+str(MAI)+".jpg"

                        elif str(x[4]) == "NGO":
                            NGO = NGO + 1
                            fname = "data/"+x[4]+"/"+str(NGO)+".jpg"

                        elif str(x[4]) == "NGU":
                            NGU = NGU + 1
                            fname = "data/"+x[4]+"/"+str(NGU)+".jpg"

                        elif str(x[4]) == "DAR":
                            DAR = DAR + 1
                            fname = "data/"+x[4]+"/"+str(DAR)+".jpg"

                        elif str(x[4]) == "NYAN":
                            NYAN = NYAN + 1
                            fname = "data/"+x[4]+"/"+str(NYAN)+".jpg"

                        elif str(x[4]) == "NYO":
                            NYO = NYO + 1
                            fname = "data/"+x[4]+"/"+str(NYO)+".jpg"

                        elif str(x[4]) == "NYAR":
                            NYAR = NYAR + 1
                            fname = "data/"+x[4]+"/"+str(NYAR)+".jpg"

                        elif str(x[4]) == "NYAH":
                            NYAH = NYAH + 1
                            fname = "data/"+x[4]+"/"+str(NYAH)+".jpg"

                        elif str(x[4]) == "JAI":
                            JAI = JAI + 1
                            fname = "data/"+x[4]+"/"+str(JAI)+".jpg"

                        elif str(x[4]) == "DAU":
                            DAU = DAU + 1
                            fname = "data/"+x[4]+"/"+str(DAU)+".jpg"

                        elif str(x[4]) == "HO":
                            HO = HO + 1
                            fname = "data/"+x[4]+"/"+str(HO)+".jpg"

                        elif str(x[4]) == "MAU":
                            MAU = MAU + 1
                            fname = "data/"+x[4]+"/"+str(MAU)+".jpg"

                        elif str(x[4]) == "MANG":
                            MANG = MANG + 1
                            fname = "data/"+x[4]+"/"+str(MANG)+".jpg"

                        elif str(x[4]) == "HU":
                            HU = HU + 1
                            fname = "data/"+x[4]+"/"+str(HU)+".jpg"

                        elif str(x[4]) == "HAH":
                            HAH = HAH + 1
                            fname = "data/"+x[4]+"/"+str(HAH)+".jpg"

                        elif str(x[4]) == "WU":
                            WU = WU + 1
                            fname = "data/"+x[4]+"/"+str(WU)+".jpg"

                        elif str(x[4]) == "D":
                            D = D + 1
                            fname = "data/"+x[4]+"/"+str(D)+".jpg"

                        elif str(x[4]) == "HAU":
                            HAU = HAU + 1
                            fname = "data/"+x[4]+"/"+str(HAU)+".jpg"

                        elif str(x[4]) == "CAU":
                            CAU = CAU + 1
                            fname = "data/"+x[4]+"/"+str(CAU)+".jpg"

                        elif str(x[4]) == "WAU":
                            WAU = WAU + 1
                            fname = "data/"+x[4]+"/"+str(WAU)+".jpg"

                        elif str(x[4]) == "RE":
                            RE = RE + 1
                            fname = "data/"+x[4]+"/"+str(RE)+".jpg"

                        elif str(x[4]) == "RO":
                            RO = RO + 1
                            fname = "data/"+x[4]+"/"+str(RO)+".jpg"

                        elif str(x[4]) == "MAR":
                            MAR = MAR + 1
                            fname = "data/"+x[4]+"/"+str(MAR)+".jpg"

                        elif str(x[4]) == "GAI":
                            GAI = GAI + 1
                            fname = "data/"+x[4]+"/"+str(GAI)+".jpg"

                        elif str(x[4]) == "JO":
                            JO = JO + 1
                            fname = "data/"+x[4]+"/"+str(JO)+".jpg"

                        elif str(x[4]) == "NGAU":
                            NGAU = NGAU + 1
                            fname = "data/"+x[4]+"/"+str(NGAU)+".jpg"

                        elif str(x[4]) == "NGANG":
                            NGANG = NGANG + 1
                            fname = "data/"+x[4]+"/"+str(NGANG)+".jpg"

                        elif str(x[4]) == "NYANG":
                            NYANG = NYANG + 1
                            fname = "data/"+x[4]+"/"+str(NYANG)+".jpg"

                        elif str(x[4]) == "YAH":
                            YAH = YAH + 1
                            fname = "data/"+x[4]+"/"+str(YAH)+".jpg"

                        elif str(x[4]) == "MAH":
                            MAH = MAH + 1
                            fname = "data/"+x[4]+"/"+str(MAH)+".jpg"

                        elif str(x[4]) == "CAH":
                            CAH = CAH + 1
                            fname = "data/"+x[4]+"/"+str(CAH)+".jpg"

                        elif str(x[4]) == "CAI":
                            CAI = CAI + 1
                            fname = "data/"+x[4]+"/"+str(CAI)+".jpg"

                        elif str(x[4]) == "GAU":
                            GAU = GAU + 1
                            fname = "data/"+x[4]+"/"+str(GAU)+".jpg"

                        elif str(x[4]) == "GAH":
                            GAH = GAH + 1
                            fname = "data/"+x[4]+"/"+str(GAH)+".jpg"

                        elif str(x[4]) == "YE":
                            YE = YE + 1
                            fname = "data/"+x[4]+"/"+str(YE)+".jpg"

                        elif str(x[4]) == "YI":
                            YI = YI + 1
                            fname = "data/"+x[4]+"/"+str(YI)+".jpg"

                        elif str(x[4]) == "NYAU":
                            NYAU = NYAU + 1
                            fname = "data/"+x[4]+"/"+str(NYAU)+".jpg"

                        elif str(x[4]) == "GHAR":
                            GHAR = GHAR + 1
                            fname = "data/"+x[4]+"/"+str(GHAR)+".jpg"

                        elif str(x[4]) == "CI":
                            CI = CI + 1
                            fname = "data/"+x[4]+"/"+str(CI)+".jpg"

                        elif str(x[4]) == "YO":
                            YO = YO + 1
                            fname = "data/"+x[4]+"/"+str(YO)+".jpg"

                        elif str(x[4]) == "RAN":
                            RAN = RAN + 1
                            fname = "data/"+x[4]+"/"+str(RAN)+".jpg"

                        elif str(x[4]) == "JAH":
                            JAH = JAH + 1
                            fname = "data/"+x[4]+"/"+str(JAH)+".jpg"

                        else : 
                        	fname = "data/"+x[4]+".jpg"                        

                        #i = 0
                        #im = cv2.rectangle(im,(x[0],x[1]),(x[2],x[3]),(255,0,0),5)
                        tmp_im = im[x[1]:x[3], x[0]:x[2]]
                        #plt.imshow(tmp_im)
                        tmp_im_scale = cv2.resize(tmp_im,(70,70))
                        tmp_im_scale = tmp_im_scale.astype('float32') #set x_train data type as float32
                        tmp_im_scale /= 255 #change x_train value between 0 - 1
                        arr_tmp_im = []
                        arr_tmp_im.append(tmp_im_scale.reshape(1, 70, 70, 3))
                        #pred = model.predict_classes(arr_tmp_im)
                        #print("Ground Truth: " + x[4] + ", Prediksi: " + get_class(str(pred)))
                        #im = cv2.putText(im, int(x[0]), (int(x[0]), int(x[1])-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
                        #print(x[4])
                        #os.mkdir(img_dir) 
                        img_dir_pkl = "data/"+x[4]
                        try:
                            os.mkdir(img_dir_pkl)
                        except:
                            pass
                        #j = str(x)
                        #print (fname)
                        cv2.imwrite(fname,tmp_im)
                        #plt.imsave(fname,tmp_im,format="jpg")
                        #plt.show()
                    #print("FOTO ANOTASI")
                    #plt.imshow(im)
                    #plt.show()
                    im_arr.append({"nama":name, "box":boxes})

                    #os.mkdir(img_dir)
                    

            except Exception as e: 
                print("Error: "+str(e))
        #total = mobil+motor+pohon+pkl+pejalan_kaki+truk+bus+rambu+rumah+sepeda+becak+sedan+halte

        print("motor ",motor)
        print("pohon ",pohon)
        print("pkl ",pkl)
        print("pejalan kaki ",pejalan_kaki)
        print("truk ",truk)
        print("bus ",bus)
        print("rambu ",rambu)
        print("rumah ",rumah)
        print("sepeda ",sepeda)
        print("becak ",becak)
        print("sedan ",sedan)
        print("halte ",halte)
        #print("total = ",total)
           #print("Jumlah "+str(i)+" : "+str(count))
label = label + 1
#print ("Dilarang Stop : ",mobil)    
process(PA,GI,I,JI,MI,N,JA,K,PE,DO,M,GHA,SA,NE,BE,TO,H,NI,HAN,GE,GO,BI,A,NYA,HA,GA,T,WA,GHU,NG,NGE,LI,KA,KAN,NU,MAN,PI,KAH,KU,TI,TU,KI,LA,PAH,GAN,TA,GH,SE,YU,LAH,GU,S,MU,L,YAN,YAU,SAI,PAN,DAI,HE,LAU,GHI,RA,MA,DI,LO,LU,RU,NGAN,JE,MO,NGI,CA,SU,SANG,BU,JU,RAI,NAN,SI,NA,DU,WAI,E,NYE,BA,KAR,KANG,BO,LAN,TE,PO,YA,CU,WAH,U,GHAU,NGAH,WANG,NANG,LANG,ME,NAI,NYU,WO,BAI,BAH,YANG,KE,BAN,YAI,DE,TAI,LAI,JAR,JANG,CE,NYAI,NO,YAR,LE,BAR,PU,RANG,JAN,DA,NAU,JAU,KO,SAN,DAH,HAR,RAH,RI,AH,TANG,KAI,NGA,WAR,NAR,BANG,PAI,RAU,GHAN,B,GHANG,SO,HI,NAH,TAN,KAU,CAN,WAN,CO,R,BAU,DAN,CAR,HANG,ANG,PAU,SAR,SAU,TAU,AN,GAR,SAH,TAR,WI,GHAH,GHE,GHO,GHAI,TAH,PANG,WE,PAR,RAR,CANG,LAR,NGAR,DANG,NGAI,NYI,GANG,HAI,AU,AI,AR,O,MAI,NGO,NGU,DAR,NYAN,NYO,NYAR,NYAH,JAI,DAU,HO,MAU,MANG,HU,HAH,WU,D,HAU,CAU,WAU,RE,RO,MAR,GAI,JO,NGAU,NGANG,NYANG,YAH,MAH,CAH,CAI,GAU,GAH,YE,YI,NYAU,GHAR,CI,YO,RAN,JAH)