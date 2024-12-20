def parse(file):
    htmlName = f"{file.removesuffix(".tml")}.html"
    finishedhtml = ""
    print(f"Parsing... {file}")
    with open(file, "r") as f:
        tml = f.readlines()
    for line in tml:
        line = line.removesuffix("\n")
        while line.startswith(" "):
            line = line.removeprefix(" ")

        # Body tags
        if line.startswith("h1"):
            htmlTag = "<h1>%</h1>"
            tmlTag = "h1"
        elif line.startswith("h2"):
            htmlTag = "<h2>%</h2>" 
            tmlTag = "h2"
        elif line.startswith("p"):
            htmlTag = "<p>%</p>" 
            tmlTag = "p"
        elif line.startswith("img"):
            htmlTag = '<img src="%">'
            tmlTag = "img"
        elif line.startswith("*"):
            htmlTag = '<li>%</li>'
            tmlTag = "*"
        elif line.startswith("div"):
            htmlTag = '<hr>'
            tmlTag = "div"
        elif line.startswith("banner"):
            htmlTag = '<div class="banner">%</div>'
            tmlTag = "banner"

        elif line.startswith("center("):
            htmlTag = '<div class="center">\n%'
            tmlTag = "center"
        elif line.startswith(")center"):
            htmlTag = '\n</div class="center">'
            tmlTag = ")center"

        elif line.startswith("box("):
            htmlTag = '<div class="root"><div class="box">\n%'
            tmlTag = "box"
        elif line.startswith(")box"):
            htmlTag = '\n</div class="box"></div class="root">'
            tmlTag = ")box"

        elif line.startswith("body("):
            htmlTag = "<body>"
            tmlTag = "inf("
        elif line.startswith(")body"):
            htmlTag = "</body>"
            tmlTag = ")inf"    

        elif line.startswith("<"):
            htmlTag = line
            tmlTag = ""

        # Head tags
        elif line.startswith("inf{"):
            htmlTag = "<head>"
            tmlTag = "inf("
        elif line.startswith(")inf"):
            htmlTag = "</head>"
            tmlTag = ")inf"    
        elif line.startswith("theme"):
            htmlTag = '<link href="%" rel="stylesheet" type="text/css" media="all">'
            tmlTag = "theme"
        elif line.startswith("title"):
            htmlTag = "<title>%</title>"
            tmlTag = "title"
        else:
            htmlTag = ""
            tmlTag = ""

        tagContents = line.removeprefix(f'{tmlTag}(')
        tagContents = tagContents.removesuffix(")")
        parsedtml = htmlTag.replace("%", tagContents)
        finishedhtml = f"{finishedhtml}\n{parsedtml}"
    with open(htmlName, "w") as f:
        f.write(finishedhtml)
        print(f"Finished parsing {file}!")

parse("example.tml")