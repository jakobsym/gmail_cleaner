# Marks all emails as read
import ezgmail

unreadEmails = ezgmail.unread(maxResults=300)
print(f"There are {len(unreadEmails)} unread emails in your email")
for i in unreadEmails:
    print(ezgmail.summary(i), "\n")
    i.markAsRead()
