from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaulttags import register
import pyrebase

@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)
    
config = {
    'apiKey': "AIzaSyCvJQP-Z8hF_BkoYpudJe3m6Gfh_PaBOag",
    'authDomain': "autoteamsdb.firebaseapp.com",
    'databaseURL': "https://autoteamsdb-default-rtdb.firebaseio.com",
    'projectId': "autoteamsdb",
    'storageBucket': "autoteamsdb.appspot.com",
    'messagingSenderId': "708243226636",
    'appId': "1:708243226636:web:959863bf893447c04d2e29",
    'measurementId': "G-3DC80QM3PR"
  };
print('Inicio')
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()
storage = firebase.storage()
print('Fin')

def index(request):
        d1={}
        d2={}
        all_players = database.child('Players').get()
        for player in all_players.each():
            d1[player.key()]=player.val()
            d2[player.key()]=storage.child(player.key()+".jpg").get_url(1)
            print(player.key())
            print(player.val())
            print(type(player.val()))
        print(d1)
        context = {
            'all_players':d1,
            'images': d2
        }
        return render(request, 'autoTeams/index.html', context)