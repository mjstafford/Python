from flask import Flask, redirect, render_template, session, flash, request
from app import app

@app.route("/")
def home_page():
    return render_template("index.html")