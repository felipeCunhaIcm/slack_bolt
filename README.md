# CHATBOT Slack

This project is a chatbot for interact with users.

a) Clone the 'branche' project, and entry on folder 'nome da pasta' project:
(Before, you need to set "SSH Key" and "SSO" on your GitHub)

git clone https://github.com/felipeCunhaIcm/slack_bolt.git


b) Create and activate one "virtualenv" (SO Linux):

python -m venv venv
source venv/bin/activate


c) Install the dependences of project:

pip install -r requirements.txt


d) Create your '.env' file based on template 'example_env', filling in all the informatons.
(If this is not done, it will cause an error in execution)


e) Run the file main.py:

f) You will receiving the message (Running on http://localhost:5000/slack/events)

g) Is necessary register your service on slack in "Event Subscriptions" search Request URL -> insert your adress service + /slack/events

h) Case you are working with localhost i suggest you use ngrok how intermediary between you localhost and slack web service

## API Slack

Ours chatbot can response in case to notified any events in Slack to type message, to this we input a URI (where is our server) on register from slack API.

### Folders

* `slack` - "Main" folder of project.
* `app` - folder of ours views (all queries for azure active directory) and slack (methodes to send message and files)

### Files

* `.env` - Environments variables of the project (based in env.example file).
* `.gitignore` - Lists files and directories which should not be added to git repository.

