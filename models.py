from flask import Flask, jsonify

class user:
    def sign_up(self):
        user={"_id":"123","user":"adas","passc":"145"}
        return jsonify(user),200
