import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import googleapiclient.discovery
from google.oauth2 import service_account
import os
import json


certificate = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
cred = credentials.Certificate(certificate)
firebase_admin.initialize_app(cred)
db = firestore.client()

# This requires the rights of the key to be updated
# since it only has the access to view docs


def get_policy(project_id, version=1):
    """Gets IAM policy for a project."""
    credentials = service_account.Credentials.from_service_account_file(
        filename=os.environ["GOOGLE_APPLICATION_CREDENTIALS"],
        scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )

    service = googleapiclient.discovery.build(
        "cloudresourcemanager", "v1", credentials=credentials
    )
    policy = (
        service.projects()
        .getIamPolicy(
            resource=project_id,
            body={"options": {"requestedPolicyVersion": version}},
        )
        .execute()
    )
    print(json.dumps(policy['bindings'], indent=4))


def write_data():
    with open("movies.json") as file:
        data = json.load(file)['movies']

    for movie in data:
        db.collection(u'movies').document(str(movie['movieId'])).set(movie)


def read_data():
    movies = list(db.collection(u'movies').stream())
    for movie in movies[:1]:
        print(json.dumps(movie.to_dict(), indent=4))


read_data()
# get_policy("trim-001")
print("Completed!")
