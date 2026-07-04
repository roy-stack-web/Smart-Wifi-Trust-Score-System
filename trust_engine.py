import json
from datetime import datetime


def load_database():
    try:
        with open("database.json", "r") as file:
            return json.load(file)
    except:
        return {}


def save_database(data):
    with open("database.json", "w") as file:
        json.dump(data, file, indent=4)


def update_device(mac):
    database = load_database()

    if mac not in database:
        database[mac] = {
            "first_seen": str(datetime.now()),
            "times_seen": 1,
            "known_device": False
        }
    else:
        database[mac]["times_seen"] += 1

    save_database(database)

    return database[mac]


def calculate_trust_score(device):
    score = 100

    if device["times_seen"] == 1:
        score -= 30

    if device["vendor"] == "Unknown":
        score -= 20
    trusted_vendors = [
    "Samsung Electronics",
    "Apple",
    "Dell Inc.",
    "Intel Corporate"
]

    if device["vendor"] in trusted_vendors:
        score += 5

    if device["times_seen"] >= 10:
        score += 10

    if device["known_device"]:
        score += 10

    current_hour = datetime.now().hour

    if 1 <= current_hour <= 5:
        if device["times_seen"] <= 2:
            score -= 15

    return max(0, min(score, 100))