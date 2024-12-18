# List of email addresses (some duplicates)
email_address = [
            "user1@example.com","user2@example.com","user3@example.com",
            "user1@example.com","user4@example.com","user2@example.com"
]

# use a set to remove duplicates
unique_emails = set(email_address)

# Convert the set back to a sorted list if needed
unique_email_list = sorted(unique_emails)

# Output the unique email addresses
print("Unique email addresses : ")
for email in unique_email_list:
    print(email)
