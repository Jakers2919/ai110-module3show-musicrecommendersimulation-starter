
"""
Music Recommender Simulation

Tests different music preferences and displays the top five
recommendations for each user profile.
"""

from pathlib import Path

try:
    from .recommender import load_songs, recommend_songs
except ImportError:
    from recommender import load_songs, recommend_songs


def display_recommendations(profile_name, user_prefs, songs):
    """Displays the five highest-scoring songs for a user."""
    print("\n" + "=" * 55)
    print(f"USER PROFILE: {profile_name}")
    print("=" * 55)

    print(f"Favorite genre: {user_prefs['favorite_genre']}")
    print(f"Favorite mood: {user_prefs['favorite_mood']}")
    print(f"Target energy: {user_prefs['target_energy']}")
    print(f"Likes acoustic: {user_prefs['likes_acoustic']}")

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTOP 5 RECOMMENDATIONS")

    for position, (song, score, explanation) in enumerate(
        recommendations, start=1
    ):
        print(f"\n{position}. {song['title']} - {song['artist']}")
        print(f"   Genre: {song['genre']}")
        print(f"   Mood: {song['mood']}")
        print(f"   Energy: {song['energy']}")
        print(f"   Score: {score:.2f}")
        print(f"   Why: {explanation}")


def main():
    """Loads songs and evaluates three different music profiles."""
    project_folder = Path(__file__).resolve().parent.parent
    csv_path = project_folder / "data" / "songs.csv"

    songs = load_songs(str(csv_path))

    print("=" * 55)
    print("VIBEMATCH 1.0 - MUSIC RECOMMENDER")
    print("=" * 55)
    print(f"\nTotal songs loaded: {len(songs)}")

    profiles = {
        "High-Energy Pop": {
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.90,
            "likes_acoustic": False,
        },
        "Chill Lo-Fi": {
            "favorite_genre": "lofi",
            "favorite_mood": "chill",
            "target_energy": 0.35,
            "likes_acoustic": True,
        },
        "Intense Rock": {
            "favorite_genre": "rock",
            "favorite_mood": "intense",
            "target_energy": 0.95,
            "likes_acoustic": False,
        },
    }

    for profile_name, user_prefs in profiles.items():
        display_recommendations(profile_name, user_prefs, songs)

    print("\n" + "=" * 55)
    print("EVALUATION COMPLETE")
    print("=" * 55)


if __name__ == "__main__":
    main()
