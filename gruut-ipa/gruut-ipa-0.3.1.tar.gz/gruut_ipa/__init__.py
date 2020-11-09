"""Classes for dealing with phones and phonemes"""
import logging
import re
import typing
import unicodedata
from collections import defaultdict
from pathlib import Path

from .constants import (  # noqa: F401
    CONSONANTS,
    IPA,
    SCHWAS,
    VOWELS,
    BreakType,
    Consonant,
    Dipthong,
    Schwa,
    Stress,
    Vowel,
    VowelHeight,
    VowelPlacement,
)
from .espeak import espeak_to_ipa, ipa_to_espeak  # noqa: F401
from .sampa import ipa_to_sampa, sampa_to_ipa  # noqa: F401

# -----------------------------------------------------------------------------

_LOGGER = logging.getLogger("gruut_ipa")

_DIR = Path(__file__).parent

_DATA_DIR = _DIR / "data"

# -----------------------------------------------------------------------------


class Phone:
    """Single IPA phone with diacritics and suprasegmentals"""

    def __init__(
        self,
        letters: str,
        stress: Stress = Stress.NONE,
        is_long: bool = False,
        is_nasal: bool = False,
        is_raised: bool = False,
        diacritics: typing.Optional[typing.Set[str]] = None,
        suprasegmentals: typing.Optional[typing.Set[str]] = None,
        tone: str = "",
    ):
        self.letters: str = unicodedata.normalize("NFC", letters)
        self.stress: Stress = stress
        self.is_long: bool = is_long
        self.is_nasal: bool = is_nasal
        self.is_raised: bool = is_raised
        self.tone: str = tone

        self.diacritics: typing.Set[str] = diacritics or set()
        self.suprasegmentals: typing.Set[str] = suprasegmentals or set()

        # Decompose suprasegmentals and diacritics
        if self.stress == Stress.PRIMARY:
            self.suprasegmentals.add(IPA.STRESS_PRIMARY)
        elif self.stress == Stress.SECONDARY:
            self.suprasegmentals.add(IPA.STRESS_SECONDARY)

        if self.is_long:
            self.suprasegmentals.add(IPA.LONG)

        if self.is_nasal:
            self.diacritics.add(IPA.NASAL)

        if self.is_raised:
            self.diacritics.add(IPA.RAISED)

        self._text: str = ""

        self.vowel: typing.Optional[Vowel] = VOWELS.get(self.letters)
        self.consonant: typing.Optional[Consonant] = CONSONANTS.get(self.letters)
        self.schwa: typing.Optional[Schwa] = SCHWAS.get(self.letters)

    @property
    def text(self) -> str:
        """Get textual representation of phone (NFC normalized)"""
        if self._text:
            return self._text

        # Pre-letter suprasegmentals
        if self.stress == Stress.PRIMARY:
            self._text += IPA.STRESS_PRIMARY
        elif self.stress == Stress.SECONDARY:
            self._text += IPA.STRESS_SECONDARY

        # Letters
        self._text += self.letters

        # Diacritics
        for diacritic in self.diacritics:
            self._text += diacritic

        # Tone
        if self.tone:
            self._text += self.tone

        # Post-letter suprasegmentals
        if self.is_long:
            self._text += IPA.LONG

        # Re-normalize and combine
        self._text = unicodedata.normalize("NFC", self._text)

        return self._text

    @property
    def is_vowel(self) -> bool:
        """True if phone is a vowel"""
        return self.vowel is not None

    @property
    def is_consonant(self) -> bool:
        """True if phone is a consonant"""
        return self.consonant is not None

    @property
    def is_schwa(self) -> bool:
        """True if phone is a schwa"""
        return self.schwa is not None

    def __repr__(self) -> str:
        return self.text

    @staticmethod
    def from_string(phone_str: str) -> "Phone":
        """Parse phone from string"""
        # Decompose into base and combining characters
        codepoints = unicodedata.normalize("NFD", phone_str)
        kwargs: typing.Dict[str, typing.Any] = {
            "letters": "",
            "diacritics": set(),
            "tone": "",
        }

        in_tone = False

        for c in codepoints:
            # Check for stress
            if c == IPA.STRESS_PRIMARY:
                kwargs["stress"] = Stress.PRIMARY
            elif c == IPA.STRESS_SECONDARY:
                kwargs["stress"] = Stress.SECONDARY
            elif in_tone and (c in {IPA.TONE_GLOTTALIZED, IPA.TONE_SHORT}):
                # Interpret as part of tone
                kwargs["tone"] += c
            elif IPA.is_long(c):
                # Check for elongation
                kwargs["is_long"] = True
            elif IPA.is_nasal(c):
                # Check for nasalation
                kwargs["is_nasal"] = True
            elif IPA.is_raised(c):
                # Check for raised articulation
                kwargs["is_raised"] = True
            elif IPA.is_bracket(c) or IPA.is_break(c):
                # Skip brackets/syllable breaks
                pass
            elif IPA.is_tie(c):
                # Keep ties in letters
                kwargs["letters"] += c
            elif IPA.is_tone(c):
                # Tone numbers/letters
                kwargs["tone"] += c
                in_tone = True
            elif unicodedata.combining(c) > 0:
                # Stow some diacritics that we don't do anything with
                kwargs["diacritics"].add(c)
            else:
                # Include all other characters in letters
                kwargs["letters"] += c

        return Phone(**kwargs)


class Break:
    """IPA break/boundary"""

    def __init__(self, break_type: BreakType):
        self.type = break_type

        if self.type == BreakType.MINOR:
            self.text = IPA.BREAK_MINOR
        elif self.type == BreakType.MAJOR:
            self.text = IPA.BREAK_MAJOR
        elif self.type == BreakType.WORD:
            self.text = IPA.BREAK_WORD
        else:
            raise ValueError(f"Unrecognized break type: {type}")

    def __repr__(self) -> str:
        return self.text

    @staticmethod
    def from_string(break_str: str) -> "Break":
        """Parse break from string"""
        if break_str == IPA.BREAK_MINOR:
            break_type = BreakType.MINOR
        elif break_str == IPA.BREAK_MAJOR:
            break_type = BreakType.MAJOR
        elif break_str == IPA.BREAK_WORD:
            break_type = BreakType.WORD
        else:
            raise ValueError(f"Unrecognized break type: {break_str}")

        return Break(break_type)


class Intonation:
    """IPA rising/falling intonation"""

    def __init__(self, rising: bool):
        self.rising = rising

        if self.rising:
            self.text = IPA.INTONATION_RISING
        else:
            self.text = IPA.INTONATION_FALLING

    def __repr__(self) -> str:
        return self.text

    @staticmethod
    def from_string(intonation_str: str) -> "Intonation":
        """Parse intonation from string"""
        if intonation_str == IPA.INTONATION_RISING:
            rising = True
        elif intonation_str == IPA.INTONATION_FALLING:
            rising = False
        else:
            raise ValueError(f"Unrecognized intonation type: {intonation_str}")

        return Intonation(rising)


# -----------------------------------------------------------------------------


class Pronunciation:
    """Collection of phones and breaks for some unit of text (word, sentence, etc.)"""

    def __init__(
        self, phones_and_others: typing.List[typing.Union[Phone, Break, Intonation]]
    ):
        self.phones_and_others = phones_and_others

        self.phones: typing.List[Phone] = []
        self.breaks: typing.List[Break] = []
        self.intonations: typing.List[Intonation] = []

        # Decompose into phones, breaks, and intonations
        for p in self.phones_and_others:
            if isinstance(p, Phone):
                self.phones.append(p)
            elif isinstance(p, Break):
                self.breaks.append(p)
            elif isinstance(p, Intonation):
                self.intonations.append(p)

        self._text = ""

    @property
    def text(self) -> str:
        """Get text representation of pronunciation (NFC normalized)"""
        if not self._text:
            self._text = "".join(p.text for p in self.phones_and_others)

        return self._text

    def __repr__(self) -> str:
        return self.text

    def __iter__(self):
        return iter(self.phones_and_others)

    def __getitem__(self, idx):
        return self.phones_and_others[idx]

    @staticmethod
    def from_string(
        pron_str: str, keep_stress: bool = True, drop_tones: bool = False
    ) -> "Pronunciation":
        """Split an IPA pronunciation into phones.

        Stress markers bind to the next non-combining codepoint (e.g., ˈa).
        Elongation markers bind to the previous non-combining codepoint (e.g., aː).
        Ties join two non-combining sequences (e.g. t͡ʃ).

        Whitespace and brackets are skipped.

        Returns list of phones.
        """
        clusters = []
        cluster = ""
        tone = ""
        in_tone = False
        skip_next_cluster = False

        codepoints = unicodedata.normalize("NFD", pron_str)

        for codepoint in codepoints:
            new_cluster = False

            if (
                codepoint.isspace()
                or IPA.is_bracket(codepoint)
                or (codepoint in {IPA.BREAK_SYLLABLE})
            ):
                # Skip whitespace, brackets, and syllable breaks
                continue

            if IPA.is_break(codepoint) or IPA.is_intonation(codepoint):
                # Keep minor/major/word breaks and intonation markers
                new_cluster = True

            if IPA.is_stress(codepoint):
                if keep_stress:
                    new_cluster = True
                    skip_next_cluster = True
                else:
                    # Drop stress
                    continue
            elif in_tone and (codepoint in {IPA.TONE_GLOTTALIZED, IPA.TONE_SHORT}):
                # Interpret as part of tone
                if not drop_tones:
                    tone += codepoint

                continue
            elif IPA.is_long(codepoint):
                # Add to current cluster
                pass
            elif IPA.is_tie(codepoint):
                # Add next non-combining to current cluster
                skip_next_cluster = True
            elif IPA.is_tone(codepoint):
                # Add to end of current cluster
                if not drop_tones:
                    tone += codepoint

                in_tone = True
                continue
            elif unicodedata.combining(codepoint) == 0:
                # Non-combining character
                if skip_next_cluster:
                    # Add to current cluster
                    skip_next_cluster = False
                else:
                    # Start a new cluster
                    new_cluster = True

            if new_cluster and cluster:
                clusters.append(cluster + tone)
                cluster = ""
                tone = ""

            cluster += codepoint

        if cluster:
            clusters.append(cluster + tone)

        phones_and_others: typing.List[typing.Union[Phone, Break, Intonation]] = []
        for cluster in clusters:
            if IPA.is_break(cluster):
                phones_and_others.append(Break.from_string(cluster))
            elif IPA.is_intonation(cluster):
                phones_and_others.append(Intonation.from_string(cluster))
            else:
                phones_and_others.append(Phone.from_string(cluster))

        return Pronunciation(phones_and_others)


# -----------------------------------------------------------------------------


class Phoneme:
    """Phoneme composed of international phonetic alphabet symbols"""

    def __init__(self, text: str, example: str = "", unknown: bool = False):
        self._text = ""
        self._text_compare = ""
        self.example = example
        self.unknown = unknown

        self.stress: Stress = Stress.NONE
        self.elongated: bool = False
        self.nasalated: bool = False
        self.raised: bool = False
        self._extra_combining: typing.List[str] = []

        # Decompose into base and combining characters
        codepoints = unicodedata.normalize("NFD", text)
        self.letters = ""
        self.tone = ""
        in_tone = False

        for c in codepoints:
            # Check for stress
            if c == IPA.STRESS_PRIMARY:
                self.stress = Stress.PRIMARY
            elif c == IPA.STRESS_SECONDARY:
                self.stress = Stress.SECONDARY
            elif in_tone and (c in {IPA.TONE_GLOTTALIZED, IPA.TONE_SHORT}):
                # Interpret as part of tone
                self.tone += c
            elif IPA.is_long(c):
                # Check for elongation
                self.elongated = True
            elif IPA.is_nasal(c):
                # Check for nasalation
                self.nasalated = True
            elif IPA.is_raised(c):
                # Check for raised articulation
                self.raised = True
            elif IPA.is_bracket(c) or IPA.is_break(c):
                # Skip brackets/syllable breaks
                pass
            elif IPA.is_tone(c):
                # Keep tone separate
                self.tone += c
                in_tone = True
            elif c in {IPA.SYLLABIC, IPA.NON_SYLLABIC, IPA.EXTRA_SHORT}:
                # Stow some diacritics that we don't do anything with
                self._extra_combining.append(c)
            else:
                # Include all other characters in base
                self.letters += c

        # Re-normalize and combine letters
        self.letters = unicodedata.normalize("NFC", self.letters)
        self.letters_graphemes = IPA.graphemes(self.letters)

        # Categorize
        self.vowel: typing.Optional[Vowel] = VOWELS.get(self.letters)
        self.consonant: typing.Optional[Consonant] = CONSONANTS.get(self.letters)
        self.schwa: typing.Optional[Schwa] = SCHWAS.get(self.letters)
        self.dipthong: typing.Optional[Dipthong] = None

        if (
            (not self.vowel)
            and (not self.consonant)
            and (not self.schwa)
            and (len(self.letters) == 2)
        ):
            # Check if dipthong (two vowels)
            vowel1 = VOWELS.get(self.letters[0])
            vowel2 = VOWELS.get(self.letters[1])
            if vowel1 and vowel2:
                self.dipthong = Dipthong(vowel1, vowel2)

    @property
    def text(self) -> str:
        """Return letters with stress and elongation (NFC normalized)"""
        if self._text:
            return self._text

        self._text = self.letters
        if self.stress == Stress.PRIMARY:
            self._text = IPA.STRESS_PRIMARY + self._text
        elif self.stress == Stress.SECONDARY:
            self._text = IPA.STRESS_SECONDARY + self._text

        if self.nasalated:
            self._text += IPA.NASAL

        if self.raised:
            self._text += IPA.RAISED

        for c in self._extra_combining:
            self._text += c

        if self.tone:
            self._text += self.tone

        if self.elongated:
            self._text += IPA.LONG

        # Re-normalize and combine
        self._text = unicodedata.normalize("NFC", self._text)

        return self._text

    @property
    def text_compare(self) -> str:
        """Return letters and elongation with no stress/tones (NFC normalized)"""
        if self._text_compare:
            return self._text_compare

        self._text_compare = self.letters

        if self.nasalated:
            self._text_compare += IPA.NASAL

        if self.raised:
            self._text_compare += IPA.RAISED

        for c in self._extra_combining:
            self._text_compare += c

        if self.elongated:
            self._text_compare += IPA.LONG

        # Re-normalize and combine
        self._text_compare = unicodedata.normalize("NFC", self._text_compare)

        return self._text_compare

    def copy(self) -> "Phoneme":
        """Create a copy of this phonemes"""
        return Phoneme(text=self.text, example=self.example, unknown=self.unknown)

    def __repr__(self) -> str:
        """Return symbol with stress and elongation."""
        return self.text

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return properties of phoneme as a dict"""
        type_name = "Phoneme"
        props: typing.Dict[str, typing.Any] = {
            "text": repr(self),
            "letters": self.letters,
            "tone": self.tone,
        }

        if self.unknown:
            props["unknown"] = True

        if self.example:
            props["example"] = self.example

        props["stress"] = self.stress.value

        if self.vowel:
            type_name = "Vowel"
            props["height"] = self.vowel.height.value
            props["placement"] = self.vowel.placement.value
            props["rounded"] = self.vowel.rounded
        elif self.consonant:
            type_name = "Consonant"
            props["type"] = self.consonant.type.value
            props["place"] = self.consonant.place.value
            props["voiced"] = self.consonant.voiced
        elif self.dipthong:
            type_name = "Dipthong"
        elif self.schwa:
            type_name = "Schwa"
            props["r_coloured"] = self.schwa.r_coloured

        props["type"] = type_name

        props["nasalated"] = self.nasalated
        props["raised"] = self.raised
        props["elongated"] = self.elongated

        return props

    def to_string(self) -> str:
        """Return descriptive string of phoneme"""
        props = self.to_dict()
        type_name = props.get("type", "Phoneme")

        prop_strs = [f"{k}={v}" for k, v in props.items()]

        return f"{type_name}(" + ", ".join(prop_strs) + ")"


# -----------------------------------------------------------------------------


class Phonemes:
    """Set of phonemes and allophones for a language"""

    COMMENT_STR = "#"

    def __init__(self, phonemes=None, ipa_map=None):
        self.phonemes = phonemes or []
        self.ipa_map = ipa_map or {}

        # Regex for replacing IPA
        self._ipa_map_regex = None

        # Phonemes sorted by descreasing length
        self._phonemes_sorted = None

        self.update()

    def __iter__(self):
        return iter(self.phonemes)

    def __len__(self):
        return len(self.phonemes)

    def __getitem__(self, key):
        return self.phonemes[key]

    @staticmethod
    def from_language(language: str) -> "Phonemes":
        """Load phonemes for a given language"""
        phonemes_path = _DATA_DIR / language / "phonemes.txt"
        with open(phonemes_path, "r") as phonemes_file:
            return Phonemes.from_text(phonemes_file)

    @staticmethod
    def from_text(text_file) -> "Phonemes":
        """Load text file with phonemes, examples, and allophones"""
        lang = Phonemes()

        for line in text_file:
            # Remove comments
            line, *_ = line.split(Phonemes.COMMENT_STR, maxsplit=1)
            line = line.strip()
            if line:
                # phoneme [example] [allophone] [allophone]...
                parts = line.split()
                phoneme_ipa = parts[0]
                example = ""

                if len(parts) > 1:
                    example = parts[1]

                if len(parts) > 2:
                    # Map allophone back to phoneme
                    for homophone in parts[2:]:
                        lang.ipa_map[homophone] = phoneme_ipa

                lang.phonemes.append(Phoneme(text=phoneme_ipa, example=example))

        lang.update()

        return lang

    def update(self):
        """Call after modifying phonemes or IPA map to re-sort"""
        # Create single regex that will be used to replace IPA.
        # The final regex is of the form (AAA|BB|C) where each case is in
        # decreasing length order.
        #
        # If the replacement is >= to the length of the text to match, then the
        # replacement is straightforward.
        #
        # If it is smaller *and* a substring, however, we need to be careful.
        # For example, replacing "e" with "eɪ" in the string "beɪ" will produce
        # "beeɪ" when we want it to be "beɪ".
        #
        # So the substring case becomes "e(?!ɪ)" which uses a negative lookahead
        # to avoid the problem.
        cases = []
        for match_text, replace_text in sorted(
            self.ipa_map.items(), key=lambda kv: len(kv[0]), reverse=True
        ):
            num_extra = len(replace_text) - len(match_text)
            if (num_extra > 0) and replace_text.startswith(match_text):
                cases.append(
                    "{}(?!{})".format(
                        re.escape(match_text[:num_extra]),
                        re.escape(replace_text[num_extra:]),
                    )
                )
            else:
                cases.append(re.escape(match_text))

        ipa_map_regex_str = "({})".format("|".join(cases))
        self._ipa_map_regex = re.compile(ipa_map_regex_str)

        # Split phonemes and sort by reverse length
        split_phonemes = [
            ([pb.text for pb in Pronunciation.from_string(p.text)], p)
            for p in self.phonemes
        ]

        self._phonemes_sorted = sorted(
            split_phonemes, key=lambda kp: len(kp[0]), reverse=True
        )

    def split(
        self,
        pron_str: typing.Union[str, Pronunciation],
        keep_stress: bool = False,
        drop_tones: bool = False,
    ) -> typing.List[Phoneme]:
        """Split an IPA pronunciation into phonemes"""
        if not self._ipa_map_regex:
            self.update()

        word_phonemes: typing.List[Phoneme] = []

        if self.ipa_map:
            if isinstance(pron_str, Pronunciation):
                pron_str = "".join(p.text for p in pron_str)

            def handle_replace(match):
                text = match.group(1)
                return self.ipa_map.get(text, text)

            pron_str = self._ipa_map_regex.sub(handle_replace, pron_str)

        if isinstance(pron_str, Pronunciation):
            # Use supplied pronunication
            pron = pron_str
        else:
            # Split string into pronunciation
            pron = Pronunciation.from_string(
                pron_str, keep_stress=keep_stress, drop_tones=drop_tones
            )

        # Get text for IPA phones
        ipas = [pb.text for pb in pron]

        # Keep stress and tones separate to make phoneme comparisons easier
        ipa_stress: typing.Dict[int, str] = defaultdict(str)
        ipa_tones: typing.Dict[int, str] = defaultdict(str)
        in_tone = False
        for ipa_idx, ipa in enumerate(ipas):
            if ipa:
                keep_ipa = ""
                for codepoint in ipa:
                    if IPA.is_stress(codepoint):
                        if keep_stress:
                            ipa_stress[ipa_idx] += codepoint
                    elif in_tone and (
                        codepoint in {IPA.TONE_GLOTTALIZED, IPA.TONE_SHORT}
                    ):
                        # Interpret as part of time
                        if not drop_tones:
                            ipa_tones[ipa_idx] += codepoint
                    elif IPA.is_tone(codepoint):
                        if not drop_tones:
                            ipa_tones[ipa_idx] += codepoint

                        in_tone = True
                    else:
                        keep_ipa += codepoint

                ipas[ipa_idx] = keep_ipa

        num_ipas: int = len(ipas)

        # ---------------------------------------------------------------------

        # pylint: disable=consider-using-enumerate
        for ipa_idx in range(len(ipas)):
            ipa = ipas[ipa_idx]
            if ipa is None:
                # Skip replaced piece
                continue

            phoneme_match = False
            for phoneme_ipas, phoneme in self._phonemes_sorted:
                if ipa_idx <= (num_ipas - len(phoneme_ipas)):
                    phoneme_match = True
                    phoneme_stress = ""
                    phoneme_tones = ""

                    # Look forward into sequence
                    for phoneme_idx in range(len(phoneme_ipas)):
                        phoneme_stress += ipa_stress[ipa_idx + phoneme_idx]
                        phoneme_tones += ipa_tones[ipa_idx + phoneme_idx]

                        if phoneme_ipas[phoneme_idx] != ipas[ipa_idx + phoneme_idx]:
                            phoneme_match = False
                            break

                    if phoneme_match:
                        # Successful match
                        if phoneme_stress or phoneme_tones:
                            # Create a copy of the phoneme with applied stress/tones
                            phoneme = Phoneme(
                                text=(phoneme_stress + phoneme.text + phoneme_tones),
                                example=phoneme.example,
                            )

                        word_phonemes.append(phoneme)

                        # Patch ipas to skip replaced pieces
                        for phoneme_idx in range(1, len(phoneme_ipas)):
                            ipas[ipa_idx + phoneme_idx] = None

                        break

            if not phoneme_match:
                # Add unknown phoneme
                word_phonemes.append(Phoneme(text=ipa, unknown=True))

        return word_phonemes
