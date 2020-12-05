import sys
lines = sys.stdin.read().splitlines()

max_string_id = ""
max_gc_content = 0.0

temp_string_id = ""
gc_count = 0
total_count = 0
for line in lines:
    if ">" in line:
        if total_count:
            gc_content = gc_count / float(total_count)
            if gc_content > max_gc_content:
                max_gc_content = gc_content
                max_string_id = temp_string_id
        gc_count = 0
        total_count = 0
        temp_string_id = line.split(">")[1]
    else:
        for i in line:
            total_count += 1
            if i == "C" or i == "G":
                gc_count += 1

gc_content = gc_count / float(total_count)
if gc_content > max_gc_content:
    max_gc_content = gc_content
    max_string_id = temp_string_id

print(max_string_id)
print(max_gc_content*100)

#Custominput given
