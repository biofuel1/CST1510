def parse_line(raw_line):
    raw_line = raw_line.strip()
    hostname_part, rest = raw_line.split(",", 1)
    hostname = hostname_part.strip().lower()
    rest_split = rest.split(",")
    rest_cleaned = [i.replace(" ", "") for i in rest_split]
    used = rest_cleaned[0].split("=")
    total = rest_cleaned[1].split("=")
    return {'hostname': hostname, used[0]: float(used[1]), total[0]: float(total[1])}
    
def status_of(parsed_line):
    percent = (parsed_line["used"] / parsed_line["total"]) * 100
    
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"
	
lines = ["  Srv-01 , used=87 , total=100",
		 "	SRV-02,used=120,total=100      ",
		 "  srv-03,used=45 ,total=100   ",
         "  Srv-04 , used = 93 , total=100  ",
		 "  srv-05    , used=84,  total  = 100"]
         
with open("lines.txt", "w") as file:
    for line in lines:
        file.write(line + '\n')
        
   
line_count = 0
overlimit_count = 0

with open("lines.txt") as file:
    for line in file:
        parsed_line = parse_line(line)
        status = status_of(parsed_line)
        print(f"{parsed_line['hostname']} {status}")
        
        if status == "OVER LIMIT":
            overlimit_count += 1
        line_count += 1
        
        
print(f"{overlimit_count} records out of {line_count} were overlimit.")