#!/usr/bin/env python

import musescore_parser as mp
import sys
from fractions import Fraction
from dataclasses import dataclass, field
from typing import Optional
import re

#https://github.com/OpenLilyPondFonts/lilyjazz/blob/master/JazzSampler.pdf


@dataclass
class Base:
    def __post_init__(self):
        print("%%", self)
        pass

@dataclass
class LyricHandler(Base):
    note_duration: Optional[Fraction] = None
    text: Optional[str] = None
    note_pitch: Optional[str] = None
    extender_line: Optional[str] = None
    extender_duration: Optional[Fraction] = None
    slur: Optional[str] = None

parser_key_signature = {
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

parser_key_signature_duration = {
    '4/4': "1",
    '3/4': "2.",
    '2/4': "2",
}

parser_duration_fractions = {
    'whole' : "4/4",
    'half' : "2/4",
    'quarter' : "1/4",
    'eighth' : "1/8",
    '16th' : "1/16",
    '32nd' : "1/32",
    '64th' : "1/64"
}

parser_tpc = {
    '' : 's',    
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

parser_barline = {
    "startRepeat" : ".|:",
    "endRepeat" : ":|.",
    "double" : "||",
    "end" : "|."
}

parser_clefs = {
    "G8vb" : "tenorG",
    "F" : "bass",
    '' : "treble",
    'G' : "treble"
}

parser_name = {
    "": "Zero",
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
}

parser_dots_fractions = {
    "": 1,
    "1": 1 + 1/2,
    "2": 1 + 1/2 + 1/2/2,
    "3": 1 + 1/2 + 1/2/2 + 1/2/2/2,
    "4": 1 + 1/2 + 1/2/2 + 1/2/2/2 + 1/2/2/2/2,
}

parser_fraction_to_duration = {
    "1": "1",
    "1/1": "1",

    "1/2": "2",

    "1/4": "4",
    "2/4": "2",
    "3/4": "2.",

    "1/8": "8",
    "3/8": "4.",
    "7/8": "2..",

    "1/16": "16",
    "3/16": "8.",
    "7/16": "4..",
    "15/16": "2...",

    "1/32": "32",
    "3/32": "16.",
    "7/32": "8..",
    "15/32": "4...",

    "1/64": "64",
    "3/64": "32.",
}

parse_measure_end_repeat = {
    "2": ":|."
}

#https://github.com/OpenLilyPondFonts/lilyjazz/blob/master/JazzSampler.pdf
parse_chord_names = {
    "m7": "m7",
    "(add9)": "9^7",
    "7": "7",
    "m6": "m6",
    "dim6": "dim6",
    "dim7": "dim7",
    "dim": "dim",
    "m7(11)": "m7.11",
    "6": "6",
    "Maj9": "maj9",
    "7(b9)": "9-",
    "m": "m",
    "0": "m7.5-",
    "7(#9)": "9+",
    "o7": "dim7",
    "7(#5)": "7.5+",
    "(b5)": "dim",
    "sus4": "sus4",
    "7sus4": "sus4.7"
}

last_pitch = 60
last_tpc = 14

def get_pitch(pitch, tpc):
        global last_pitch, last_tpc
        line = parser_tpc[tpc]
        pitch_diff = int(pitch) - int(last_pitch)
        tcp_diff = int(tpc) - int(last_tpc)
        last_pitch = pitch
        last_tpc = tpc
        #print("%%%% pitch_diff %s, last_pitch %s, pitch %s, tcp_diff %s" % (pitch_diff, last_pitch, pitch, tcp_diff))

        #TODO: clean up this mess
        if (pitch_diff >= 6 and pitch_diff < 18):
            if (pitch_diff == 6 and tcp_diff == 6):
                #print("%% pitch_diff > but exception")
                line += ""
            else:
                #print("%% pitch_diff >")
                line += "'"
        elif (pitch_diff >= 18 and pitch_diff < 30):
            if (pitch_diff == 18 and tcp_diff == 6):
                #print("%% pitch_diff >> but exception")
                line += "'"
            else:
                #print("%% pitch_diff >>")
                line += "''"
        elif (pitch_diff >= 30):
            if (pitch_diff == 30 and tcp_diff == 6):
                #print("%% pitch_diff >>> but exception")
                line += "''"
            else:
                #print("%% pitch_diff >>>")
                line += "'''"
        elif (pitch_diff <= -6 and pitch_diff > -18):
            if (pitch_diff == -6 and tcp_diff == -6):
                #print("%% pitch_diff < but exception")
                line += ""
            else:
                #print("%% pitch_diff <")
                line += ","
        elif (pitch_diff <= -18 and pitch_diff > -30):

            if (pitch_diff == -18 and tcp_diff == -6):
                #print("%% pitch_diff << but exception")
                line += ","
            else:
                #print("%% pitch_diff <<")
                line += ",,"
        elif (pitch_diff <= -30):
            if (pitch_diff == -30 and tcp_diff == -6):
                #print("%% pitch_diff <<< but exception")
                line += ",,"
            else:
                #print("%% pitch_diff <<<")
                line += ",,,"
        return line
    

class LilypondGenerator(mp.MuseScoreParser):
    def get_head(self):
        string = []
        string.append("\\version \"2.24.1\"")
        string.append("\\include \"deutsch.ly\"")
        string.append("jazzChords = { \\semiGermanChords }")
        string.append("aFourL = {}")
        string.append("%\\include \"../config/include.ily\"")
        string.append("markMoj = #(define-music-function (letter) (string?) #{ \\mark \\markup { \\box \\bold #letter } #})")
        string.append("")
        string.append("\layout {")
        string.append("  indent = 0")
        string.append("}")
        return string

    def get_header(self):
        string = []
        string.append("\header {")
        string.append("  titlex = \"Pjevajte Jahvi\"")
        poet_found = False
        part_found = False
        for e in self.staffs[0].children:
            if isinstance(e, mp.VBox):
                if e.style == "Title":
                    string.append(f"  title = \"%s\"" % e.text.upper())
                elif e.style == "Composer":
                    string.append("  composer = \"%s\"" % e.text)
                elif e.style == "Lyricist":
                    string.append("  %%poet = \"%s\"" % e.text)
                    string.append("  style = \"%s\"" % e.text)
                    poet_found = True
                elif e.style == "Instrument Name (Part)":
                    string.append("  %%meter = \"%s\"" % e.text)
                    string.append("  broj = \"%s\"" % e.text)
                    part_found = True
        if not poet_found:
            string.append("  style = \"\"")
        if not part_found:
            string.append("  broj = \"1\"")
        string.append("  %tagline = \\markup { \\override #'(font-name . \"JohnSans White Pro\") \\override #'(font-size . -3) { Izvorno: Name, Album } }")

        string.append("}")
        return string        

    def get_paper(self):
        string = []
        string.append("\\paper {")
        string.append("  \\aFourL")
        string.append("  %min-systems-per-page = #7")
        string.append("  %annotate-spacing = ##t")
        string.append("  %system-system-spacing.padding = #3.2")
        string.append("  %page-breaking = #ly:one-page-breaking")
        string.append("  %last-bottom-spacing.minimum-distance = #8")
        string.append("}")
        return string

    def get_staff_start(self, staff):
        string = []
        string.append("staff%s = \\relative c' {" % parser_name[staff.id])
        return string

    def get_staff_end(self):
        string = []
        string.append("}")
        return string              

    def fractions_add_missing(self, bar, time_signature):
        fraction_sum = Fraction(0)
        for e in bar:
            if isinstance(e, Fraction):
                fraction_sum += e
        if fraction_sum != time_signature:
            bar.append(time_signature - fraction_sum)
        return bar

    def fractions_sum_neighbor(self, bar):
        summed_bar = []
        fraction = None
        for e in bar:
            if isinstance(e, Fraction):
                if fraction is not None:
                    fraction += e
                else:
                    fraction = e
            else:
                if fraction is not None:
                    summed_bar.append(fraction)
                    fraction = None
                summed_bar.append(e)
        if fraction is not None:
            summed_bar.append(fraction)
            fraction = None
        return summed_bar

    def fractions_add_skip_if_bar_starts_with_fraction(self, bar):
        if len(bar) > 0 and isinstance(bar[0], Fraction):
            bar.insert(0, "s")
        return bar

    def fractions_convert_bar_with_fractions_to_ly(self, bar, lyrics=False):
        line = ""
        for e in bar:
            if isinstance(e, Fraction):
                if not lyrics:
                    line += parser_fraction_to_duration[str(e)]
                    line += " "
            else:
                line += e
                if lyrics:
                    line += " "
                if "bar" in e or "mark" in e or "clef" in e or "repeat" in e:
                    line += " "
                if "{" in e or "}" in e:
                    line += " "

        return line

    def fractions_convert_harmony_bar_with_fractions_to_ly(self, bar):
        line = ""
        harmony = None
        for e in bar:
            if isinstance(e, Fraction):
                if harmony is not None:
                    line += parser_tpc[harmony.root]
                line += parser_fraction_to_duration[str(e)]
                if harmony is not None:
                    if harmony.name:
                        line += ":" + parse_chord_names[harmony.name]
                    if harmony.base:
                        line += "/" + parser_tpc[harmony.base]
                line += " "
                harmony = None
            elif isinstance(e, mp.Harmony):
                harmony = e
            else:
                line += e
            
        return line

    def get_staff_data(self, staff):
        string = []
        for sc in staff.children:
            if isinstance(sc, mp.Measure):
                bar = []
                line = "  "
                has_break = False
                for e in sc.children:
                    if isinstance(e, mp.TimeSig):
                        string.append("  \\time %s/%s" % (e.sig_n, e.sig_d))
                    elif isinstance(e, mp.Tempo):
                        string.append("  \\tempo 4 = %s" % int((60 * float(e.tempo))))
                    elif isinstance(e, mp.Rest):
                        if e.duration_type == "measure":
                            bar.append("r")
                            predicted_duration = Fraction(e.duration)
                            bar.append(predicted_duration)
                        else:
                            bar.append("r")
                            predicted_duration = Fraction(parser_duration_fractions[e.duration_type])
                            predicted_duration *= Fraction(parser_dots_fractions[e.dots])
                            bar.append(predicted_duration)
                    elif isinstance(e, mp.Chord):
                        bar.append(get_pitch(e.note_pitch, e.note_tpc))
                        predicted_duration = Fraction(parser_duration_fractions[e.duration_type])
                        predicted_duration *= Fraction(parser_dots_fractions[e.dots])
                        bar.append(predicted_duration)
                    elif isinstance(e, mp.KeySig):
                        tpc_value = str(14 + int(e.accidental))
                        string.append("  \\key %s \\major" % parser_tpc[tpc_value])
                    elif isinstance(e, mp.ChordNoteSpanner):
                        if e.type == "Tie":
                            if e.next_location_fractions or e.next_location_measures:
                                bar.append("~")
                    elif isinstance(e, mp.ChordSpanner):
                        if e.type == "Slur":
                            if e.next_location_fractions or e.next_location_measures:
                                bar.append("(")
                            elif e.prev_location_fractions or e.prev_location_measures:
                                bar.append(")")
                    elif isinstance(e, mp.BarLine):
                        bar.append("\\bar \"%s\"" % parser_barline[e.subtype])
                    elif isinstance(e, mp.RehearsalMark):
                        #text = "\\mark \\markup { \\box \\bold %s }" % e.text
                        #bar.append(text)
                        text = "\\markMoj \"%s\"" % e.text
                        #text = "\\markMoj"
                        bar.append(text)
                        #text = "%\\markMojPonn"
                        #bar.append(text)
                    elif isinstance(e, mp.Clef):
                        if e.concert_clef_type:
                            text = "\\clef %s" % parser_clefs[e.concert_clef_type]
                            bar.append(text)
                        elif e.transposing_clef_type:
                            text = "\\clef %s" % parser_clefs[e.transposing_clef_type]
                            bar.append(text)
                    elif isinstance(e, mp.LayoutBreak):
                        if e.subtype == "line":
                            has_break = True
                    elif isinstance(e, mp.VoltaSpanner):
                        if e.next_location_measures:
                            text = "\\set Score.repeatCommands = #\'((volta \"%s\"))" % e.begin_text
                            bar.append(text)
                        elif e.prev_location_measures:
                            text = "\\set Score.repeatCommands = #\'((volta #f))"
                            bar.append(text)
                    elif isinstance(e, mp.Tuplet):
                        text = "\\tuplet %s/%s {" % (e.actual_notes, e.normal_notes)
                        bar.append(text)
                    elif isinstance(e, mp.EndTuplet):
                        text = "}"
                        bar.append(text)

                #line += str(bar) + "\n  "
                if sc.len:
                    line += "\\partial %s" % parser_fraction_to_duration[sc.len]
                    line += "\n  "
                line += self.fractions_convert_bar_with_fractions_to_ly(bar)
                if sc.end_repeat:
                    line += "\\bar \"%s\"" % parse_measure_end_repeat[sc.end_repeat]
                    line += " "
                line += "|"
                #if has_break:
                #    line += " \\break"
                string.append(line)
        return string        


    def get_harmony(self, staff):
        string = []

        #harmony_found = False
        #for sc in staff.children:
        #    if isinstance(sc, mp.Measure):
        #        for e in sc.children:
        #            if isinstance(e, mp.Harmony):
        #                harmony_found = True
        #if not harmony_found:
        #    return string

        string.append("harmony%s = \chordmode  {" % parser_name[staff.id])
        time_signature = None
        for sc in staff.children:
            if isinstance(sc, mp.Measure):
                bar = []
                line = "  "
                for e in sc.children:

                    if isinstance(e, mp.TimeSig):
                        time_signature = Fraction(f"{e.sig_n}/{e.sig_d}")
                    elif isinstance(e, mp.Harmony):
                        bar.append(e)
                    elif isinstance(e, mp.Chord):
                        predicted_duration = Fraction(parser_duration_fractions[e.duration_type])
                        predicted_duration *= Fraction(parser_dots_fractions[e.dots])
                        bar.append(predicted_duration)
                    elif isinstance(e, mp.Rest):
                        if e.duration_type == "measure":
                            predicted_duration = Fraction(e.duration)
                            bar.append(predicted_duration)
                        else:
                            predicted_duration = Fraction(parser_duration_fractions[e.duration_type])
                            predicted_duration *= Fraction(parser_dots_fractions[e.dots])
                            bar.append(predicted_duration)
                    elif isinstance(e, mp.Location):
                        predicted_duration = Fraction(e.fractions)
                        bar.append(predicted_duration)
                if sc.len:
                    bar = self.fractions_add_missing(bar, Fraction(sc.len))
                else:
                    bar = self.fractions_add_missing(bar, time_signature)
                bar = self.fractions_sum_neighbor(bar)
                bar = self.fractions_add_skip_if_bar_starts_with_fraction(bar)
                line += self.fractions_convert_harmony_bar_with_fractions_to_ly(bar)
                #line += str(bar)
                line += "|"
                string.append(line)
        # force end bar
        string.append("  \\bar \"|.\"")
        string.append("}")
        return(string)

    def get_lyric_nos(self, staff):
        nos = []
        for sc in staff.children:
            if isinstance(sc, mp.Measure):
                for e in sc.children:
                    if isinstance(e, mp.Lyrics):
                        if e.no not in nos:
                            nos.append(e.no)
        return sorted(nos)

    def fractions_swap_with_elements(self, bar):
        swaped_bar = []
        fraction = None
        for e in bar:
            if isinstance(e, Fraction):
                if fraction is None:
                    fraction = e
                else:
                    swaped_bar.append(fraction)
                    fraction = e
            else:
                swaped_bar.append(e)
                if fraction is not None:
                    swaped_bar.append(fraction)
                    fraction = None
        if fraction is not None:
            swaped_bar.append(fraction)
            fraction = None
        return swaped_bar

    def get_lyric(self, staff, no):
        bars = []
        for sc in staff.children:
            if isinstance(sc, mp.Measure):
                bar = []
                lyric_handler = LyricHandler()
                for e in sc.children:
                    if isinstance(e, mp.Lyrics):
                        if e.no == no:
                            #print(repr(e.text))
                            if "\xa0" in e.text:
                                lyric_handler.text = "\"%s\"" % e.text
                            else:
                                lyric_handler.text = e.text
                            if e.syllabic in ["begin", "middle"]:
                                lyric_handler.extender_line = "--"
                            if e.ticks_f and e.ticks:
                                predicted_duration = - Fraction(e.ticks_f)
                                lyric_handler.extender_line = "__"
                                lyric_handler.extender_duration = abs(predicted_duration)
                    elif isinstance(e, mp.Chord):
                        if lyric_handler.note_duration is not None:
                            bar.append(lyric_handler)
                            lyric_handler = LyricHandler()
                        predicted_duration = Fraction(parser_duration_fractions[e.duration_type])
                        predicted_duration *= Fraction(parser_dots_fractions[e.dots])
                        lyric_handler.note_pitch = "c"
                        lyric_handler.note_duration = predicted_duration
                    elif isinstance(e, mp.Rest):
                        if e.duration_type == "measure":
                            if lyric_handler.note_duration is not None:
                                bar.append(lyric_handler)
                                lyric_handler = LyricHandler()
                            predicted_duration = Fraction(e.duration)
                            lyric_handler.note_pitch = "r"
                            lyric_handler.note_duration = predicted_duration
                        else:
                            if lyric_handler.note_duration is not None:
                                bar.append(lyric_handler)
                                lyric_handler = LyricHandler()
                            predicted_duration = Fraction(parser_duration_fractions[e.duration_type])
                            predicted_duration *= Fraction(parser_dots_fractions[e.dots])
                            lyric_handler.note_pitch = "r"
                            lyric_handler.note_duration = predicted_duration

                    if lyric_handler.note_duration is not None and lyric_handler.text is not None:
                        bar.append(lyric_handler)
                        lyric_handler = LyricHandler()

                if lyric_handler.note_duration is not None:
                    bar.append(lyric_handler)
                    lyric_handler = LyricHandler()

                bars.append(bar)

        # add slurs for extender line and replace non text notes to rests
        extender_duration = None
        for bar in bars:
            #print("|")
            for b in bar:
                #print("  ", b)
                if b.text is not None:
                    if b.extender_duration:
                        extender_duration = b.extender_duration - b.note_duration
                        #print(extender_duration, "adding (")
                        b.slur = "("
                else:
                    if extender_duration is None:
                        b.note_pitch = "r"
                    else:
                        extender_duration -= b.note_duration
                        #print(extender_duration, "calculating")
                        if extender_duration < 0:
                            extender_duration = None
                            #print("adding )")
                            b.slur = ")"

        string = []

        #string.append("%%test%s%s = {" % (parser_name[staff.id], parser_name[no]))
        #for bar in bars:
        #    for b in bar:
        #        line = "%  "
        #        line += str(b)
        #        string.append(line)
        #    string.append("%  |")
        #string.append("%}")
        #string.append("")

        string.append("aligner%s%s = \\relative {" % (parser_name[staff.id], parser_name[no]))
        for bar in bars:
            line = "  "
            for b in bar:
                line += b.note_pitch + parser_fraction_to_duration[str(b.note_duration)]
                if b.slur:
                    line += b.slur
                line += " "
            line += "|"
            if len(line.strip()):
                string.append(line)
        string.append("}")
        string.append("")
        string.append("lyric%s%s = \\lyricmode {" % (parser_name[staff.id], parser_name[no]))
        for bar in bars:
            line = "  "
            for b in bar:
                if b.text is not None:
                    line += b.text
                    line += " "
                if b.extender_line is not None:
                    line += b.extender_line
                    line += " "
            line += "%|"
            if len(line.strip()):
                string.append(line)
        string.append("}")
        return string 

    def get_tbox(self):
        string = []

        #tbox_found = False
        #for e in self.staffs[0].children:
        #    if isinstance(e, mp.TBox):
        #        tbox_found = True
        #        break
        #if not tbox_found:
        #    return string

        stanzas = []
        lyrics = []
        for e in self.staffs[0].children:
            if isinstance(e, mp.TBox):
                if e.style == "Frame":
                    line_count = 0
                    for line in e.text.split("\n"):
                        line = line.strip()
                        if len(line) > 0:
                            if re.match("\\d\\.", line):
                                stanzas.append("    \\line { \\bold %s }" % line)
                            else:
                                line_count += 1
                                lyrics.append("    \\line { %s }" % line)
                        else:
                            stanzas.append("    \\vspace #%s" % (line_count))
                            line_count = 0
                            lyrics.append("    \\vspace #1")

        string.append("\\markup {")
        string.append("  \\column {")
        string += stanzas
        string.append("  }")
        string.append("  \\hspace #1")
        string.append("  \\column {")
        string += lyrics
        string.append("  }")
        string.append("}")
        return string        


    def get_score(self):
        string = []
        string.append("\\score {")
        string.append("    <<")
        for staff in self.staffs:
            string.append("    \\new ChordNames { \\jazzChords \\harmony%s }" % parser_name[staff.id])
            string.append("    \\new Staff {")
            string.append("        <<")
            string.append("        \\new Voice { \\staff%s }" % parser_name[staff.id])
            for no in self.get_lyric_nos(staff):
                string.append("        \\new NullVoice = \"aligner%s%s\" { \\aligner%s%s }" % (parser_name[staff.id], parser_name[no], parser_name[staff.id], parser_name[no]))
                string.append("        \\new Lyrics \\lyricsto \"aligner%s%s\" { \\lyric%s%s }" % (parser_name[staff.id], parser_name[no], parser_name[staff.id], parser_name[no]))
            string.append("        >>")
            string.append("    }")
            #string.append("    \\new Staff {")
            #for no in self.get_lyric_nos(staff):
            #    string.append("        \\new Voice = \"aligner%s%s\" { \\transpose c c'' \\aligner%s%s }" % (parser_name[staff.id], parser_name[no], parser_name[staff.id], parser_name[no]))
            #string.append("    }")
        string.append("    >>")
        string.append("}")
        return(string)

    def get_file(self):
        string = []
        string += self.get_head()
        string.append("")
        string += self.get_header()
        string.append("")
        string += self.get_paper()
        string.append("")
        for s in self.staffs:
            string += self.get_staff_start(s)
            string += self.get_staff_data(s)
            string += self.get_staff_end()
            string.append("")
            string += self.get_harmony(s)
            string.append("")
            for no in self.get_lyric_nos(s):
                string += self.get_lyric(s, no)
                string.append("")
        string += self.get_score()
        string.append("")
        string += self.get_tbox()
        return(string)

if __name__ == "__main__":
    lg = LilypondGenerator(sys.argv[1])
    print("\n".join(lg.get_file()))
