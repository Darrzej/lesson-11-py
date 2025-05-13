import datetime
# current_datetime = datetime.datetime.now()
# print(current_datetime)

# print("Year", current_datetime.year)
# print("Month", current_datetime.month)
# print("Day", current_datetime.day)
# print("Hour", current_datetime.hour)
# print("Minute", current_datetime.minute)
# print("Second", current_datetime.second)
# print("Microsecond", current_datetime.microsecond)

# current_datetime1 = datetime.datetime.now().date()
# print(current_datetime1)
# current_datetime2 = datetime.datetime.now().time()
# print(current_datetime2)

# koha_aktuale = datetime.time(12, 30, 45 ,123456)
# print(koha_aktuale)
# koha_aktuale1 = datetime.date(2025, 5, 13)
# print(koha_aktuale1)


# sky_time = datetime.timedelta(days=5, hours=6)
# print(sky_time)

# duration = current_datetime + sky_time
# print(duration)

# sky_time2 = datetime.timedelta(days=6234, hours=5)
# birthday = current_datetime - sky_time2

# print(birthday)

# challenge

current_datetime10 = datetime.datetime.now()
print(current_datetime10)

print("Year", current_datetime10.year)
print("Month", current_datetime10.month)
print("Day", current_datetime10.day)
print("Hour", current_datetime10.hour)
print("Minute", current_datetime10.minute)
print("Second", current_datetime10.second)
print("Microsecond", current_datetime10.microsecond)


sky_time2 = datetime.timedelta(days=100, hours=6)
print(sky_time2)

duration_minus = current_datetime10 - sky_time2
duration_plus = current_datetime10 + sky_time2
print(duration_plus)
print(duration_minus)

file_path = file_path = "C:/Users/Student/Desktop/lesson-11-py/leximi.txt"

with open(file_path, "w")as file:
    file.write((f"{duration_minus}"))
    file.write((f"{duration_plus}"))











