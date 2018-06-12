*** first ***

pip install --upgrade google-cloud-speech
pip install --upgrade google-cloud-texttospeech
pip install --upgrade google-cloud-translate

add this to the bash_profile
export GOOGLE_APPLICATION_CREDENTIALS="[PATH]/g_credentials.json"


*** second - link your gmail account to the api
gcloud auth login

*** last - this one needs the json file attatched
gcloud auth activate-service-account --key-file="[PATH]/g_credentials.json" 
