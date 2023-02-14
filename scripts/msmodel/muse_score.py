from dataclasses import dataclass, field
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate


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
class Rest:
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
class Style:
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
    text: Optional[str] = field(
        default=None,
        metadata={
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
class MetaTag:
    class Meta:
        name = "metaTag"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    value: Union[str, XmlDate] = field(
        default=""
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
                    "name": "sym",
                    "type": str,
                },
            ),
        }
    )


@dataclass
class Unsorted:
    class Meta:
        name = "unsorted"

    group: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Channel:
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


@dataclass
class Tempo:
    tempo: Optional[int] = field(
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
    text: Optional[Text2] = field(
        default=None,
        metadata={
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
    text: List[Text1] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
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
    family: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    unsorted: Optional[Unsorted] = field(
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
    articulation: List[Articulation] = field(
        default_factory=list,
        metadata={
            "name": "Articulation",
            "type": "Element",
        }
    )
    channel: Optional[Channel] = field(
        default=None,
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
    instrument: Optional[Instrument2] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    section: List[Section] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    family: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    soloists: Optional[object] = field(
        default=None,
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
class Voice:
    class Meta:
        name = "voice"

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
    tempo: Optional[Tempo] = field(
        default=None,
        metadata={
            "name": "Tempo",
            "type": "Element",
        }
    )
    rest: List[Rest] = field(
        default_factory=list,
        metadata={
            "name": "Rest",
            "type": "Element",
        }
    )


@dataclass
class Measure:
    voice: Optional[Voice] = field(
        default=None,
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
    staff_type: Optional[StaffType] = field(
        default=None,
        metadata={
            "name": "StaffType",
            "type": "Element",
        }
    )
    bracket: Optional[Bracket] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    bar_line_span: Optional[int] = field(
        default=None,
        metadata={
            "name": "barLineSpan",
            "type": "Element",
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
    default_clef: Optional[str] = field(
        default=None,
        metadata={
            "name": "defaultClef",
            "type": "Element",
        }
    )


@dataclass
class Part:
    staff: List[Staff] = field(
        default_factory=list,
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
    part: Optional[Part] = field(
        default=None,
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
