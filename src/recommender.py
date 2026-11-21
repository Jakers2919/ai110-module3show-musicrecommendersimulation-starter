
import csv
from dataclasses import dataclass
from typing import List, Dict, Tuple


@dataclass
class Song:
    """Stores the attributes of a song."""
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """Stores a user's music preferences."""
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


def load_songs(csv_path: str) -> List[Dict]:
    """Loads songs from a CSV file and converts numeric fields."""
    songs = []

    with open(csv_path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["id"] = int(row["id"])

            for field in (
                "energy",
                "tempo_bpm",
                "valence",
                "danceability",
                "acousticness",
            ):
                row[field] = float(row[field])

            songs.append(row)

    return songs


def score_song(
    user_prefs: Dict, song: Dict
) -> Tuple[float, List[str]]:
    """Calculates a song's score and explains each scoring factor."""
    score = 0.0
    reasons = []

    favorite_genre = str(
        user_prefs.get("favorite_genre", "")
    ).strip().lower()

    favorite_mood = str(
        user_prefs.get("favorite_mood", "")
    ).strip().lower()

    target_energy = max(
        0.0,
        min(1.0, float(user_prefs.get("target_energy", 0.5))),
    )

    song_genre = str(song["genre"]).strip().lower()
    song_mood = str(song["mood"]).strip().lower()
    song_energy = float(song["energy"])

    # Genre is worth 2 points.
    if favorite_genre and song_genre == favorite_genre:
        score += 2.0
        reasons.append("Genre match (+2.00)")

    # Mood is worth 1 point.
    if favorite_mood and song_mood == favorite_mood:
        score += 1.0
        reasons.append("Mood match (+1.00)")

    # Songs closer to the target energy receive more points.
    energy_points = max(
        0.0,
        1.0 - abs(song_energy - target_energy),
    )
    score += energy_points

    reasons.append(
        f"Energy similarity (+{energy_points:.2f})"
    )

    # Optional acoustic preference.
    if user_prefs.get("likes_acoustic", False):
        acoustic_points = (
            max(0.0, min(1.0, float(song["acousticness"])))
            * 0.5
        )
        score += acoustic_points
        reasons.append(
            f"Acoustic preference (+{acoustic_points:.2f})"
        )

    return round(score, 4), reasons


def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5,
) -> List[Tuple[Dict, float, str]]:
    """Ranks songs by score and returns the top recommendations."""
    ranked_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)

        explanation = "; ".join(reasons)
        ranked_songs.append((song, score, explanation))

    ranked_songs.sort(
        key=lambda result: (-result[1], result[0]["id"])
    )

    return ranked_songs[:max(0, k)]


class Recommender:
    """Provides object-oriented music recommendations."""

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(
        self, user: UserProfile, k: int = 5
    ) -> List[Song]:
        """Returns the highest-scoring songs for a user."""
        ranked = sorted(
            self.songs,
            key=lambda song: (
                -score_song(
                    vars(user), vars(song)
                )[0],
                song.id,
            ),
        )

        return ranked[:max(0, k)]

    def explain_recommendation(
        self, user: UserProfile, song: Song
    ) -> str:
        """Explains why a particular song was recommended."""
        score, reasons = score_song(
            vars(user), vars(song)
        )

        return (
            f"{song.title} scored {score:.2f}: "
            + "; ".join(reasons)
        )
