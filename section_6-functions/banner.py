# Write a function to format text
def banner_text(text):
    screen_width = 80
    if len(text) > screen_width - 4:
        print('EEK!\nTHE TEXT IS TOO LONG TO FIT IN THE WINDOW')

    if text=='*':
        print('*'*screen_width)
    else:
        centered_text = text.center(screen_width-4)
        # this starts bit is neatly done
        output_string = '**{0}**'.format(centered_text)
        print(output_string)

banner_text('*')
banner_text('Eoin is cool')
banner_text('Next line')
banner_text(' ')
banner_text('what about here')
banner_text('*')
# Havent specified what to return so its returning None
result = banner_text('Eoin is here ')
print(result)
print(result == None)

# Make it be able to handle invalid args
# We're gonna make it throw an exception if it gets someting invalid
# Also make the function take screen_width as an arg
def banner_text(text,screen_width=80):
    if len(text) > screen_width - 4:
        raise ValueError("String {} is larger than specified width {}".format(text,screen_width))

    if text=='*':
        print('*'*screen_width)
    else:
        centered_text = text.center(screen_width-4)
        # this centered  bit is neatly done
        output_string = '**{0}**'.format(centered_text)
        print(output_string)

banner_text('Eoin is handsome | Eoin is handsome | Eoin is handsome | Eoin is handsome | Eoin is handsome | ',200)
banner_text('Next line | Next line | Next line | Next line | Next line | ',140)
banner_text('*')
banner_text(' ')
banner_text('what about here',80)
banner_text('*',80)


# Improve the func with keyword args defaults
def banner_text(text: str = ' ',screen_width: int = 80) -> None:
    """
    Print a centered text banner enclosed by two asterix on either side


    :param text: String to print to console
    :param screen_width: Console screen size metric
    :raises ValueError: If passed string is larger than assigned screen width
    """
    if len(text) > screen_width - 4:
        raise ValueError("String {} is larger than specified width {}".format(text,screen_width))

    if text=='*':
        print('*'*screen_width)
    else:
        centered_text = text.center(screen_width-4)
        # this centered  bit is neatly done
        output_string = '**{0}**'.format(centered_text)
        print(output_string)

banner_text('Eoin is handsome | Eoin is handsome | Eoin is handsome | Eoin is handsome | Eoin is handsome | ',200)
banner_text('Next line | Next line | Next line | Next line | Next line | ',140)
banner_text('*')
banner_text(screen_width = 60)
banner_text('what about here',80)
banner_text('*',80)