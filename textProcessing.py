# REDEFINE Below methods to add parsed fields correctly to the Stickies (Parsed fields: Assumptions, acceptance
# Criteria etc) TODO: Define a method that addresses cases of sub-bullets in stories: (Case1: Main bullet is general
#  statement, each sub is its own story) (Case2: main bullet is story and sub bullets are description)
# TODO: **Depending on formatting possibly just modify populate text to accept the added fields **
from PopulateStickies import populate_category


def populate_text_General_statement(run, storyCategory, storyBullets):
    for txbx in run.iter(w + "txbxContent"):
        # Add story category to first existing paragraph
        for subParagraph in txbx.iter(w + "p"):
            populate_category(subParagraph, storyCategory)
            break  # Break execution and move into sub-paragraph

        # Insert Main Bullet as a general statement
        bullet = etree.Element(w + "p",
                               attrib={w + "rsidR": "00924485", w + "rsidRPr": "00924485",
                                       w + "rsidRDefault": "00924485", w + "rsidP": "002853AF"})  # 00524C8F

        # Insert iteratively each sub-bullet as its own story point
        # TODO:  Do the initial check here to see if the sub bullets have their own story points.
        startIndex = 0
    for k, bulletText in zip(range(len(storyBullets)), storyBullets):
        # Two asterisk indicates that the bullet text in storyBullets is actually describing the story,
        # thus the previous line must be story bullet (its owns story)
        for line in lines[startIndex: len(lines)]:
            if line.startswith("==="):  # "===" indicates the beginning of a story category
                bullet = etree.Element(w + "p", attrib={w + "rsidR": "00924485", w + "rsidRPr": "00924485",
                                                        w + "rsidRDefault": "00924485", w + "rsidP": "002853AF"})
                # Add paragraph formatting
                pPr = etree.Element(w + "pPr")
                numPr = etree.Element(w + "numPr")
                etree.SubElement(numPr, w + "ilvl", attrib={w + "val": "0"})
                etree.SubElement(numPr, w + "numId", attrib={w + "val": "11"})
                etree.SubElement(pPr, w + "pStyle", attrib={w + "val": "ListParagraph"})
                pPr.insert(0, numPr)
                etree.SubElement(pPr, w + "spacing",
                                 attrib={w + "before": "100", w + "beforeAutospacing": "1", w + "after": "100",
                                         w + "afterAutospacing": "1", w + "line": "240", w + "lineRule": "auto"})
                bullet.insert(0, pPr)

                # Add the run
                newRun = etree.Element(w + "r", attrib={w + "rsidRPr": "002853AF"})

                # Run formatting
                rPr = etree.Element(w + "rPr")
                etree.SubElement(rPr, w + "rFonts",
                                 attrib={w + "ascii": "Times New Roman", w + "eastAsia": "Times New Roman",
                                         w + "hAnsi": "Times New Roman", w + "cs": "Times New Roman"})
                etree.SubElement(rPr, w + "sz", attrib={w + "val": "24"})
                etree.SubElement(rPr, w + "szCs", attrib={w + "val": "24"})
                newRun.insert(0, rPr)

                # Run the text append
                newText = etree.Element(w + "t")
                newText.text = bulletText
                newRun.insert(1, newText)
                bullet.insert(1, newRun)
                txbx.insert(-1, bullet)


def populate_text_acceptanceCriteria(run, storyCategory, storyDescription, storyBullets, acceptanceCriteria):
    for txbx in run.iter(w + "txbxContent"):  # Get first available Paragraph
        # Add story category to first existing paragraph
        for subParagraph in txbx.iter(w + "p"):
            populate_category(subParagraph, storyCategory)
            break
        # Populates the text with the requested acceptance Criteria
        for subParagraph in txbx.iter(w + "p"):
            populate_category(acceptanceCriteria, storyCategory)
            break

        # Add new paragraph containing the story points
        content = etree.Element(w + "p",
                                attrib={w + "rsidR": "0014164D", w + "rsidRPr": "00DB3E27",
                                        w + "rsidRDefault": "00143C72", w + "rsidP": "00DB3E27"})

        newRun = etree.Element(w + "r")
        newText = etree.Element(w + "t")
        newText.text = storyDescription
        newText.text = acceptanceCriteria
        newRun.insert(0, newText)
        newRun.insert(1, acceptanceCriteria)  # This line may not be needed
        content.insert(0, newRun)
        txbx.insert(1, content)

        # If there are bullets, add new paragraphs for them
        for i, bulletText in zip(range(len(storyBullets)), storyBullets):
            bullet = etree.Element(w + "p",
                                   attrib={w + "rsidR": "00924485", w + "rsidRPr": "00924485",
                                           w + "rsidRDefault": "00924485", w + "rsidP": "002853AF"})  # 00524C8F

            # TODO: Adjust the paragraph formatting here to better accommodate the acceptanceCriteria field name
            # Add paragraph formatting
            pPr = etree.Element(w + "pPr")
            numPr = etree.Element(w + "numPr")
            etree.SubElement(numPr, w + "ilvl", attrib={w + "val": "0"})
            etree.SubElement(numPr, w + "numId", attrib={w + "val": "11"})
            etree.SubElement(pPr, w + "pStyle", attrib={w + "val": "ListParagraph"})
            pPr.insert(0, numPr)
            etree.SubElement(pPr, w + "spacing",
                             attrib={w + "before": "100", w + "beforeAutospacing": "1", w + "after": "100",
                                     w + "afterAutospacing": "1", w + "line": "240", w + "lineRule": "auto"})
            bullet.insert(0, pPr)

            # Add run
            newRun = etree.Element(w + "r", attrib={w + "rsidRPr": "002853AF"})

            # Run formatting
            rPr = etree.Element(w + "rPr")
            etree.SubElement(rPr, w + "rFonts",
                             attrib={w + "ascii": "Times New Roman", w + "eastAsia": "Times New Roman",
                                     w + "hAnsi": "Times New Roman", w + "cs": "Times New Roman"})
            etree.SubElement(rPr, w + "sz", attrib={w + "val": "24"})
            etree.SubElement(rPr, w + "szCs", attrib={w + "val": "24"})
            newRun.insert(0, rPr)

            # Run text
            newText = etree.Element(w + "t")
            newText.text = bulletText
            newRun.insert(1, newText)
            bullet.insert(1, newRun)
            txbx.insert(-1, bullet)
