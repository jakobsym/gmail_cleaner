# Marks all emails as read
import ezgmail

unreadEmails = ezgmail.unread(maxResults=500)
print(f"There are {len(unreadEmails)} unread emails in your email")
for i in unreadEmails:
    i.markAsRead()


