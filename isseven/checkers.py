# -*- coding: utf-8 -*-
import datetime
import re
from typing import Tuple, Collection

from .models import IsSevenResult, yep, nope


def is_numeric_seven(possible_seven: str) -> IsSevenResult:
    try:
        if float(possible_seven) == 7:
            return yep("According to python this casts to 7")
    except:
        pass

    return nope("This doesn't seem to be 7 or 7.0")


sevens: Collection[Tuple[str, str]] = [
    ("seven", "That was seven in english"),
    ("sju", "That was seven in swedish"),
    ("sept", "That was seven in french"),
    ("sieben", "That was seven in german"),
    ("7️⃣", "That was an emoji seven"),
]


def is_the_word_seven(possible_seven: str) -> IsSevenResult:
    tidied_possible_seven = possible_seven.strip().lower()
    for (actual_seven, description) in sevens:
        if actual_seven == tidied_possible_seven:
            return yep(description)
    return nope("Not the word seven")


def is_roman_numeral_for_seven(possible_seven: str) -> IsSevenResult:
    tidied_possible_seven = possible_seven.strip().lower()
    if tidied_possible_seven == "vii":
        return yep("Roman numeral for 7!")
    return nope("Minimē")


repeated_seven_times = re.compile(r"^(.)\1{6}$")


def is_seven_of_something_repeated(possible_seven: str) -> IsSevenResult:
    match = repeated_seven_times.match(possible_seven)
    if match:
        return yep(f"It was {match[1]} repeated 7 times")
    return nope("sorry")


seven_am = datetime.time(hour=7)
seven_pm = datetime.time(hour=19)


def is_the_time_seven(possible_seven: str) -> IsSevenResult:
    time = _attempt_to_parse_out_time(possible_seven)
    if time == seven_am:
        return yep("That's 7 am")
    if time == seven_pm:
        return yep("That's 7 pm")
    return nope("Not 0700 or 1900")


def _attempt_to_parse_out_time(possible_seven):
    try:
        return datetime.time.fromisoformat(possible_seven.strip())
    except:
        pass
    try:
        full_datetime = datetime.datetime.fromisoformat(possible_seven.strip())
        return full_datetime.time()
    except:
        pass
    return None


def _clean_reference(raw: str):
    return (
        raw.strip().lower().replace(" ", "").replace("-", "").replace("thenumberof", "")
    )


references = [
    _clean_reference(reference)
    for reference in [
        "dwarves in snow white",
        "rings for the dwarf-lords in their halls of stone",
        "rings for the dwarf-lords",
        "deadly sins",
    ]
]


def is_it_a_pop_culture_reference(possible_seven: str) -> IsSevenResult:
    cleaned = _clean_reference(possible_seven)
    if cleaned in references:
        return yep("I know that reference")
    return nope("I don't know that reference for 7")


def is_it_maths_with_the_answer_seven(possible_seven: str) -> IsSevenResult:
    cleaned_statement = possible_seven.replace(" ", "")
    try:
        if "+" in cleaned_statement:
            a, b = cleaned_statement.split("+")
            if float(a) + float(b) == 7.0:
                return yep("That adds up to seven")
        if "-" in cleaned_statement:
            a, b = cleaned_statement.split("-")
            if float(a) - float(b) == 7.0:
                return yep("The answer of that subtraction is seven")
    except:
        pass
    return nope("That doesn't seem to work out as 7")
