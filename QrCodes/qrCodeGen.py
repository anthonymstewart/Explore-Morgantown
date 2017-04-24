import sys, pyqrcode, io


#Straights:
#N-S - '1010' = 10
NS = pyqrcode.create(10)
NS.svg('NSqr.svg', scale=10, background="blue",module_color="yellow")
buffer = io.BytesIO()
NS.svg(buffer)

#W-E - '0101' = 5
WE = pyqrcode.create(5)
WE.svg('WEqr.svg', scale=10, background="blue",module_color="yellow")
buffer = io.BytesIO()
WE.svg(buffer)

#Curves
#N-E - '1100' = 12
NE = pyqrcode.create(12)
NE.svg('NEqr.svg', scale=10, background="blue",module_color="yellow")
buffer = io.BytesIO()
NE.svg(buffer)

#E-S - '0110' = 6
ES = pyqrcode.create(6)
ES.svg('ESqr.svg', scale=10, background="blue",module_color="yellow")
buffer = io.BytesIO()
ES.svg(buffer)

#S-W - '0011' = 3
SW = pyqrcode.create(3)
SW.svg('SWqr.svg', scale=10, background="blue",module_color="yellow")
buffer = io.BytesIO()
SW.svg(buffer)

#W-N - '1001' = 9
WN = pyqrcode.create(9)
WN.svg('WNqr.svg', scale=10, background="blue",module_color="yellow")
buffer = io.BytesIO()
WN.svg(buffer)

#3-ways
#N-E-S - '1110' = 14
NES = pyqrcode.create(14)
NES.svg('NESqr.svg', scale=10, background="blue",module_color="yellow")
buffer = io.BytesIO()
NES.svg(buffer)


#E-S-W - '0111' = 7
ESW = pyqrcode.create(7)
ESW.svg('ESWqr.svg', scale=10, background="blue",module_color="yellow")
buffer = io.BytesIO()
ESW.svg(buffer)

#S-W-N - '1011' = 11
SWN = pyqrcode.create(11)
SWN.svg('SWNqr.svg', scale=10, background="blue",module_color="yellow")
buffer = io.BytesIO()
SWN.svg(buffer)

#W-N-E - '1101' = 13
WNE = pyqrcode.create(13)
WNE.svg('WNEqr.svg', scale=10, background="blue",module_color="yellow")
buffer = io.BytesIO()
WNE.svg(buffer)

#4-way
#N-E-S-W - '1111' = 15
NESW = pyqrcode.create(15)
NESW.svg('NESWqr.svg', scale=10, background="blue",module_color="yellow")
buffer = io.BytesIO()
NESW.svg(buffer)