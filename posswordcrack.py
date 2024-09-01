import subprocess

try:
    # Running command to get Wi-Fi profiles
    command_output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="ignore")
    command_lines = command_output.split('\n')
    profiles = [line.split(":")[1].strip() for line in command_lines if "All User Profile" in line]

    for profile in profiles:
        try:
            # Running command to get profile details
            profile_output = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors="ignore")
            profile_lines = profile_output.split('\n')
            key_content = [line.split(":")[1].strip() for line in profile_lines if "Key Content" in line]
            # Print profile name and password (if found)
            if key_content:
                print("{:<30}|  {:<}".format(profile, key_content[0]))
            else:
                print("{:<30}|  {:<}".format(profile, "No password found"))
        except subprocess.CalledProcessError as e:
            print(f"Error retrieving profile {profile}: {e}")
except subprocess.CalledProcessError as e:
    print(f"Error running netsh command: {e}")

input("Press Enter to exit...")
