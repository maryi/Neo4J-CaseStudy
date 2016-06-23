import os

# open list of issue ids
issue_ids = open("issue_id.txt")

# for each issue id in the file
for issue in issue_ids.read().splitlines():
	url = 'https://github.com/neo4j/neo4j/issues/' + issue;
	# os.system("webkit2png " + url + " -F")
	os.system("wkhtmltopdf " + url + " " + issue + ".pdf")