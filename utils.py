import pandas as pd
import os
from datetime import datetime

def mark_attendance(name):
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")
    path = f"attendance/{date}.csv"
    os.makedirs("attendance", exist_ok=True)

    if not os.path.exists(path):
        pd.DataFrame(columns=["Name", "Time"]).to_csv(path, index=False)

    df = pd.read_csv(path)
    if name not in df["Name"].values:
        df.loc[len(df)] = [name, time]
        df.to_csv(path, index=False)
        print(f"[INFO] Marked attendance for {name} at {time}")


























# import pandas as pd
# import os
# from datetime import datetime

# def mark_attendance(name):
#     date = datetime.now().strftime("%Y-%m-%d")
#     time = datetime.now().strftime("%H:%M:%S")
#     path = f"attendance/{date}.csv"
    
#     # Ensure the attendance folder exists
#     os.makedirs("attendance", exist_ok=True)

#     # Create file with header if it doesn't exist
#     if not os.path.exists(path):
#         pd.DataFrame(columns=["Name", "Time"]).to_csv(path, index=False)

#     # Always add a new entry with current time
#     new_entry = pd.DataFrame([[name, time]], columns=["Name", "Time"])
#     new_entry.to_csv(path, mode='a', header=False, index=False)

#     print(f"[INFO] Marked attendance for {name} at {time}")
