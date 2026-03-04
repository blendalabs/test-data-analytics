#!/usr/bin/env python3
"""Generate sample CSV of kids animation show performance metrics for YouTube."""

import csv
import random
from datetime import datetime, timedelta

# Word arrays for building unique kid-friendly titles: "Adjective Noun Noun #123"
ADJECTIVES = [
    "Magic", "Tiny", "Super", "Rainbow", "Happy", "Cosmic", "Sparkly",
    "Funny", "Sleepy", "Brave", "Silly", "Golden", "Bouncy", "Fluffy",
    "Wild", "Sweet", "Cool", "Giant", "Little", "Mystery", "Secret",
]
NOUNS_1 = [
    "Sunflower", "Puppy", "Dinosaur", "Bunny", "Kitten", "Dragon", "Unicorn",
    "Robot", "Pirate", "Princess", "Castle", "Forest", "Ocean", "Moon",
    "Cookie", "Crayon", "Bubble", "Cloud", "Garden", "Space", "Kitchen",
]
NOUNS_2 = [
    "World", "Adventures", "Party", "Friends", "Heroes", "Dreams", "Chaos",
    "Parade", "Mystery", "Daycare", "Builders", "Champions", "Sing-Along",
]

CATEGORIES = ["animation", "education", "entertainment"]
THUMBNAIL_STYLES = ["bright", "colorful", "cartoon", "minimal", "character_closeup"]

# Realistic ranges for kids content (views can be high, engagement varies)
VIEWS_RANGE = (5_000, 2_500_000)
WATCH_TIME_PER_VIEW = (60, 420)  # seconds (kids often watch shorter or full episodes)
LIKES_RATIO = (0.01, 0.05)  # of views
COMMENTS_RATIO = (0.0005, 0.005)
SHARES_RATIO = (0.001, 0.02)


def random_date(start: datetime, end: datetime) -> str:
    d = start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))
    return d.strftime("%Y-%m-%d")


def generate_row(video_id: int) -> list:
    views = random.randint(*VIEWS_RANGE)
    avg_watch = random.randint(*WATCH_TIME_PER_VIEW)
    watch_time_seconds = views * avg_watch

    likes = int(views * random.uniform(*LIKES_RATIO))
    comments = int(views * random.uniform(*COMMENTS_RATIO))
    shares = int(views * random.uniform(*SHARES_RATIO))

    start = datetime(2023, 1, 1)
    end = datetime(2024, 12, 31)
    publish_date = random_date(start, end)

    title = (
        f"{random.choice(ADJECTIVES)} {random.choice(NOUNS_1)} {random.choice(NOUNS_2)} #{video_id}"
    )
    category = random.choice(CATEGORIES)
    thumbnail = random.choice(THUMBNAIL_STYLES)

    return [
        f"v{video_id:03d}",
        title,
        category,
        publish_date,
        views,
        watch_time_seconds,
        likes,
        comments,
        shares,
        thumbnail,
    ]


def main():
    num_rows = 1000
    headers = [
        "video_id", "title", "category", "publish_date",
        "views", "watch_time_seconds", "likes", "comments", "shares", "thumbnail_style",
    ]
    output_path = "sample_videos.csv"

    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for i in range(1, num_rows + 1):
            writer.writerow(generate_row(i))

    print(f"Wrote {num_rows} rows to {output_path}")


if __name__ == "__main__":
    main()
