#!/usr/bin/env python

import sys
from xml.sax import ContentHandler
from xml.sax import make_parser
import pprint

ly_data = {
    "title": "",
    "measure_count": 0,
    "staff_1": []
}

##### get title #####
in_title_style = [
    {"name": "museScore"},
    {"name": "Score"},
    {"name": "Staff"},
    {"name": "VBox"},
    {"name": "Text"},
    {"name": "style"}
]

in_title_text = [
    {"name": "museScore"},
    {"name": "Score"},
    {"name": "Staff"},
    {"name": "VBox"},
    {"name": "Text"},
    {"name": "text"}
]

##### staff id #####

in_staff = [
    {"name": "museScore"},
    {"name": "Score"},
    {"name": "Staff"},
]


##### count measure #####

in_measure = [
    {"name": "museScore"},
    {"name": "Score"},
    {"name": "Staff"},
    {"name": "Measure"}
]

##### key signature #####

in_key_signature = [
    {"name": "museScore"},
    {"name": "Score"},
    {"name": "Staff"},
    {"name": "Measure"},
    {"name": "voice"},
    {"name": "KeySig"},
    {"name": "accidental"}
]

##### time signature ######

in_time_signature = [
    {"name": "museScore"},
    {"name": "Score"},
    {"name": "Staff"},
    {"name": "Measure"},
    {"name": "voice"},
    {"name": "TimeSig"}
]

##### chord #####

in_chord = [
    {"name": "museScore"},
    {"name": "Score"},
    {"name": "Staff"},
    {"name": "Measure"},
    {"name": "voice"},
    {"name": "Chord"}
]

in_chord_duration = [
    {"name": "museScore"},
    {"name": "Score"},
    {"name": "Staff"},
    {"name": "Measure"},
    {"name": "voice"},
    {"name": "Chord"},
    {"name": "durationType"}
]

in_chord_dots = [
    {"name": "museScore"},
    {"name": "Score"},
    {"name": "Staff"},
    {"name": "Measure"},
    {"name": "voice"},
    {"name": "Chord"},
    {"name": "dots"}
]


in_chord_note_pitch = [
    {"name": "museScore"},
    {"name": "Score"},
    {"name": "Staff"},
    {"name": "Measure"},
    {"name": "voice"},
    {"name": "Chord"},
    {"name": "Note"},
    {"name": "pitch"}
]

in_chord_note_tpc = [
    {"name": "museScore"},
    {"name": "Score"},
    {"name": "Staff"},
    {"name": "Measure"},
    {"name": "voice"},
    {"name": "Chord"},
    {"name": "Note"},
    {"name": "tpc"}
]

in_chord_slur_start = [
    {"name": "museScore"},
    {"name": "Score"},
    {"name": "Staff"},
    {"name": "Measure"},
    {"name": "voice"},
    {"name": "Chord"},
    {"name": "Spanner"},
    {"name": "next"}
]

in_chord_slur_end = [
    {"name": "museScore"},
    {"name": "Score"},
    {"name": "Staff"},
    {"name": "Measure"},
    {"name": "voice"},
    {"name": "Chord"},
    {"name": "Spanner"},
    {"name": "prev"}
]

in_barline = [
    {"name": "museScore"},
    {"name": "Score"},
    {"name": "Staff"},
    {"name": "Measure"},
    {"name": "voice"},
    {"name": "BarLine"},
    {"name": "subtype"}
]

##### helper functions #####


def is_tree_path_eq(list1, list2):
    if (len(list1) != len(list2)):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True


def is_tree_path_lt(list1, list2):
    if (len(list1) >= len(list2)):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True


class LyConversionHandler(ContentHandler):

    global ly_data
    indent = []
    in_title = False
    in_chord = False
    staff_id = ""

    def __init__(self):
        pass

    def tab(self, extra=0):
        return (len(self.indent) * 2 + extra * 2) * " "

    def get_title(self, ch):
        if is_tree_path_eq(in_title_style, self.indent):
            self.in_title = True
        elif is_tree_path_eq(in_title_text, self.indent):
            ly_data["title"] = ch.strip()
            self.in_title = False

    def get_staff_id(self, attrs):
        if is_tree_path_eq(in_staff, self.indent):
            self.staff_id = attrs.get('id', "")

    def get_measure_count(self):
        if (self.staff_id == "1"):
            if is_tree_path_eq(in_measure, self.indent):
                ly_data['measure_count'] += 1

    def get_key_signature(self, ch):
        if (self.staff_id == "1"):
            if is_tree_path_eq(in_key_signature, self.indent):
                ly_data['staff_1'].append({'key_signature': ch.strip()})

    def add_time_signature_field(self):
        if (self.staff_id == "1"):
            if is_tree_path_eq(in_time_signature, self.indent):
                ly_data['staff_1'].append({"time_signature": []})

    def get_time_signature(self, ch):
        if (self.staff_id == "1"):
            if is_tree_path_lt(in_time_signature, self.indent):
                ly_data['staff_1'][-1]["time_signature"].append(ch.strip())

    def add_chord_start(self):
        if (self.staff_id == "1"):
            if is_tree_path_eq(in_chord, self.indent):
                ly_data['staff_1'].append({"chord": []})
            elif is_tree_path_eq(in_chord_slur_start, self.indent):
                ly_data['staff_1'][-1]['chord'].append("slur_start")
            elif is_tree_path_eq(in_chord_slur_end, self.indent):
                ly_data['staff_1'][-1]['chord'].append("slur_end")

    def get_chord(self, ch):
        if (self.staff_id == "1"):
            if is_tree_path_eq(in_chord_duration, self.indent):
                ly_data['staff_1'][-1]['chord'].append(
                    {'duration': ch.strip()})
            elif is_tree_path_eq(in_chord_note_pitch, self.indent):
                ly_data['staff_1'][-1]['chord'].append({'pitch': ch.strip()})
            elif is_tree_path_eq(in_chord_note_tpc, self.indent):
                ly_data['staff_1'][-1]['chord'].append({'tpc': ch.strip()})
            elif is_tree_path_eq(in_chord_dots, self.indent):
                ly_data['staff_1'][-1]['chord'].append({'dots': ch.strip()})

    def get_barline(self, ch):
        if (self.staff_id == "1"):
            if is_tree_path_eq(in_barline, self.indent):
                ly_data['staff_1'].append({"barline" : ch.strip()})

    def add_barline_validation(self):
        if (self.staff_id == "1"):
            if is_tree_path_eq(in_measure, self.indent):
                ly_data['staff_1'].append("bar_line_validation")

    def startElement(self, name, attrs):
        self.indent.append({"name": name})
        self.get_staff_id(attrs)
        self.get_measure_count()
        self.add_time_signature_field()
        self.add_chord_start()

    def characters(self, ch):
        self.get_title(ch)
        self.get_key_signature(ch)
        self.get_time_signature(ch)
        self.get_chord(ch)
        self.get_barline(ch)

    def endElement(self, name):
        # print(self.tab(), "endElement[%s]" % name)
        self.add_barline_validation()
        self.indent.pop()


def get_head():
    string = []
    string.append("\\version \"2.19.83\"")
    string.append("\\include \"deutsch.ly\"")
    return string

def get_header(data):
    string = []
    string.append("\header {")
    string.append("  title = \"%s\"" % data['title'])
    string.append("}")
    return string


def get_score_start():
    string = []
    string.append("\score {")
    string.append("  \\new Staff \\relative c' {")
    string.append("  \clef treble")
    return string


def get_score_end():
    string = []
    # string.append("  \\bar \"|.\"") #TODO: what if there is no end?
    string.append("  }")
    string.append("}")
    return string


tpc_2_pitch = {
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

duration_2_num = {
    'whole' : '1',
    'half' : '2',
    'quarter' : '4',
    'eighth' : '8'
}

key_signature_2_key = {
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

barline_2_bar = {
    "double" : "||",
    "end" : "|."
}

last_pitch = 60

def get_note(data):
    global last_pitch
    line = ""
    for e in data:
        if ("tpc" in e):
            line += tpc_2_pitch[e['tpc']]
    for e in data:
        if ("pitch" in e):
            pitch = int(e['pitch'])
    if (last_pitch - pitch > 6): #TODO: which number for octave
        line += ","
    elif (last_pitch - pitch < -6):
        line += "'"
    last_pitch = pitch
    for e in data:
        if ("duration" in e):
            line += duration_2_num[e['duration']]
    for e in data:
        if ("dots" in e):
            line += int(e['dots']) * "."

    for e in data:
        if ("slur_end" in e):
            line += " )"
    
    for e in data:
        if ("slur_start" in e):
            line += " ("

    return line

def parse_data(data):
    string = []
    line = "  "
    for element in data['staff_1']:
        if ("key_signature" in element):
            string.append("  \\key " + key_signature_2_key[element['key_signature']] + " \\major")
        elif ("time_signature" in element):
            string.append("  \\time " + element['time_signature'][0] + "/" + element['time_signature'][1])
        elif ("chord" in element):
            line += get_note(element['chord'])
            line += " "
        elif ("barline" in element):
            line += "\\bar \"" + barline_2_bar[element['barline']] + "\""
            line += " "
        elif ("bar_line_validation" in element):
            line += "|"
            string.append(line)
            line = "  "
    return string


def generate_ly_output(data):
    string = []
    string += get_head()
    string.append("")
    string += get_header(data)
    string.append("")
    string += get_score_start()
    string += parse_data(data)
    string += get_score_end()
    return(string)


if __name__ == "__main__":
    dh = LyConversionHandler()
    parser = make_parser()
    parser.setContentHandler(dh)
    parser.parse(sys.stdin)
    # pp = pprint.PrettyPrinter(indent=2)
    # pp.pprint(ly_data)
    print("\n".join(generate_ly_output(ly_data)))
