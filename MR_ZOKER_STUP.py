import os
import time
import sys 
import base64
import marshal
import zlib
import random
from rich.progress import track

#--------------COLOR-------------#
l="\033[1;90m"      # Black
r="\033[1;91m"        # Red
g="\033[1;92m"      # Green
y="\033[1;93m"     # Yellow
b="\033[1;94m"       # Blue
p="\033[1;95m"     # Purple
c="\033[1;96m"       # Cyan
w="\033[1;97m"      # White
l="\033[1;90m"      # Black
r="\033[1;91m"        # Red
g="\033[1;92m"      # Green
y="\033[1;93m"     # Yellow
b="\033[1;94m"       # Blue
p="\033[1;95m"     # Purple
c="\033[1;96m"       # Cyan
w="\033[1;97m"      # White
x = "\033[0;37m"
z = "\033[1;30m"
k = "\033[1;31m"
m = "\033[1;32m"
n = "\033[1;34m"
o = "\033[1;35m"
q = "\033[1;36m"
s = "\033[1;37m"
A="\033[1;90m"      # Black
C="\033[1;91m"        # Red
D="\033[1;92m"      # Green
E="\033[1;93m"     # Yellow
F="\033[1;94m"       # Blue
G="\033[1;95m"     # Purple
H="\033[1;96m"       # Cyan
#---------------DEF LINE------------#
def line():
	print(22*'\033[1;91m━━')
#----------------LOGO--------------#
ben = f"""
{r}███    ███ ██████       █████  ██████  ██ ██████  
{c}████  ████ ██   ██     ██   ██ ██   ██ ██ ██   ██ 
{b}██ ████ ██ ██████      ███████ ██   ██ ██ ██████  
{c}██  ██  ██ ██   ██     ██   ██ ██   ██ ██ ██   ██ 
{r}██      ██ ██   ██     ██   ██ ██████  ██ ██████  

              {p}╔════════════════════╗ 
              {y}┃ \033[37;41mENCRYPTION TOOLS\033[0;m\033    \033[1;32m{y}┃ 
              {p}╚════════════════════╝ 
"""
def jalan():
    os.system("clear")
    print(ben)
    line()
    print(f"{b}[{w}={b}]  {w}OWNNER    {y}: {c}AHMED ADIB")
    print(f"{b}[{w}={b}]  {w}FB PAGE   {y}: {w}HELLO WORLD")
    print(f"{b}[{w}={b}]  {w}GITHUB    {y}: {w}MR{r}-{w}ADIB{r}-{w}7{r}0{w}7")
    print(f"{b}[{w}={b}]  {w}TOOLS     {y}: {w}F{c}/{w}R{c}/{w}G")
    line()
def MR_ADIB():
	jalan()
	line()
	print(f"{b}[{w}01{b}] {w}BASE{r}-{p}64   {y}: {w}ENCRYPTION ")
	print(f"{b}[{w}02{b}] {w}MARSHAL   {y}: {w}ENCRYPTION ")
	print(f"{b}[{w}03{b}] {w}ZLIB      {y}: {w}ENCRYPTION ")
	print(f"{b}[{w}04{b}] {w}BASE{r}-{p}64 {y}& {y}: {w}MARSHAL ENCRYPTION ")
	print(f"{b}[{w}05{b}] {w}MARSHAL   {y}: {w}IMOJI ENCRYPTION ")
	print(f"{b}[{w}01{b}] {c}EXIT MY   {y}: {r}TOOLS")
	line()
	ops=input(f" {y}[{b}={y}] {y}[{b}->{y}] {w}CHO{l}O{w}SSE {y}:{l} ")
	if ops in ['01','1']:
		BASE()
	if ops in ['02','2']:
		MARSHAL()
	if ops in ['03','3']:
		ZLIB()
	if ops in ['04','4']:
		MAR_BASE()
	if ops in ['05','5']:
		IMOJI()
#----------------BASE64---------------#
def BASE():
	jalan()
	time.sleep(1)
	file=input(f"   {b}[{p}={b}] {w}ENTER YOUR SOURCE FILE {y}:{c} ")
	line()
	time.sleep(1)
	out_file=input(f"   {b}[{p}={b}] {w}ENTER YOUR OUTPUT FILE NAME {y}:{c} ")
	line()
	time.sleep(1)
	try:
	    op_file=open(file,'r').read()
	except:
		fk=f"\n\n\n         {b}[{y}×{b}] {w}FILE N{r}O{w}T F{r}O{w}UND ERR{r}O{w}R \n"
		for char in fk:
			sys.stdout.write(char)
			sys.stdout.flush()
			time.sleep(0.09)
		exit()
	jalan()
	comx=base64.b64encode(op_file.encode())
	show=f'import base64\nexec(__REAL__KING__AHMED ADIB__base64.b64decode({comx}))'
	adib=open(out_file,'w')
	adib.write("#CREAT BY AHMED ADIB\n")
	adib.write("#FB PAGE : HELLO WORLD\n")
	adib.write("#GITHUB  : MR-ADIB-707\n\n")
	adib.write("""
       🥰🥰 𝐑𝐄𝐀𝐋 𝐊𝐈𝐍𝐆   🥰🥰  
😈  🥰😙      😎😎          🥰🥰  😈
😈  🥰😎      😎😎          🤩🥰  😈
😈  🥰😙      😎😎          🤩🥰  😈
😈  🥰😙      😎😎          🤩🥰  😈
       🥰🥰𝐀𝐇𝐌𝐄𝐃 𝐀𝐃𝐈𝐁🥰🥰 \n\n""")
	adib.write(show)
	adib.close()
	time.sleep(4)
	print(f"   {b}[{y}={b}] {w}ENCRYPTION {g}PROCESSING{c}・{y}・{g}・{p}・")
	line()
	time.sleep(3)
	print(f"   {b}[{y}={b}] {l}Please Wait{w}.{r}.{g}.{c}.")
	line()
	def adiib(sumaiya):
		for i in track(range(100),description=sumaiya):
		    time.sleep(0.1)
	adiib(f"{g}PR{l}O{c}CESS{r}ING ")
	jalan()
	adibx = f"""
        {p}█▀▀ █▄ █ █▀▀ █▀█ █▄█ █▀█ ▀█▀ █ █▀█ █▄ █
        ██▄ █ ▀█ █▄▄ █▀▄  █  █▀▀  █  █ █▄█ █ ▀█ 

                {l}█▀▀ █▀█ █▀▄▀█ █▀█ █   █▀▀ ▀█▀ █▀▀
                █▄▄ █▄█ █ ▀ █ █▀▀ █▄▄ ██▄  █  ██▄ 
\n"""
	for char in adibx:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.01)
	time.sleep(2)
	line()
	print(f"{b}[{w}√{b}] {w}BASE64 ENCRYPTION {c}COMPLETE{l}√{l}√")
	line()
	time.sleep(2)
	print(f"{b}[{c}√{b}] {w}SAVE {g}AS {c}={y} "+out_file)
	line()
	print("            \033[37;41m☠️CREAT BY/AHMED ADIB☠️\033[0;m\033    \033[1;32m")
#---------------------------BASE64PROGRAM END--------------------------#
#------------MARSHAL------------#
def MARSHAL():
	jalan()
	time.sleep(1)
	filex=input(f"   {b}[{p}={b}] {w}ENTER YOUR SOURCE FILE {y}:{c} ")
	line()
	time.sleep(1)
	out_filex=input(f"   {b}[{p}={b}] {w}ENTER YOUR OUTPUT FILE NAME {y}:{c} ")
	line()
	time.sleep(1)
	try:
	    chek_file=open(filex,'r').read()
	except:
		fk=f"\n\n\n         {b}[{y}×{b}] {w}FILE N{r}O{w}T F{r}O{w}UND ERR{r}O{w}R \n"
		for char in fk:
			sys.stdout.write(char)
			sys.stdout.flush()
			time.sleep(0.09)
		exit()
	jalan()
	sex=compile(chek_file,'dg','exec')
	heda=marshal.dumps(sex)
	showing=f'import marshal\nexec__TERA BAP___AHMED ADIB__(marshal.loads({heda}))'
	zokerxx=open(out_filex,'w')
	zokerxx.write("#CREAT BY AHMED ADIB\n")
	zokerxx.write("#FB PAGE : HELLO WORLD\n")
	zokerxx.write("#GITHUB  : MR-ADIB-707\n\n")
	zokerxx.write("""
       🥰🥰 𝐑𝐄𝐀𝐋 𝐊𝐈𝐍𝐆   🥰🥰  
😈  🥰😙      😎😎          🥰🥰  😈
😈  🥰😎      😎😎          🤩🥰  😈
😈  🥰😙      😎😎          🤩🥰  😈
😈  🥰😙      😎😎          🤩🥰  😈
       🥰🥰𝐀𝐇𝐌𝐄𝐃 𝐀𝐃𝐈𝐁🥰🥰  \n\n""")
	zokerxx.write(showing)
	zokerxx.close()
	time.sleep(4)
	print(f"   {b}[{y}={b}] {w}ENCRYPTION {g}PROCESSING{c}・{y}・{g}・{p}・")
	line()
	time.sleep(3)
	print(f"   {b}[{y}={b}] {l}Please Wait{w}.{r}.{g}.{c}.")
	line()
	time.sleep(3)
	for i in range(4):
		os.system("clear")
		print("        PROSSEING ENC ")
		print(f"        {g}[■□□□□□□□□□]")
		time.sleep(0.2)
		os.system("clear")
		print("        PROSSEING ENC ")
		print(f"        {r}[■■□□□□□□□□]")
		time.sleep(0.1)
		os.system("clear")
		print("        PROSSEING ENC ")
		print(f"        {y}[■■■□□□□□□□]")
		time.sleep(0.1)
		os.system("clear")
		print("        PROSSEING ENC ")
		print(f"        {y}[■■■■□□□□□□]")
		time.sleep(0.1)
		os.system("clear")
		print("        PROSSEING ENC ")
		print(f"        {g}[■■■■■□□□□□]")
		time.sleep(0.1)
		os.system("clear")
		print("        PROSSEING ENC ")
		print(f"        {c}[■■■■■■□□□□]")
		time.sleep(0.1)
		os.system("clear")
		print("        PROSSEING ENC ")
		print(f"        {b}[■■■■■■■□□□]")
		time.sleep(0.1)
		os.system("clear")
		print("        PROSSEING ENC ")
		print(f"        {y}[■■■■■■■■□□]")
		time.sleep(0.1)
		os.system("clear")
		print("        PROSSEING ENC ")
		print(f"        {r}[■■■■■■■■■□]")
		time.sleep(0.1)
		os.system("clear")
		print("        PROSSEING ENC ")
		print(f"        {g}[■■■■■■■■■■]")
		time.sleep(0.1)
	jalan()
	adibx = f"""
        {p}█▀▀ █▄ █ █▀▀ █▀█ █▄█ █▀█ ▀█▀ █ █▀█ █▄ █
        ██▄ █ ▀█ █▄▄ █▀▄  █  █▀▀  █  █ █▄█ █ ▀█ 

                {l}█▀▀ █▀█ █▀▄▀█ █▀█ █   █▀▀ ▀█▀ █▀▀
                █▄▄ █▄█ █ ▀ █ █▀▀ █▄▄ ██▄  █  ██▄ 
\n"""
	for char in adibx:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.01)
	time.sleep(2)
	line()
	print(f"{b}[{w}√{b}] {w}MARSHAL ENCRYPTION {c}COMPLETE{l}√{l}√")
	line()
	time.sleep(2)
	print(f"{b}[{c}√{b}] {w}SAVE {g}AS {c}={y} "+out_filex)
	line()
	print("            \033[37;41m☠️CREAT BY/AHMED ADIB☠️\033[0;m\033    \033[1;32m")
#--------------------------MARSHAL END----------------------------#

#------------XLIB-ENCRYPTION-----------#
def ZLIB():
	jalan()
	time.sleep(1)
	fiLL=input(f"   {b}[{p}={b}] {w}ENTER YOUR SOURCE FILE {y}:{c} ")
	line()
	time.sleep(1)
	out_fiLL=input(f"   {b}[{p}={b}] {w}ENTER YOUR OUTPUT FILE NAME {y}:{c} ")
	line()
	time.sleep(1)
	try:
	    z_file=open(fiLL,'r').read()
	except:
		fk=f"\n\n\n         {b}[{y}×{b}] {w}FILE N{r}O{w}T F{r}O{w}UND ERR{r}O{w}R \n"
		for char in fk:
			sys.stdout.write(char)
			sys.stdout.flush()
			time.sleep(0.09)
		exit() 
	jalan()
	lib=zlib.compress(z_file.encode())
	main=f'import zlib\nexec(___REAL___KING___AHMED ADIB___zlib.decompress({lib}).decode())'
	jan=open(out_fiLL,'w')
	jan.write("#CREAT BY AHMED ADIB\n")
	jan.write("#FB PAGE : HELLO WORLD\n")
	jan.write("#GITHUB  : MR-ADIB-707\n\n")
	jan.write("""
       🥰🥰 𝐑𝐄𝐀𝐋 𝐊𝐈𝐍𝐆   🥰🥰  
😈  🥰😙      😎😎          🥰🥰  😈
😈  🥰😎      😎😎          🤩🥰  😈
😈  🥰😙      😎😎          🤩🥰  😈
😈  🥰😙      😎😎          🤩🥰  😈
   .   🥰🥰𝐀𝐇𝐌𝐄𝐃 𝐀𝐃𝐈𝐁🥰🥰 \n\n""")
	jan.write(main)
	jan.close()
	time.sleep(2)
	print(f"   {b}[{y}={b}] {w}ENCRYPTION {g}PROCESSING{c}・{y}・{g}・{p}・")
	line()
	time.sleep(3)
	print(f"   {b}[{y}={b}] {l}Please Wait{w}.{r}.{g}.{c}.")
	line()
	time.sleep(1)
	def adiib(sumaiya):
		for i in track(range(100),description=sumaiya):
		    time.sleep(0.1)
	adiib(f"{g}PR{l}O{c}CESS{r}ING ")
	time.sleep(2)
	jalan()
	adibx = f"""
        {p}█▀▀ █▄ █ █▀▀ █▀█ █▄█ █▀█ ▀█▀ █ █▀█ █▄ █
        ██▄ █ ▀█ █▄▄ █▀▄  █  █▀▀  █  █ █▄█ █ ▀█ 

                {l}█▀▀ █▀█ █▀▄▀█ █▀█ █   █▀▀ ▀█▀ █▀▀
                █▄▄ █▄█ █ ▀ █ █▀▀ █▄▄ ██▄  █  ██▄ 
\n"""
	for char in adibx:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.01)
	time.sleep(2)
	line()
	print(f"{b}[{w}√{b}] {w}ZLIB ENCRYPTION {c}COMPLETE{l}√{l}√")
	line()
	time.sleep(2)
	print(f"{b}[{c}√{b}] {w}SAVE {g}AS {c}={y} "+out_fiLL)
	line()
	print("            \033[37;41m☠️CREAT BY/AHMED ADIB☠️\033[0;m\033    \033[1;32m")
#---------------------zlib program finished-----------------#
#----------MARSHAL&BASE64-----------#
def MAR_BASE():
	jalan()
	time.sleep(1)
	py_file_na=input(f"   {b}[{p}={b}] {w}ENTER YOUR SOURCE FILE {y}:{c} ")
	line()
	time.sleep(1)
	out_py_file=input(f"   {b}[{p}={b}] {w}ENTER YOUR OUTPUT FILE NAME {y}:{c} ")
	line()
	time.sleep(1)
	try:
	    openx_file=open(py_file_na,'r').read()
	except:
		fk=f"\n\n\n         {b}[{y}×{b}] {w}FILE N{r}O{w}T F{r}O{w}UND ERR{r}O{w}R \n"
		for char in fk:
			sys.stdout.write(char)
			sys.stdout.flush()
			time.sleep(0.09)
		exit()
	jalan()
	fuck=compile(openx_file,'dg','exec')
	khanki=marshal.dumps(fuck)
	fucking=f'import marshal\nimport base64\nexec_ = lambda __ : __import__marshal.loads__import__base64.b64decode(__[::-1])));(marshal.loads({khanki})base64.b64decode({khanki}))'
	bow=open(out_py_file,'w')
	bow.write("#CREAT BY AHMED ADIB\n")
	bow.write("#FB PAGE : HELLO WORLD\n")
	bow.write("#GITHUB  : MR-ADIB-707\n\n")
	bow.write("""
       🥰🥰 𝐑𝐄𝐀𝐋 𝐊𝐈𝐍𝐆   🥰🥰  
😈  🥰😙      😎😎          🥰🥰  😈
😈  🥰😎      😎😎          🤩🥰  😈
😈  🥰😙      😎😎          🤩🥰  😈
😈  🥰😙      😎😎          🤩🥰  😈
       🥰🥰𝐀𝐇𝐌𝐄𝐃 𝐀𝐃𝐈𝐁🥰🥰   \n\n""")
	bow.write("😈𝐑𝐄𝐀𝐋 𝐊𝐈𝐍𝐆 - 𝐀𝐇𝐌𝐄𝐃 𝐀𝐃𝐈𝐁😈\n\n")
	bow.write(fucking)
	bow.close()
	time.sleep(4)
	print(f"   {b}[{y}={b}] {w}ENCRYPTION {g}PROCESSING{c}・{y}・{g}・{p}・")
	line()
	time.sleep(3)
	print(f"   {b}[{y}={b}] {l}Please Wait{w}.{r}.{g}.{c}.")
	line()
	time.sleep(3)
	for i in range(100):
	    adiiiib=random.choice([A,C,D,E,F,G,H])
	    print(f"\n\n\n\n\n\n          {adiiiib}Prossesing....",i)
	    os.system("clear")
	    time.sleep(0.01)
	time.sleep(2)
	jalan()
	adibx = f"""
        {p}█▀▀ █▄ █ █▀▀ █▀█ █▄█ █▀█ ▀█▀ █ █▀█ █▄ █
        ██▄ █ ▀█ █▄▄ █▀▄  █  █▀▀  █  █ █▄█ █ ▀█ 

                {l}█▀▀ █▀█ █▀▄▀█ █▀█ █   █▀▀ ▀█▀ █▀▀
                █▄▄ █▄█ █ ▀ █ █▀▀ █▄▄ ██▄  █  ██▄ 
\n"""
	for char in adibx:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.01)
	time.sleep(2)
	line()
	print(f"{b}[{w}√{b}] {w}BASE64+MARSHAL  ENCRYPTION {c}COMPLETE{l}√{l}√")
	line()
	time.sleep(2)
	print(f"{b}[{c}√{b}] {w}SAVE {g}AS {c}={y} "+out_py_file)
	line()
	print("            \033[37;41m☠️CREAT BY/AHMED ADIB☠️\033[0;m\033    \033[1;32m")	
#-------------------------**LAST ENCIMOJI----------------------#
def IMOJI():
	jalan()
	time.sleep(1)
	ADIB_sumaiya=input(f"   {b}[{p}={b}] {w}ENTER YOUR SOURCE FILE {y}:{c} ")
	line()
	time.sleep(1)
	bowx=input(f"   {b}[{p}={b}] {w}ENTER YOUR OUTPUT FILE NAME {y}:{c} ")
	line()
	time.sleep(1)
	try:
	    chek_filexx=open(ADIB_sumaiya,'r').read()
	except:
		fk=f"\n\n\n         {b}[{y}×{b}] {w}FILE N{r}O{w}T F{r}O{w}UND ERR{r}O{w}R \n"
		for char in fk:
			sys.stdout.write(char)
			sys.stdout.flush()
			time.sleep(0.09)
		exit()
	jalan()
	sex=compile(chek_filexx,'dg','exec')
	heda=marshal.dumps(sex)
	showing=f'import marshal\nexec__TERA BAP___AHMED ADIB__(🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰marshal.loads({heda}))'
	zokerx=open(bowx,'w')
	zokerx.write("#CREAT BY AHMED ADIB\n")
	zokerx.write("#FB PAGE : HELLO WORLD\n")
	zokerx.write("#GITHUB  : MR-ADIB-707\n\n")
	zokerx.write("""
       🥰🥰 𝐑𝐄𝐀𝐋 𝐊𝐈𝐍𝐆   🥰🥰  
😈  🥰😙      😎😎          🥰🥰  😈
😈  🥰😎      😎😎          🤩🥰  😈
😈  🥰😙      😎😎          🤩🥰  😈
😈  🥰😙      😎😎          🤩🥰  😈
       🥰🥰𝐀𝐇𝐌𝐄𝐃 𝐀𝐃𝐈𝐁🥰🥰  \n\n""")
	zokerx.write(showing)
	zokerx.close()
	time.sleep(4)
	print(f"   {b}[{y}={b}] {w}ENCRYPTION {g}PROCESSING{c}・{y}・{g}・{p}・")
	line()
	time.sleep(3)
	print(f"   {b}[{y}={b}] {l}Please Wait{w}.{r}.{g}.{c}.")
	line()
	time.sleep(3)
	for i in range(4):
		os.system("clear")
		print("        PROSSEING ENC ")
		print(f"        {g}[■□□□□□□□□□]")
		time.sleep(0.2)
		os.system("clear")
		print("        PROSSEING ENC ")
		print(f"        {r}[■■□□□□□□□□]")
		time.sleep(0.1)
		os.system("clear")
		print("        PROSSEING ENC ")
		print(f"        {y}[■■■□□□□□□□]")
		time.sleep(0.1)
		os.system("clear")
		print("        PROSSEING ENC ")
		print(f"        {y}[■■■■□□□□□□]")
		time.sleep(0.1)
		os.system("clear")
		print("        PROSSEING ENC ")
		print(f"        {g}[■■■■■□□□□□]")
		time.sleep(0.1)
		os.system("clear")
		print("        PROSSEING ENC ")
		print(f"        {c}[■■■■■■□□□□]")
		time.sleep(0.1)
		os.system("clear")
		print("        PROSSEING ENC ")
		print(f"        {b}[■■■■■■■□□□]")
		time.sleep(0.1)
		os.system("clear")
		print("        PROSSEING ENC ")
		print(f"        {y}[■■■■■■■■□□]")
		time.sleep(0.1)
		os.system("clear")
		print("        PROSSEING ENC ")
		print(f"        {r}[■■■■■■■■■□]")
		time.sleep(0.1)
		os.system("clear")
		print("        PROSSEING ENC ")
		print(f"        {g}[■■■■■■■■■■]")
		time.sleep(0.1)
	jalan()
	adibx = f"""
        {p}█▀▀ █▄ █ █▀▀ █▀█ █▄█ █▀█ ▀█▀ █ █▀█ █▄ █
        ██▄ █ ▀█ █▄▄ █▀▄  █  █▀▀  █  █ █▄█ █ ▀█ 

                {l}█▀▀ █▀█ █▀▄▀█ █▀█ █   █▀▀ ▀█▀ █▀▀
                █▄▄ █▄█ █ ▀ █ █▀▀ █▄▄ ██▄  █  ██▄ 
\n"""
	for char in adibx:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.01)
	time.sleep(2)
	line()
	print(f"{b}[{w}√{b}] {w}MARSHAL IMOJI ENCRYPTION {c}COMPLETE{l}√{l}√")
	line()
	time.sleep(2)
	print(f"{b}[{c}√{b}] {w}SAVE {g}AS {c}={y} "+bowx)
	line()
	print("            \033[37;41m☠️CREAT BY/AHMED ADIB☠️\033[0;m\033    \033[1;32m")
#----------------- END PROGRAMME-------------#
MR_ADIB()