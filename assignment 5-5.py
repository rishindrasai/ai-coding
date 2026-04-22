#generate a Python script that logs user activity (username, IP address, timestamp).Examine whether sensitive data is logged unnecessarily or insecurely
import logging
from datetime import datetime
import socket
import getpass
# Configure logging
logging.basicConfig(filename='user_activity.log', level=logging.INFO, format='%(asctime)s - %(message)s')   
def log_user_activity():
    # Get username
    username = getpass.getuser()
    
    # Get IP address
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    # Get timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Log user activity
    logging.info(f'Username: {username}, IP Address: {ip_address}, Timestamp: {timestamp}')
if __name__ == "__main__":
    log_user_activity()
# Review of logged data
# The script logs the username, IP address, and timestamp of user activity.
# While this information is useful for tracking user activity, it is important to consider the sensitivity of the data being logged.
# The username and IP address can be considered sensitive information, especially in environments   where privacy is a concern.
# To enhance security, consider the following measures:
# 1. Anonymize or hash the username before logging.     
# 2. Avoid logging the full IP address; consider logging only the subnet or anonymizing it.
# 3. Ensure that the log file has appropriate permissions to restrict access to authorized personnel only
# 4. Regularly review and purge old log entries to minimize data retention risks.   
# 5. Implement encryption for log files to protect sensitive data at rest.

