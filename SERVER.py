def check_malicious_processes():
    # Read the CSV file containing the names of malicious processes
    with open('malicious_processes.csv', 'r') as f:
        reader = csv.reader(f)
        malicious_processes = list(reader)

    for f in files:
        if f.startswith("PROINFO") or f.startswith("SYSINFO"):
            print(f)
            fx = open(f)
            lines = fx.readlines()
            fx.close()

            # Extract the hostname and port from the filename
            filename_parts = f.split('-')
            hostname = filename_parts[1]
            port = filename_parts[2]

            # Create a new CSV file to store the malicious processes found
            new_filename = 'MALINFO-' + hostname + '-' + port + '.csv'
            with open(new_filename, 'w', newline='') as csvfile:
                fieldnames = ['PROCESSID', 'PROCESSNAME', 'IP', 'PORT', 'SOURCE']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()

                for line in lines[1:]:  # Skip the header line
                    data = line.split(',')
                    process_id = data[0]
                    process_name = data[1]
                    ip = data[2]
                    port = data[3]

                    # Check if the process name is in the list of malicious processes
                    if [process_name] in malicious_processes:
                        print("Found malicious process:", process_name)
                        writer.writerow({'PROCESSID': process_id, 'PROCESSNAME': process_name, 'IP': ip, 'PORT': port, 'SOURCE': f})
                    else:
                        print("Process not found in malicious_processes.csv:", process_name)

# Call the function
check_malicious_processes()