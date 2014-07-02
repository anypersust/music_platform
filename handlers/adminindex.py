#coding=utf-8

import tornado.web
from handlers.adminbase import AdminBaseHandler
from models.database import *
from tornado.escape import json_encode


def generate_musics_table():
    music_list = personal_recommend()
    to_send_music_info_list = []
    for music in music_list:
        current_music_url = music["music_url"]
        current_music_name = music["music_name"]
        current_music_artist = music["music_artist"]
        current_music_picture_url = music["music_picture_url"]
        one_music =  {
            'music_url': current_music_url,
            'music_name': current_music_name,
            'music_artist': current_music_artist,
            'music_picture_url': current_music_picture_url,
        }
        to_send_music_info_list.append(one_music)
    return to_send_music_info_list



class AdminIndexHandler(AdminBaseHandler):
    @tornado.web.authenticated
    def get(self):
        if not self.get_current_user():
            self.redirect(self.get_argument('next', '/adminlogin'))
            return
        self.render('adminindex.html', admin_user=self.current_user)


    @tornado.web.authenticated
    def post(self):
        action = self.get_argument("action", "default")

        if action == "refresh":
            to_send_music_info_list = generate_musics_table()
            print to_send_music_info_list
            self.write( json_encode(to_send_music_info_list) )

