websiteF = open("index.html", "wt")
contentF = open("content.amd", "rt")

content = contentF.read()

websiteF.write(content)

websiteF.close()
contentF.close()