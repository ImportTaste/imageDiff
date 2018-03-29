import sys

talkitive = True
try:
    if sys.argv[3] == "-s":
        talkitive = False
except IndexError:
    pass

if talkitive:
    print("Starting decode...")

from skimage import io
from base64 import b64decode as b64d
import based

baseImage = io.imread(sys.argv[1]).tolist()
encodedImage = io.imread(sys.argv[2]).tolist()

if len(baseImage) != len(encodedImage) or len(baseImage[0]) != len(encodedImage[0]):
    print("Mis-matching dimensions!")
    sys.exit()

if talkitive:
    print("Scanning image...")

diffs = []

r = True
x = True
for i in range(len(baseImage)):
    if not r:
        break
    for o in range(len(baseImage[i])):
        if not r:
            break
        for p in range(3):
            if baseImage[i][o][p] == encodedImage[i][o][p]:
                r = False
                break
            if x:
                encoding = abs(baseImage[i][o][p] - encodedImage[i][o][p])
                x = False
            else:
                diffs.append(abs(baseImage[i][o][p] - encodedImage[i][o][p]))

if talkitive:
    print("Converting text...")

message = based.unprocess(diffs, encoding)

if talkitive:
    print("Message decrypted!")
print(message)
