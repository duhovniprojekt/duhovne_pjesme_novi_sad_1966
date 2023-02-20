from dataclasses import dataclass
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser

from msmodel.muse_score import *

@dataclass
class TypeHeader:
    title: str
    subtitle: str
    composer: str
    lyricist: str


@dataclass
class TypeKeySignature():
    number: int
    key: Optional[str] = None

    parser = {
        -7 : 'ces',
        -6 : 'ges',
        -5 : 'des',
        -4 : 'as',
        -3 : 'es',
        -2 : 'b',
        -1 : 'f',
        0 : 'c',
        1 : 'g',
        2 : 'd',
        3 : 'a',
        4 : 'e',
        5 : 'h',
        6 : 'fis',
        7 : 'cis',
    }

    def __init__(self, number):
        self.number = number
        self.key = self.parser[self.number]


@dataclass
class TypeTimeSignature():
    n: int
    d: int

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
                self.rest = 'r%s*%s' % (n, d)
            else:
                self.rest = 'r1'
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

    def __init__(self, lastPitch, pitch, lastTpc, tpc, duration, dots):
        self.line = ""
        self.line += self.parserTpc[tpc]
        self.pitch = pitch
        pitchDiff = int(pitch) - int(lastPitch)
        tpcDiff = int(tpc) - int(lastTpc)
        print("%%%% pitchDiff %s, lastPitch %s, pitch %s, tpcDiff %s" % (pitchDiff, lastPitch, pitch, tpcDiff))
        #TODO: clean up this mess
        if (pitchDiff >= 6 and pitchDiff < 18):
            if (pitchDiff == 6 and tpcDiff == 6):
                print("%% pitchDiff > but exception")
                self.line += ""
            else:
                print("%% pitchDiff >")
                self.line += "'"
        elif (pitchDiff >= 18 and pitchDiff < 30):
            if (pitchDiff == 18 and tpcDiff == 6):
                print("%% pitchDiff >> but exception")
                self.line += "'"
            else:
                print("%% pitchDiff >>")
                self.line += "''"
        elif (pitchDiff >= 30):
            if (pitchDiff == 30 and tpcDiff == 6):
                print("%% pitchDiff >>> but exception")
                self.line += "''"
            else:
                print("%% pitchDiff >>>")
                self.line += "'''"
        elif (pitchDiff <= -6 and pitchDiff > -18):
            if (pitchDiff == -6 and tpcDiff == -6):
                print("%% pitchDiff < but exception")
                self.line += ""
            else:
                print("%% pitchDiff <")
                self.line += ","
        elif (pitchDiff <= -18 and pitchDiff > -30):
            if (pitchDiff == -18 and tpcDiff == -6):
                print("%% pitchDiff << but exception")
                self.line += ","
            else:
                print("%% pitchDiff <<")
                self.line += ",,"
        elif (pitchDiff <= -30):
            if (pitchDiff == -30 and tpcDiff == -6):
                print("%% pitchDiff <<< but exception")
                self.line += ",,"
            else:
                print("%% pitchDiff <<<")
                self.line += ",,,"
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


class TypeLyrics():
    def __init__(self, no, text, syllabic):
        self.no = no
        self.text = text
        self.syllabic = syllabic

    def getNo(self):
        return self.no

    def getText(self):
        return self.text

    def hasSyllabic(self):
        return self.syllabic in ["begin", "middle"]

    def getSyllabic(self):
        return "--"


class TypeClef():
    types = {
        "G8vb" : "tenorG",
        "F" : "bass",
        '' : "treble"
    }
    def __init__(self, type): 
        self.type = type

    def getType(self):
        return "\\clef %s" % self.types[self.type]


def get_musescore(filename):
    parser = XmlParser(context=XmlContext())
    return parser.parse(filename, MuseScore)


def get_first_element(element):
    if isinstance(element, list):
        return element[0]
    else:
        return element


def get_header(musescore: MuseScore) -> TypeHeader:
    title = ""
    subtitle = ""
    composer = ""
    lyricist = ""
    for t in get_first_element(musescore.score.staff).vbox.text:
        match t.style:
            case "Title":
                title = t.text
            case "Subtitle":
                subtitle = t.text
            case "Composer":
                composer = t.text
            case "Lyricist":
                lyricist = t.text
    return TypeHeader(title=title, subtitle=subtitle, composer=composer, lyricist=lyricist)


def get_measure_count(musescore: MuseScore) -> int:
    s = get_first_element(musescore.score.staff)
    return len(s.measure)


def get_measure(musescore: MuseScore, index: int, staff: int = 0) -> Optional[Measure]:
    try:
        if staff == 0:
            s = get_first_element(musescore.score.staff)
            if index == 0:
                return get_first_element(s.measure)
            else:
                return s.measure[index]
        else:
            s = musescore.score.staff
            if index == 0:
                return get_first_element(s[staff].measure)
            else:
                return s[staff].measure[index]
    except Exception as e:
        print(e)
        return None


def get_time_signature(measure: Measure) -> Optional[str]:
    for t in measure.voice.content:
        if isinstance(t, TimeSig):
            return TypeTimeSignature(t.sig_n, t.sig_d)
    else:
        return None


def get_key_signature(measure: Measure, is_first_measure=False) -> Optional[str]:
    for k in measure.voice.content:
        if isinstance(k, KeySig):
            return TypeKeySignature(k.accidental)
    if is_first_measure:
        return TypeKeySignature(0)
    return None


def parse_measure(measure: Measure) -> Optional[str]:
    content = []
    for e in measure.voice.content:
        if isinstance(e, Rest):
            content.append(TypeRest(e.duration_type, None, ""))
    return content


if __name__ == "__main__":
    musescore = get_musescore("msmodel_examples/test_note_duration.mscx")
    for i in range(get_measure_count(musescore)):
        print(parse_measure(get_measure(musescore, i)))
