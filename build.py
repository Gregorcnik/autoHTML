import markdown
import os

# Create sites directory if it doesn't exist
os.makedirs("_site", exist_ok=True)

websiteF = open("./_site/index.html", "wt")
contentF = open("content.amd", "rt")

content = contentF.read().split('\n')
websiteContent = ""

def tagit (text: str, tag: str) -> str:
  return f"<{tag}>{text}</{tag}>"

title = ""
style = ""

i = 0;
while (len(content[i]) > 0 and content[i][0] == "$"):
  variable = content[i].split(" ")[0];
  value = " ".join(content[i].split(" ")[1:]).strip('\n');

  if (variable == "$TITLE"): title = value
  elif (variable == "$STYLE"): style = value

  i += 1

websiteContent = markdown.markdown("\n".join(content[i:]), extensions=['codehilite'])

websiteF.write(f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;700&display=swap">
  <link rel="stylesheet" href="codeTheme.css">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="p-4 text-center" id="naslov">
    <h1 id="title">{title}</h1>
  </div>
  <div class="container-xl mt-5 px-sm-5 pb-5">
    {websiteContent}
  </div>
</body>
</html>
''')

# Add selected stylesheet to _site/
with open(f"themes/{style}", "rt") as stylesheet:
  with open("./_site/style.css", "wt") as newFile:
    newFile.write(stylesheet.read())

websiteF.close()
contentF.close()