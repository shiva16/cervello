import urllib.request
url = 'http://export.arxiv.org/api/query?search_query=all:brain&start=0&max_results=5'
data = urllib.request.urlopen(url).read()
# print (data)

with open('data_', 'w') as data_file:
    data_file.write(str(data))
