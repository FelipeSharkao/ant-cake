from flask import Flask
from gql.schema import schema
from strawberry.flask.views import GraphQLView

app = Flask(__name__)
app.add_url_rule('/graphql',
                 view_func=GraphQLView.as_view('graphql_view', schema=schema))