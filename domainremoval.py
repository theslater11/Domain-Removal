#DomainRemoval function that also counts number of bad domains in list
domainless = []
bad_domain = []
def remove_domain(email: list[str]) -> list[str]:
    """
    A function to remove the email domain from the input list

    Args:
        email (list[str]): the list of emails
    Returns:
        list[str]: The list with modified strings
    """
    #check to see if value was entered
    if email == []:
        return email
    else:
        pass
    #This function appends to a new list, domainless, to hold the modified values
    #Values that do not meet criteria for email are put into list, bad_domain
    for domain in email:
        if domain == str(domain) and "@" in domain:
            half_domain = domain.split("@")
            domainless.append(half_domain[0])
        else:
            bad_domain.append(domain)
            email.remove(domain)
            print(-1)
    email = domainless
    return email
#This line will permanently modify the original list with updated values
'''
COLLECTED LIST VARIABLE = domainless
'''
