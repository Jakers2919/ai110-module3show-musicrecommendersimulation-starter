
# 🎵 VibeMatch 1.0 - Music Recommender Simulation

## Project Summary

VibeMatch is a music recommendation simulation I built using Python. It recommends songs by comparing a user's favorite genre, mood, and energy level with information stored in a CSV file.

The program gives each song a score, ranks the songs, and displays the five best matches with explanations.

I also tested different music preferences and experimented with changing the scoring weights to see how the recommendations changed.

## How The System Works

Real music platforms like Spotify use information such as listening history, likes, skips, and playlists to predict what users might enjoy.

Two common recommendation approaches are collaborative filtering, which uses patterns from similar listeners, and content-based filtering, which uses characteristics of songs.

VibeMatch is a simplified content-based recommender. It uses fixed scoring rules instead of machine learning.

### Song Features

The dataset contains these features:

- ID
- Title
- Artist
- Genre
- Mood
- Energy
- Tempo (BPM)
- Valence
- Danceability
- Acousticness

The current scoring system uses genre, mood, energy, and optionally acousticness.

### User Profile

Each user profile includes:

- `favorite_genre`
- `favorite_mood`
- `target_energy`
- `likes_acoustic`

### Scoring Algorithm

Each song receives points based on how well it matches the user.

- Genre match: +2.0 points
- Mood match: +1.0 point
- Energy similarity: up to +1.0 point
- Acoustic preference: up to +0.5 points if enabled

Energy similarity is calculated using:

`1.0 - abs(song_energy - target_energy)`

The acoustic bonus is calculated using:

`0.5 * acousticness`

The program scores every song, sorts them from highest to lowest, and returns the top five.

It also displays an explanation showing how each song earned its score.

### Data Flow

User Preferences → Load CSV → Score Songs → Sort Scores → Recommend Top 5

One possible bias is that genre receives more points than mood or energy. This could cause the recommender to favor songs from the correct genre even when other songs have a better energy match.

## Getting Started

### Setup

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Run the program:

```bash
python3 -m src.main
```

### Running Tests

Run the automated tests:

```bash
python3 -m pytest -v
```

The starter tests passed during development:

```text
test_recommend_returns_songs_sorted_by_score PASSED
test_explain_recommendation_returns_non_empty_string PASSED

2 passed in 0.03s
```

## Sample Recommendation Output

The program was tested with three different user profiles.

### Profile 1: High-Energy Pop

Preferences:
- Genre: pop
- Mood: happy
- Energy: 0.90
- Acoustic: False

Actual recommendation output:

```text
1. Sunrise City - Neon Echo
   Score: 3.92
   Why: Genre match (+2.00); Mood match (+1.00); Energy similarity (+0.92)

2. Gym Hero - Max Pulse
   Score: 2.97
   Why: Genre match (+2.00); Energy similarity (+0.97)

3. Weekend Feeling - Sunset Radio
   Score: 1.98
   Why: Mood match (+1.00); Energy similarity (+0.98)

4. Rooftop Lights - Indigo Parade
   Score: 1.86
   Why: Mood match (+1.00); Energy similarity (+0.86)

5. Golden Hour - Willow Fields
   Score: 1.55
   Why: Mood match (+1.00); Energy similarity (+0.55)
```

### Profile 2: Chill Lo-Fi

Preferences:
- Genre: lofi
- Mood: chill
- Energy: 0.35
- Acoustic: True

Actual recommendation output:

```text
1. Library Rain - Paper Lanterns
   Score: 4.43
   Why: Genre match (+2.00); Mood match (+1.00); Energy similarity (+1.00); Acoustic preference (+0.43)

2. Midnight Coding - LoRoom
   Score: 4.29
   Why: Genre match (+2.00); Mood match (+1.00); Energy similarity (+0.93); Acoustic preference (+0.35)

3. Focus Flow - LoRoom
   Score: 3.34
   Why: Genre match (+2.00); Energy similarity (+0.95); Acoustic preference (+0.39)

4. Spacewalk Thoughts - Orbit Bloom
   Score: 2.39
   Why: Mood match (+1.00); Energy similarity (+0.93); Acoustic preference (+0.46)

5. Coffee Shop Stories - Slow Stereo
   Score: 1.43
   Why: Energy similarity (+0.98); Acoustic preference (+0.45)
```

### Profile 3: Intense Rock

Preferences:
- Genre: rock
- Mood: intense
- Energy: 0.95
- Acoustic: False

Actual recommendation output:

```text
1. Storm Runner - Voltline
   Score: 3.96
   Why: Genre match (+2.00); Mood match (+1.00); Energy similarity (+0.96)

2. Gym Hero - Max Pulse
   Score: 1.98
   Why: Mood match (+1.00); Energy similarity (+0.98)

3. Heavy Impact - Iron District
   Score: 1.97
   Why: Mood match (+1.00); Energy similarity (+0.97)

4. Electric Rush - Nova Circuit
   Score: 0.98
   Why: Energy similarity (+0.98)

5. Weekend Feeling - Sunset Radio
   Score: 0.93
   Why: Energy similarity (+0.93)
```

## Experiments You Tried

I tested how changing the scoring weights affected the recommendations.

### Original Weights

- Genre: 2.0
- Mood: 1.0
- Energy: 1.0

### Experimental Weights

- Genre: 1.0
- Mood: 1.0
- Energy: 2.0

The experiment compared genre, mood, and energy without the optional acoustic bonus.

### High-Energy Pop Results

```text
Original:
Sunrise City: 3.92
Gym Hero: 2.97
Weekend Feeling: 1.98
Rooftop Lights: 1.86
Golden Hour: 1.55

Experimental:
Sunrise City: 3.84
Weekend Feeling: 2.96
Gym Hero: 2.94
Rooftop Lights: 2.72
Golden Hour: 2.10
```

### Chill Lo-Fi Results

```text
Original:
Library Rain: 4.00
Midnight Coding: 3.93
Focus Flow: 2.95
Spacewalk Thoughts: 1.93
Coffee Shop Stories: 0.98

Experimental:
Library Rain: 4.00
Midnight Coding: 3.86
Focus Flow: 2.90
Spacewalk Thoughts: 2.86
Coffee Shop Stories: 1.96
```

### Intense Rock Results

```text
Original:
Storm Runner: 3.96
Gym Hero: 1.98
Heavy Impact: 1.97
Electric Rush: 0.98
Weekend Feeling: 0.93

Experimental:
Storm Runner: 3.92
Gym Hero: 2.96
Heavy Impact: 2.94
Electric Rush: 1.96
Weekend Feeling: 1.86
```

### Experiment Observations

The highest-ranked song stayed the same for all three profiles.

However, the ranking changed for High-Energy Pop. Weekend Feeling moved ahead of Gym Hero because its energy and mood matched the user's preferences more closely.

The experiment showed me that changing the importance of different features can affect the recommendations without changing the dataset.

I kept the original weights in the main recommender after the experiment.

## Limitations and Risks

VibeMatch has several limitations.

First, the dataset only contains 20 fictional songs, so there is not much variety.

Second, some genres have more songs than others, which could favor certain user preferences.

Third, genre receives more weight than mood or energy. This can sometimes make the algorithm prioritize genre over other useful features.

Another issue is that energy similarity can give songs high scores even when their style is very different from what the user wants.

For example, Weekend Feeling, a disco song, appeared in the Intense Rock recommendations because its energy was close to the target.

The system also cannot learn from listening history, skips, or likes.

## Reflection

See the [Model Card](model_card.md) for more information about the model's evaluation, limitations, and future improvements.

This project helped me understand how recommendation systems use data and scoring rules to suggest content. I learned that even a simple algorithm can create different recommendations based on user preferences.

The most interesting part was changing the scoring weights and seeing how the rankings changed. I also learned that a program can run correctly while still making recommendations that do not completely match someone's taste.

AI helped me organize the code, understand the scoring logic, and troubleshoot problems. I checked the results by running the program, reviewing the explanations, and using automated tests.

If I continued working on this project, I would add more songs, allow users to rate recommendations, and improve the algorithm using more song features.
