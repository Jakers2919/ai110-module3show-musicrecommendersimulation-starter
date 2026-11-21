
# 🎧 Model Card: VibeMatch 1.0

## 1. Model Name

**VibeMatch 1.0 - Music Recommender Simulation**

VibeMatch is a Python program that recommends songs based on a user's music preferences.

## 2. Intended Use

VibeMatch recommends songs by comparing a user's favorite genre, mood, energy level, and acoustic preference with a small music dataset.

It is designed for classroom learning and experimentation, not for use as a commercial music recommendation service.

The program assumes users can describe their music preferences using a few simple categories.

It does not learn from actual listening history.

## 3. How the Model Works

VibeMatch uses a weighted scoring system to compare songs with user preferences.

A matching genre adds 2 points, and a matching mood adds 1 point. Songs can also receive up to 1 point based on how close their energy level is to the user's target.

If the user likes acoustic music, songs can receive an additional bonus of up to 0.5 points based on acousticness.

The program scores all 20 songs, ranks them from highest to lowest, and displays the five best matches.

Each recommendation includes an explanation showing which factors contributed to its score.

I replaced the original starter functions with working code for loading songs, scoring them, ranking recommendations, and explaining the results.

## 4. Data

The starter dataset contained 10 fictional songs. I expanded it to 20 songs by adding 10 more entries.

The catalog includes pop, rock, lo-fi, jazz, ambient, EDM, metal, reggae, hip hop, country, classical, disco, and other genres.

Each song includes:

- ID
- Title
- Artist
- Genre
- Mood
- Energy
- Tempo
- Valence
- Danceability
- Acousticness

The song attributes are sample data created for this simulation.

The dataset does not include real listening history, lyrics, ratings, or user feedback.

## 5. Strengths

One strength of VibeMatch is that it explains its recommendations instead of only displaying song titles.

It also gives points for energy similarity, meaning a song does not need an exact energy match to be recommended.

During evaluation, the program correctly ranked Sunrise City first for High-Energy Pop, Library Rain first for Chill Lo-Fi, and Storm Runner first for Intense Rock.

These results made sense because the top songs matched each profile's genre, mood, and energy preferences.

The program also passed both starter automated tests.

## 6. Limitations and Bias

The biggest limitation is the small dataset of only 20 songs. Some genres have multiple songs, while others only have one, which limits variety.

The scoring algorithm also gives genre more importance than mood or energy. This can cause a genre match to rank higher even when another song better matches the user's energy preference.

The program also recommends songs based on energy similarity even when their musical style is very different.

For example, Weekend Feeling is a disco song, but it appeared in the top five for the Intense Rock profile because its energy was close to the target.

Another limitation is that the system does not learn from likes, skips, or listening history. It cannot automatically adjust when someone's preferences change.

These limitations show how both the dataset and the scoring rules can influence recommendation quality.

## 7. Evaluation

I tested VibeMatch with three different user profiles.

### Profile 1: High-Energy Pop

Preferences:
- Genre: pop
- Mood: happy
- Energy: 0.90
- Acoustic: False

Top five results:

1. Sunrise City - 3.92
2. Gym Hero - 2.97
3. Weekend Feeling - 1.98
4. Rooftop Lights - 1.86
5. Golden Hour - 1.55

Sunrise City ranked first because it matched the genre and mood and had a similar energy level.

### Profile 2: Chill Lo-Fi

Preferences:
- Genre: lofi
- Mood: chill
- Energy: 0.35
- Acoustic: True

Top five results:

1. Library Rain - 4.43
2. Midnight Coding - 4.29
3. Focus Flow - 3.34
4. Spacewalk Thoughts - 2.39
5. Coffee Shop Stories - 1.43

Library Rain ranked first because it matched both genre and mood, had an exact energy match, and received an acoustic bonus.

### Profile 3: Intense Rock

Preferences:
- Genre: rock
- Mood: intense
- Energy: 0.95
- Acoustic: False

Top five results:

1. Storm Runner - 3.96
2. Gym Hero - 1.98
3. Heavy Impact - 1.97
4. Electric Rush - 0.98
5. Weekend Feeling - 0.93

Storm Runner ranked first because it matched the genre and mood and had an energy level close to the target.

I noticed that Weekend Feeling appeared in the Intense Rock recommendations even though it was disco. This showed me that energy similarity alone does not always mean a song is a good recommendation.

### Scoring Experiment

I also ran an experiment to see how changing the scoring weights affected the rankings.

Original weights:
- Genre: 2.0
- Mood: 1.0
- Energy: 1.0

Experimental weights:
- Genre: 1.0
- Mood: 1.0
- Energy: 2.0

The experiment compared genre, mood, and energy without including the optional acoustic bonus.

For High-Energy Pop, the results changed:

Original ranking:

1. Sunrise City - 3.92
2. Gym Hero - 2.97
3. Weekend Feeling - 1.98
4. Rooftop Lights - 1.86
5. Golden Hour - 1.55

Experimental ranking:

1. Sunrise City - 3.84
2. Weekend Feeling - 2.96
3. Gym Hero - 2.94
4. Rooftop Lights - 2.72
5. Golden Hour - 2.10

Weekend Feeling moved ahead of Gym Hero because its mood and energy were closer to the user's preferences.

For Chill Lo-Fi and Intense Rock, the top-ranked songs stayed the same, although their scores changed.

The experiment showed that changing feature weights can change the order of recommendations without changing the song dataset.

I kept the original scoring weights in the final recommender.

### Automated Tests

I ran the starter tests using pytest.

Both tests passed:

- `test_recommend_returns_songs_sorted_by_score`
- `test_explain_recommendation_returns_non_empty_string`

The results confirmed that the object-oriented recommender returned ranked songs and generated explanations.

## 8. Future Work

If I continued developing VibeMatch, I would make several improvements.

First, I would expand the dataset with more songs from different genres and artists.

Second, I would let users like, dislike, or skip songs so the system could adjust its recommendations.

Third, I would experiment with using tempo, danceability, and valence in the scoring system.

I would also like to create a simple interface where users could select their preferences without editing Python code.

## 9. Personal Reflection

This project helped me understand how recommendation systems use data to make suggestions. Before this project, I knew that apps like Spotify recommended music, but I did not really understand how song features could be turned into scores.

The most interesting part was testing different profiles and changing the scoring weights. I saw that even a small change in the algorithm could affect which songs appeared near the top.

I used AI to help build the code, understand the scoring system, and troubleshoot errors. One issue I ran into was an extra blank line in the CSV file, which caused the program to fail when loading the songs. Fixing that reminded me that small formatting problems can affect the entire program.

I also learned that just because a recommendation has a high score does not mean it perfectly matches someone's taste. The dataset and scoring rules both matter.

If I worked on this project again, I would focus on making the recommendations more personalized and adding more variety.
