import re
txt_to_search = "123.34.2.12"
pattern = re.compile(r"^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$")
result = pattern.finditer(txt_to_search)
for i in result:
	print(i.start(),i.end(),i.group(0),i.group(1),i.group(2),i.group(3))

# IPV6: patern = re.compile(r"^((([0-9a-fA-F]){1,4}\:){7}([0-9a-fA-F]){1,4})$")