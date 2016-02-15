# coding=UTF-8
import csv
import  os
import sys

csv.field_size_limit(sys.maxsize)
# this file is to handle the csv to row,easy to handle it
for root,dirs,files in os.walk("/mnt/hgfs/webodata/csv/"):
    for f in files:

        print f
        readOne=open("/mnt/hgfs/webodata/csv/" + f, 'r')
        # saveUserId=open("/mnt/hgfs/webodata/userId/userId"+f,'w')
        # saveIssueId=open("/mnt/hgfs/webodata/issueId/issueId"+f,'w')
        saveComment=open("/mnt/hgfs/webodata/comment/comment"+f,'w')
        for row in csv.DictReader(readOne):
            saveComment.write(row["mid"]+","+row["text"]+"\n")

        readOne.close()
        saveComment.close()

