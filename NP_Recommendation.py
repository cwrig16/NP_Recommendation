nps_and_features = {
'Acadia':'cdfijklnst',
'American Samoa':'hkljsu',
'Arches':'abdgklpt',
'Badlands':'dkot',
'Big Bend':'abcdgijklnst',
'Biscayne':'bcdist',
'Black Canyon of the Gunnison':'bcdfijklnqst',
'Bryce Canyon':'bcgjkl',
'Canyonlands':'bcdgiklst',
'Capitol Reef':'bdikls',
'Carlsbad Caverns':'bdel',
'Channel Islands':'cdhst',
'Congaree':'cijlst',
'Crater Lake':'bdijlnsu',
'Cuyahoga Valley':'cfijklst',
'Death Valley':'bdgkln',
'Denali':'bdlnt',
'Dry Tortugas':'cdhist',
'Everglades':'bcdilst',
'Gates of the Arctic':'bint',
'Gettysberg':'djlm',
'Glacier':'acdfjklonqst',
'Glacier Bay':'cijlnst',
'Grand Canyon':'bcdgiklst',
'Grand Teton':'bcdfijlnqst',
'Great Basin':'abdegijklnst',
'Great Sand Dunes':'dgjlpt',
'Great Smokey Mountains':'bdijln',
'Guadalupe Mountains':'bdgklnt',
'Haleakala':'dgjklnu',
'Hawaii Volcanoes':'bdklstu',
'Harpers Ferry':'jlt',
'Hot Springs':'adlrs',
'Indiana Dunes':'lpst',
'Isle Royale':'abcdijklst',
'Joshua Tree':'dgkln',
'Katmai':'bdilnt',
'Kenai Fjords':'bcdlnst',
'Kings Canyon':'jklnst',
'Kobuk Valley':'bijlnt',
'Lake Clark':'ijlnst',
'Lassen Volcanic':'dfilqu',
'Mammoth Cave':'cdeijklt',
'Mesa Verde':'aklt',
'Mount Rainier':'bdjlnst',
'North Cascades':'bdijklnst',
'Organ Pipe Cactus':'glt',
'Olympic':'bcdijlnpst',
'Petrified Forest':'bgkl',
'Pinnacles':'elnstu',
'Redwood':'bijlst',
'Rocky Mountain':'bdijlnt',
'Saguaro':'gjlt',
'Sequoia':'ejklnst',
'Shenandoah':'bdijlnst',
'Theodore Roosevelt':'dflot',
'Valley Forge':'lmt',
'Virgin Islands':'acghijlpst',
'Voyageurs':'cdis',
'Wind Cave':'bdejlot',
'White Sands':'bdgklpt',
'Wrangell-St. Elias':'bjklnst',
'Yellowstone':'abcdfijklmnqrstu',
'Yosemite':'bdijklnst',
'Zion':'bdgijklnst',
}

features = {
    'a': 'archeology',
    'b': 'backcountry',
    'c': 'boating', 
    'd': 'camping',
    'e': 'caves', 
    'f': 'cross country skiing',
    'g': 'desert',
    'h': 'diving',
    'i': 'fishing',
    'j': 'forest',
    'k': 'geology',
    'l': 'hiking',
    'm': 'military', 
    'n': 'mountains',
    'o': 'plains',
    'p': 'sand',
    'q': 'snowshoeing',
    'r': 'thermal features',
    's': 'water',
    't': 'wildlife',
    'u': 'volcanoes'
}

feature_string = ''
for key, value in features.items():
    feature_string += f'{key} - {value}\n'

def show_features():
    print(feature_string)

def greet():
    print('\nWelcome to National Park Recommendation!!! \nBy selecting a feature of the National Parks, you will be given a list of recommended parks to visit.\n')

def farewell():
    print('Thank you for using National Park Recommendation.')

def new_selection():
    while True:
        again = input('Would you like to make another selection? (y)es or (n)o: \n')
        if again.lower() == 'y':
            reprint = input('Would you like to see available features again? (y)es or (n)o: \n')
            if reprint.lower() == 'y':
                show_features()
                give_recommendation()
            elif reprint.lower() == 'n':
                give_recommendation()
            else:
                print('Invalid selection.  Please try again.\n')
                continue
        elif again.lower() == 'n':
            farewell()
            break
        else:
            print('Invalid selection.  Please try again.\n')
            continue

def get_feature():
    while True:
        feature = input('Please select one or more features by typing the cooresponding letter(s) below without spaces or commas.\nYour selection(s): ')
        chosen_features = ''
        choices = []
        for letter in feature:
            if letter.lower() in features.keys() and letter.lower() not in choices:
                chosen_features += f'{features[letter]}\n' 
                choices.append(letter)     
        if len(feature) == len(choices):
            print(f'\nYou selected:\n{chosen_features}\n')
            return choices
        else:
            print('\nInvalid selection.  Please try again.\n')
            continue

def give_recommendation():
    selection = get_feature()
    recommendation = '\n'
    for key, value in nps_and_features.items():   
        if all([char in value for char in selection]):
            recommendation += f'{key}\n'
    if len(recommendation) > 2:
        print(f'Your recommneded National Parks to visit are: \n{recommendation}')
    else:
        print(f'Unable to recommend National Park with all of your selections.\n')

def np_recommendation():
    greet()
    show_features()
    give_recommendation()
    new_selection()

np_recommendation()
