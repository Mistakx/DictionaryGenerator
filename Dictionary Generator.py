import os

WebpageWordsFileLocation: str = "/home/mistakx/Desktop/Dict"
DictionaryLocation: str = "/home/mistakx/Desktop/Dictionary"

linesAlreadySeen = []

with open(WebpageWordsFileLocation) as WebpageWordsFile:

    with open(DictionaryLocation, "w") as DictionaryWrite:
        os.system("clear")

        for line in WebpageWordsFile.readlines():

            for word in line.split(" "):
                for word in word.split("="):
                    parsedWord: str = word
                    parsedWord = parsedWord.replace("!", "")
                    parsedWord = parsedWord.replace(".", "")
                    parsedWord = parsedWord.replace(",", "")
                    parsedWord = parsedWord.replace("\n", "")
                    parsedWord = parsedWord.replace(" ", "")
                    parsedWord = parsedWord.replace("(", "")
                    parsedWord = parsedWord.replace(")", "")
                    parsedWord = parsedWord.replace(":", "")
                    parsedWord = parsedWord.replace("[", "")
                    parsedWord = parsedWord.replace("]", "")
                    parsedWord = parsedWord.replace(";", "")
                    parsedWord = parsedWord.replace("\"", "")
                    parsedWord = parsedWord.replace("'", "")
                    parsedWord = parsedWord.replace("*", "")
                    parsedWord = parsedWord.replace("-", "")
                    parsedWord = parsedWord.replace("?", "")

                    #! Capitalized version
                    capitalizedParsedWord = parsedWord.capitalize()
                    
                    if capitalizedParsedWord != "":
                        if capitalizedParsedWord not in linesAlreadySeen:
                            DictionaryWrite.write(capitalizedParsedWord + "\n")
                            linesAlreadySeen.append(capitalizedParsedWord)

                    #! Uncapitalized version
                    uncapitalizedParsedWord = parsedWord.lower()
                    if uncapitalizedParsedWord != "":
                        if uncapitalizedParsedWord not in linesAlreadySeen:
                            DictionaryWrite.write(uncapitalizedParsedWord + "\n")
                            linesAlreadySeen.append(uncapitalizedParsedWord)

os.system("sort " + DictionaryLocation + " -o " + DictionaryLocation)