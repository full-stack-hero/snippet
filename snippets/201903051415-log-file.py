# :autor: @full.stack.hero
# :url: https://github.com/full-stack-hero/snippet/blob/master/snippet/snippets/201903051415-log-file.py
# An Apache logfile can be huge and hard to read.
# Here is a way to get a list of the most visited pages (or files) from an
# Apache logfile.
#
# In this example, we only want to know the URLs from GET requests. We will use
# the wonderful Counter which is in Python's Collections
import collections

logfile = open("yourlogfile.log", "r")

clean_log=[]

for line in logfile:
    try:
        # copy the URLS to an empty list.
        # We get the part between GET and HTTP
        clean_log.append(line[line.index("GET")+4:line.index("HTTP")])
    except:
        pass

counter = collections.Counter(clean_log)

# get the Top 50 most popular URLs
for count in counter.most_common(50):
    print(str(count[1]) + "	" + str(count[0]))

logfile.close()
