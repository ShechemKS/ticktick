from ticktick.api import TickTickClient
from ticktick.oauth2 import OAuth2
import datetime
import sys
import os

def create_task(client: TickTickClient, name: str, due_date: datetime.datetime):
    temp_task = client.task.builder(name, projectId="64805f1a26b45d5bff8771db", startDate=due_date)
    task = client.task.create(temp_task)
    print(task)
    return


if __name__ == "__main__":
    name = os.environ["INPUT_NAME"]
    date = os.environ["INPUT_DATE"]
    print(name, date)
    client_id = os.environ["TICKTICK_ID"]
    client_secret = os.environ["TICKTICK_SECRET"]
    uri = "http://127.0.0.1:8080"
    username = "shechemsumanthiran@gmail.com"
    password = os.environ["TICKTICK_PASSWORD"]
    auth_client = OAuth2(client_id=client_id,
                     client_secret=client_secret,
                     redirect_uri=uri)
    client = TickTickClient(username, password, auth_client)
    create_task(client, name, datetime.datetime(date))