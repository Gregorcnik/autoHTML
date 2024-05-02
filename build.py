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

  if (line == ""): pass
  elif (line.split(" ")[0] == "#"): line = tagit(" ".join(line.split(" ")[1:]), "h1")
  elif (line.split(" ")[0] == "##"): line = tagit(" ".join(line.split(" ")[1:]), "h2")
  elif (line.split(" ")[0] == "###"): line = tagit(" ".join(line.split(" ")[1:]), "h3")
  elif (line.split(" ")[0] == "####"): line = tagit(" ".join(line.split(" ")[1:]), "h4")
  else: line = tagit(line, "p")

  websiteContent += line+'\n'

websiteF.write(f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;700&display=swap">
  <link rel="stylesheet" href="templates/{style}">
</head>
<body>
  <div class="p-4 bg-dark text-white text-center" id="naslov">
    <h1 id="title">{title}</h1>
  </div>
  <div class="container-xl mt-5 px-sm-5">
{websiteContent}
  </div>
</body>
</html>
''')

websiteF.close()
contentF.close()