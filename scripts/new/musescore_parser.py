#!/usr/bin/env python

import sys
from xml_parser import XmlParser
from dataclasses import dataclass, field
from pprint import pprint


@dataclass
class Base:
    def __post_init__(self):
        print("%%", self)

@dataclass
class Staff(Base):
    id: int
    children: list = field(default_factory=lambda: [])

@dataclass
class Measure(Base):
    children: list = field(default_factory=lambda: [])

@dataclass
class VBox(Base):
    style: str
    text: str

@dataclass
class TimeSig(Base):
    sig_n: str
    sig_d: str

@dataclass
class Harmony(Base):
    root: str
    root_case: str
    name: str
    base: str

@dataclass
class Rest(Base):
    duration_type: str
    duration: str
    dots: str

@dataclass
class Location(Base):
    fractions: str

@dataclass
class Chord(Base):
    duration_type: str
    note_pitch: str
    note_tpc: str
    dots: str

@dataclass
class KeySig(Base):
    duration_type: str

@dataclass
class Clef(Base):
    concert_clef_type: str

@dataclass
class RehearsalMark(Base):
    text: str

@dataclass
class BarLine(Base):
    subtype: str

@dataclass
class LayoutBreak(Base):
    subtype: str

@dataclass
class Lyrics(Base):
    text: str
    syllabic: str
    ticks: str
    ticks_f: str
    no: str

class MuseScoreParser(XmlParser):
    staffs = []

    def add_to_staff(self, e):
        self.staffs[-1].children.append(e)

    def add_to_measure(self, e):
        self.staffs[-1].children[-1].children.append(e)

    def parse_element(self, node):
        # if you got all data from node and don't want to make a recursion on that node return True

        if self.get_path() == "/museScore/Score/Staff":
            for attr in self.get_attributes(node):
                if (attr[0] == 'id'):
                    id = attr[1]
                    self.staffs.append(Staff(id))
            return False

        if self.get_path() == "/museScore/Score/Staff/Measure":
            self.add_to_staff(Measure())
            return False

        if self.get_path() == "/museScore/Score/Staff/VBox/Text":
            style = self.get_text_from_child(node, "style")
            text = self.get_text_from_child(node, "text")
            self.add_to_staff(VBox(style, text))
            return False

        if self.get_path() == "/museScore/Score/Staff/Measure/voice/TimeSig":
            sig_n = self.get_text_from_child(node, "sigN")
            sig_d = self.get_text_from_child(node, "sigD")
            self.add_to_measure(TimeSig(sig_n, sig_d))
            return False
           
        if self.get_path() == "/museScore/Score/Staff/Measure/voice/Harmony":
            root = self.get_text_from_child(node, "root")
            root_case = self.get_text_from_child(node, "rootCase")
            name = self.get_text_from_child(node, "name")
            base = self.get_text_from_child(node, "base")
            self.add_to_measure(Harmony(root, root_case, name, base))
            return False

        if self.get_path() == "/museScore/Score/Staff/Measure/voice/Rest":
            duration_type = self.get_text_from_child(node, "durationType")
            duration = self.get_text_from_child(node, "duration")
            dots = self.get_text_from_child(node, "dots")
            self.add_to_measure(Rest(duration_type, duration, dots))
            return False

        if self.get_path() == "/museScore/Score/Staff/Measure/voice/location":
            fractions = self.get_text_from_child(node, "fractions")
            self.add_to_measure(Location(fractions))
            return False

        if self.get_path() == "/museScore/Score/Staff/Measure/voice/Chord":
            duration_type = self.get_text_from_child(node, "durationType")
            note_pitch = self.get_text_from_child(node, "Note/pitch")
            note_tpc = self.get_text_from_child(node, "Note/tpc")
            dots = self.get_text_from_child(node, "dots")
            self.add_to_measure(Chord(duration_type, note_pitch, note_tpc, dots))
            return False

        if self.get_path() == "/museScore/Score/Staff/Measure/voice/KeySig":
            accidental = self.get_text_from_child(node, "accidental")
            self.add_to_measure(KeySig(accidental))
            return False

        if self.get_path() == "/museScore/Score/Staff/Measure/voice/Clef":
            concert_clef_type = self.get_text_from_child(node, "concertClefType")
            self.add_to_measure(Clef(concert_clef_type))
            return False

        if self.get_path() == "/museScore/Score/Staff/Measure/voice/RehearsalMark":
            text = self.get_text_from_child(node, "text")
            self.add_to_measure(RehearsalMark(text))
            return False

        if self.get_path() == "/museScore/Score/Staff/Measure/voice/BarLine":
            subtype = self.get_text_from_child(node, "subtype")
            self.add_to_measure(BarLine(subtype))
            return False
        
        

        if self.get_path() == "/museScore/Score/Staff/Measure/LayoutBreak":
            subtype = self.get_text_from_child(node, "subtype")
            self.add_to_measure(LayoutBreak(subtype))
            return False
        
        if self.get_path() == "/museScore/Score/Staff/Measure/voice/Chord/Lyrics":
            text = self.get_text_from_child(node, "text")
            syllabic = self.get_text_from_child(node, "syllabic")
            ticks = self.get_text_from_child(node, "ticks")
            ticks_f = self.get_text_from_child(node, "ticks_f")
            no = self.get_text_from_child(node, "no")
            self.add_to_measure(Lyrics(text, syllabic, ticks, ticks_f, no))
            return False

        if self.get_path() == "/museScore/Score/Part/Staff":
            for attr in self.get_attributes(node):
                if (attr[0] == 'id'):
                    id = attr[1]
                    default_clef = self.get_text_from_child(node, "defaultClef")
            return False

        if self.get_path() == "/museScore/Score/Staff/Measure/voice/Spanner":
            attr = self.get_attributes(node)
            for a in attr:
                attr_type, attr_text = a
                if attr_type == "type" and attr_text == "Volta":
                    if self.has_child(node, "next"):
                        volta_text = self.get_text_from_child(node, "Volta/begin_text")
                        volta_end_type = self.get_text_from_child(node, "Volta/end_hook_type")
                        #self.on_volta_start(volta_text, volta_end_type)
                    elif self.has_child(node, "prev"):
                        pass
                        #self.on_volta_end()
            return False

        if self.get_path() == "/museScore/Score/Staff/Measure/voice/Chord/Spanner":
            attr = self.get_attributes(node)
            for a in attr:
                attr_type, attr_text = a
                if attr_type == "type" and attr_text == "Slur":
                    if self.has_child(node, "next"):
                        pass
                        #self.on_slur_start()
                    elif self.has_child(node, "prev"):
                        pass
                        #self.on_slur_end()
            return False

        if self.get_path() == "/museScore/Score/Staff/Measure/voice/Chord/Note/Spanner":
            attr = self.get_attributes(node)
            for a in attr:
                attr_type, attr_text = a
                if attr_type == "type" and attr_text == "Tie":
                    if self.has_child(node, "next"):
                        pass
                        #self.on_tie_start()
                    elif self.has_child(node, "prev"):
                        pass
                        #self.on_tie_end()
            return False

        return False

if __name__ == "__main__":
    m = MuseScoreParser(sys.argv[1])
    pprint(m.staffs)

