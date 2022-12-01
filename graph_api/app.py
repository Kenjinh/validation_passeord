from flask import Blueprint, request, jsonify
from ariadne import gql, QueryType, MutationType, make_executable_schema, graphql_sync

urls_graph = Blueprint('quaphql', __name__)

type_defs = gql(
    """
    type Query { 
        verify(password: String!, rules: [RulesInput]): Response
    }
    type Verify{
        password: String!
        rules: [Rules]
    }
    type Rules {
        rule: String!
        value: Int!
    }
    input RulesInput{
        rule: String!
        value: Int!
    }
    type Response{
        verify: Boolean
        noMatch: [String]
    }
    """
)

query = QueryType()
mutation = MutationType()


@query.field("verify")
def verify(*_, password, rules):
    noMatch = []
    verify = True
    if password:
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
                if not len(password)> rule['value']:
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
    return {'verify': verify, 'noMatch': noMatch}




schema = make_executable_schema(type_defs, query)


@urls_graph.route('/', methods=['POST'])
def graphql():  # put application's code here
    data = request.get_json()
    success, result = graphql_sync(schema, data, context_value={"request": request})
    status_code = 200 if success else 400
    return jsonify(result), status_code

