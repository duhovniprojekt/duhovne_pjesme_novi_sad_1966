from dataclasses import dataclass, field
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate


@dataclass
class Accidental:
    role: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    subtype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Articulation:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    velocity: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    gate_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "gateTime",
            "type": "Element",
        }
    )


@dataclass
class BarLine:
    subtype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Clef:
    concert_clef_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "concertClefType",
            "type": "Element",
        }
    )
    transposing_clef_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "transposingClefType",
            "type": "Element",
        }
    )


@dataclass
class Fingering:
    text: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Fragment:
    y1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    y2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class HairPin:
    subtype: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Harmony:
    root: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    root_case: Optional[int] = field(
        default=None,
        metadata={
            "name": "rootCase",
            "type": "Element",
        }
    )
    name: Optional[Union[int, str]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    base: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    base_case: Optional[int] = field(
        default=None,
        metadata={
            "name": "baseCase",
            "type": "Element",
        }
    )


@dataclass
class KeySig:
    accidental: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class LayerTag:
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    tag: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class LayoutBreak:
    subtype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class NoteDot:
    visible: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Number:
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    text: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class RehearsalMark:
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class StaffType:
    group: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Stem:
    user_len: Optional[float] = field(
        default=None,
        metadata={
            "name": "userLen",
            "type": "Element",
        }
    )


@dataclass
class TimeSig:
    subtype: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    sig_n: Optional[int] = field(
        default=None,
        metadata={
            "name": "sigN",
            "type": "Element",
        }
    )
    sig_d: Optional[int] = field(
        default=None,
        metadata={
            "name": "sigD",
            "type": "Element",
        }
    )


@dataclass
class Bracket:
    class Meta:
        name = "bracket"

    type: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    span: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    col: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Controller:
    class Meta:
        name = "controller"

    ctrl: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Family:
    class Meta:
        name = "family"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    value: str = field(
        default=""
    )


@dataclass
class Font:
    class Meta:
        name = "font"

    face: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Location:
    class Meta:
        name = "location"

    measures: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    staves: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fractions: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class MetaTag:
    class Meta:
        name = "metaTag"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    value: Union[int, str, XmlDate, float] = field(
        default=""
    )


@dataclass
class O1:
    class Meta:
        name = "o1"

    x: Optional[Union[int, float]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    y: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class O2:
    class Meta:
        name = "o2"

    x: Optional[Union[float, int]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    y: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class O3:
    class Meta:
        name = "o3"

    x: Optional[Union[float, int]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    y: Optional[Union[float, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class O4:
    class Meta:
        name = "o4"

    x: Optional[Union[float, int]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    y: Optional[Union[float, int]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Off2:
    class Meta:
        name = "off2"

    x: Optional[Union[float, int]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    y: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Offset:
    class Meta:
        name = "offset"

    x: Optional[Union[float, int]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    y: Optional[Union[float, int, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Program:
    class Meta:
        name = "program"

    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Section:
    class Meta:
        name = "section"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    brackets: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    show_system_markings: Optional[bool] = field(
        default=None,
        metadata={
            "name": "showSystemMarkings",
            "type": "Attribute",
        }
    )
    bar_line_span: Optional[bool] = field(
        default=None,
        metadata={
            "name": "barLineSpan",
            "type": "Attribute",
        }
    )
    thin_brackets: Optional[bool] = field(
        default=None,
        metadata={
            "name": "thinBrackets",
            "type": "Attribute",
        }
    )
    family: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class StaffPosAbove:
    class Meta:
        name = "staffPosAbove"

    x: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    y: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Beam:
    stem_direction: Optional[str] = field(
        default=None,
        metadata={
            "name": "StemDirection",
            "type": "Element",
        }
    )
    fragment: Optional[Fragment] = field(
        default=None,
        metadata={
            "name": "Fragment",
            "type": "Element",
        }
    )


@dataclass
class Channel:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    controller: List[Controller] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    program: Optional[Program] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    synti: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    mute: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    solo: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Fermata:
    subtype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    offset: Optional[Offset] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Lyrics:
    no: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    syllabic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    ticks: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    ticks_f: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    offset: Optional[Offset] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Segment:
    subtype: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    offset: Optional[Offset] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    off2: Optional[Off2] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    min_distance: Optional[float] = field(
        default=None,
        metadata={
            "name": "minDistance",
            "type": "Element",
        }
    )
    leading_space: Optional[float] = field(
        default=None,
        metadata={
            "name": "leadingSpace",
            "type": "Element",
        }
    )


@dataclass
class SlurSegment:
    no: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    o2: Optional[O2] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    o3: Optional[O3] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    o1: Optional[O1] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    o4: Optional[O4] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    offset: Optional[Offset] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class StaffText:
    offset: Optional[Offset] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Style:
    lyrics_min_distance: Optional[float] = field(
        default=None,
        metadata={
            "name": "lyricsMinDistance",
            "type": "Element",
        }
    )
    lyrics_dash_ypos_ratio: Optional[float] = field(
        default=None,
        metadata={
            "name": "lyricsDashYposRatio",
            "type": "Element",
        }
    )
    lyrics_odd_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "lyricsOddFontFace",
            "type": "Element",
        }
    )
    lyrics_odd_font_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "lyricsOddFontSize",
            "type": "Element",
        }
    )
    lyrics_even_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "lyricsEvenFontFace",
            "type": "Element",
        }
    )
    lyrics_even_font_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "lyricsEvenFontSize",
            "type": "Element",
        }
    )
    bar_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "barWidth",
            "type": "Element",
        }
    )
    double_bar_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "doubleBarWidth",
            "type": "Element",
        }
    )
    end_bar_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "endBarWidth",
            "type": "Element",
        }
    )
    page_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "pageWidth",
            "type": "Element",
        }
    )
    page_height: Optional[float] = field(
        default=None,
        metadata={
            "name": "pageHeight",
            "type": "Element",
        }
    )
    page_printable_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "pagePrintableWidth",
            "type": "Element",
        }
    )
    page_even_left_margin: Optional[float] = field(
        default=None,
        metadata={
            "name": "pageEvenLeftMargin",
            "type": "Element",
        }
    )
    page_odd_left_margin: Optional[float] = field(
        default=None,
        metadata={
            "name": "pageOddLeftMargin",
            "type": "Element",
        }
    )
    page_even_top_margin: Optional[float] = field(
        default=None,
        metadata={
            "name": "pageEvenTopMargin",
            "type": "Element",
        }
    )
    page_even_bottom_margin: Optional[float] = field(
        default=None,
        metadata={
            "name": "pageEvenBottomMargin",
            "type": "Element",
        }
    )
    page_odd_top_margin: Optional[float] = field(
        default=None,
        metadata={
            "name": "pageOddTopMargin",
            "type": "Element",
        }
    )
    page_odd_bottom_margin: Optional[float] = field(
        default=None,
        metadata={
            "name": "pageOddBottomMargin",
            "type": "Element",
        }
    )
    lyrics_dash_force: Optional[int] = field(
        default=None,
        metadata={
            "name": "lyricsDashForce",
            "type": "Element",
        }
    )
    double_bar_distance: Optional[float] = field(
        default=None,
        metadata={
            "name": "doubleBarDistance",
            "type": "Element",
        }
    )
    end_bar_distance: Optional[float] = field(
        default=None,
        metadata={
            "name": "endBarDistance",
            "type": "Element",
        }
    )
    repeat_barline_dot_separation: Optional[float] = field(
        default=None,
        metadata={
            "name": "repeatBarlineDotSeparation",
            "type": "Element",
        }
    )
    bracket_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "bracketWidth",
            "type": "Element",
        }
    )
    stem_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "stemWidth",
            "type": "Element",
        }
    )
    staff_line_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "staffLineWidth",
            "type": "Element",
        }
    )
    ledger_line_length: Optional[float] = field(
        default=None,
        metadata={
            "name": "ledgerLineLength",
            "type": "Element",
        }
    )
    hairpin_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "hairpinWidth",
            "type": "Element",
        }
    )
    hairpin_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "hairpinFontFace",
            "type": "Element",
        }
    )
    hairpin_font_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "hairpinFontSize",
            "type": "Element",
        }
    )
    pedal_line_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "pedalLineWidth",
            "type": "Element",
        }
    )
    pedal_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "pedalFontFace",
            "type": "Element",
        }
    )
    harmony_play: Optional[int] = field(
        default=None,
        metadata={
            "name": "harmonyPlay",
            "type": "Element",
        }
    )
    chord_symbol_afont_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "chordSymbolAFontFace",
            "type": "Element",
        }
    )
    chord_symbol_afont_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "chordSymbolAFontSize",
            "type": "Element",
        }
    )
    chord_symbol_bfont_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "chordSymbolBFontFace",
            "type": "Element",
        }
    )
    chord_symbol_bfont_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "chordSymbolBFontSize",
            "type": "Element",
        }
    )
    nashville_number_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "nashvilleNumberFontFace",
            "type": "Element",
        }
    )
    create_multi_measure_rests: Optional[int] = field(
        default=None,
        metadata={
            "name": "createMultiMeasureRests",
            "type": "Element",
        }
    )
    slur_mid_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "slurMidWidth",
            "type": "Element",
        }
    )
    musical_symbol_font: Optional[str] = field(
        default=None,
        metadata={
            "name": "musicalSymbolFont",
            "type": "Element",
        }
    )
    musical_text_font: Optional[str] = field(
        default=None,
        metadata={
            "name": "musicalTextFont",
            "type": "Element",
        }
    )
    volta_line_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "voltaLineWidth",
            "type": "Element",
        }
    )
    ottava_line_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "ottavaLineWidth",
            "type": "Element",
        }
    )
    ottava_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "ottavaFontFace",
            "type": "Element",
        }
    )
    tuplet_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "tupletFontFace",
            "type": "Element",
        }
    )
    tuplet_font_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "tupletFontSize",
            "type": "Element",
        }
    )
    default_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "defaultFontFace",
            "type": "Element",
        }
    )
    title_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "titleFontFace",
            "type": "Element",
        }
    )
    title_font_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "titleFontSize",
            "type": "Element",
        }
    )
    sub_title_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "subTitleFontFace",
            "type": "Element",
        }
    )
    sub_title_font_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "subTitleFontSize",
            "type": "Element",
        }
    )
    composer_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "composerFontFace",
            "type": "Element",
        }
    )
    composer_font_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "composerFontSize",
            "type": "Element",
        }
    )
    lyricist_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "lyricistFontFace",
            "type": "Element",
        }
    )
    lyricist_font_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "lyricistFontSize",
            "type": "Element",
        }
    )
    fingering_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "fingeringFontFace",
            "type": "Element",
        }
    )
    lh_guitar_fingering_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "lhGuitarFingeringFontFace",
            "type": "Element",
        }
    )
    rh_guitar_fingering_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "rhGuitarFingeringFontFace",
            "type": "Element",
        }
    )
    rh_guitar_fingering_font_style: Optional[int] = field(
        default=None,
        metadata={
            "name": "rhGuitarFingeringFontStyle",
            "type": "Element",
        }
    )
    string_number_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "stringNumberFontFace",
            "type": "Element",
        }
    )
    long_instrument_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "longInstrumentFontFace",
            "type": "Element",
        }
    )
    long_instrument_font_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "longInstrumentFontSize",
            "type": "Element",
        }
    )
    short_instrument_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "shortInstrumentFontFace",
            "type": "Element",
        }
    )
    short_instrument_font_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "shortInstrumentFontSize",
            "type": "Element",
        }
    )
    part_instrument_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "partInstrumentFontFace",
            "type": "Element",
        }
    )
    part_instrument_font_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "partInstrumentFontSize",
            "type": "Element",
        }
    )
    dynamics_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "dynamicsFontFace",
            "type": "Element",
        }
    )
    dynamics_font_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "dynamicsFontSize",
            "type": "Element",
        }
    )
    expression_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "expressionFontFace",
            "type": "Element",
        }
    )
    expression_font_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "expressionFontSize",
            "type": "Element",
        }
    )
    tempo_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "tempoFontFace",
            "type": "Element",
        }
    )
    metronome_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "metronomeFontFace",
            "type": "Element",
        }
    )
    metronome_font_style: Optional[int] = field(
        default=None,
        metadata={
            "name": "metronomeFontStyle",
            "type": "Element",
        }
    )
    measure_number_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "measureNumberFontFace",
            "type": "Element",
        }
    )
    measure_number_font_spatium_dependent: Optional[int] = field(
        default=None,
        metadata={
            "name": "measureNumberFontSpatiumDependent",
            "type": "Element",
        }
    )
    measure_number_font_style: Optional[int] = field(
        default=None,
        metadata={
            "name": "measureNumberFontStyle",
            "type": "Element",
        }
    )
    translator_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "translatorFontFace",
            "type": "Element",
        }
    )
    translator_font_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "translatorFontSize",
            "type": "Element",
        }
    )
    system_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "systemFontFace",
            "type": "Element",
        }
    )
    staff_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "staffFontFace",
            "type": "Element",
        }
    )
    rehearsal_mark_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "rehearsalMarkFontFace",
            "type": "Element",
        }
    )
    rehearsal_mark_frame_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "rehearsalMarkFrameWidth",
            "type": "Element",
        }
    )
    rehearsal_mark_frame_round: Optional[int] = field(
        default=None,
        metadata={
            "name": "rehearsalMarkFrameRound",
            "type": "Element",
        }
    )
    repeat_left_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "repeatLeftFontFace",
            "type": "Element",
        }
    )
    repeat_left_font_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "repeatLeftFontSize",
            "type": "Element",
        }
    )
    repeat_right_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "repeatRightFontFace",
            "type": "Element",
        }
    )
    repeat_right_font_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "repeatRightFontSize",
            "type": "Element",
        }
    )
    frame_font_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "frameFontFace",
            "type": "Element",
        }
    )
    frame_font_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "frameFontSize",
            "type": "Element",
        }
    )
    use_pre_3_6_defaults: Optional[int] = field(
        default=None,
        metadata={
            "name": "usePre_3_6_defaults",
            "type": "Element",
        }
    )
    defaults_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "defaultsVersion",
            "type": "Element",
        }
    )
    clef_left_margin: Optional[float] = field(
        default=None,
        metadata={
            "name": "clefLeftMargin",
            "type": "Element",
        }
    )
    clef_key_right_margin: Optional[float] = field(
        default=None,
        metadata={
            "name": "clefKeyRightMargin",
            "type": "Element",
        }
    )
    bar_note_distance: Optional[float] = field(
        default=None,
        metadata={
            "name": "barNoteDistance",
            "type": "Element",
        }
    )
    harmony_fret_dist: Optional[float] = field(
        default=None,
        metadata={
            "name": "harmonyFretDist",
            "type": "Element",
        }
    )
    enable_vertical_spread: Optional[int] = field(
        default=None,
        metadata={
            "name": "enableVerticalSpread",
            "type": "Element",
        }
    )
    use_standard_note_names: Optional[int] = field(
        default=None,
        metadata={
            "name": "useStandardNoteNames",
            "type": "Element",
        }
    )
    use_german_note_names: Optional[int] = field(
        default=None,
        metadata={
            "name": "useGermanNoteNames",
            "type": "Element",
        }
    )
    lower_case_bass_notes: Optional[int] = field(
        default=None,
        metadata={
            "name": "lowerCaseBassNotes",
            "type": "Element",
        }
    )
    default_frame_padding: Optional[float] = field(
        default=None,
        metadata={
            "name": "defaultFramePadding",
            "type": "Element",
        }
    )
    default_frame_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "defaultFrameWidth",
            "type": "Element",
        }
    )
    default_frame_round: Optional[int] = field(
        default=None,
        metadata={
            "name": "defaultFrameRound",
            "type": "Element",
        }
    )
    title_frame_padding: Optional[float] = field(
        default=None,
        metadata={
            "name": "titleFramePadding",
            "type": "Element",
        }
    )
    title_frame_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "titleFrameWidth",
            "type": "Element",
        }
    )
    title_frame_round: Optional[int] = field(
        default=None,
        metadata={
            "name": "titleFrameRound",
            "type": "Element",
        }
    )
    sub_title_frame_padding: Optional[float] = field(
        default=None,
        metadata={
            "name": "subTitleFramePadding",
            "type": "Element",
        }
    )
    sub_title_frame_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "subTitleFrameWidth",
            "type": "Element",
        }
    )
    sub_title_frame_round: Optional[int] = field(
        default=None,
        metadata={
            "name": "subTitleFrameRound",
            "type": "Element",
        }
    )
    composer_frame_padding: Optional[float] = field(
        default=None,
        metadata={
            "name": "composerFramePadding",
            "type": "Element",
        }
    )
    composer_frame_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "composerFrameWidth",
            "type": "Element",
        }
    )
    composer_frame_round: Optional[int] = field(
        default=None,
        metadata={
            "name": "composerFrameRound",
            "type": "Element",
        }
    )
    lyricist_frame_padding: Optional[float] = field(
        default=None,
        metadata={
            "name": "lyricistFramePadding",
            "type": "Element",
        }
    )
    lyricist_frame_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "lyricistFrameWidth",
            "type": "Element",
        }
    )
    lyricist_frame_round: Optional[int] = field(
        default=None,
        metadata={
            "name": "lyricistFrameRound",
            "type": "Element",
        }
    )
    fingering_frame_padding: Optional[float] = field(
        default=None,
        metadata={
            "name": "fingeringFramePadding",
            "type": "Element",
        }
    )
    fingering_frame_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "fingeringFrameWidth",
            "type": "Element",
        }
    )
    fingering_frame_round: Optional[int] = field(
        default=None,
        metadata={
            "name": "fingeringFrameRound",
            "type": "Element",
        }
    )
    lh_guitar_fingering_frame_padding: Optional[float] = field(
        default=None,
        metadata={
            "name": "lhGuitarFingeringFramePadding",
            "type": "Element",
        }
    )
    lh_guitar_fingering_frame_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "lhGuitarFingeringFrameWidth",
            "type": "Element",
        }
    )
    lh_guitar_fingering_frame_round: Optional[int] = field(
        default=None,
        metadata={
            "name": "lhGuitarFingeringFrameRound",
            "type": "Element",
        }
    )
    rh_guitar_fingering_frame_padding: Optional[float] = field(
        default=None,
        metadata={
            "name": "rhGuitarFingeringFramePadding",
            "type": "Element",
        }
    )
    rh_guitar_fingering_frame_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "rhGuitarFingeringFrameWidth",
            "type": "Element",
        }
    )
    rh_guitar_fingering_frame_round: Optional[int] = field(
        default=None,
        metadata={
            "name": "rhGuitarFingeringFrameRound",
            "type": "Element",
        }
    )
    part_instrument_frame_padding: Optional[float] = field(
        default=None,
        metadata={
            "name": "partInstrumentFramePadding",
            "type": "Element",
        }
    )
    part_instrument_frame_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "partInstrumentFrameWidth",
            "type": "Element",
        }
    )
    part_instrument_frame_round: Optional[int] = field(
        default=None,
        metadata={
            "name": "partInstrumentFrameRound",
            "type": "Element",
        }
    )
    tempo_frame_padding: Optional[float] = field(
        default=None,
        metadata={
            "name": "tempoFramePadding",
            "type": "Element",
        }
    )
    tempo_frame_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "tempoFrameWidth",
            "type": "Element",
        }
    )
    tempo_frame_round: Optional[int] = field(
        default=None,
        metadata={
            "name": "tempoFrameRound",
            "type": "Element",
        }
    )
    system_frame_padding: Optional[float] = field(
        default=None,
        metadata={
            "name": "systemFramePadding",
            "type": "Element",
        }
    )
    system_frame_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "systemFrameWidth",
            "type": "Element",
        }
    )
    system_frame_round: Optional[int] = field(
        default=None,
        metadata={
            "name": "systemFrameRound",
            "type": "Element",
        }
    )
    staff_align: Optional[str] = field(
        default=None,
        metadata={
            "name": "staffAlign",
            "type": "Element",
        }
    )
    staff_pos_above: Optional[StaffPosAbove] = field(
        default=None,
        metadata={
            "name": "staffPosAbove",
            "type": "Element",
        }
    )
    staff_frame_padding: Optional[float] = field(
        default=None,
        metadata={
            "name": "staffFramePadding",
            "type": "Element",
        }
    )
    staff_frame_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "staffFrameWidth",
            "type": "Element",
        }
    )
    staff_frame_round: Optional[int] = field(
        default=None,
        metadata={
            "name": "staffFrameRound",
            "type": "Element",
        }
    )
    repeat_left_frame_padding: Optional[float] = field(
        default=None,
        metadata={
            "name": "repeatLeftFramePadding",
            "type": "Element",
        }
    )
    repeat_left_frame_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "repeatLeftFrameWidth",
            "type": "Element",
        }
    )
    repeat_left_frame_round: Optional[int] = field(
        default=None,
        metadata={
            "name": "repeatLeftFrameRound",
            "type": "Element",
        }
    )
    repeat_right_frame_padding: Optional[float] = field(
        default=None,
        metadata={
            "name": "repeatRightFramePadding",
            "type": "Element",
        }
    )
    repeat_right_frame_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "repeatRightFrameWidth",
            "type": "Element",
        }
    )
    repeat_right_frame_round: Optional[int] = field(
        default=None,
        metadata={
            "name": "repeatRightFrameRound",
            "type": "Element",
        }
    )
    spatium: Optional[float] = field(
        default=None,
        metadata={
            "name": "Spatium",
            "type": "Element",
        }
    )


@dataclass
class Text1:
    class Meta:
        name = "Text"

    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    offset: Optional[Offset] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    text: Optional[Union[int, str]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class TieSegment:
    no: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    o2: Optional[O2] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    o3: Optional[O3] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Tuplet:
    normal_notes: Optional[int] = field(
        default=None,
        metadata={
            "name": "normalNotes",
            "type": "Element",
        }
    )
    actual_notes: Optional[int] = field(
        default=None,
        metadata={
            "name": "actualNotes",
            "type": "Element",
        }
    )
    base_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "baseNote",
            "type": "Element",
        }
    )
    number: Optional[Number] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Element",
        }
    )


@dataclass
class B:
    class Meta:
        name = "b"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "font",
                    "type": Font,
                },
            ),
        }
    )


@dataclass
class Instrument2:
    class Meta:
        name = "instrument"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    family: Optional[Family] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Next:
    class Meta:
        name = "next"

    location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Prev:
    class Meta:
        name = "prev"

    location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Instrument1:
    class Meta:
        name = "Instrument"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    long_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "longName",
            "type": "Element",
        }
    )
    short_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
        }
    )
    track_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "trackName",
            "type": "Element",
        }
    )
    min_pitch_p: Optional[int] = field(
        default=None,
        metadata={
            "name": "minPitchP",
            "type": "Element",
        }
    )
    max_pitch_p: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxPitchP",
            "type": "Element",
        }
    )
    min_pitch_a: Optional[int] = field(
        default=None,
        metadata={
            "name": "minPitchA",
            "type": "Element",
        }
    )
    max_pitch_a: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxPitchA",
            "type": "Element",
        }
    )
    instrument_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "instrumentId",
            "type": "Element",
        }
    )
    clef: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    articulation: List[Articulation] = field(
        default_factory=list,
        metadata={
            "name": "Articulation",
            "type": "Element",
        }
    )
    channel: List[Channel] = field(
        default_factory=list,
        metadata={
            "name": "Channel",
            "type": "Element",
        }
    )


@dataclass
class Order:
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    customized: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    instrument: List[Instrument2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    soloists: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    section: Optional[Section] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    family: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    unsorted: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Rest:
    dots: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    offset: Optional[Offset] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    visible: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    duration_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "durationType",
            "type": "Element",
        }
    )
    duration: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    lyrics: List[Lyrics] = field(
        default_factory=list,
        metadata={
            "name": "Lyrics",
            "type": "Element",
        }
    )


@dataclass
class Slur:
    slur_segment: Optional[SlurSegment] = field(
        default=None,
        metadata={
            "name": "SlurSegment",
            "type": "Element",
        }
    )


@dataclass
class Tie:
    tie_segment: Optional[TieSegment] = field(
        default=None,
        metadata={
            "name": "TieSegment",
            "type": "Element",
        }
    )


@dataclass
class Vbox:
    class Meta:
        name = "VBox"

    height: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    box_auto_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "boxAutoSize",
            "type": "Element",
        }
    )
    text: List[Text1] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
        }
    )


@dataclass
class Volta:
    end_hook_type: Optional[int] = field(
        default=None,
        metadata={
            "name": "endHookType",
            "type": "Element",
        }
    )
    begin_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "beginText",
            "type": "Element",
        }
    )
    segment: Optional[Segment] = field(
        default=None,
        metadata={
            "name": "Segment",
            "type": "Element",
        }
    )
    endings: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Text2:
    class Meta:
        name = "text"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "font",
                    "type": Font,
                },
                {
                    "name": "sym",
                    "type": str,
                },
            ),
        }
    )


@dataclass
class Spanner:
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    slur: Optional[Union[str, Slur]] = field(
        default=None,
        metadata={
            "name": "Slur",
            "type": "Element",
        }
    )
    tie: Optional[Union[str, Tie]] = field(
        default=None,
        metadata={
            "name": "Tie",
            "type": "Element",
        }
    )
    hair_pin: Optional[HairPin] = field(
        default=None,
        metadata={
            "name": "HairPin",
            "type": "Element",
        }
    )
    volta: Optional[Volta] = field(
        default=None,
        metadata={
            "name": "Volta",
            "type": "Element",
        }
    )
    next: Optional[Next] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    prev: Optional[Prev] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Tempo:
    tempo: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    follow_text: Optional[int] = field(
        default=None,
        metadata={
            "name": "followText",
            "type": "Element",
        }
    )
    offset: Optional[Offset] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    text: Optional[Text2] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Note:
    fingering: Optional[Fingering] = field(
        default=None,
        metadata={
            "name": "Fingering",
            "type": "Element",
        }
    )
    accidental: Optional[Accidental] = field(
        default=None,
        metadata={
            "name": "Accidental",
            "type": "Element",
        }
    )
    spanner: Optional[Spanner] = field(
        default=None,
        metadata={
            "name": "Spanner",
            "type": "Element",
        }
    )
    visible: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    note_dot: Optional[NoteDot] = field(
        default=None,
        metadata={
            "name": "NoteDot",
            "type": "Element",
        }
    )
    pitch: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    tpc: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Chord:
    dots: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    offset: Optional[Offset] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    duration_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "durationType",
            "type": "Element",
        }
    )
    lyrics: List[Lyrics] = field(
        default_factory=list,
        metadata={
            "name": "Lyrics",
            "type": "Element",
        }
    )
    spanner: List[Spanner] = field(
        default_factory=list,
        metadata={
            "name": "Spanner",
            "type": "Element",
        }
    )
    stem: Optional[Stem] = field(
        default=None,
        metadata={
            "name": "Stem",
            "type": "Element",
        }
    )
    stem_direction: Optional[str] = field(
        default=None,
        metadata={
            "name": "StemDirection",
            "type": "Element",
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
        }
    )


@dataclass
class Voice:
    class Meta:
        name = "voice"

    clef: Optional[Clef] = field(
        default=None,
        metadata={
            "name": "Clef",
            "type": "Element",
        }
    )
    key_sig: Optional[KeySig] = field(
        default=None,
        metadata={
            "name": "KeySig",
            "type": "Element",
        }
    )
    time_sig: Optional[TimeSig] = field(
        default=None,
        metadata={
            "name": "TimeSig",
            "type": "Element",
        }
    )
    tuplet: List[Tuplet] = field(
        default_factory=list,
        metadata={
            "name": "Tuplet",
            "type": "Element",
        }
    )
    staff_text: Optional[StaffText] = field(
        default=None,
        metadata={
            "name": "StaffText",
            "type": "Element",
        }
    )
    tempo: Optional[Tempo] = field(
        default=None,
        metadata={
            "name": "Tempo",
            "type": "Element",
        }
    )
    rehearsal_mark: Optional[RehearsalMark] = field(
        default=None,
        metadata={
            "name": "RehearsalMark",
            "type": "Element",
        }
    )
    chord: List[Chord] = field(
        default_factory=list,
        metadata={
            "name": "Chord",
            "type": "Element",
            "sequential": True,
        }
    )
    end_tuplet: List[object] = field(
        default_factory=list,
        metadata={
            "name": "endTuplet",
            "type": "Element",
            "sequential": True,
        }
    )
    harmony: List[Harmony] = field(
        default_factory=list,
        metadata={
            "name": "Harmony",
            "type": "Element",
            "sequential": True,
        }
    )
    rest: List[Rest] = field(
        default_factory=list,
        metadata={
            "name": "Rest",
            "type": "Element",
            "sequential": True,
        }
    )
    location: List[Location] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fermata: List[Fermata] = field(
        default_factory=list,
        metadata={
            "name": "Fermata",
            "type": "Element",
            "sequential": True,
        }
    )
    bar_line: Optional[BarLine] = field(
        default=None,
        metadata={
            "name": "BarLine",
            "type": "Element",
        }
    )
    spanner: List[Spanner] = field(
        default_factory=list,
        metadata={
            "name": "Spanner",
            "type": "Element",
        }
    )
    beam: Optional[Union[str, Beam]] = field(
        default=None,
        metadata={
            "name": "Beam",
            "type": "Element",
        }
    )
    segment: Optional[Segment] = field(
        default=None,
        metadata={
            "name": "Segment",
            "type": "Element",
        }
    )


@dataclass
class Measure:
    len: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    start_repeat: Optional[object] = field(
        default=None,
        metadata={
            "name": "startRepeat",
            "type": "Element",
        }
    )
    irregular: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    end_repeat: Optional[int] = field(
        default=None,
        metadata={
            "name": "endRepeat",
            "type": "Element",
        }
    )
    layout_break: Optional[LayoutBreak] = field(
        default=None,
        metadata={
            "name": "LayoutBreak",
            "type": "Element",
        }
    )
    voice: List[Voice] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Staff:
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    vbox: Optional[Vbox] = field(
        default=None,
        metadata={
            "name": "VBox",
            "type": "Element",
        }
    )
    measure: List[Measure] = field(
        default_factory=list,
        metadata={
            "name": "Measure",
            "type": "Element",
        }
    )
    staff_type: Optional[StaffType] = field(
        default=None,
        metadata={
            "name": "StaffType",
            "type": "Element",
        }
    )
    default_clef: Optional[str] = field(
        default=None,
        metadata={
            "name": "defaultClef",
            "type": "Element",
        }
    )
    bracket: Optional[Bracket] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Part:
    staff: Optional[Staff] = field(
        default=None,
        metadata={
            "name": "Staff",
            "type": "Element",
        }
    )
    track_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "trackName",
            "type": "Element",
        }
    )
    instrument: Optional[Instrument1] = field(
        default=None,
        metadata={
            "name": "Instrument",
            "type": "Element",
        }
    )


@dataclass
class Score:
    layer_tag: Optional[LayerTag] = field(
        default=None,
        metadata={
            "name": "LayerTag",
            "type": "Element",
        }
    )
    current_layer: Optional[int] = field(
        default=None,
        metadata={
            "name": "currentLayer",
            "type": "Element",
        }
    )
    division: Optional[int] = field(
        default=None,
        metadata={
            "name": "Division",
            "type": "Element",
        }
    )
    style: Optional[Style] = field(
        default=None,
        metadata={
            "name": "Style",
            "type": "Element",
        }
    )
    show_invisible: Optional[int] = field(
        default=None,
        metadata={
            "name": "showInvisible",
            "type": "Element",
        }
    )
    show_unprintable: Optional[int] = field(
        default=None,
        metadata={
            "name": "showUnprintable",
            "type": "Element",
        }
    )
    show_frames: Optional[int] = field(
        default=None,
        metadata={
            "name": "showFrames",
            "type": "Element",
        }
    )
    show_margins: Optional[int] = field(
        default=None,
        metadata={
            "name": "showMargins",
            "type": "Element",
        }
    )
    meta_tag: List[MetaTag] = field(
        default_factory=list,
        metadata={
            "name": "metaTag",
            "type": "Element",
        }
    )
    order: Optional[Order] = field(
        default=None,
        metadata={
            "name": "Order",
            "type": "Element",
        }
    )
    part: List[Part] = field(
        default_factory=list,
        metadata={
            "name": "Part",
            "type": "Element",
        }
    )
    staff: List[Staff] = field(
        default_factory=list,
        metadata={
            "name": "Staff",
            "type": "Element",
        }
    )


@dataclass
class MuseScore:
    class Meta:
        name = "museScore"

    version: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    program_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "programVersion",
            "type": "Element",
        }
    )
    program_revision: Optional[str] = field(
        default=None,
        metadata={
            "name": "programRevision",
            "type": "Element",
        }
    )
    score: Optional[Score] = field(
        default=None,
        metadata={
            "name": "Score",
            "type": "Element",
        }
    )
