import subprocess,os,time,sys


with open("/etc/udev/rules.d/70-persistent-net.rules","r") as f:
	fa = f.read().encode("utf8")

t = fa.count('SUBSYSTEM')

if t > 1:
	q = re.compile('SUBSYSTEM.*eth\d{1,2}"\\n\\n').findall(fa)
	for i in range(len(q)):  
		fa = fa.replace(q[i],'')
	a = re.compile('eth\d{1,2}').findall(fa)[0]
	p = fa.replace(a,'eth0')
	with open("/etc/udev/rules.d/70-persistent-net.rules","w") as f:
		f.write(p)
	os.system("sudo reboot")

else:
	address = sys.argv[1]
	work_dir = os.path.dirname(os.path.realpath(__file__))
	work_dir = os.path.join(work_dir,'debug_log')
	if not os.path.exists(work_dir):
		os.makedirs(work_dir)
	res = subprocess.Popen('sudo python {0}'.format(address),
	       stdout = subprocess.PIPE,
	       stderr = subprocess.PIPE,
	       shell = True,
	)
	out,err = res.communicate()


	nowTime = time.strftime("%y-%m-%d-%H-%M-%S",time.localtime())
	listdir = os.listdir(work_dir)
	if len(listdir) >= 10:
		for i,e in enumerate(listdir[::-1]):
			if i >= 10:
				filename = os.path.join(work_dir,e)
				os.remove(filename)
	with open(os.path.join(work_dir,"{0}.log".format(nowTime)),"w") as f:
		f.write("out:\n"+out)
		f.write("err:\n"+err)