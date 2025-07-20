def extract_outline(doc):
    outline = []
    font_sizes = {}

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                line_text = ""
                max_font_size = 0
                for span in line.get("spans", []):
                    text = span["text"].strip()
                    if not text:
                        continue
                    size = round(span["size"], 1)
                    font_sizes[size] = font_sizes.get(size, 0) + 1
                    line_text += " " + text
                    max_font_size = max(max_font_size, size)

                line_text = line_text.strip()
                if not line_text:
                    continue
                level = classify_heading_level(max_font_size, font_sizes)
                if level:
                    outline.append({
                        "level": level,
                        "text": line_text,
                        "page": page_num
                    })

    return outline

def classify_heading_level(size, font_sizes):
    sorted_sizes = sorted(font_sizes.keys(), reverse=True)
    if len(sorted_sizes) < 3:
        return None

    if size == sorted_sizes[0]:
        return "H1"
    elif size == sorted_sizes[1]:
        return "H2"
    elif size == sorted_sizes[2]:
        return "H3"
    else:
        return None