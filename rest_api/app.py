from flask import Blueprint, request

urls_rest = Blueprint('verify', __name__)


@urls_rest.route('/', methods=['POST'])
def verify():
    data = request.get_json()
    rules = data['rules']
    password = data['password']
    noMatch = []
    verify = True
    for rule in rules:
        if rule['rule'] == 'minSize':
            if len(password) < rule['value']:
                noMatch.append('minSize')
                verify = False

        elif rule['rule'] == 'minSpecialChars':
            count = 0
            for char in password:
                if not char.isalnum():
                    count += 1
            if count < rule['value']:
                noMatch.append('minSpecialChars')
                verify = False

        elif rule['rule'] == 'noRepeted':
            Repeted = False
            if rule['value'] == 1:
                split = list(password)
                count = 1
                for char in password:
                    if char != split[count]:
                        if count == len(password) - 1:
                            break
                        count += 1
                    else:
                        Repeted = True
                        verify = False
                        break
            if Repeted:
                noMatch.append('noRepeted')

        elif rule['rule'] == 'minDigit':
            count = 0
            for char in password:
                if char.isdigit():
                    count += 1
            if count < rule['value']:
                noMatch.append('minDigit')
                verify = False
        elif rule['rule'] == 'minUppercase':
            count = 0
            for char in password:
                if char.isupper():
                    count += 1
            if count < rule['value']:
                noMatch.append('minUppercase')
                verify = False
        elif rule['rule'] == 'minLowercase':
            count = 0
            for char in password:
                if char.islower():
                    count += 1
            if count < rule['value']:
                noMatch.append('minLowercase')
                verify = False

        data = {'verify': verify, 'noMatch': noMatch}
    return data
