

# Network Intrusion Detection System (NIDS)

This project is a Network Intrusion Detection System (NIDS) implemented in Python. It uses the `psutil` library to gather system and process information, and `selectors` for handling multiple connections to the server.

## Modules

The project consists of the following modules:

1. `CLIENT.py`: This module gathers system, process, and network connection information from the client machine and sends it to the server.

2. `SERVER.py`: This module listens for incoming connections from clients, receives the system, process, and network connection information, and saves it to a file.

3. `ANALYSER.py`: This module reads the files generated by the server and formats the data for further analysis.

4. `MALICIOUS_CHECK.py`: This module checks the process information against a list of known malicious processes. If a malicious process is found, it is logged to a new CSV file.

## Dependencies

The project requires Python 3 and the following Python packages:

- `psutil == 5.9.7`

These dependencies can be installed using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the server:

```bash
python SERVER.py <host> <port>
```

2. Start the client:

```bash
python CLIENT.py <server_host> <server_port>
```

3. Analyze the data:

```bash
python ANALYSER.py
```

4. Check for malicious processes:

```bash
python MALICIOUS_CHECK.py
```

## Note

This project is a basic implementation of a Network Intrusion Detection System (NIDS). It is not intended for use in a production environment.
