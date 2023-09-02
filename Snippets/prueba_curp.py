from re import findall

regex = r"^([A-Z]{3,})(\d{6})(H|M)([A-Z]{1,2}|[A-Z]{3})([A-Z]{2,})(\d{1,})$"

print(findall(regex, "VARA021005HNLLVLA4"))
