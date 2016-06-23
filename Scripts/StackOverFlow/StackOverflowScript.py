import os

# open list of issue ids
issue_ids = open("StackOverflowIds.csv")

# for each issue id in the file
for issue in issue_ids.read().splitlines():
	url = 'http://stackoverflow.com/questions/' + issue;
	# os.system("webkit2png " + url + " -F")
	os.system("wkhtmltopdf " + url + " " + issue + ".pdf")