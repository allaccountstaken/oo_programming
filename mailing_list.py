from collections import defaultdict

class MailingList:
    """Manage groups of e-mail addresses for sending e-mails."""
    def __init__(self):
        self.email_map = defaultdict(set)
        
    def add_to_group(self, email, group):
        self.email_map[email].add(group)
    
    def emails_in_groups(self, *groups): 
        groups = set(groups)
        emails = set() 
        for e, g in self.email_map.items(): 
            if g & groups: 
                emails.add(e)
        return emails
    
    def send_mailing(self,
                     subject,
                     message,
                     from_addr,
                     *groups,
                     headers=None):
        emails = self.emails_in_groups(*groups)
        send_email(subject, message, from_addr, *emails, header=headers)
    