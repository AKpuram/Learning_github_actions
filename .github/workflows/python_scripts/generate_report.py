from datetime import datetime

with open("report.txt", "w") as f:
    f.write("GitHub Actions Report\n")
    f.write(f"Generated on: {datetime.now()}\n")

print("Report generated successfully!")
