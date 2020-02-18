#!/usr/bin/env python

from xml.dom import minidom
import sys


class XmlParser():
    indent = ['']

    def __init__(self, node):
        print("%% init")
        self.parseNode(node)

    def enterNode(self, node):
        self.indent.append(self.getName(node))
        attributes = "" if len(self.getAttributes(
            node)) == 0 else ' attr="' + str(self.getAttributes(node)) + '"'
        text = ' text="' + self.getText(node) + \
            '"' if len(self.getText(node)) else ""
        print("%% ->", self.getPath() + text + attributes)

    def onNodeExit(self):
        pass

    def exitNode(self, node):
        print("%% <-", self.getPath())
        self.onNodeExit()
        self.indent.pop()

    def getPath(self, customIndent=None):
        if (customIndent == None):
            customIndent = self.indent
        return('/'.join(customIndent))

    def getName(self, node):
        return node.tagName

    def getText(self, node):
        rc = []
        for node in node.childNodes:
            if node.nodeType == node.TEXT_NODE:
                rc.append(node.data)
        return ''.join(rc).strip()

    def getAttributes(self, node):
        attrs = []
        for attr in node.attributes.items():
            attrs.append(attr)
        return attrs

    def getParentNodeByPath(self, currentNode, path):
        indentPath = list(self.indent)
        nodeParent = currentNode
        while (len(indentPath)):
            indentPath.pop()
            nodeParent = nodeParent.parentNode
            if (self.getPath(indentPath) == path):
                break
        return nodeParent

    def parseElement(self, node):
        return False

    def parseNode(self, node):
        if node.nodeType == node.ELEMENT_NODE:
            self.enterNode(node)
            if (not self.parseElement(node)):
                for subnode in node.childNodes:
                    self.parseNode(subnode)
            self.exitNode(node)

    def isTextInChildren(self, node, text):
        childrenText = []
        # TODO: recursive?
        for subnode in node.childNodes:
            childrenText.append(self.getText(subnode))
        return text in childrenText

    def getTextFromChild(self, node, childName):
        for subnode in node.childNodes:
            if subnode.nodeType == subnode.ELEMENT_NODE:
                if ('/' in childName):
                    if (self.getName(subnode) == childName.split('/')[0]):
                        return self.getTextFromChild(subnode, "/".join(childName.split('/')[1:]))
                else:
                    if (self.getName(subnode) == childName):
                        return self.getText(subnode)
        return ""

    def hasChild(self, node, childName):
        for subnode in node.childNodes:
            if subnode.nodeType == subnode.ELEMENT_NODE:
                if (self.getName(subnode) == childName):
                    return True
        return False


class MuseScoreParser(XmlParser):
    xml_paths = {
        "measure" : "/museScore/Score/Staff/Measure",
        "chord": "/museScore/Score/Staff/Measure/voice/Chord",
        "rest": "/museScore/Score/Staff/Measure/voice/Rest",
        "staff": "/museScore/Score/Staff",
        "header": "/museScore/Score/Staff/VBox/Text",
        "keySignature": "/museScore/Score/Staff/Measure/voice/KeySig",
        "timeSignature": "/museScore/Score/Staff/Measure/voice/TimeSig",
        "rehearsalMark": "/museScore/Score/Staff/Measure/voice/RehearsalMark",
        "barLine": "/museScore/Score/Staff/Measure/voice/BarLine",
        "startRepeat": "/museScore/Score/Staff/Measure/startRepeat",
        "endRepeat": "/museScore/Score/Staff/Measure/endRepeat",
        "measureSpanner" : "/museScore/Score/Staff/Measure/voice/Spanner",
        "chordSpanner" : "/museScore/Score/Staff/Measure/voice/Chord/Spanner",
        "noteSpanner" : "/museScore/Score/Staff/Measure/voice/Chord/Note/Spanner",
        "layoutBreak" : "/museScore/Score/Staff/Measure/LayoutBreak"
    }
    measure = 0

    def getStaffId(self, node):
        staff = self.getParentNodeByPath(node, self.xml_paths['staff'])
        for attr in self.getAttributes(staff):
            if (attr[0] == 'id'):
                return attr[1]
        return None

    def onMeasure(self):
        self.measure += 1
        print("%% measure:", self.measure)
    
    def onHeaderTitle(self, title):
        print("%% title:", title)
    
    def onHeaderComposer(self, composer):
        print("%% composer:", composer)

    def onNote(self, pitch, tpc, duration, dots):
        print("%% chord:", pitch, tpc, duration, dots)

    def onKeySignature(self, keySignature):
        print("%% keySignature:", keySignature)

    def onTimeSignature(self, n, d):
        print("%% timeSignature:", n + "/" + d)

    def onRehearsalMark(self, rehearsalMark):
        print("%% rehearsalMark:", rehearsalMark)

    def onRest(self, rest, dots):
        print("%% rest:", rest, dots)

    def onStartRepeat(self):
        print("%% startRepeat")

    def onEndRepeat(self):
        print("%% endRepeat")

    def onVoltaStart(self, volta_text, volta_end_type):
        print("%% voltaStart:", volta_text, volta_end_type)

    def onVoltaEnd(self):
        print("%% voltaEnd")

    def onTieStart(self):
        print("%% tieStart")

    def onTieEnd(self):
        print("%% tieEnd")

    def onSlurStart(self):
        print("%% slurStart")

    def onSlurEnd(self):
        print("%% slurEnd")

    def onStaffEnter(self, id):
        print("%% staff:", id)

    def onLayoutBreak(self, text):
        print("%% layout:", text)

    def onBarLine(self, text):
        print("%% barLine:", text)

    def parseElement(self, node):
        # if you got all data from node and don't want to make a recursion on that node return True
        if (self.getPath() == self.xml_paths['measure']):
            self.onMeasure()
            return False

        if (self.getPath() == self.xml_paths['header']):
            if (self.getTextFromChild(node, "style") == "Title"):
                title = self.getTextFromChild(node, "text")
                self.onHeaderTitle(title)
                return False
            elif (self.getTextFromChild(node, "style") == "Composer"):
                composer = self.getTextFromChild(node, "text")
                self.onHeaderComposer(composer)
                return False
        
        if (self.getPath() == self.xml_paths['chord']):
            duration = self.getTextFromChild(node, "durationType")
            pitch = self.getTextFromChild(node, "Note/pitch")
            tpc = self.getTextFromChild(node, "Note/tpc")
            dots = self.getTextFromChild(node, "dots")
            self.onNote(pitch, tpc, duration, dots)
            return False

        if (self.getPath() == self.xml_paths['keySignature']):
            keySignature = self.getTextFromChild(node, "accidental")
            self.onKeySignature(keySignature)
            return False

        if (self.getPath() == self.xml_paths['timeSignature']):
            n = self.getTextFromChild(node, "sigN")
            d = self.getTextFromChild(node, "sigD")
            self.onTimeSignature(n, d)
            return False
        
        if (self.getPath() == self.xml_paths['rehearsalMark']):
            rehearsalMark = self.getTextFromChild(node, "text")
            self.onRehearsalMark(rehearsalMark)
            return False

        if (self.getPath() == self.xml_paths['rest']):
            rest = self.getTextFromChild(node, "durationType")
            dots = self.getTextFromChild(node, "dots")
            self.onRest(rest, dots)
            return False
        
        if (self.getPath() == self.xml_paths['barLine']):
            text = self.getTextFromChild(node, "subtype")
            self.onBarLine(text)
            return False
        
        if (self.getPath() == self.xml_paths['startRepeat']):
            self.onStartRepeat()
            return False

        if (self.getPath() == self.xml_paths['endRepeat']):
            self.onEndRepeat()
            return False

        if (self.getPath() == self.xml_paths['measureSpanner']):
            attr = self.getAttributes(node)
            for a in attr:
                attrType, attrText = a
                if attrType == "type" and attrText == "Volta":
                    if self.hasChild(node, "next"):
                        volta_text = self.getTextFromChild(node, "Volta/beginText")
                        volta_end_type = self.getTextFromChild(node, "Volta/endHookType")
                        self.onVoltaStart(volta_text, volta_end_type)
                    elif self.hasChild(node, "prev"):
                        self.onVoltaEnd()
            return False

        if (self.getPath() == self.xml_paths['chordSpanner']):
            attr = self.getAttributes(node)
            for a in attr:
                attrType, attrText = a
                if attrType == "type" and attrText == "Slur":
                    if self.hasChild(node, "next"):
                        self.onSlurStart()
                    elif self.hasChild(node, "prev"):
                        self.onSlurEnd()
            return False

        if (self.getPath() == self.xml_paths['noteSpanner']):
            attr = self.getAttributes(node)
            for a in attr:
                attrType, attrText = a
                if attrType == "type" and attrText == "Tie":
                    if self.hasChild(node, "next"):
                        self.onTieStart()
                    elif self.hasChild(node, "prev"):
                        self.onTieEnd()
            return False
        
        if (self.getPath() == self.xml_paths['staff']):
            for attr in self.getAttributes(node):
                if (attr[0] == 'id'):
                    id = attr[1]
                    self.onStaffEnter(id)
            return False

        if (self.getPath() == self.xml_paths['layoutBreak']):
            text = self.getTextFromChild(node, "subtype")
            self.onLayoutBreak(text)
            return False

        return False

    def onMeasureExit(self):
        pass

    def onNodeExit(self):
        if (self.getPath() == self.xml_paths['measure']):
            self.onMeasureExit()

class TypeKeySignature():
    parser = {
        '-7' : 'ces',
        '-6' : 'ges',
        '-5' : 'des',
        '-4' : 'as',
        '-3' : 'es',
        '-2' : 'b',
        '-1' : 'f',
        '0' : 'c',
        '1' : 'g',
        '2' : 'd',
        '3' : 'a',
        '4' : 'e',
        '5' : 'h',
        '6' : 'fis',
        '7' : 'cis',
    }

    def __init__(self, number):
        self.key = self.parser[number]

    def getKey(self):
        return self.key

class TypeTimeSignature():
    def __init__(self, n, d):
        self.n = n
        self.d = d

    def getTime(self):
        return (self.n, self.d)

class TypeDuration():
    parserDuration = {
        'whole' : '1',
        'half' : '2',
        'quarter' : '4',
        'eighth' : '8',
        '16th' : '16',
        '32nd' : '32'
    }

class TypeRest(TypeDuration):
    def __init__(self, duration, lastTypeTimeSignature, dots):
        if (duration == "measure"):
            if (lastTypeTimeSignature):
                d, n = lastTypeTimeSignature.getTime()
                self.rest = 'R%s*%s' % (n, d)
            else:
                self.rest = 'R1'
        else:
            if (dots):
                dots = int(dots) * "."
            self.rest = 'r' + self.parserDuration[duration] + dots


    def getRest(self):
        return self.rest

class TypeNote(TypeDuration):
    parserTpc = {
        '-1' : 'feses',
        '0' : 'ceses',
        '1' : 'geses',
        '2' : 'deses',
        '3' : 'ases',
        '4' : 'eses',
        '5' : 'bes',
        '6' : 'fes',
        '7' : 'ces',
        '8' : 'ges',
        '9' : 'des',
        '10' : 'as',
        '11' : 'es',
        '12' : 'b',
        '13' : 'f',
        '14' : 'c',
        '15' : 'g',
        '16' : 'd',
        '17' : 'a',
        '18' : 'e',
        '19' : 'h',
        '20' : 'fis',
        '21' : 'cis',
        '22' : 'gis',
        '23' : 'dis',
        '24' : 'ais',
        '25' : 'eis',
        '26' : 'his',
        '27' : 'fisis',
        '28' : 'cisis',
        '29' : 'gisis',
        '30' : 'disis',
        '31' : 'aisis',
        '32' : 'eisis',
        '33' : 'hisis'
    }

    def __init__(self, lastPitch, pitch, tpc, duration, dots):
        self.line = ""
        self.line += self.parserTpc[tpc]
        self.pitch = pitch
        if (int(lastPitch) - int(pitch) > 6): #TODO: which number for octave
            self.line += ","
        elif (int(lastPitch) - int(pitch) < -6): #TODO: -5???
            self.line += "'"
        self.line += self.parserDuration[duration]
        if (dots):
            self.line += int(dots) * "."
    
    def getNote(self):
        return self.line

    def getPitch(self):
        return self.pitch

class TypeBarLine():
    parser = {
        "startRepeat" : ".|:",
        "endRepeat" : ":|.",
        "double" : "||",
        "end" : "|."
    }

    def __init__(self, line):
        self.line = self.parser[line]

    def getLine(self):
        return self.line

class TypeBarValidator():
    def __init__(self):
        pass

class TypeTie():
    def __init__(self):
        pass

    def getTie(self):
        return "~"

class TypeSlur():
    def __init__(self, type):
        self.type = type

    def getSlur(self):
        if self.type == "start":
            return "("
        else:
            return ")"

class TypeRehearsalMark():
    def __init__(self, text):
        self.text = text    

    def getMark(self):
        return "\\mark \\markup { \\box \\bold %s }" % self.text

class TypeVolta():
    def __init__(self, type, voltaText, voltaEndType):
        self.type = type
        self.voltaText = voltaText
        self.voltaEndType = voltaEndType

    def getEnd(self):
        return self.voltaEndType

    def getVolta(self):
        if (self.type == "start"):
            return "\\set Score.repeatCommands = #\'((volta \"%s\"))" % self.voltaText
        elif (self.type == "end"):
            return "\\set Score.repeatCommands = #\'((volta #f))"

class TypeLayoutBreak():
    def __init__(self, text): 
        self.text = text

    def getBreak(self):
        return "\\break"

class LilypondGenerator(MuseScoreParser):

    staff = {}
    lastPitch = 60
    lastTypeTimeSignature = None
    lastTypeVolta = None
    addOnMeasureExit = []

    def onMeasure(self):
        self.measure += 1
        print("%% onMeasureEnter:", self.measure)
    
    def onHeaderTitle(self, title):
        print("%% title:", title)
        self.title = title
    
    def onHeaderComposer(self, composer):
        print("%% composer:", composer)
        self.composer = composer

    def onNote(self, pitch, tpc, duration, dots):
        print("%% chord:", pitch, tpc, duration, dots)
        typeNote = TypeNote(self.lastPitch, pitch, tpc, duration, dots)
        self.lastPitch = typeNote.getPitch()
        self.staff[self.currentStaffId].append(typeNote)

    def onKeySignature(self, keySignature):
        print("%% keySignature:", keySignature)
        self.staff[self.currentStaffId].append(TypeKeySignature(keySignature))

    def onTimeSignature(self, n, d):
        print("%% timeSignature:", n + "/" + d)
        typeTimeSignature = TypeTimeSignature(n, d)
        self.staff[self.currentStaffId].append(typeTimeSignature)
        self.lastTypeTimeSignature = typeTimeSignature

    def onRehearsalMark(self, rehearsalMark):
        print("%% rehearsalMark:", rehearsalMark)
        self.staff[self.currentStaffId].append(TypeRehearsalMark(rehearsalMark))

    def onRest(self, rest, dots):
        print("%% rest:", rest)
        self.staff[self.currentStaffId].append(TypeRest(rest, self.lastTypeTimeSignature, dots))
        self.lastTypeTimeSignature = None

    def onBarLine(self, text):
        print("%% barLine:", text)
        self.staff[self.currentStaffId].append(TypeBarLine(text))

    def onStartRepeat(self):
        print("%% startRepeat")
        self.staff[self.currentStaffId].append(TypeBarLine('startRepeat'))

    def onEndRepeat(self):
        print("%% endRepeat")
        self.addOnMeasureExit.append(TypeBarLine('endRepeat'))
        # self.staff[self.currentStaffId].append(TypeBarLine('endRepeat'))

    def onVoltaStart(self, volta_text, volta_end_type):
        print("%% voltaStart:", volta_text, volta_end_type)
        typeVolta = TypeVolta('start', volta_text, volta_end_type)
        # self.addOnMeasureExit.append(typeVolta)
        self.staff[self.currentStaffId].append(typeVolta)
        self.lastTypeVolta = typeVolta

    def onVoltaEnd(self):
        print("%% voltaEnd")
        # self.addOnMeasureExit.append(TypeVolta('end', "", self.lastTypeVolta.getEnd()))
        self.staff[self.currentStaffId].append(TypeVolta('end', "", self.lastTypeVolta.getEnd()))
        self.lastTypeVolta = None

    def onTieStart(self):
        print("%% tieStart")
        self.staff[self.currentStaffId].append(TypeTie())

    def onTieEnd(self):
        print("%% tieEnd")

    def onSlurStart(self):
        print("%% slurStart")
        self.staff[self.currentStaffId].append(TypeSlur('start'))

    def onSlurEnd(self):
        print("%% slurEnd")
        self.staff[self.currentStaffId].append(TypeSlur('end'))

    def onStaffEnter(self, id):
        print("%% staff:", id)
        self.staff[id] = []
        self.currentStaffId = id

    def onMeasureExit(self):
        print("%% onMeasureExit")
        while (len(self.addOnMeasureExit)):
            self.staff[self.currentStaffId].append(self.addOnMeasureExit.pop())
        self.staff[self.currentStaffId].append(TypeBarValidator())

    def onLayoutBreak(self, text):
        print("%% layout:", text)
        self.addOnMeasureExit.append(TypeLayoutBreak(text))

    def getHead(self):
        string = []
        string.append("\\version \"2.19.84\"")
        string.append("\\include \"deutsch.ly\"")
        string.append("")
        string.append("\layout {")
        string.append("  indent = 0")
        string.append("}")
        return string

    def getHeader(self):
        string = []
        string.append("\header {")
        if (hasattr(self, 'title')):
            string.append("  title = \"%s\"" % self.title)
        if (hasattr(self, 'composer')):
            string.append("  composer = \"%s\"" % self.composer)
        string.append("}")
        return string        

    def getStaffStart(self, id):
        string = []
        string.append("staffOne = \\relative c' {") #TODO: % str(id))
        return string

    def getStaffEnd(self):
        string = []
        string.append("  \\bar \"|.\"") #TODO: what if there is no end?
        string.append("}")
        return string              

    def getStaffData(self, id):
        string = []
        line = "  "
        for element in self.staff[id]:
            if isinstance(element, TypeKeySignature):
                string.append("  \\key %s \\major" % element.getKey())
            elif isinstance(element, TypeTimeSignature):
                string.append("  \\time %s/%s" % element.getTime())
            elif isinstance(element, TypeNote):
                line += element.getNote()
                line += " "
            elif isinstance(element, TypeRest):
                line += element.getRest()
                line += " "
            elif isinstance(element, TypeTie):
                line += element.getTie()
                line += " "
            elif isinstance(element, TypeSlur):
                line += element.getSlur()
                line += " "
            elif isinstance(element, TypeBarLine):
                line += "\\bar \"%s\"" % element.getLine()
                line += " "
            elif isinstance(element, TypeLayoutBreak):
                line += element.getBreak()
                line += " "
            elif isinstance(element, TypeRehearsalMark):
                line += '\n'
                line += '  '
                line += element.getMark()
                line += '\n'
                line += "  "
            elif isinstance(element, TypeVolta):
                line += '\n'
                line += '  '
                line += element.getVolta()
                line += '\n'
                line += "  "
            elif isinstance(element, TypeBarValidator):
                line += "|"
                string.append(line)
                line = "  "
        return string        

    def getScore(self):
        string = []
        string.append("\score {")
        string.append("  <<")
        string.append("  \\new Staff {")
        string.append("    \\staffOne")
        string.append("  }")
        string.append("  \\new TabStaff {")
        string.append("    \\set Staff.stringTunings = \\stringTuning <e a d\' g\'>")
        string.append("    \\staffOne")
        string.append("  }")
        string.append(">>")
        string.append("}")
        return(string)

    def getFile(self):
        string = []
        string += self.getHead()
        string.append("")
        string += self.getHeader()
        string.append("")
        string += self.getStaffStart('1')
        string += self.getStaffData('1')
        string += self.getStaffEnd()
        string.append("")
        string += self.getScore()
        return(string)

if __name__ == "__main__":
    doc = minidom.parse(sys.stdin)
    rootNode = doc.childNodes[0]
    ly = LilypondGenerator(rootNode)
    file = ly.getFile()
    print("%% #####")
    print("\n".join(file))