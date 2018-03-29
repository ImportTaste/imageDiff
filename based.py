import base64 as b64
from textwrap import wrap

def b2encode(text):

    out = ""
    for i in text:
        tmp = bin(ord(i))[2:]
        while len(tmp) < 7:
            tmp = "0" + tmp
        out += tmp
    return out

def b2decode(text):

    cutMessage = wrap(text, 7)
    out = ""
    for i in cutMessage:
        out += chr(int(i, 2))
    return out

def b8encode(text):

    out = ""
    for i in text:
        tmp = oct(ord(i))[1:]
        while len(tmp) < 3:
            tmp = "0" + tmp
        out += tmp
    return out

def b8decode(text):

    cutMessage = wrap(text, 3)
    out = ""
    for i in cutMessage:
        out += chr(int(i, 8))
    return out

def process(message, imageLength):

    encType = ""
    encMessage = None

    tencMessage = b64.b64encode(message)
    if imageLength > len(tencMessage):
        encMessage = tencMessage
        alphaBit = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
        encType = 64

    tencMessage = b64.b32encode(message)
    if imageLength > len(tencMessage):
        encMessage = tencMessage
        alphaBit = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567="
        encType = 32

    tencMessage = b64.b16encode(message)
    if imageLength > len(tencMessage):
        encMessage = tencMessage
        alphaBit = "0123456789ABCDEF"
        encType = 16

    tencMessage = b8encode(message)
    if imageLength > len(tencMessage):
        encMessage = tencMessage
        alphaBit = "01234567"
        encType = 8

    tencMessage = b2encode(message)
    if imageLength > len(tencMessage):
        encMessage = tencMessage
        alphaBit = "01"
        encType = 2

    if encMessage == None:
        return None

    aboot = []
    for i in encMessage:
        x = 0
        for o in alphaBit:
            x += 1
            if i == o:
                aboot.append(int(x))

    return [encType, aboot]

def unprocess(aboot, encoding):

    alphaBit = None

    if encoding == 64:
        alphaBit = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

    if encoding == 32:
        alphaBit = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567="

    if encoding == 16:
        alphaBit = "0123456789ABCDEF"

    if encoding == 8:
        alphaBit = "01234567"

    if encoding == 2:
        alphaBit = "01"

    if alphaBit == None:
        return None

    basedMessage = ""
    for i in range(len(aboot)):
        basedMessage += alphaBit[aboot[i] - 1]

    message = ""
    if encoding == 64:
        message = b64.b64decode(basedMessage)

    if encoding == 32:
        message = b64.b32decode(basedMessage)

    if encoding == 16:
        message = b64.b16decode(basedMessage)

    if encoding == 8:
        message = b8decode(basedMessage)

    if encoding == 2:
        message = b2decode(basedMessage)

    return message
