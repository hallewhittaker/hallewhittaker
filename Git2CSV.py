from os import remove
import subprocess
r= subprocess.run('git --no-pager blame --line-porcelain README.md',stdout= subprocess.PIPE)
#currently uses system command line to read a specific document.

tab = r.stdout.split(b'\t') 
arrayofDictionaries = []

for lineinfoS in tab:
    linearray= lineinfoS.split(b'\n')
    tempdictionary = {}
    
    for individL in linearray:
        individL = individL.decode("utf-8")
        splitline = individL.split(" ")

        for i in splitline[0]:
            if i in splitline[0] ==('d6b24e6dec9eca5db2acfcb393a62146f640759f'): 
                tempdictionary["Hash"] = splitline[0]
                
        tempkeyN = splitline[0]
        splitline[0] = " "

        joinline = " ".join(splitline).lstrip()

        for x in joinline:
            if x in joinline == ('1 1 1'):
                tempdictionary["LineNumbers"] = joinline
        
        for key,value in dict(tempdictionary).items():
            if key == ('d6b24e6dec9eca5db2acfcb393a62146f640759f'):
                    del tempdictionary[key]
    
        tempdictionary[tempkeyN] = joinline
    arrayofDictionaries.append(tempdictionary)
    break
print(arrayofDictionaries)



#Using Dictionaries
# testH = {}
# Array1 = ["value1", "value2", "value3"]
# testH["hash"] = Array1[1]
# print(testH)











# testdictionary1= {"email": "whittaker@gmail.com", "message": "hello welcom"}
# testdictionary2= {"email": "like@gmail.com", "message": "bye welcom"}

# #print(testdictionary1["email"])
# arrayofD= [testdictionary1,testdictionary2]

# #print(arrayofD)

# for currentDictionary in arrayofD:
#     print(currentDictionary["email"])





#if str(arrayofDictionaries) == "[{b'author': b'hallewhittaker', b'author-mail': b'<88335095+hallewhittaker@users.noreply.github.com>', b'author-time': b'1627917128', b'author-tz': b'+0100', b'committer': b'GitHub', b'committer-mail': b'<noreply@github.com>', b'committer-time': b'1627917128', b'committer-tz': b'+0100', b'summary': b'Create README.md', b'boundary': b'', b'filename': b'README.md', b'': b''}, {b'--->': b'', b\"'\": b''}]":
#    print("passed!")
# else:
#    print("FAILED!!!!")

# test_data = b"author hallewhittaker\nauthor-mail <88335095+hallewhittaker@users.noreply.github.com>\nauthor-time 1627917128\nauthor-tz +0100\ncommitter GitHub\ncommitter-mail <noreply@github.com>\ncommitter-time 1627917128\ncommitter-tz +0100\nsummary Create README.md\nboundary\nfilename README.md\n\t--->\n'"
# tab = test_data.split(b'\t') 

#Using re.split
# cheader =[]
# cdata = []

# import re
# a="b'filename README.md'" #work
# b="b'boundary'" #work
# c="b'author-mail <88335095+hallewhittaker@users.noreply.github.com>'" #work

# #pattern = r"\s+|[']|'(?=\s)"
# result = [s for s in re.split(pattern, c) if s]
# print(result)

# cheader.append(result[1])
# print(cheader)

# if len(result) >2:
#     cdata.append(result[2])       
# else:
#     cdata.append('N/A')
# print(cdata) 
#currently uses a string, splits said string into column header + data