from faker import Faker


fake = Faker()

subjects = ["Social Studies", "Sanskrit"]
gender_checkboxes = ["male","female", "other"]
hobbies_checkboxes = ["sports", "reading", "music"]
states = ["NCR", "Uttar Pradesh", "Haryana", "Rajasthan"]
cities_in_states = {"NCR" : ["Delhi", "Gurgaon", "Noida"],
                    "Uttar Pradesh" : ["Agra", "Lucknow", "Merrut"],
                    "Haryana" : ["Karnal", "Panipat"],
                    "Rajasthan" : ["Jaipur", "Jaiselmer"]}

required_data_to_fill = {"first_name" : fake.first_name(),
                         "last_name" : fake.last_name(),
                         "email" : fake.email(),
                         "mobile_number" : "1234567891",
                         "subjects_input" : subjects[0],
                         "address_input" : fake.street_address()}

all_data_to_fill = {"first_name" : fake.first_name(),
                         "last_name" : fake.last_name(),
                         "email" : fake.email(),
                         "mobile_number" : "1234567891",
                         "subjects_input" : subjects[0],
                         "address_input" : fake.street_address()}