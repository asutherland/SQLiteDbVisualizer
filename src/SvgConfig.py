from DbInfoTemplate import PageType


main = {
    "encoding": "utf-8",
}

page = {
    "width": 512,

    "fillColor": "#ffffff",
    "strokeWidth": 2,
    PageType.TABLE_LEAF + "strokeColor": "#ff3333",
    PageType.TABLE_INTERIOR + "strokeColor": "#aa0000",
    PageType.INDEX_LEAF + "strokeColor": "#3333ff",
    PageType.INDEX_INTERIOR + "strokeColor": "#0000aa",
    PageType.OVERFLOW + "strokeColor": "#33ff33",
    PageType.UNCERTAIN + "strokeColor": "#666666",
}

btreeList = {  # Top element
    "x": 0,
    "y": 10,

    "legendFontSize": 6,
    "legendHeight": 6,
    "legendNCol": 2,

    "legendTopMargin": 4,
    "legendStrokeWidth": "1",
    "legendStrokeColor": "#000000",
}

btreeColorPalette = [
    "LightSteelBlue",
    "LightSeaGreen",
    "Pink",
    "OldLace",
    "Silver",
    "MediumTurquoise",
    "Green",
    "Honeydew",
    "Beige",
    "Wheat",
    "AliceBlue",
    "Ivory",
    "ForestGreen",
    "PaleGoldenrod",
    "Goldenrod",
    "Bisque",
    "SandyBrown",
    "Salmon",
    "DodgerBlue",
    "GreenYellow",
    "BlanchedAlmond",
    "SteelBlue",
    "MediumSpringGreen",
    "MintCream",
    "Orchid",
    "Linen",
    "LightCyan",
    "Turquoise",
    "DarkTurquoise",
    "Violet",
    "PaleVioletRed",
    "DarkSeaGreen",
    "IndianRed",
    "Azure",
    "WhiteSmoke",
    "LightSkyBlue",
    "Purple",
    "LightSalmon",
    "DarkOrchid",
    "SaddleBrown",
    "Chocolate",
    "Fuchsia",
    "PowderBlue",
    "Chartreuse",
    "Brown",
    "MediumOrchid",
    "Gainsboro",
    "Navy",
    "Orange",
    "LightPink",
    "FireBrick",
    "SlateGray",
    "Lavender",
    "LightGreen",
    "Snow",
    "LimeGreen",
    "Magenta",
    "DeepSkyBlue",
    "DarkSlateBlue",
    "Seashell",
    "SeaGreen",
    "Moccasin",
    "LightCoral",
    "DimGray",
    "Crimson",
    "BlueViolet",
    "Yellow",
    "LemonChiffon",
    "Gold",
    "MistyRose",
    "Tan",
    "CadetBlue",
    "MediumSlateBlue",
    "Peru",
    "Lime",
    "DarkOrange",
    "LightYellow",
    "Plum",
    "PaleTurquoise",
    "Aquamarine",
    "DarkKhaki",
    "CornflowerBlue",
    "Teal",
    "Aqua",
    "LightGray",
    "Gray",
    "LightSlateGray",
    "MidnightBlue",
    "DarkSlateGray",
    "Olive",
    "LavenderBlush",
    "DeepPink",
    "Coral",
    "LightBlue",
    "PaleGreen",
    "Indigo",
    "Sienna",
    "NavajoWhite",
    "PeachPuff",
    "White",
    "DarkBlue",
    "Cyan",
    "RosyBrown",
    "BurlyWood",
    "AntiqueWhite",
    "DarkGray",
    "DarkOliveGreen",
    "Blue",
    "Maroon",
    "OrangeRed",
    "Black",
    "PapayaWhip",
    "Thistle",
    "Tomato",
    "OliveDrab",
    "MediumVioletRed",
    "LawnGreen",
    "DarkMagenta",
    "DarkGoldenrod",
    "HotPink",
    "Cornsilk",
    "DarkGreen",
    "MediumPurple",
    "YellowGreen",
    "MediumAquamarine",
    "RoyalBlue",
    "LightGoldenrodYellow",
    "Red",
    "DarkViolet",
    "SkyBlue",
    "SpringGreen",
    "MediumBlue",
    "SlateBlue",
    "DarkCyan",
    "DarkSalmon",
    "GhostWhite",
    "MediumSeaGreen",
    "FloralWhite",
    "Khaki",
    "DarkRed",
]

pageList = {  # Top element
    "x": 0,
    "yPadFromBtreeList": 0,

    "pageNumWidth": 36,
    "pageNumFontSize": 4,
    "pageNumLeftMargin": 4,
    "pageNumTopMargin": 4,
}

cell = {
    "height": 4,
}
