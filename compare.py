import re

def extract_follower_names(file_path):
    """Extracts follower names from a file containing HTML-like content."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Regex to extract names within the span element with the class "_ap3a _aaco _aacw _aacx _aad7 _aade"
    follower_names = re.findall(r'<span class="_ap3a _aaco _aacw _aacx _aad7 _aade" dir="auto">([^<]+)</span>', content)
    
    return set(follower_names)

def compare_followers(file1, file2):
    """Compares follower names from two files and returns names from file1 not in file2."""
    followers_file1 = extract_follower_names(file1)
    followers_file2 = extract_follower_names(file2)
    
    # Find followers in file1 but not in file2
    unique_followers = followers_file1 - followers_file2
    
    return unique_followers

# Specify your file paths here
file1 = 'Following.txt'  # Followers list 1
file2 = 'Followers.txt'  # Followers list 2

unique_followers = compare_followers(file1, file2)

# Output the result
if unique_followers:
    print("Followers in file1 but not in file2:")
    # Open a new file to write the unique followers
    with open('newNonFollowers.txt', 'w', encoding='utf-8') as outfile:
        for follower in unique_followers:
            print(follower)
            outfile.write(follower + '\n')
else:
    print("No followers found in file1 that are not in file2.")
