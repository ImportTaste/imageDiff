import sys, based

talkitive = True
try:
    if sys.argv[2] == "-s":
        talkitive = False
except IndexError:
    pass

if talkitive:
    print("Starting encode...")

import warnings
warnings.filterwarnings("ignore", category=Warning)
from skimage import io
from base64 import b64encode as b64e

imageIn = io.imread(sys.argv[1]).tolist()
rawMessage = " ".join(sys.argv[2:])

imgLen = 0
for i in imageIn:
    for o in imageIn:
        imgLen += 3

if talkitive:
    print("Readying message...")

message = based.process(rawMessage, imgLen)

if message == None:
    print("Message too long for image! Try a larger image or a shorter message.")
    sys.exit()

messageLen = len(message[1])

if talkitive:
    print("Altering image...")
x = -1
r = True
for i in range(len(imageIn)):
    if not r:
        break
    for o in range(len(imageIn[i])):
        if not r:
            break
        for p in range(3):
            if x >= messageLen:
                r = False
                break
            if x == -1:
                if imageIn[i][o][p] < 128:
                    imageIn[i][o][p] += message[0]
                else:
                    imageIn[i][o][p] -= message[0]
                x += 1
                continue
            if imageIn[i][o][p] < 128:
                imageIn[i][o][p] += message[1][x]
            else:
                imageIn[i][o][p] -= message[1][x]
            x += 1

if talkitive:
    print("Writing image...")
io.imsave("enc_" + sys.argv[1], imageIn)
if talkitive:
    print("Encode successful!")
