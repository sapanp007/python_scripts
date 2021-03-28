"""
Script to read multiple log files and get output based on reequirement.
Here it is to get max occuring user per log file
"""

"""
sample of log data:
73.92.19.149 - - [13/Mar/2021:20:44:37 +0000] "GET /images/icons/common/Icon_Edge.svg HTTP/1.1" 200 1382 "https://prosimodemo.admin.prosimo.io/dashboard/main" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
10.16.1.1 - - [13/Mar/2021:20:36:47 +0000] "GET /live HTTP/1.1" 200 0 "-" "kube-probe/1.15+"
"""
import concurrent.futures
import subprocess, re
from collections import Counter


class ReadLogFile:
	def __init__(self,filename):
		self.file_data = []
		self.users = []
		self.filename = filename
		self.make_dict()


	def make_dict(self):
		pattern = re.compile(r'(?P<user>[\d.]*)[\s\S]*(?P<type>(GET|POST)) (?P<path>[\s\S]*) [\s\S]*" (?P<status_code>\d*) \d* "(?P<url>[\w:/.]*)"[\s\S]* (?P<last_col>\w*\/\d*\.\d*)')
		with open(self.filename,'r') as f:
			while len(f.readline())>0:
				result = pattern.search(f.readline())
				if result is not None:
					self.file_data.append(result.groupdict())
					self.users.append(result.groupdict()["user"])
				f.seek(f.tell()+1)


	def return_max_user(self):
		return Counter(self.users).most_common(1)[0][0]


def get_all_files(search_key):
	files_list =subprocess.run(f"ls {search_key}", capture_output = True, encoding = 'UTF-8').stdout.split("\n")[:-1]
	return files_list


if __name__ == "__main__":
	files_list = get_all_files("f*.txt")	#get all the .txt log files with f*
	with concurrent.futures.ThreadPoolExecutor() as executor:
		file_objs = executor.map(ReadLogFile,files_list)
		for file_obj in file_objs:
			user = file_obj.return_max_user()
			print(f"user with max entry in {file_obj.filename} is {user}")
