from faker import Faker

fake = Faker()

subjects = ["Social Studies", "Sanskrit"]
gender = ["Male","Female", "Other"]
hobbies = ["Sports", "Reading", "Music"]
states = ["NCR", "Uttar Pradesh", "Haryana", "Rajasthan"]
cities_in_states = {"NCR" : ["Delhi", "Gurgaon", "Noida"],
                    "Uttar Pradesh" : ["Agra", "Lucknow", "Merrut"],
                    "Haryana" : ["Karnal", "Panipat"],
                    "Rajasthan" : ["Jaipur", "Jaiselmer"]}

required_data_to_fill = {"first_name" : fake.first_name(),
                         "last_name" : fake.last_name(),
                         "email" : fake.email(),
                         "gender" : gender[0],
                         "mobile_number" : "1234567891",
                         "address_input" : fake.street_address()}

first_all_data_to_fill = {"first_name" : fake.first_name_male(),
                         "last_name" : fake.last_name_male(),
                         "email" : fake.email(),
                          "gender" : gender[0],
                         "mobile_number" : "1234567891",
                         "subjects" : subjects[0],
                          "hobbies" : [hobbies[0], hobbies[1]],
                          "picture" : "data/test_img.png",
                         "address_input" : fake.address(),
                          "state" : states[0],
                          "city" : cities_in_states["NCR"][0]}

second_all_data_to_fill = {"first_name" : fake.first_name_female(),
                         "last_name" : fake.last_name_female(),
                         "email" : fake.email(),
                          "gender" : gender[1],
                         "mobile_number" : "1234567891",
                         "subjects" : subjects[1],
                          "hobbies" : hobbies[1],
                          "picture" : "data/test_img.png",
                         "address_input" : fake.address(),
                          "state" : states[1],
                          "city" : cities_in_states["Uttar Pradesh"][1]}
print(first_all_data_to_fill)
print(second_all_data_to_fill)