import re
import subprocess
def main():	
	ls = []
	device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
	df = subprocess.check_output("lsusb", shell=True)
	for i in df.split('\n'):
	    if i:
	        info = device_re.match(i)
	        if info:
	            dinfo = info.groupdict()
	            # Uncomment if you wish tags too
	            # print dinfo
	            ls.append((dinfo['tag'], dinfo['id']))

	for i in ls:
		print ls.index(i),".", i[0],i[1]
	n = 0
	while 1:

		try:
			n = int(raw_input("Choose your device:"))
		except:
			pass
		if n >= 0 and n < len(ls):
			break
	return ls[n][1]

# print main()