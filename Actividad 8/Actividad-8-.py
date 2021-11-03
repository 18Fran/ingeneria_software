import time
arrayToken = []
arrayRepeats = []
arrayPosting = []
arrayHtmlPosting = []
arrayHardPosting = []
arrayMediumPosting = []
arraySimplePosting = []

execution_time = time.time()

posting_path = 'posting.txt'
simple_token = 'tokenized/simple.txt'
medium_token = 'tokenized/medium.txt'
hard_token = 'tokenized/hard.txt'
htmltoken = 'tokenized/049.txt'

posting_list =  open(posting_path, mode="r", errors="ignore")
hard_list =  open(hard_token, mode="r", errors="ignore")
medium_list =  open(medium_token, mode="r", errors="ignore")
simple_list = open(simple_token, mode="r", errors="ignore")
html_list =  open(htmltoken, mode="r", errors="ignore")

for item in html_list:
    stringsFromList = item.partition(' ')
    arrayToken.append(stringsFromList[0])
    arrayRepeats.append(stringsFromList[2].replace("\n",""))
    for post in posting_list:
        stringInPost = post.partition('|')
        if stringInPost[0] == '049.html ':
            correctstring = stringInPost[2].replace(" ","")
            arrayHtmlPosting.append(correctstring[0].replace("n",""))
    arrayPosting.extend(arrayHtmlPosting)


for item in hard_list:
    stringsFromList = item.partition(' ')
    arrayToken.append(stringsFromList[0])
    arrayRepeats.append(stringsFromList[2].replace("\n",""))
    for post in posting_list:
        stringInPost = post.partition('|')
        if stringInPost[0] == 'hard.html ':
            correctstring = stringInPost[2].replace(" ","")
            arrayHardPosting.append(correctstring[0].replace("n",""))
    
    arrayPosting.extend(arrayHardPosting)



for item in medium_list:
    stringsFromList = item.partition(' ')
    arrayToken.append(stringsFromList[0])
    arrayRepeats.append(stringsFromList[2].replace("\n",""))
    for post in posting_list:
        stringInPost = post.partition('|')
        if stringInPost[0] == 'medium.html ':
            correctstring = stringInPost[2].replace(" ","")
            arrayMediumPosting.append(correctstring[0].replace("n",""))
    arrayPosting.extend(arrayMediumPosting)



for item in simple_list:
    stringsFromList = item.partition(' ')
    arrayToken.append(stringsFromList[0])
    repeatCorrect = stringsFromList[2].replace(" ","")
    arrayRepeats.append(repeatCorrect.replace("n",""))
    for post in posting_list:
        stringInPost = post.partition('|')
        if stringInPost[0] == 'simple.html ':
            correctstring = stringInPost[2].replace(" ","")
            arraySimplePosting.append(correctstring[0].replace("n",""))
    arrayPosting.extend(arraySimplePosting)




dictionary = {
    'Token':arrayToken,
    'Repeats':arrayRepeats,
    'Posting':arrayPosting,
}


with open('a8matricula.txt', 'w') as file:
    tokens =  dictionary.get('Token',1)
    repeats =  dictionary.get('Repeats',1)
    posting =  dictionary.get('Posting',1)

    for x in range(len(tokens)):
        token = ''
        repeat = ''
        post = ''

        if tokens[x] == ' ':
            token = '------'
        else:
            token = str(tokens[x])
            
        if repeats[x] == ' ':
            repeat = '------'
        else:
            repeat = str(repeats[x])
            
        if posting[x] == ' ':
            post = '------'
        else:
            post = str(posting[x])


        data = token + "                                    " + repeat + "                                    " + post + "\n"
        file.write(str(data))
        
    file.write("Time of execution: " + str(execution_time) + " seconds. \n")
