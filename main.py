from ftplib import FTP
import os

ftp = FTP()
ftp.connect(host='127.0.0.1',port=21)
ftp.login('klaus', 'klaus')     
# ftp.retrlines('LIST') 

listing = []
ftp.retrlines("NLST", listing.append)
print(listing)
# for f in listing:
#     print(f.split(" ")[-1])
# # ftp.file('')
# ftp.cwd('Janjaap')
# cf = open("test.txt", "wb")
# f = "effe.txt"
# ftp.retrbinary('RETR %s' % "effe.txt", cf.write)
ftp.quit()

