import click
import click_config_file

def lookup_username(username):
    print(username)

def lookup_email(email):
    print(email)

@click.command()
@click.option('--username', '-u', help='Perform lookup using a username')
@click.option('--email', '-e', help='Perform lookup using an email')
@click.option('--username-file', '-uf', type=click.File('r'), help='File of usernames separated by newlines')
@click.option('--email-file', '-ef', type=click.File('r'), help='File of emails separated by newlines')
@click.option('--filter', help='Filter sites to be searched by list property value, e.g. cat=social') #TODO
@click.option('--no-nsfw', is_flag=True, help='Do not search sites Not Suitable For Work') #TODO
@click.option('--timeout', type=click.INT, default=30, help='Timeout in seconds for each request') #TODO
@click.option('--max-concurrent-requests', type=click.INT, default=30, help='Maximum number of concurrently awaited requests') #TODO
@click.option('--proxy', help='Proxy to send requests through') #TODO
@click.option('--csv', is_flag=True, help='Save the output to a .csv file') #TODO
#functionality deliberately removed: pdf export, permutations
@click.help_option('--help', '-h')
@click_config_file.configuration_option(implicit=False)
def main(username, email, username_file, email_file, filter, no_nsfw, timeout,  max_concurrent_requests, proxy, csv):
    if email:
        lookup_email(email)
    elif username:
        lookup_username(username)
    elif username_file:
        map(lookup_username, username_file)
    elif email_file:
        map(lookup_email, email_file)
        

if __name__ == '__main__':
    main()