def format_text(text):
    """
    Format text by:
    1. Removing extra spaces between words
    2. Fixing space issues around punctuation
    3. Proper capitalization after periods
    4. Removing split words
    """
    # Split text into lines and join with spaces to handle line breaks
    text = ' '.join(text.split('\n'))
    
    # Remove extra spaces
    text = ' '.join(text.split())
    
    # Fix spaces around punctuation
    for punct in [',', '.', ':', ';', '!', '?']:
        text = text.replace(f' {punct}', punct)
        text = text.replace(f'{punct}', f'{punct} ')
    
    # Remove extra spaces that might have been created
    text = ' '.join(text.split())
    
    # Fix quotes
    text = text.replace(" ' ", "'")
    text = text.replace(" '", "'")
    text = text.replace("' ", "'")
    
    # Handle parentheses
    text = text.replace('( ', '(')
    text = text.replace(' )', ')')
    
    # Split into sentences for proper capitalization
    sentences = text.split('. ')
    sentences = [s.capitalize() for s in sentences]
    text = '. '.join(sentences)
    
    # Format numbered list items
    text = text.replace('.', '. ')
    
    # Final cleanup of any double spaces
    text = ' '.join(text.split())
    
    # Split into paragraphs
    paragraphs = []
    current_paragraph = []
    
    for sentence in text.split('. '):
        if sentence.strip().startswith('1'):  # Start of numbered list
            if current_paragraph:
                paragraphs.append('. '.join(current_paragraph) + '.')
                current_paragraph = []
            paragraphs.append(sentence + '.')
        elif sentence.startswith(('2', '3')):  # Continuing numbered list
            paragraphs.append(sentence + '.')
        else:
            current_paragraph.append(sentence)
    
    if current_paragraph:
        paragraphs.append('. '.join(current_paragraph) + '.')
    
    # Join paragraphs with double newlines
    return '\n\n'.join(paragraphs)

# Your text content
text = """A solar eclipse is a natural astronom ical event that occurs when the Moon moves between the Earth and the Sun , tempor arily obsc uring the Sun ' s light . During a solar eclipse , the observer on Earth will see the Sun appear to be either partially or fully covered by the Moon , depending on the type of eclipse .
There are three main types of solar e cli ps es :
1 . Total Sol ar Eclipse : This happens when the Moon completely covers the Sun , as seen from Earth . The sky gets dark as if it were night in the path of tot ality ( the area experien cing the total eclipse ), and the typical features of the Sun , such as the cor ona , become visible . The cor ona is the Sun ' s outer most atmosphere , usually seen only during a total solar eclipse .
2 . Part ial Sol ar Eclipse : During a partial solar eclipse , only a part of the Sun is covered by the Moon . Ob ser vers experiences a partial covering of the solar disk . This phenomen on happens within the bro ader area guaranteed by an ann ular solar eclipse .
3 . Ann ular Sol ar Eclipse : This occurs when the Moon covers the center of the Sun , but the edges do not align properly , leaving a ring - like appearance known as the " ring of fire ." The reason for this angle dis cre p ancy lies in the Moon ' s elli pt ical orbit around the Earth ; at some points , it ' s further from Earth and appears smaller in the sky , unable to block the bright photos phere .
S olar e cli ps es only happen during the new Moon phase and can be seen with the right equipment , such as eclipse glass es , solar filters , or by project ing the image through a pin hole project or . It ' s cru cial not to look directly at the Sun without proper protection , even during an eclipse — using solar view ing materials can prevent serious eye damage .
D ue to the distances and sizes involved , solar e cli ps es don ' t happen every month ( even though the new Moon phase occurs every month ), but rather about twice a year at points of intersection of the Moon ' s orbit with the e cli ptic plane ( the apparent path of the Sun across our sky ).
The beautiful a we - in sp iring spect acle of a solar eclipse leaves a last ing impression on anyone fort un ate enough to witness it , although prepar ation and ca ution are vital to ensure safe observation"""

# # Format and print the text
# formatted_text = format_text(text)
# print(formatted_text)




# from ..DictDB import dictdb

# dbORM = dictdb.DictDB()

# print(dbORM.find_one("User", "user_unique_id" "ZWJZiZnbFov4RxJ5u5OkGzeplPTnCOEYUFAl"))