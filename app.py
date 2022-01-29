from synology_api import universal_search
from workflow import Workflow3,ICON_WEB
import sys,os
import json

def main(wf):
	query = wf.args[0]
	hst=os.getenv('host')
	port = os.getenv('port')
	user = os.getenv('user')
	pwd = os.getenv('pwd')
	sq = universal_search.UniversalSearch(hst, port, user, pwd, secure=True, cert_verify=False, dsm_version=6, debug=False, otp_code=None)
	res=sq.search(query)['data']['hits']
	dat=[]
	for item in res:
		t=""
		if item['SYNOMDIsDir'] != 'y':
			t="/"+item["SYNOMDFSName"]
		result = {
			"title": item["SYNOMDFSName"],
			"subtitle": item["SYNOMDSharePath"],
			"arg": item["SYNOMDSharePath"].replace(t,""),
			"autocomplete": "",
			"icon": {
				"path": "./icon.png"
			}
		}
		dat.append(result)
	response = json.dumps({
		"items": dat
	})
	sys.stdout.write(response)

if __name__ == '__main__':
	wf = Workflow3()
	sys.exit(wf.run(main))