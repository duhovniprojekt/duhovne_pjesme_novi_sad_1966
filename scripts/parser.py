from dataclasses import dataclass
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser

from msmodel.muse_score import *


def get_musescore(filename):
    parser = XmlParser(context=XmlContext())
    return parser.parse(filename, MuseScore)


def get_first_element(element):
    if isinstance(element, list):
        return element[0]
    else:
        return element


@dataclass
class Header:
    title: str
    subtitle: str
    composer: str
    lyricist: str


def get_header(musescore: MuseScore) -> Header:
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
    return Header(title=title, subtitle=subtitle, composer=composer, lyricist=lyricist)


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
    t = get_first_element(measure.voice).time_sig
    if t is not None:
        return f"{t.sig_n}/{t.sig_d}"
    else:
        return None


class TypeKeySignature():
    parser = {
        -7: 'ces',
        -6: 'ges',
        -5: 'des',
        -4: 'as',
        -3: 'es',
        -2: 'b',
        -1: 'f',
        0: 'c',
        1: 'g',
        2: 'd',
        3: 'a',
        4: 'e',
        5: 'h',
        6: 'fis',
        7: 'cis',
    }


def get_key_signature(measure: Measure, is_first_measure=False) -> Optional[str]:
    k = get_first_element(measure.voice).key_sig
    if k is not None:
        return TypeKeySignature.parser[k.accidental]
    else:
        if is_first_measure:
            return TypeKeySignature.parser[0]
        else:
            return None


def parse_measure(measure: Measure) -> Optional[str]:
    return measure


if __name__ == "__main__":
    musescore = get_musescore("msmodel_examples/test_note_duration.mscx")
    for i in range(get_measure_count(musescore)):
        print(parse_measure(get_measure(musescore, i)))
