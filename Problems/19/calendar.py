months = {"jan":31, "feb":28, "mar":31, "apr":30, "may":31,
          "jun":30, "jul":31, "aug":31, "sep":30, "oct":31,
          "nov":30, "dec":31}
days = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]

count = 0
dayIndex = 2
for year in range(1901, 2001):
    if year % 100 == 0:
        if year % 400 == 0:
            months["feb"] = 29
    elif year % 4 == 0:
        months["feb"] = 29
    else:
        months["feb"] = 28
    for month in months:
        print(month, "of", year, "starts on a", days[dayIndex])
        if dayIndex == 0:
            count += 1
        dayIndex = (months[month] + dayIndex) % 7 
print("Total count: ", count)

