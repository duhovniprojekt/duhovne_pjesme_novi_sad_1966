from dataclasses import dataclass
import utils
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser

SONG = "msmodel_examples/test_score.mscx"

from msmodel.muse_score import *


@dataclass
class Header:
    title: str
    subtitle: str
    composer: str
    lyricist: str
    copyright: str


def get_header(museScore: MuseScore) -> Header:
    title = ""
    subtitle = ""
    composer = ""
    lyricist = ""
    copyright = ""
    for t in museScore.score.meta_tag:
        match t.name:
            case "copyright":
                copyright = t.value
    for t in museScore.score.staff[0].vbox.text:
        match t.style:
            case "Title":
                title = t.text
            case "Subtitle":
                subtitle = t.text
            case "Composer":
                composer = t.text
            case "Lyricist":
                lyricist = t.text
    return Header(title=title, subtitle=subtitle, composer=composer, lyricist=lyricist, copyright=copyright)


def get_time_signature(measure: Measure) -> str:
    ts = measure.voice.time_sig
    if ts is not None:
        return f"{ts.sig_n}/{ts.sig_d}"
    return ""


if __name__ == "__main__":
    parser = XmlParser(context=XmlContext())
    museScore = parser.parse(SONG, MuseScore)
    # print(get_header(museScore))
    print(museScore.score.staff[0].measure[1])
    # print(get_time_signature(museScore.score.staff[0].measure[0]))
