#!/usr/bin/python3

import random

# List of professions and address parts for randomization
professions = [
    "accountant",
    "doctor - ophthalmologist",
    "lawyer",
    "doctor - pediatrician",
    "teacher",
    "chef",
    "psychologist",
    "engineer",
    "artist",
    "nurse",
    "architect",
    "dentist",
    "veterinarian",
    "writer",
    "pilot",
    "pharmacist",
    "scientist",
    "musician",
    "police officer",
    "firefighter",
    "entrepreneur",
    "designer",
    "chef",
    "electrician",
    "plumber",
    "mechanic",
    "real estate agent",
    "photographer",
    "marketing manager",
    "financial advisor",
    "HR manager",
    "social worker",
    "web developer",
    "graphic designer",
    "data analyst",
    "event planner",
    "journalist",
    "physical therapist",
    "flight attendant",
    "paramedic",
    "nutritionist",
    "landscape architect",
    "fashion designer",
    "film director"
    # Add more professions here if needed
]


first_names = [
    "Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Henry", "Ivy", "Jack", "Katie", "Leo",
    "Mia", "Noah", "Olivia", "Peter", "Quinn", "Rachel", "Sam", "Tina", "Uma", "Victor", "Wendy", "Xavier",
    "Yara", "Zane", "Ava", "Ben", "Cara", "Dylan", "Emma", "Finn", "Gina", "Hank", "Iris", "Jake", "Kira",
    "Liam", "Molly", "Nate", "Olive", "Paul", "Qin"
    # Add more first names here if needed
]

last_names = [
    "Johnson", "Smith", "Williams", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson",
    "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark",
    "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King", "Wright",
    "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell",
    "Perez", "Roberts", "Turner", "Phillips"
    # Add more last names here if needed
]




streets = [
    "Elm St.", "Oak Ave.", "Pine St.", "Cedar Lane", "Cherry St.", "Maple Avenue", "Oak Lane", "Pine Street", "Cedar Blvd.",
    # Add more street names here if needed
]

cities = [
    # American cities (25%)
    "New York, NY, USA",
    "Los Angeles, CA, USA",
    "Chicago, IL, USA",
    "Houston, TX, USA",
    "Phoenix, AZ, USA",
    "Philadelphia, PA, USA",
    "San Antonio, TX, USA",
    "San Diego, CA, USA",
    "Dallas, TX, USA",
    "San Jose, CA, USA",
    "Austin, TX, USA",
    "Jacksonville, FL, USA",
    "Indianapolis, IN, USA",
    "San Francisco, CA, USA",
    "Columbus, OH, USA",
    "Fort Worth, TX, USA",
    "Charlotte, NC, USA",
    "Seattle, WA, USA",
    "Denver, CO, USA",
    "Washington, DC, USA",
    # European cities (25%)
    "London, United Kingdom",
    "Paris, France",
    "Berlin, Germany",
    "Rome, Italy",
    "Madrid, Spain",
    "Vienna, Austria",
    "Amsterdam, Netherlands",
    "Lisbon, Portugal",
    "Athens, Greece",
    "Stockholm, Sweden",
    "Dublin, Ireland",
    "Brussels, Belgium",
    "Oslo, Norway",
    "Copenhagen, Denmark",
    "Helsinki, Finland",
    "Warsaw, Poland",
    "Budapest, Hungary",
    "Prague, Czech Republic",
    "Moscow, Russia",
    "Istanbul, Turkey",
    # Middle Eastern cities (25%)
    "Dubai, UAE",
    "Tel Aviv, Israel",
    "Doha, Qatar",
    "Riyadh, Saudi Arabia",
    "Abu Dhabi, UAE",
    "Amman, Jordan",
    "Muscat, Oman",
    "Beirut, Lebanon",
    "Manama, Bahrain",
    "Kuwait City, Kuwait",
    "Tehran, Iran",
    "Baghdad, Iraq",
    "Sana'a, Yemen",
    "Jerusalem, Israel",
    "Damascus, Syria",
    "Ankara, Turkey",
    "Erbil, Iraq",
    "Kabul, Afghanistan",
    "Nicosia, Cyprus",
    # Asian cities (25%)
    "Tokyo, Japan",
    "Beijing, China",
    "Seoul, South Korea",
    "Delhi, India",
    "Shanghai, China",
    "Jakarta, Indonesia",
    "Mumbai, India",
    "Manila, Philippines",
    "Osaka, Japan",
    "Bangkok, Thailand",
    "Kuala Lumpur, Malaysia",
    "Hanoi, Vietnam",
    "Taipei, Taiwan",
    "Singapore",
    "Hong Kong",
    "Karachi, Pakistan",
    "Ho Chi Minh City, Vietnam",
    "Dhaka, Bangladesh",
    "Sri Jayawardenepura Kotte, Sri Lanka",
    "Astana, Kazakhstan",
    # Add more cities as needed
]

# Number of records to generate
num_records = 495

# Function to generate a random record
def generate_record():
    profession = random.choice(professions)
    if "doctor" in profession:
        profession = f"{profession}\nDr. {random.choice(first_names)} {random.choice(last_names)}"
    else:
        profession = f"{profession}\n{random.choice(first_names)} {random.choice(last_names)}"

    address = f"{random.randint(100, 9999)} {random.choice(streets)}"
    city = random.choice(cities)

    return f"{profession}\n{address}\n{city}\n\n"


def main():
    # Generating records
    file_content = ""
    for _ in range(num_records):
        file_content += generate_record()
    print(file_content)


if __name__ == '__main__':
    main()
# Writing to a file named '500_records.txt'

