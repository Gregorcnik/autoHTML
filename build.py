websiteF = open("index.html", "wt")
contentF = open("content.amd", "rt")

content = contentF.read().split('\n')
websiteContent = ""

def tagit (text: str, tag: str) -> str:
  return f"<{tag}>{text}</{tag}>"

title = ""
style = ""

i = 0;
while (content[i][0] == "$"):
  variable = content[i].split(" ")[0];
  value = " ".join(content[i].split(" ")[1:]).strip('\n');

  if (variable == "$TITLE"): title = value
  elif (variable == "$STYLE"): style = value

  i += 1

for i in range(i, len(content)):
  line = content[i].strip()

  if (line == ""): line = "<br>"
  elif (line.split(" ")[0] == "#"): line = tagit(" ".join(line.split(" ")[1:]), "h1")
  elif (line.split(" ")[0] == "##"): line = tagit(" ".join(line.split(" ")[1:]), "h2")
  elif (line.split(" ")[0] == "###"): line = tagit(" ".join(line.split(" ")[1:]), "h3")
  elif (line.split(" ")[0] == "####"): line = tagit(" ".join(line.split(" ")[1:]), "h4")
  else: line = tagit(line, "p")

  websiteContent += line+'\n'

websiteF.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="stylesheet" href="{style}">
</head>
<body>
{websiteContent}
</body>
</html>
""")

websiteF.close()
contentF.close()