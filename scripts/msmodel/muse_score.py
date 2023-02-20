from dataclasses import dataclass, field
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate


@dataclass
class Channel:
    synti: Optional[str] = field(
        default=None,
        metadata={
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
class Note:
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
    spatium: Optional[float] = field(
        default=None,
        metadata={
            "name": "Spatium",
            "type": "Element",
        }
    )


@dataclass
class Text:
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
class Chord:
    duration_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "durationType",
            "type": "Element",
        }
    )
    note: Optional[Note] = field(
        default=None,
        metadata={
            "name": "Note",
            "type": "Element",
        }
    )


@dataclass
class Instrument:
    track_name: Optional[object] = field(
        default=None,
        metadata={
            "name": "trackName",
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
class Vbox:
    class Meta:
        name = "VBox"

    height: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    text: List[Text] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
        }
    )


@dataclass
class Voice:
    class Meta:
        name = "voice"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "KeySig",
                    "type": KeySig,
                },
                {
                    "name": "Chord",
                    "type": Chord,
                },
                {
                    "name": "TimeSig",
                    "type": TimeSig,
                },
                {
                    "name": "Rest",
                    "type": Rest,
                }
            )
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
    value: str = field(
        default=""
    )
    staff_type: Optional[StaffType] = field(
        default=None,
        metadata={
            "name": "StaffType",
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
    track_name: Optional[object] = field(
        default=None,
        metadata={
            "name": "trackName",
            "type": "Element",
        }
    )
    instrument: Optional[Instrument] = field(
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
    part: Optional[Part] = field(
        default=None,
        metadata={
            "name": "Part",
            "type": "Element",
        }
    )
    staff: Optional[Staff] = field(
        default=None,
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
