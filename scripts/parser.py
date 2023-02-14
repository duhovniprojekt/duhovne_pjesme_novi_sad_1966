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


def get_header(museScore: MuseScore) -> Header:
    title = ""
    subtitle = ""
    composer = ""
    lyricist = ""
    for t in get_first_element(museScore.score.staff).vbox.text:
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


if __name__ == "__main__":
    museScore = get_musescore("msmodel_examples/test_header.mscx")
    print(get_first_element(museScore.score.staff).measure[0])
    # print(get_time_signature(museScore.score.staff[0].measure[0]))
