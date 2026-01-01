#!/usr/bin/env python

import sys
from xml_parser import XmlParser
from dataclasses import dataclass, field
from pprint import pprint

print_debug = False

@dataclass
class Base:
    def __post_init__(self):
        if print_debug: print("%%", self)
        pass

@dataclass
class Staff(Base):
    id: int
    children: list = field(default_factory=lambda: [])

@dataclass
class Measure(Base):
    end_repeat: str
    len: str
    children: list = field(default_factory=lambda: [])

@dataclass
class VBox(Base):
    style: str
    text: str

@dataclass
class TBox(Base):
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
    accidental: str

@dataclass
class Clef(Base):
    concert_clef_type: str
    transposing_clef_type: str

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

@dataclass
class ChordNoteSpanner(Base):
    type: str
    next_location_fractions: str
    prev_location_fractions: str
    next_location_measures: str
    prev_location_measures: str

@dataclass
class ChordSpanner(Base):
    type: str
    next_location_fractions: str
    prev_location_fractions: str
    next_location_measures: str
    prev_location_measures: str

@dataclass
class VoltaSpanner(Base):
    end_hook_type: str
    begin_text: str
    endings: str
    next_location_measures: str
    prev_location_measures: str

@dataclass
class Tempo(Base):
    tempo: str
    text: str
    text_sym: str

@dataclass
class Tuplet(Base):
    normal_notes: str
    actual_notes: str
    base_note: str
    number_style: str
    number_text: str

@dataclass
class EndTuplet(Base):
    pass

@dataclass
class StartRepeat(Base):
    pass

@dataclass
class StaffText(Base):
    text: str

class MuseScoreParser(XmlParser):
    staffs = []

    def add_to_staff(self, e):
        self.staffs[-1].children.append(e)

    def add_to_measure(self, e):
        self.staffs[-1].children[-1].children.append(e)

    def parse_element(self, node):
        # if you got all data from node and don't want to make a recursion on that node return True

        if self.get_path() == "/museScore/Score/Staff":
            attr = self.get_attributes(node)
            id = attr["id"]
            self.staffs.append(Staff(id))
            return False

        if self.get_path() == "/museScore/Score/Staff/Measure":
            attr = self.get_attributes(node)
            end_repeat = self.get_text_from_child(node, "endRepeat")
            measure_len = attr.get("len", "")
            self.add_to_staff(Measure(end_repeat, measure_len))
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
            transposing_clef_type = self.get_text_from_child(node, "transposingClefType")
            self.add_to_measure(Clef(concert_clef_type, transposing_clef_type))
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
            #attr = self.get_attributes(node)
            #id = attr["id"]
            #default_clef = self.get_text_from_child(node, "defaultClef")
            return False

        if self.get_path() == "/museScore/Score/Staff/Measure/voice/Spanner":
            attr = dict(self.get_attributes(node))
            attr_type = attr["type"]
            if attr_type == "Volta":
                end_hook_type = self.get_text_from_child(node, "Volta/endHookType")
                begin_text = self.get_text_from_child(node, "Volta/beginText")
                endings = self.get_text_from_child(node, "Volta/endings")
                next_location_measures = self.get_text_from_child(node, "next/location/measures")
                prev_location_measures = self.get_text_from_child(node, "prev/location/measures")
                self.add_to_measure(VoltaSpanner(end_hook_type, begin_text, endings, next_location_measures, prev_location_measures))
            return False

        if self.get_path() == "/museScore/Score/Staff/Measure/voice/Chord/Spanner":
            attr = dict(self.get_attributes(node))
            attr_type = attr["type"]
            next_location_fractions = self.get_text_from_child(node, "next/location/fractions")
            prev_location_fractions = self.get_text_from_child(node, "prev/location/fractions")
            next_location_measures = self.get_text_from_child(node, "next/location/measures")
            prev_location_measures = self.get_text_from_child(node, "prev/location/measures")
            self.add_to_measure(ChordSpanner(attr_type, next_location_fractions, prev_location_fractions, next_location_measures, prev_location_measures))
            return False

        if self.get_path() == "/museScore/Score/Staff/Measure/voice/Chord/Note/Spanner":
            attr = dict(self.get_attributes(node))
            attr_type = attr["type"]
            next_location_fractions = self.get_text_from_child(node, "next/location/fractions")
            prev_location_fractions = self.get_text_from_child(node, "prev/location/fractions")
            next_location_measures = self.get_text_from_child(node, "next/location/measures")
            prev_location_measures = self.get_text_from_child(node, "prev/location/measures")
            self.add_to_measure(ChordNoteSpanner(attr_type, next_location_fractions, prev_location_fractions, next_location_measures, prev_location_measures))
            return False

        if self.get_path() == "/museScore/Score/Staff/Measure/voice/Tempo":
            tempo = self.get_text_from_child(node, "tempo")
            text =self.get_text_from_child(node, "text")
            text_sym = self.get_text_from_child(node,"text/sym")
            self.add_to_measure(Tempo(tempo, text, text_sym))
            return False

        if self.get_path() == "/museScore/Score/Staff/TBox/Text":
            style = self.get_text_from_child(node, "style")
            text = self.get_text_from_child(node, "text")
            self.add_to_staff(TBox(style, text))
            return False

        if self.get_path() == "/museScore/Score/Staff/Measure/voice/Tuplet":
            normal_notes = self.get_text_from_child(node, "normalNotes")
            actual_notes = self.get_text_from_child(node, "actualNotes")
            base_note = self.get_text_from_child(node, "baseNote")
            number_style = self.get_text_from_child(node, "Number/style")
            number_text = self.get_text_from_child(node, "Number/text")
            self.add_to_measure(Tuplet(normal_notes, actual_notes, base_note, number_style, number_text))
            return False

        if self.get_path() == "/museScore/Score/Staff/Measure/voice/endTuplet":
            self.add_to_measure(EndTuplet())
            return False

        if self.get_path() == "/museScore/Score/Staff/Measure/startRepeat":
            self.add_to_measure(StartRepeat())
            return False

        if self.get_path() == "/museScore/Score/Staff/Measure/voice/StaffText":
            text = self.get_text_from_child(node, "text")
            self.add_to_measure(StaffText(text))
            return False


        return False

if __name__ == "__main__":
    m = MuseScoreParser(sys.argv[1])
    #pprint(m.staffs)

