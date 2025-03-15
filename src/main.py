#!/usr/bin/env python3

from typing import List

import sys

import numpy as np

PITCHES = list(range(12))
NOTES = list(zip("ABCDEFG", [9, 11, 0, 2, 4, 5, 7]))


def main() -> None:
    assert len(sys.argv) == 4, sys.argv
    params = [int(sys.argv[1]), int(sys.argv[2]), bool(int(sys.argv[3]))]

    weights = np.empty(12, dtype="float64")
    pitches: List[int] = []
    notes = []

    rng = np.random.default_rng()
    for _ in range(params[0]):
        weights[:] = 1
        for k, pitch in enumerate(pitches[::-1]):
            weights[pitch] *= 0.05 / (k + 1)
        for pitch in pitches[-1:]:
            weights[(pitch - 7) % 12] *= 8
            weights[(pitch - 5) % 12] *= 4

        pitch = rng.choice(PITCHES, p=weights / weights.sum())

        spellings = []
        for n, p in NOTES:
            if pitch == p:
                spellings.append(n + " ")
            elif pitch == ((p - 1) % 12):
                spellings.append(n + "b")
            elif pitch == ((p + 1) % 12):
                spellings.append(n + "#")

        pitches.append(pitch)

        spelling = rng.choice(spellings)
        if params[2]:
            spelling += " " + rng.choice(["maj", "min"])
        notes.append(spelling)

    while len(notes) != 0:
        delim = "   "
        if params[2]:
            delim += " "
        print(delim.join(notes[: params[1]]).strip())
        notes = notes[params[1] :]


if __name__ == "__main__":
    main()
