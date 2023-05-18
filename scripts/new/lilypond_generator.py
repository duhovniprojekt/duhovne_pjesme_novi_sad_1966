#!/usr/bin/env python

import musescore_parser as mp
import sys
from fractions import Fraction

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

parser_duration = {
    'whole' : '1',
    'half' : '2',
    'quarter' : '4',
    'eighth' : '8',
    '16th' : '16',
    '32nd' : '32'
}

parser_duration_fractions = {
    'whole' : "4/4",
    'half' : "2/4",
    'quarter' : "1/4",
    'eighth' : "1/8",
    '16th' : "1/16",
    '32nd' : "1/32"
}

parser_tpc = {
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
    '' : "treble"
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

last_pitch = 60
last_tpc = 14

def get_note(pitch, tpc, duration, dots):
        global last_pitch, last_tpc
        line = parser_tpc[tpc]
        pitch_diff = int(pitch) - int(last_pitch)
        tcp_diff = int(tpc) - int(last_tpc)
        last_pitch = pitch
        last_tpc = tpc
        print("%%%% pitch_diff %s, last_pitch %s, pitch %s, tcp_diff %s" % (pitch_diff, last_pitch, pitch, tcp_diff))

        #TODO: clean up this mess
        if (pitch_diff >= 6 and pitch_diff < 18):
            if (pitch_diff == 6 and tcp_diff == 6):
                print("%% pitch_diff > but exception")
                line += ""
            else:
                print("%% pitch_diff >")
                line += "'"
        elif (pitch_diff >= 18 and pitch_diff < 30):
            if (pitch_diff == 18 and tcp_diff == 6):
                print("%% pitch_diff >> but exception")
                line += "'"
            else:
                print("%% pitch_diff >>")
                line += "''"
        elif (pitch_diff >= 30):
            if (pitch_diff == 30 and tcp_diff == 6):
                print("%% pitch_diff >>> but exception")
                line += "''"
            else:
                print("%% pitch_diff >>>")
                line += "'''"
        elif (pitch_diff <= -6 and pitch_diff > -18):
            if (pitch_diff == -6 and tcp_diff == -6):
                print("%% pitch_diff < but exception")
                line += ""
            else:
                print("%% pitch_diff <")
                line += ","
        elif (pitch_diff <= -18 and pitch_diff > -30):

            if (pitch_diff == -18 and tcp_diff == -6):
                print("%% pitch_diff << but exception")
                line += ","
            else:
                print("%% pitch_diff <<")
                line += ",,"
        elif (pitch_diff <= -30):
            if (pitch_diff == -30 and tcp_diff == -6):
                print("%% pitch_diff <<< but exception")
                line += ",,"
            else:
                print("%% pitch_diff <<<")
                line += ",,,"
        line += parser_duration[duration]
        if (dots):
            line += int(dots) * "."
        return line
    
#~
#\(
#\)
#\\mark \\markup { \\box \\bold %s }" % self.text
#\\set Score.repeatCommands = #\'((volta \"%s\"))" % self.voltaText
#\\set Score.repeatCommands = #\'((volta #f))"
#\\break"
#\\clef %s" % self.types[self.type]

class LilypondGenerator(mp.MuseScoreParser):
    def get_head(self):
        string = []
        string.append("\\version \"2.19.84\"")
        string.append("\\include \"deutsch.ly\"")
        string.append("")
        string.append("\layout {")
        string.append("  indent = 0")
        string.append("}")
        return string

    def get_header(self):
        string = []
        string.append("\header {")
        for e in self.staffs[0].children:
            if isinstance(e, mp.VBox):
                if e.style == "Title":
                    string.append(f"  title = \"%s\"" % e.text)
                elif e.style == "Composer":
                    string.append("  composer = \"%s\"" % e.text)
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

    def get_staff_data(self, staff):
        string = []
        for sc in staff.children:
            if isinstance(sc, mp.Measure):
                line = "  "
                for e in sc.children:
                    if isinstance(e, mp.TimeSig):
                        string.append("  \\time %s/%s" % (e.sig_n, e.sig_d))
                    elif isinstance(e, mp.Rest):
                        if e.duration_type == "measure":
                            line += "r" + parser_key_signature_duration[e.duration]
                        else:
                            line += "r" + parser_duration[e.duration_type]
                        line += " "
                    elif isinstance(e, mp.Chord):
                        line += get_note(e.note_pitch, e.note_tpc, e.duration_type, e.dots)
                        line += " "
                line += "|"
                string.append(line)
#            elif isinstance(element, TypeKeySignature):
#                string.append("  \\key %s \\major" % element.getKey())
#            elif isinstance(element, TypeTie):
#                line += element.getTie()
#                line += " "
#            elif isinstance(element, TypeSlur):
#                line += element.getSlur()
#                line += " "
#            elif isinstance(element, TypeBarLine):
#                line += "\\bar \"%s\"" % element.getLine()
#                line += " "
#            elif isinstance(element, TypeLayoutBreak):
#                line += element.getBreak()
#                line += " "
#            elif isinstance(element, TypeRehearsalMark):
#                line += '\n'
#                line += '  '
#                line += element.getMark()
#                line += '\n'
#                line += "  "
#            elif isinstance(element, TypeVolta):
#                line += '\n'
#                line += '  '
#                line += element.getVolta()
#                line += '\n'
#                line += "  "
#            elif isinstance(element, TypeClef):
#                string.append("  %s" % element.getType())
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
            bar.insert(0, "S")
        return bar

    def fractions_convert_bar_with_fractions_to_ly(self, bar):
        line = ""
        for e in bar:
            if isinstance(e, Fraction):
                found = False
                for key, value in parser_duration_fractions.items():
                    if e == Fraction(value):
                        found = True
                        line += parser_duration[key]
                if not found:
                    line += f"fraction_not_found[{e}]"
                line += " "
            else:
                line += e
        return line

    def get_harmony(self, staff):
        string = []
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
                        harmony = parser_tpc[e.root]
                        bar.append(harmony)
                    elif isinstance(e, mp.Chord):
                        predicted_duration = Fraction(parser_duration_fractions[e.duration_type])
                        bar.append(predicted_duration)
                    elif isinstance(e, mp.Rest):
                        if e.duration_type == "measure":
                            predicted_duration = Fraction(e.duration)
                            bar.append(predicted_duration)
                        else:
                            predicted_duration = Fraction(parser_duration_fractions[e.duration_type])
                            bar.append(predicted_duration)
                    elif isinstance(e, mp.Location):
                        predicted_duration = Fraction(e.fractions)
                        bar.append(predicted_duration)
                      
                bar = self.fractions_add_missing(bar, time_signature)
                bar = self.fractions_sum_neighbor(bar)
                bar = self.fractions_add_skip_if_bar_starts_with_fraction(bar)
                line += self.fractions_convert_bar_with_fractions_to_ly(bar)
                line += "|"
                string.append(line)
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
        return nos

    def fractions_swap_with_elements(self, bar):
        swaped_bar = []
        fraction = None
        for e in bar:
            if isinstance(e, Fraction):
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
        string = []
        string.append("lyric%s%s = \\lyricmode {" % (parser_name[staff.id], parser_name[no]))
        time_signature = None
        for sc in staff.children:
            if isinstance(sc, mp.Measure):
                bar = []
                line = "  "
                for e in sc.children:

                    if isinstance(e, mp.TimeSig):
                        time_signature = Fraction(f"{e.sig_n}/{e.sig_d}")
                    if isinstance(e, mp.Lyrics):
                        if e.no == no:
                            bar.append(e.text)
                    elif isinstance(e, mp.Chord):
                        predicted_duration = Fraction(parser_duration_fractions[e.duration_type])
                        bar.append(predicted_duration)
                    elif isinstance(e, mp.Rest):
                        if e.duration_type == "measure":
                            predicted_duration = Fraction(e.duration)
                            bar.append(predicted_duration)
                        else:
                            predicted_duration = Fraction(parser_duration_fractions[e.duration_type])
                            bar.append(predicted_duration)

                bar = self.fractions_add_missing(bar, time_signature)
                bar = self.fractions_sum_neighbor(bar)
                bar = self.fractions_swap_with_elements(bar)
                bar = self.fractions_add_skip_if_bar_starts_with_fraction(bar)
                line += self.fractions_convert_bar_with_fractions_to_ly(bar)
                #line += str(bar)
                line += "|"
                string.append(line)

        string.append("}")
        return string 


    def get_score(self):
        string = []
        string.append("\\score {")
        string.append("    <<")
        for staff in self.staffs:
            string.append("    \\new ChordNames \\harmony%s" % parser_name[staff.id])
            string.append("    \\new Staff {")
            string.append("        \\new Voice = \"lead\" { \\staff%s }" % parser_name[staff.id])
            string.append("    }")
            for no in self.get_lyric_nos(staff):
                string.append("    \\new Lyrics \"lead\" { \\lyric%s%s }" % (parser_name[staff.id], parser_name[no]))
        string.append("    >>")
        string.append("}")
        return(string)

    def get_file(self):
        string = []
        string += self.get_head()
        string.append("")
        string += self.get_header()
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
        return(string)

if __name__ == "__main__":
    lg = LilypondGenerator(sys.argv[1])
    print("\n".join(lg.get_file()))
