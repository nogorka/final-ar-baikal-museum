from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)


@main.route('/')
def welcome():
    return render_template('main/welcome.html')


@main.route('/photobooth')
def photobooth():
    return render_template('main/photobooth.html')


@main.route('/gallery')
def gallery():
    return render_template('main/gallery.html')


@main.route('/portal')
def portal():
    return render_template('main/portals.html')
