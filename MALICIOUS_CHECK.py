import csv
import os
import datetime

myPath = os.getcwd()
files = os.listdir(myPath)

def check_malicious_processes():
    # Read the CSV file containing the names of malicious processes
    with open('malicious_processes.csv', 'r') as f:
        reader = csv.reader(f)
        malicious_processes = list(reader)

    for f in files:
        if f.startswith("PROINFO"):
            print(f)
            with open(f, 'r') as fx:
                reader = csv.reader(fx)
                lines = list(reader)

            # Extract the hostname and port from the filename
            filename_parts = f.split('-')
            now = datetime.datetime.now()

            formatted_timestamp = now.strftime("%Y-%m-%d-%H-%M-%S")
            # Create a new CSV file to store the malicious processes found
            new_filename = 'MALINFO-'+formatted_timestamp+'.csv'
            with open(new_filename, 'w', newline='') as csvfile:
                fieldnames = ['PROCESSID', 'PROCESSNAME', 'STATUS', 'STARTTIME']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()

                for data in lines[1:]:  # Skip the header line
                    process_id = data[0]
                    process_name = data[1]
                    status = data[2]
                    start_time = data[3]

                    # Check if the process name is in the list of malicious processes
                    if [process_name] in malicious_processes:
                        print("Found malicious process:", process_name)
                        writer.writerow({'PROCESSID': process_id, 'PROCESSNAME': process_name, 'STATUS': status, 'STARTTIME': start_time})
                    else:
                        print("Process not found in malicious_processes.csv:", process_name)

# Call the function
check_malicious_processes()